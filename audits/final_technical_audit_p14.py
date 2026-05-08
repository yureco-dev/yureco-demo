from __future__ import annotations

import hashlib
import json
import posixpath
import re
import sys
from collections import defaultdict
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urljoin, urlparse
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
AUDITS = ROOT / "audits"
JSON_REPORT = AUDITS / "final_technical_audit_p14.json"
TXT_REPORT = AUDITS / "final_technical_audit_p14.txt"

IGNORED_SCHEMES = {"mailto", "tel", "javascript", "data", "sms", "viber", "whatsapp"}
ASSET_EXTENSIONS = {
    ".css",
    ".js",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".avif",
    ".ico",
    ".bmp",
    ".tif",
    ".tiff",
    ".woff",
    ".woff2",
    ".ttf",
    ".otf",
    ".eot",
    ".mp4",
    ".webm",
    ".mp3",
    ".wav",
    ".pdf",
}
TEXT_EXTENSIONS = {".html", ".htm", ".css", ".xml", ".txt"}
MOJIBAKE_MARKERS = (
    "Ð",
    "Ñ",
    "Рџ",
    "РЅ",
    "Р°",
    "Р±",
    "Рµ",
    "Р¶",
    "Р·",
    "Рё",
    "Р№",
    "Рє",
    "Р»",
    "Рј",
    "Рѕ",
    "Рї",
    "С„",
    "С…",
    "С†",
    "С‡",
    "С€",
    "С‰",
    "СЊ",
    "СЏ",
    "СЋ",
)
AUX_DIRS = {"audits", "docs", ".vscode", "node_modules", "scripts"}
AUX_EXACT = {
    ".env",
    ".env.example",
    "deploy.sh",
    "README.md",
    "CHANGELOG.md",
    "package.json",
    "package-lock.json",
}
AUX_EXTENSIONS = {".md", ".csv", ".json", ".ps1", ".sh"}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hrefs: list[tuple[str, str]] = []
        self.assets: list[tuple[str, str, str]] = []
        self.images: list[dict[str, str]] = []
        self.json_ld: list[str] = []
        self.title_parts: list[str] = []
        self.h1_parts: list[str] = []
        self.meta_description = ""
        self.meta_robots = ""
        self.canonical = ""
        self.has_viewport = False
        self._in_title = False
        self._in_h1 = False
        self._in_json_ld = False
        self._json_chunks: list[str] = []

    @staticmethod
    def _attrs(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
        return {k.lower(): (v or "") for k, v in attrs}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        data = self._attrs(attrs)

        if tag == "title":
            self._in_title = True
        elif tag == "h1":
            self._in_h1 = True
        elif tag == "script":
            if data.get("type", "").strip().lower() == "application/ld+json":
                self._in_json_ld = True
                self._json_chunks = []
            src = data.get("src", "").strip()
            if src:
                self.assets.append(("script", src, "script src"))
        elif tag == "a":
            href = data.get("href", "").strip()
            if href:
                self.hrefs.append(("a", href))
        elif tag == "img":
            src = data.get("src", "").strip()
            width = data.get("width", "").strip()
            height = data.get("height", "").strip()
            if src:
                self.assets.append(("img", src, "img src"))
            self.images.append({"src": src, "width": width, "height": height})
        elif tag == "link":
            href = data.get("href", "").strip()
            rel = {item.lower() for item in data.get("rel", "").split()}
            if "canonical" in rel and href:
                self.canonical = href
            if "stylesheet" in rel and href:
                self.assets.append(("link", href, "stylesheet"))
            if href and ({"icon", "apple-touch-icon", "shortcut", "mask-icon"} & rel):
                self.assets.append(("link", href, "icon"))
            if href and self._looks_like_asset(href):
                self.assets.append(("link", href, "local href asset"))
        elif tag in {"source", "video", "audio", "iframe", "embed"}:
            src = data.get("src", "").strip()
            if src:
                self.assets.append((tag, src, f"{tag} src"))
        elif tag == "meta":
            name = data.get("name", "").strip().lower()
            if name == "description" and not self.meta_description:
                self.meta_description = data.get("content", "").strip()
            elif name == "robots" and not self.meta_robots:
                self.meta_robots = data.get("content", "").strip()
            elif name == "viewport":
                self.has_viewport = True

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self._in_title = False
        elif tag == "h1":
            self._in_h1 = False
        elif tag == "script" and self._in_json_ld:
            self.json_ld.append("".join(self._json_chunks).strip())
            self._in_json_ld = False
            self._json_chunks = []

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_parts.append(data)
        if self._in_h1:
            self.h1_parts.append(data)
        if self._in_json_ld:
            self._json_chunks.append(data)

    @staticmethod
    def _looks_like_asset(value: str) -> bool:
        parsed = urlparse(value)
        return Path(parsed.path).suffix.lower() in ASSET_EXTENSIONS


def read_utf8(path: Path) -> tuple[str | None, str | None]:
    try:
        return path.read_text(encoding="utf-8"), None
    except UnicodeDecodeError as exc:
        return None, str(exc)


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip().casefold()


def fingerprint_dist() -> dict[str, dict[str, Any]]:
    fingerprint: dict[str, dict[str, Any]] = {}
    for path in sorted(DIST.rglob("*")):
        if path.is_file():
            rel = path.relative_to(DIST).as_posix()
            stat = path.stat()
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            fingerprint[rel] = {"size": stat.st_size, "mtime_ns": stat.st_mtime_ns, "sha256": digest}
    return fingerprint


def parse_sitemap() -> tuple[list[str], str]:
    sitemap = DIST / "sitemap.xml"
    tree = ET.parse(sitemap)
    root = tree.getroot()
    namespace = ""
    if root.tag.startswith("{"):
        namespace = root.tag.split("}", 1)[0] + "}"
    urls = [loc.text.strip() for loc in root.findall(f".//{namespace}loc") if loc.text and loc.text.strip()]
    base_host = urlparse(urls[0]).netloc if urls else ""
    return urls, base_host


def url_to_dist_file(url: str) -> Path:
    parsed = urlparse(url)
    path = unquote(parsed.path or "/")
    if path in {"", "/"}:
        return DIST / "index.html"
    clean = path.lstrip("/")
    if clean.endswith("/"):
        return DIST / clean / "index.html"
    local = DIST / clean
    if local.suffix:
        return local
    return local.with_suffix(".html")


def dist_file_to_url(path: Path, base_host: str) -> str:
    rel = path.relative_to(DIST).as_posix()
    if rel == "index.html":
        return f"https://{base_host}/"
    return f"https://{base_host}/{rel}"


def local_target_to_file(value: str, base_url: str, base_host: str) -> tuple[Path | None, str | None]:
    value = value.strip()
    if not value or value.startswith("#"):
        return None, None
    parsed = urlparse(value)
    if parsed.scheme and parsed.scheme.lower() in IGNORED_SCHEMES:
        return None, None
    absolute = urljoin(base_url, value)
    abs_parsed = urlparse(absolute)
    if abs_parsed.scheme in {"http", "https"} and abs_parsed.netloc and abs_parsed.netloc != base_host:
        return None, None
    if abs_parsed.scheme and abs_parsed.scheme not in {"http", "https"}:
        return None, None
    path = unquote(abs_parsed.path or "/")
    if path in {"", "/"}:
        return DIST / "index.html", absolute
    clean = posixpath.normpath(path)
    if clean == ".":
        clean = "/"
    if clean.endswith("/"):
        return DIST / clean.lstrip("/") / "index.html", absolute
    target = DIST / clean.lstrip("/")
    if target.suffix:
        return target, absolute
    return target.with_suffix(".html"), absolute


def is_local_asset(value: str, base_url: str, base_host: str) -> bool:
    parsed = urlparse(value.strip())
    if parsed.scheme and parsed.scheme.lower() in IGNORED_SCHEMES:
        return False
    absolute = urljoin(base_url, value)
    abs_parsed = urlparse(absolute)
    if abs_parsed.scheme in {"http", "https"} and abs_parsed.netloc and abs_parsed.netloc != base_host:
        return False
    return Path(abs_parsed.path).suffix.lower() in ASSET_EXTENSIONS or "/img/" in abs_parsed.path


def asset_to_file(value: str, base_url: str, base_host: str) -> Path | None:
    if not is_local_asset(value, base_url, base_host):
        return None
    absolute = urljoin(base_url, value)
    parsed = urlparse(absolute)
    path = unquote(parsed.path or "")
    if not path:
        return None
    return DIST / path.lstrip("/")


def parse_pages(sitemap_urls: list[str]) -> tuple[dict[str, dict[str, Any]], list[dict[str, str]], list[Path]]:
    pages: dict[str, dict[str, Any]] = {}
    missing_sitemap_files: list[dict[str, str]] = []
    sitemap_files: list[Path] = []
    for url in sitemap_urls:
        file_path = url_to_dist_file(url)
        if not file_path.exists():
            missing_sitemap_files.append({"url": url, "expected_file": file_path.relative_to(ROOT).as_posix()})
            continue
        text, error = read_utf8(file_path)
        if text is None:
            missing_sitemap_files.append({"url": url, "expected_file": file_path.relative_to(ROOT).as_posix(), "error": error or ""})
            continue
        parser = PageParser()
        parser.feed(text)
        title = normalize_text("".join(parser.title_parts))
        h1 = normalize_text("".join(parser.h1_parts))
        pages[url] = {
            "url": url,
            "file": file_path,
            "html": text,
            "hrefs": parser.hrefs,
            "assets": parser.assets,
            "images": parser.images,
            "json_ld": parser.json_ld,
            "title": title,
            "description": normalize_text(parser.meta_description),
            "h1": h1,
            "robots": parser.meta_robots,
            "canonical": parser.canonical.strip(),
            "has_viewport": parser.has_viewport,
            "noindex": "noindex" in parser.meta_robots.casefold(),
        }
        sitemap_files.append(file_path)
    return pages, missing_sitemap_files, sitemap_files


def parse_all_html() -> dict[Path, dict[str, Any]]:
    all_pages: dict[Path, dict[str, Any]] = {}
    for file_path in sorted(DIST.rglob("*")):
        if file_path.is_file() and file_path.suffix.lower() in {".html", ".htm"}:
            text, error = read_utf8(file_path)
            if text is None:
                all_pages[file_path] = {"file": file_path, "utf8_error": error or ""}
                continue
            parser = PageParser()
            parser.feed(text)
            all_pages[file_path] = {
                "file": file_path,
                "html": text,
                "hrefs": parser.hrefs,
                "assets": parser.assets,
                "images": parser.images,
                "json_ld": parser.json_ld,
                "robots": parser.meta_robots,
                "noindex": "noindex" in parser.meta_robots.casefold(),
                "has_viewport": parser.has_viewport,
            }
    return all_pages


def display_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_redirects(base_host: str) -> tuple[list[dict[str, str]], bool]:
    htaccess = DIST / ".htaccess"
    if not htaccess.exists():
        return [], False
    text, _ = read_utf8(htaccess)
    if text is None:
        return [{"source": ".htaccess", "target": "", "problem": "dist/.htaccess is not UTF-8 readable"}], True

    redirects: list[dict[str, str]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.match(r"Redirect(?:Match)?\s+301\s+(\S+)\s+(\S+)", line, re.I)
        if match:
            redirects.append({"source": match.group(1), "target": match.group(2), "rule": line})
            continue
        match = re.match(r"RewriteRule\s+(\S+)\s+(\S+)\s+\[([^\]]*R=301[^\]]*)\]", line, re.I)
        if match:
            source = match.group(1).strip("^$")
            if not source.startswith("/"):
                source = "/" + source
            redirects.append({"source": source, "target": match.group(2), "rule": line})

    redirect_sources = {r["source"]: r for r in redirects}
    problems: list[dict[str, str]] = []

    def target_as_source(target: str) -> str:
        parsed = urlparse(target)
        if parsed.scheme in {"http", "https"}:
            return parsed.path or "/"
        if target.startswith("/"):
            return target
        return "/" + target

    for redirect in redirects:
        source = redirect["source"]
        target = redirect["target"]
        normalized_target = target_as_source(target)
        if normalized_target in redirect_sources:
            problems.append({"source": source, "target": target, "problem": "redirect chain"})

        seen: set[str] = set()
        cursor = source
        while cursor in redirect_sources:
            if cursor in seen:
                problems.append({"source": source, "target": target, "problem": "redirect loop"})
                break
            seen.add(cursor)
            cursor = target_as_source(redirect_sources[cursor]["target"])

        target_parsed = urlparse(target)
        if target_parsed.scheme in {"http", "https"} and target_parsed.netloc and target_parsed.netloc != base_host:
            continue
        if target_parsed.scheme in {"http", "https"}:
            target_url = target
        else:
            target_url = f"https://{base_host}{target if target.startswith('/') else '/' + target}"
        target_file = url_to_dist_file(target_url)
        if not target_file.exists():
            problems.append({"source": source, "target": target, "problem": "missing redirect target"})

    return problems, True


def exposed_auxiliary_files() -> list[dict[str, str]]:
    exposed: list[dict[str, str]] = []
    for path in sorted(DIST.rglob("*")):
        rel_parts = path.relative_to(DIST).parts
        name = path.name
        if path.is_dir() and name in AUX_DIRS:
            exposed.append({"path": display_path(path), "type": "forbidden directory"})
            continue
        if not path.is_file():
            continue
        if any(part in AUX_DIRS for part in rel_parts[:-1]):
            exposed.append({"path": display_path(path), "type": "inside forbidden directory"})
            continue
        lower_name = name.lower()
        suffix = path.suffix.lower()
        if name in AUX_EXACT or lower_name.startswith(".env."):
            exposed.append({"path": display_path(path), "type": "forbidden exact file"})
        elif suffix == ".txt" and lower_name != "robots.txt":
            exposed.append({"path": display_path(path), "type": "forbidden txt"})
        elif suffix in AUX_EXTENSIONS:
            exposed.append({"path": display_path(path), "type": f"forbidden {suffix}"})
    return exposed


def check_utf8_and_mojibake() -> tuple[bool, bool, list[dict[str, str]], list[dict[str, str]]]:
    utf8_errors: list[dict[str, str]] = []
    mojibake: list[dict[str, str]] = []
    for path in sorted(DIST.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        text, error = read_utf8(path)
        if text is None:
            utf8_errors.append({"path": display_path(path), "error": error or "UTF-8 decode error"})
            continue
        hits = [marker for marker in MOJIBAKE_MARKERS if marker in text]
        if hits:
            mojibake.append({"path": display_path(path), "markers": ", ".join(hits[:5])})
    return not utf8_errors, not mojibake, utf8_errors, mojibake


def duplicate_groups(pages: dict[str, dict[str, Any]], key: str) -> list[dict[str, Any]]:
    grouped: dict[str, list[str]] = defaultdict(list)
    for url, page in pages.items():
        value = page.get(key, "")
        if value:
            grouped[value].append(url)
    return [{"value": value, "pages": urls} for value, urls in grouped.items() if len(urls) > 1]


def make_txt_report(report: dict[str, Any]) -> str:
    status = report["status"]
    summary = report["summary"]
    lines = [f"П.14 Фінальний технічний контроль після оптимізації — {status}", "", "Звіт:"]
    labels = [
        ("html_files_checked", "HTML/HTM-файлів перевірено"),
        ("sitemap_url_count", "URL у sitemap.xml"),
        ("sitemap_html_files_found", "HTML-файлів знайдено для sitemap URL"),
        ("broken_internal_links", "Broken internal links"),
        ("missing_assets", "Missing assets"),
        ("json_ld_parse_errors", "JSON-LD parse errors"),
        ("noindex_urls_in_sitemap", "Noindex URLs у sitemap"),
        ("internal_links_to_noindex_pages", "Internal links to noindex pages"),
        ("duplicate_titles", "Duplicate titles"),
        ("duplicate_descriptions", "Duplicate descriptions"),
        ("duplicate_h1", "Duplicate H1"),
        ("indexable_pages_with_non_self_canonical", "Indexable pages with non-self canonical"),
        ("redirect_chains", "Redirect chains"),
        ("redirect_loops", "Redirect loops"),
        ("missing_redirect_targets", "Missing redirect targets"),
        ("exposed_auxiliary_files", "Exposed auxiliary files"),
        ("missing_viewport", "Missing viewport"),
        ("images_without_width_height", "Images without width/height"),
    ]
    for key, label in labels:
        lines.append(f"- {label}: {summary[key]}")
    lines.extend(
        [
            f"- HTML/CSS/XML/TXT читаються як UTF-8: {'так' if summary['utf8_readable'] else 'ні'}",
            f"- кирилиця не зіпсована: {'так' if summary['cyrillic_not_damaged'] else 'ні'}",
            f"- production-файли під час аудиту не редагувались: {'так' if summary['production_files_unchanged'] else 'ні'}",
            f"- створено JSON-звіт аудиту: {'так' if summary['json_report_created'] else 'ні'}",
            f"- створено TXT-звіт аудиту: {'так' if summary['txt_report_created'] else 'ні'}",
        ]
    )
    if report.get("notes"):
        lines.extend(["", "Примітки:"])
        lines.extend(f"- {note}" for note in report["notes"])

    tables = [
        ("Broken internal links", "Сторінка | href | причина", "broken_internal_links", ["page", "href", "reason"]),
        ("Missing assets", "Сторінка | asset | причина", "missing_assets", ["page", "asset", "reason"]),
        ("JSON-LD parse errors", "Сторінка | помилка", "json_ld_parse_errors", ["page", "error"]),
        ("Noindex URLs у sitemap", "URL | файл | robots meta", "noindex_urls_in_sitemap", ["url", "file", "robots_meta"]),
        ("Internal links to noindex pages", "Сторінка-джерело | href | noindex target", "internal_links_to_noindex_pages", ["source_page", "href", "noindex_target"]),
        ("Duplicate titles", "Title | сторінки", "duplicate_titles", ["title", "pages"]),
        ("Duplicate descriptions", "Description | сторінки", "duplicate_descriptions", ["description", "pages"]),
        ("Duplicate H1", "H1 | сторінки", "duplicate_h1", ["h1", "pages"]),
        ("Non-self canonical", "Сторінка | canonical", "non_self_canonical", ["page", "canonical"]),
        ("Redirect chains / loops / missing targets", "Source | Target | проблема", "redirect_problems", ["source", "target", "problem"]),
        ("Exposed auxiliary files", "Шлях | тип", "exposed_auxiliary_files", ["path", "type"]),
        ("Missing viewport", "Сторінка", "missing_viewport", ["page"]),
        ("Images without width/height", "Сторінка | img src | width | height", "images_without_width_height", ["page", "img_src", "width", "height"]),
    ]
    details = report["details"]
    for title, header, key, fields in tables:
        rows = details.get(key, [])
        if not rows:
            continue
        lines.extend(["", f"{title}:", header])
        for row in rows:
            values = row.get("pages", row.get("value")) if key.startswith("duplicate_") else None
            if key == "duplicate_titles":
                lines.append(f"{row['title']} | {', '.join(row['pages'])}")
            elif key == "duplicate_descriptions":
                lines.append(f"{row['description']} | {', '.join(row['pages'])}")
            elif key == "duplicate_h1":
                lines.append(f"{row['h1']} | {', '.join(row['pages'])}")
            else:
                lines.append(" | ".join(str(row.get(field, "")) for field in fields))
    if details.get("utf8_errors"):
        lines.extend(["", "UTF-8 decode errors:", "Шлях | помилка"])
        for row in details["utf8_errors"]:
            lines.append(f"{row.get('path', '')} | {row.get('error', '')}")
    if details.get("mojibake_markers"):
        lines.extend(["", "Mojibake / пошкоджена кирилиця:", "Шлях | маркери"])
        for row in details["mojibake_markers"]:
            lines.append(f"{row.get('path', '')} | {row.get('markers', '')}")
    return "\n".join(lines) + "\n"


def main() -> int:
    AUDITS.mkdir(exist_ok=True)
    before = fingerprint_dist()
    notes: list[str] = []

    sitemap_urls, base_host = parse_sitemap()
    sitemap_pages, missing_sitemap_files, sitemap_files = parse_pages(sitemap_urls)
    all_pages = parse_all_html()

    broken_internal_links: list[dict[str, str]] = []
    missing_assets: list[dict[str, str]] = []
    json_ld_parse_errors: list[dict[str, str]] = []
    noindex_urls_in_sitemap: list[dict[str, str]] = []
    internal_links_to_noindex_pages: list[dict[str, str]] = []
    non_self_canonical: list[dict[str, str]] = []
    missing_viewport: list[dict[str, str]] = []
    images_without_dimensions: list[dict[str, str]] = []

    url_by_file = {page["file"].resolve(): url for url, page in sitemap_pages.items()}
    noindex_files = {page["file"].resolve(): url for url, page in sitemap_pages.items() if page["noindex"]}
    all_noindex_files = {path.resolve(): display_path(path) for path, page in all_pages.items() if page.get("noindex")}

    for page_file, page in all_pages.items():
        if page.get("utf8_error"):
            continue
        page_url = url_by_file.get(page_file.resolve(), dist_file_to_url(page_file, base_host))
        page_display = display_path(page_file)
        if not page["has_viewport"]:
            missing_viewport.append({"page": page_display})

        for _, href in page["hrefs"]:
            target_file, _ = local_target_to_file(href, page_url, base_host)
            if target_file is None:
                continue
            if not target_file.exists():
                broken_internal_links.append({"page": page_display, "href": href, "reason": "local HTML target not found"})

        for _, asset, reason in page["assets"]:
            target = asset_to_file(asset, page_url, base_host)
            if target is not None and not target.exists():
                missing_assets.append({"page": page_display, "asset": asset, "reason": reason + " target not found"})

        for idx, blob in enumerate(page["json_ld"], start=1):
            try:
                parsed = json.loads(blob)
                if not isinstance(parsed, (dict, list)):
                    raise ValueError("JSON-LD root is not object or array")
            except Exception as exc:
                json_ld_parse_errors.append({"page": page_display, "error": f"JSON-LD #{idx}: {exc}"})

        for image in page["images"]:
            if not image.get("width") or not image.get("height"):
                images_without_dimensions.append(
                    {
                        "page": page_display,
                        "img_src": image.get("src", ""),
                        "width": image.get("width", ""),
                        "height": image.get("height", ""),
                    }
                )

    for url, page in sitemap_pages.items():
        page_file = page["file"]
        page_display = display_path(page_file)
        if page["noindex"]:
            noindex_urls_in_sitemap.append({"url": url, "file": page_display, "robots_meta": page["robots"]})

        canonical = page["canonical"]
        canonical_abs = urljoin(url, canonical) if canonical else ""
        canon_parsed = urlparse(canonical_abs)
        url_parsed = urlparse(url)
        canon_norm = canon_parsed._replace(query="", fragment="").geturl().rstrip("/")
        url_norm = url_parsed._replace(query="", fragment="").geturl().rstrip("/")
        if not canonical_abs or canon_norm != url_norm:
            non_self_canonical.append({"page": page_display, "canonical": canonical or "(missing)"})

        for _, href in page["hrefs"]:
            target_file, _ = local_target_to_file(href, url, base_host)
            if target_file is None:
                continue
            if not target_file.exists():
                broken_internal_links.append({"page": page_display, "href": href, "reason": "local HTML target not found"})
            elif target_file.resolve() in all_noindex_files:
                internal_links_to_noindex_pages.append(
                    {
                        "source_page": page_display,
                        "href": href,
                        "noindex_target": all_noindex_files[target_file.resolve()],
                    }
                )

    for item in missing_sitemap_files:
        broken_internal_links.append(
            {
                "page": "dist/sitemap.xml",
                "href": item["url"],
                "reason": f"sitemap URL local HTML not found: {item.get('expected_file', '')}",
            }
        )

    duplicate_titles_raw = duplicate_groups(sitemap_pages, "title")
    duplicate_descriptions_raw = duplicate_groups(sitemap_pages, "description")
    duplicate_h1_raw = duplicate_groups(sitemap_pages, "h1")
    duplicate_titles = [{"title": row["value"], "pages": row["pages"]} for row in duplicate_titles_raw]
    duplicate_descriptions = [{"description": row["value"], "pages": row["pages"]} for row in duplicate_descriptions_raw]
    duplicate_h1 = [{"h1": row["value"], "pages": row["pages"]} for row in duplicate_h1_raw]

    redirect_problems, htaccess_present = check_redirects(base_host)
    if not htaccess_present:
        notes.append("dist/.htaccess відсутній; redirect-перевірки рахуються як 0, оскільки redirect-правил у dist немає.")

    redirect_chains = [p for p in redirect_problems if p["problem"] == "redirect chain"]
    redirect_loops = [p for p in redirect_problems if p["problem"] == "redirect loop"]
    missing_redirect_targets = [p for p in redirect_problems if p["problem"] == "missing redirect target"]

    exposed = exposed_auxiliary_files()
    utf8_readable, cyrillic_not_damaged, utf8_errors, mojibake = check_utf8_and_mojibake()
    after = fingerprint_dist()
    production_unchanged = before == after

    summary = {
        "html_files_checked": sum(1 for p in all_pages if p.suffix.lower() in {".html", ".htm"}),
        "sitemap_url_count": len(sitemap_urls),
        "sitemap_html_files_found": len(sitemap_files),
        "broken_internal_links": len(broken_internal_links),
        "missing_assets": len(missing_assets),
        "json_ld_parse_errors": len(json_ld_parse_errors),
        "noindex_urls_in_sitemap": len(noindex_urls_in_sitemap),
        "internal_links_to_noindex_pages": len(internal_links_to_noindex_pages),
        "duplicate_titles": len(duplicate_titles),
        "duplicate_descriptions": len(duplicate_descriptions),
        "duplicate_h1": len(duplicate_h1),
        "indexable_pages_with_non_self_canonical": len(non_self_canonical),
        "redirect_chains": len(redirect_chains),
        "redirect_loops": len(redirect_loops),
        "missing_redirect_targets": len(missing_redirect_targets),
        "exposed_auxiliary_files": len(exposed),
        "missing_viewport": len(missing_viewport),
        "images_without_width_height": len(images_without_dimensions),
        "utf8_readable": utf8_readable,
        "cyrillic_not_damaged": cyrillic_not_damaged,
        "production_files_unchanged": production_unchanged,
        "json_report_created": True,
        "txt_report_created": True,
    }

    good = (
        all(
            summary[key] == 0
            for key in [
                "broken_internal_links",
                "missing_assets",
                "json_ld_parse_errors",
                "noindex_urls_in_sitemap",
                "internal_links_to_noindex_pages",
                "duplicate_titles",
                "duplicate_descriptions",
                "duplicate_h1",
                "indexable_pages_with_non_self_canonical",
                "redirect_chains",
                "redirect_loops",
                "missing_redirect_targets",
                "exposed_auxiliary_files",
                "missing_viewport",
                "images_without_width_height",
            ]
        )
        and utf8_readable
        and cyrillic_not_damaged
        and production_unchanged
    )

    report = {
        "audit": "П.14 Фінальний технічний контроль після оптимізації",
        "status": "ДОБРЕ" if good else "НЕ ДОБРЕ",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "dist": display_path(DIST),
        "summary": summary,
        "notes": notes,
        "details": {
            "missing_sitemap_html_files": missing_sitemap_files,
            "broken_internal_links": broken_internal_links,
            "missing_assets": missing_assets,
            "json_ld_parse_errors": json_ld_parse_errors,
            "noindex_urls_in_sitemap": noindex_urls_in_sitemap,
            "internal_links_to_noindex_pages": internal_links_to_noindex_pages,
            "duplicate_titles": duplicate_titles,
            "duplicate_descriptions": duplicate_descriptions,
            "duplicate_h1": duplicate_h1,
            "non_self_canonical": non_self_canonical,
            "redirect_problems": redirect_problems,
            "exposed_auxiliary_files": exposed,
            "missing_viewport": missing_viewport,
            "images_without_width_height": images_without_dimensions,
            "utf8_errors": utf8_errors,
            "mojibake_markers": mojibake,
        },
    }

    JSON_REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    TXT_REPORT.write_text(make_txt_report(report), encoding="utf-8")
    print(f"Status: {report['status']}")
    print(f"JSON: {JSON_REPORT.relative_to(ROOT)}")
    print(f"TXT: {TXT_REPORT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
