from __future__ import annotations

import csv
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent
CSV_PATH = ROOT / "audit-url-map.csv"
MD_PATH = ROOT / "audit-url-map.md"
REPORT_PATH = ROOT / "validation-report.md"
SITEMAP_PATH = ROOT / "sitemap.xml"

EXCLUDED_DIRS = {".git", "node_modules", "dist", "build", "__pycache__"}
REQUIRED_COLUMNS = [
    "file_path",
    "page_url",
    "canonical_url",
    "meta_robots",
    "h1",
    "title",
    "meta_description",
    "in_sitemap",
    "sitemap_url",
    "has_visible_updated_date",
    "has_json_ld",
    "schema_types",
    "detected_page_type",
    "target_status_suggestion",
    "notes",
]
YES_NO_COLUMNS = {"in_sitemap", "has_visible_updated_date", "has_json_ld"}
YES_NO_VALUES = {"YES", "NO"}
STATUS_VALUES = {
    "review_index",
    "review_noindex",
    "keep_noindex",
    "needs_manual_review",
}
PAGE_TYPES = {"article", "hub", "service", "contact", "error", "technical", "unknown"}
REQUIRED_MD_SECTIONS = [
    "# URL Map Audit",
    "## Summary",
    "## Noindex pages found in sitemap",
    "## Index pages missing from sitemap",
    "## Pages missing canonical",
    "## Pages missing H1",
    "## Pages with JSON-LD parse errors",
    "## Pages with possible encoding problems",
]
REQUIRED_MD_METRICS = [
    "total_html_files",
    "total_index_follow",
    "total_noindex",
    "total_in_sitemap",
    "noindex_in_sitemap_count",
    "index_not_in_sitemap_count",
    "missing_canonical_count",
    "missing_h1_count",
    "missing_meta_description_count",
    "missing_updated_date_count",
    "json_ld_parse_error_count",
]
ENCODING_MARKERS = ["Ð", "Ñ", "�", "РЈ", "Р°", "С‚", "\\u043", "\\u044"]
ALLOWED_GIT_PATHS = {
    "audit-url-map.csv",
    "audit-url-map.md",
    "sitemap.xml",
    "sitemap-noindex-fix-report.md",
    "validate_url_map.py",
    "validation-report.md",
}
CRITICAL_SUFFIXES = {
    ".html",
    ".css",
    ".js",
    ".xml",
    ".yaml",
    ".yml",
    ".toml",
    ".ini",
    ".cfg",
    ".conf",
    ".json",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".ico",
    ".bmp",
    ".avif",
    ".htaccess",
}
CRITICAL_NAMES = {"sitemap.xml", "robots.txt", "render.yaml", "package.json", "package-lock.json"}
HUB_STEMS = {"index", "dokumenty", "sortuvannya", "zbir", "logistyka", "vidhody", "kudy-zdaty", "pererobka", "utylizaciya"}
SERVICE_PREFIXES = (
    "utilizaciya-",
    "utylizaciya-",
    "utylizaciya-dlya-",
    "utilizaciya-dlya-",
)
ENCODING_PATTERN = re.compile("|".join(re.escape(marker) for marker in ENCODING_MARKERS))
WHITESPACE_PATTERN = re.compile(r"\s+")


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.h1_parts: list[str] = []
        self.visible_parts: list[str] = []
        self.json_ld_blocks: list[str] = []
        self.meta_robots = ""
        self.meta_description = ""
        self.canonical = ""
        self._in_title = False
        self._capture_h1 = False
        self._h1_seen = False
        self._suppressed_depth = 0
        self._capture_json_ld = False
        self._json_ld_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_map = {name.lower(): (value or "") for name, value in attrs}
        tag = tag.lower()
        if tag == "title":
            self._in_title = True
        if tag == "h1" and not self._h1_seen:
            self._capture_h1 = True
        if tag in {"script", "style", "noscript", "template"}:
            self._suppressed_depth += 1
        if tag == "meta":
            name = attrs_map.get("name", "").strip().lower()
            content = attrs_map.get("content", "").strip()
            if name == "robots" and not self.meta_robots:
                self.meta_robots = content
            if name == "description" and not self.meta_description:
                self.meta_description = content
        if tag == "link":
            rel_tokens = {token.strip().lower() for token in attrs_map.get("rel", "").split() if token.strip()}
            href = attrs_map.get("href", "").strip()
            if "canonical" in rel_tokens and href and not self.canonical:
                self.canonical = href
        if tag == "script" and attrs_map.get("type", "").strip().lower() == "application/ld+json":
            self._capture_json_ld = True
            self._json_ld_parts = []

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self._in_title = False
        if tag == "h1" and self._capture_h1:
            self._capture_h1 = False
            self._h1_seen = True
        if tag in {"script", "style", "noscript", "template"} and self._suppressed_depth:
            self._suppressed_depth -= 1
        if tag == "script" and self._capture_json_ld:
            self.json_ld_blocks.append("".join(self._json_ld_parts).strip())
            self._capture_json_ld = False
            self._json_ld_parts = []

    def handle_data(self, data: str) -> None:
        if not data:
            return
        if self._in_title:
            self.title_parts.append(data)
        if self._capture_h1:
            self.h1_parts.append(data)
        if self._capture_json_ld:
            self._json_ld_parts.append(data)
        if self._suppressed_depth == 0:
            self.visible_parts.append(data)


def normalize_space(value: str) -> str:
    return WHITESPACE_PATTERN.sub(" ", value).strip()


def normalize_rel_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def iter_html_files() -> list[Path]:
    html_files: list[Path] = []
    for path in ROOT.rglob("*.html"):
        rel_parts = path.relative_to(ROOT).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts):
            continue
        html_files.append(path)
    return sorted(html_files)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def find_encoding_markers(content: str) -> list[str]:
    return sorted({match.group(0) for match in ENCODING_PATTERN.finditer(content)})


def parse_sitemap_urls(errors: list[str] | None = None) -> set[str]:
    if not SITEMAP_PATH.exists():
        return set()
    try:
        root = ET.fromstring(SITEMAP_PATH.read_text(encoding="utf-8-sig", errors="replace"))
    except ET.ParseError as exc:
        if errors is not None:
            errors.append(f"sitemap.xml could not be parsed: {exc}.")
        return set()
    urls: set[str] = set()
    for element in root.iter():
        if element.tag.endswith("loc") and element.text:
            urls.add(element.text.strip())
    return urls


def detect_base_url(sitemap_urls: set[str]) -> str:
    for url in sorted(sitemap_urls):
        parsed = urlparse(url)
        if parsed.scheme and parsed.netloc:
            return f"{parsed.scheme}://{parsed.netloc}".rstrip("/")
    return ""


def build_page_url(rel_path: str, base_url: str) -> str:
    clean = rel_path.replace("\\", "/")
    if not base_url:
        return clean
    if clean == "index.html":
        return base_url
    if clean.endswith("/index.html"):
        return f"{base_url}/{clean[:-10].strip('/')}".rstrip("/") + "/"
    return f"{base_url}/{clean}"


def has_noindex(meta_robots: str) -> bool:
    return "noindex" in meta_robots.lower()


def collect_json_ld_types(node: Any, result: set[str]) -> None:
    if isinstance(node, dict):
        value = node.get("@type")
        if isinstance(value, str) and value.strip():
            result.add(value.strip())
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, str) and item.strip():
                    result.add(item.strip())
        for child in node.values():
            collect_json_ld_types(child, result)
    elif isinstance(node, list):
        for item in node:
            collect_json_ld_types(item, result)


def extract_schema_types(blocks: list[str]) -> tuple[str, str, bool]:
    if not blocks:
        return "NO", "", False
    parsed_types: set[str] = set()
    parse_error = False
    for block in blocks:
        if not block.strip():
            continue
        try:
            payload = json.loads(block)
        except json.JSONDecodeError:
            parse_error = True
            continue
        collect_json_ld_types(payload, parsed_types)
    if parse_error:
        return "YES", "PARSE_ERROR", True
    return "YES", "; ".join(sorted(parsed_types)), False


def detect_page_type(rel_path: str, title: str, h1: str) -> str:
    stem = Path(rel_path).stem.lower()
    combined = f"{title} {h1}".lower()
    if stem == "404":
        return "error"
    if stem == "kontakty" or "контакт" in combined:
        return "contact"
    if stem in HUB_STEMS or rel_path == "index.html" or rel_path.endswith("/index.html"):
        return "hub"
    if stem.startswith(SERVICE_PREFIXES) or "послуг" in combined or "утилізація для" in combined:
        return "service"
    if stem.startswith(("audit", "validation")):
        return "technical"
    if title or h1:
        return "article"
    return "unknown"


def suggest_target_status(
    noindex: bool,
    in_sitemap: bool,
    page_type: str,
    has_canonical: bool,
    has_h1: bool,
    has_title: bool,
    has_meta_description: bool,
    json_ld_parse_error: bool,
) -> str:
    if noindex:
        return "review_noindex" if in_sitemap else "keep_noindex"
    if page_type == "unknown" or not has_canonical or not has_h1 or not has_title or not has_meta_description or json_ld_parse_error:
        return "needs_manual_review"
    return "review_index"


def parse_page(path: Path, sitemap_urls: set[str], base_url: str) -> dict[str, str]:
    rel_path = normalize_rel_path(path)
    parser = PageParser()
    parser.feed(read_text(path))
    parser.close()

    title = normalize_space("".join(parser.title_parts))
    h1 = normalize_space("".join(parser.h1_parts))
    meta_robots = normalize_space(parser.meta_robots)
    meta_description = normalize_space(parser.meta_description)
    canonical = normalize_space(parser.canonical)
    visible_text = normalize_space(" ".join(parser.visible_parts))
    page_url = canonical or build_page_url(rel_path, base_url)
    sitemap_url = canonical if canonical in sitemap_urls else page_url if page_url in sitemap_urls else ""
    in_sitemap = sitemap_url != ""
    has_visible_updated_date = "YES" if "Оновлено:" in visible_text else "NO"
    has_json_ld, schema_types, json_ld_parse_error = extract_schema_types(parser.json_ld_blocks)
    page_type = detect_page_type(rel_path, title, h1)
    noindex = has_noindex(meta_robots)
    possible_encoding_issue = bool(find_encoding_markers("\n".join([title, h1, meta_description, visible_text])))

    notes: list[str] = []
    if not canonical:
        notes.append("missing canonical")
    if not h1:
        notes.append("missing h1")
    if not title:
        notes.append("missing title")
    if not meta_description:
        notes.append("missing meta description")
    if noindex and in_sitemap:
        notes.append("noindex but in sitemap")
    if not noindex and not in_sitemap:
        notes.append("index but not in sitemap")
    if json_ld_parse_error:
        notes.append("json-ld parse error")
    if has_visible_updated_date == "NO":
        notes.append("missing updated date")
    if possible_encoding_issue:
        notes.append("possible encoding issue")

    return {
        "file_path": rel_path,
        "page_url": page_url,
        "canonical_url": canonical,
        "meta_robots": meta_robots,
        "h1": h1,
        "title": title,
        "meta_description": meta_description,
        "in_sitemap": "YES" if in_sitemap else "NO",
        "sitemap_url": sitemap_url,
        "has_visible_updated_date": has_visible_updated_date,
        "has_json_ld": has_json_ld,
        "schema_types": schema_types,
        "detected_page_type": page_type,
        "target_status_suggestion": suggest_target_status(
            noindex,
            in_sitemap,
            page_type,
            bool(canonical),
            bool(h1),
            bool(title),
            bool(meta_description),
            json_ld_parse_error,
        ),
        "notes": "; ".join(notes),
    }


def write_csv(rows: list[dict[str, str]]) -> None:
    with CSV_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REQUIRED_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def rows_with_note(rows: Iterable[dict[str, str]], note: str) -> list[str]:
    result: list[str] = []
    for row in rows:
        notes = {item.strip() for item in row["notes"].split(";") if item.strip()}
        if note in notes:
            result.append(row["file_path"])
    return result


def render_section(items: list[str]) -> list[str]:
    if not items:
        return ["None", ""]
    return [*(f"- {item}" for item in items), ""]


def resolve_row_url(row: dict[str, str]) -> str:
    for key in ("canonical_url", "page_url", "sitemap_url"):
        value = row.get(key, "").strip()
        if value:
            return value
    return ""


def compute_sitemap_issue_urls(rows: Iterable[dict[str, str]]) -> tuple[list[str], list[str]]:
    by_url: dict[str, dict[str, bool]] = {}
    for row in rows:
        url = resolve_row_url(row)
        if not url:
            continue
        state = by_url.setdefault(url, {"has_noindex": False, "has_index": False, "in_sitemap": False})
        noindex = has_noindex(row["meta_robots"])
        state["has_noindex"] = state["has_noindex"] or noindex
        state["has_index"] = state["has_index"] or not noindex
        state["in_sitemap"] = state["in_sitemap"] or row["in_sitemap"] == "YES"

    noindex_in_sitemap = sorted(url for url, state in by_url.items() if state["has_noindex"] and state["in_sitemap"])
    index_not_in_sitemap = sorted(
        url
        for url, state in by_url.items()
        if state["has_index"] and not state["has_noindex"] and not state["in_sitemap"]
    )
    return noindex_in_sitemap, index_not_in_sitemap


def build_md_metrics(rows: list[dict[str, str]], html_count: int) -> dict[str, int]:
    noindex_in_sitemap_urls, index_not_in_sitemap_urls = compute_sitemap_issue_urls(rows)
    total_noindex = sum(1 for row in rows if has_noindex(row["meta_robots"]))
    total_index_follow = len(rows) - total_noindex
    total_in_sitemap = sum(1 for row in rows if row["in_sitemap"] == "YES")
    return {
        "total_html_files": html_count,
        "total_index_follow": total_index_follow,
        "total_noindex": total_noindex,
        "total_in_sitemap": total_in_sitemap,
        "noindex_in_sitemap_count": len(noindex_in_sitemap_urls),
        "index_not_in_sitemap_count": len(index_not_in_sitemap_urls),
        "missing_canonical_count": sum(1 for row in rows if not row["canonical_url"]),
        "missing_h1_count": sum(1 for row in rows if not row["h1"]),
        "missing_meta_description_count": sum(1 for row in rows if not row["meta_description"]),
        "missing_updated_date_count": sum(1 for row in rows if row["has_visible_updated_date"] == "NO"),
        "json_ld_parse_error_count": sum(1 for row in rows if row["schema_types"] == "PARSE_ERROR"),
    }


def write_markdown(rows: list[dict[str, str]], html_count: int) -> None:
    metrics = build_md_metrics(rows, html_count)
    noindex_in_sitemap_urls, index_not_in_sitemap_urls = compute_sitemap_issue_urls(rows)
    lines = ["# URL Map Audit", "", "## Summary", ""]
    for key in REQUIRED_MD_METRICS:
        lines.append(f"- {key}: {metrics[key]}")
    lines.extend(["", "## Noindex pages found in sitemap", ""])
    lines.extend(render_section(noindex_in_sitemap_urls))
    lines.extend(["## Index pages missing from sitemap", ""])
    lines.extend(render_section(index_not_in_sitemap_urls))
    lines.extend(["## Pages missing canonical", ""])
    lines.extend(render_section([row["file_path"] for row in rows if not row["canonical_url"]]))
    lines.extend(["## Pages missing H1", ""])
    lines.extend(render_section([row["file_path"] for row in rows if not row["h1"]]))
    lines.extend(["## Pages with JSON-LD parse errors", ""])
    lines.extend(render_section([row["file_path"] for row in rows if row["schema_types"] == "PARSE_ERROR"]))
    lines.extend(["## Pages with possible encoding problems", ""])
    lines.extend(render_section(rows_with_note(rows, "possible encoding issue")))
    MD_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def parse_md_metrics(md_text: str) -> dict[str, int]:
    metrics: dict[str, int] = {}
    for line in md_text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("- ") or ":" not in stripped:
            continue
        key, value = stripped[2:].split(":", 1)
        value = value.strip()
        if value.isdigit():
            metrics[key.strip()] = int(value)
    return metrics


def run_git_status() -> tuple[list[str], str | None]:
    try:
        completed = subprocess.run(
            ["git", "-C", str(ROOT), "status", "--short"],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except FileNotFoundError:
        return [], "git executable not found"
    stdout = completed.stdout.rstrip("\r\n")
    stderr = completed.stderr.strip()
    if completed.returncode != 0:
        return [], stderr or stdout or f"git status failed with code {completed.returncode}"
    return stdout.splitlines() if stdout else [], None


def parse_git_changed_paths(status_lines: Iterable[str]) -> list[str]:
    changed: list[str] = []
    for line in status_lines:
        if not line.strip():
            continue
        payload = line[3:] if len(line) > 3 else line
        if " -> " in payload:
            payload = payload.split(" -> ", 1)[1]
        changed.append(payload.strip().strip('"').replace("\\", "/"))
    return changed


def path_is_critical_forbidden(path: str) -> bool:
    path_obj = Path(path)
    return path_obj.suffix.lower() in CRITICAL_SUFFIXES or path_obj.name.lower() in CRITICAL_NAMES


def parse_csv(errors: list[str]) -> tuple[list[dict[str, str]], int, list[str]]:
    if not CSV_PATH.exists():
        return [], 0, []
    rows: list[dict[str, str]] = []
    file_paths: list[str] = []
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        try:
            header = next(reader)
        except StopIteration:
            errors.append("audit-url-map.csv is empty.")
            return [], 0, []
        if header != REQUIRED_COLUMNS:
            errors.append("CSV header does not match the required columns exactly.")
        total_rows = 0
        for row_number, raw_row in enumerate(reader, start=2):
            if not raw_row or not any(cell.strip() for cell in raw_row):
                continue
            total_rows += 1
            if len(raw_row) != len(REQUIRED_COLUMNS):
                errors.append(
                    f"CSV row {row_number} has {len(raw_row)} columns instead of {len(REQUIRED_COLUMNS)}."
                )
                continue
            row = dict(zip(REQUIRED_COLUMNS, raw_row))
            rows.append(row)
            file_paths.append(row["file_path"].replace("\\", "/").strip())
    return rows, total_rows, file_paths


def build_validation_state() -> dict[str, Any]:
    critical_failures: list[str] = []
    errors: list[str] = []
    warnings: list[str] = []
    git_status_lines, git_error = run_git_status()
    if git_error:
        errors.append(f"Git status unavailable: {git_error}.")
        git_status_rendered = f"git status --short unavailable: {git_error}"
    else:
        git_status_rendered = "\n".join(git_status_lines) if git_status_lines else "(clean)"
        changed_paths = parse_git_changed_paths(git_status_lines)
        unexpected_paths = [path for path in changed_paths if path not in ALLOWED_GIT_PATHS]
        forbidden_paths = [path for path in unexpected_paths if path_is_critical_forbidden(path)]
        if forbidden_paths:
            critical_failures.append("Forbidden site files changed: " + ", ".join(sorted(forbidden_paths)))
        if unexpected_paths:
            errors.append("Unexpected changed/created files found: " + ", ".join(sorted(unexpected_paths)))

    for path in (CSV_PATH, MD_PATH, ROOT / "validate_url_map.py"):
        if not path.exists():
            errors.append(f"Required file missing: {path.name}.")

    html_files = iter_html_files()
    html_rel_paths = {normalize_rel_path(path) for path in html_files}
    csv_rows, csv_row_count, csv_file_paths = parse_csv(errors)
    if csv_row_count != len(html_files):
        errors.append(f"CSV row count mismatch: {csv_row_count} rows vs {len(html_files)} HTML files.")

    csv_path_set = set(csv_file_paths)
    missing_from_csv = sorted(html_rel_paths - csv_path_set)
    missing_in_project = sorted(csv_path_set - html_rel_paths)
    if missing_from_csv:
        errors.append(f"HTML files missing from CSV file_path: {len(missing_from_csv)}.")
    if missing_in_project:
        errors.append(f"CSV contains non-existent file_path values: {len(missing_in_project)}.")

    sitemap_urls = parse_sitemap_urls(errors)

    pages_in_sitemap = 0
    noindex_pages = 0
    index_like_pages = 0
    missing_canonical = 0
    missing_h1 = 0
    missing_meta_description = 0
    missing_updated_date = 0
    json_ld_parse_errors = 0
    possible_encoding_pages = 0

    for row_number, row in enumerate(csv_rows, start=2):
        for column in YES_NO_COLUMNS:
            if row[column] not in YES_NO_VALUES:
                errors.append(f"CSV row {row_number} has invalid {column} value: {row[column]!r}.")
        if row["target_status_suggestion"] not in STATUS_VALUES:
            errors.append(
                f"CSV row {row_number} has invalid target_status_suggestion: {row['target_status_suggestion']!r}."
            )
        if row["detected_page_type"] not in PAGE_TYPES:
            errors.append(
                f"CSV row {row_number} has invalid detected_page_type: {row['detected_page_type']!r}."
            )

        url_candidates = [value.strip() for value in (row["canonical_url"], row["page_url"]) if value.strip()]
        in_actual_sitemap = any(candidate in sitemap_urls for candidate in url_candidates)
        declared_in_sitemap = row["in_sitemap"] == "YES"
        if declared_in_sitemap:
            pages_in_sitemap += 1
            if not in_actual_sitemap:
                errors.append(
                    f"CSV row {row_number} is marked in_sitemap=YES but canonical_url/page_url is absent from sitemap.xml."
                )
        elif in_actual_sitemap:
            errors.append(f"CSV row {row_number} is present in sitemap.xml but marked in_sitemap=NO.")

        if has_noindex(row["meta_robots"]):
            noindex_pages += 1
        else:
            index_like_pages += 1

        if not row["canonical_url"].strip():
            missing_canonical += 1
        if not row["h1"].strip():
            missing_h1 += 1
        if not row["meta_description"].strip():
            missing_meta_description += 1
        if row["has_visible_updated_date"] == "NO":
            missing_updated_date += 1
        if row["schema_types"] == "PARSE_ERROR":
            json_ld_parse_errors += 1
        if "possible encoding issue" in row["notes"].lower():
            possible_encoding_pages += 1

    noindex_in_sitemap_urls, index_not_in_sitemap_urls = compute_sitemap_issue_urls(csv_rows)
    noindex_pages_in_sitemap = len(noindex_in_sitemap_urls)
    index_missing_from_sitemap = len(index_not_in_sitemap_urls)

    if noindex_pages_in_sitemap:
        warnings.append(f"SEO/AIO issue: {noindex_pages_in_sitemap} noindex pages are present in sitemap.xml.")
    if index_missing_from_sitemap:
        warnings.append(f"SEO/AIO issue: {index_missing_from_sitemap} index-like pages are missing from sitemap.xml.")

    md_text = read_text(MD_PATH) if MD_PATH.exists() else ""
    csv_text = read_text(CSV_PATH) if CSV_PATH.exists() else ""
    md_metrics = parse_md_metrics(md_text)

    for section in REQUIRED_MD_SECTIONS:
        if section not in md_text:
            errors.append(f"audit-url-map.md is missing required section: {section}.")
    for metric in REQUIRED_MD_METRICS:
        if metric not in md_text:
            errors.append(f"audit-url-map.md is missing required metric label: {metric}.")

    expected_md_metrics = {
        "total_html_files": len(html_files),
        "total_index_follow": index_like_pages,
        "total_noindex": noindex_pages,
        "total_in_sitemap": pages_in_sitemap,
        "noindex_in_sitemap_count": noindex_pages_in_sitemap,
        "index_not_in_sitemap_count": index_missing_from_sitemap,
        "missing_canonical_count": missing_canonical,
        "missing_h1_count": missing_h1,
        "missing_meta_description_count": missing_meta_description,
        "missing_updated_date_count": missing_updated_date,
        "json_ld_parse_error_count": json_ld_parse_errors,
    }
    for key, expected in expected_md_metrics.items():
        actual = md_metrics.get(key)
        if actual is None:
            errors.append(f"audit-url-map.md is missing numeric metric: {key}.")
        elif actual != expected:
            errors.append(f"audit-url-map.md metric mismatch for {key}: {actual} vs expected {expected}.")

    csv_markers = find_encoding_markers(csv_text)
    md_markers = find_encoding_markers(md_text)
    if csv_markers:
        critical_failures.append(
            "Possible Cyrillic encoding corruption in audit-url-map.csv: " + ", ".join(csv_markers)
        )
    if md_markers:
        critical_failures.append(
            "Possible Cyrillic encoding corruption in audit-url-map.md: " + ", ".join(md_markers)
        )

    result = "PASS" if not critical_failures and not errors else "FAIL"
    if any(item.startswith("Forbidden site files changed:") for item in critical_failures):
        final_decision = "VALIDATION FAILED BECAUSE SITE FILES WERE MODIFIED"
    elif result == "PASS":
        final_decision = "AUDIT IS VALID"
    else:
        final_decision = "AUDIT NEEDS FIXES"

    return {
        "critical_failures": critical_failures,
        "errors": errors,
        "warnings": warnings,
        "html_count": len(html_files),
        "csv_rows": csv_row_count,
        "sitemap_urls": len(sitemap_urls),
        "index_like_pages": index_like_pages,
        "noindex_pages": noindex_pages,
        "pages_in_sitemap": pages_in_sitemap,
        "noindex_pages_in_sitemap": noindex_pages_in_sitemap,
        "index_missing_from_sitemap": index_missing_from_sitemap,
        "missing_canonical": missing_canonical,
        "missing_h1": missing_h1,
        "missing_meta_description": missing_meta_description,
        "missing_updated_date": missing_updated_date,
        "json_ld_parse_errors": json_ld_parse_errors,
        "possible_encoding_issues": possible_encoding_pages,
        "git_status": git_status_rendered,
        "result": result,
        "final_decision": final_decision,
    }


def write_validation_report(state: dict[str, Any]) -> None:
    lines = [
        "# Validation Report",
        "",
        "## Result",
        state["result"],
        "",
        "## Critical Failures",
    ]
    lines.extend(f"- {item}" for item in state["critical_failures"] or ["None"])
    lines.extend(["", "## Errors"])
    lines.extend(f"- {item}" for item in state["errors"] or ["None"])
    lines.extend(["", "## Warnings"])
    lines.extend(f"- {item}" for item in state["warnings"] or ["None"])
    lines.extend(
        [
            "",
            "## Counts",
            f"- HTML files found: {state['html_count']}",
            f"- CSV rows: {state['csv_rows']}",
            f"- Sitemap URLs: {state['sitemap_urls']}",
            f"- Index-like pages: {state['index_like_pages']}",
            f"- Noindex pages: {state['noindex_pages']}",
            f"- Pages in sitemap: {state['pages_in_sitemap']}",
            f"- Noindex pages in sitemap: {state['noindex_pages_in_sitemap']}",
            f"- Index pages missing from sitemap: {state['index_missing_from_sitemap']}",
            f"- Missing canonical: {state['missing_canonical']}",
            f"- Missing H1: {state['missing_h1']}",
            f"- Missing meta description: {state['missing_meta_description']}",
            f"- Missing visible updated date: {state['missing_updated_date']}",
            f"- JSON-LD parse errors: {state['json_ld_parse_errors']}",
            f"- Possible encoding issues: {state['possible_encoding_issues']}",
            "",
            "## Files changed or created",
            "```text",
            state["git_status"],
            "```",
            "",
            "## Final decision",
            state["final_decision"],
            "",
        ]
    )
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def build_audit_files() -> None:
    sitemap_urls = parse_sitemap_urls([])
    base_url = detect_base_url(sitemap_urls)
    rows = [parse_page(path, sitemap_urls, base_url) for path in iter_html_files()]
    write_csv(rows)
    write_markdown(rows, len(rows))


def main() -> int:
    build_audit_files()
    first_state = build_validation_state()
    write_validation_report(first_state)
    final_state = build_validation_state()
    write_validation_report(final_state)

    print(f"RESULT={final_state['result']}")
    print(f"HTML_FILES={final_state['html_count']}")
    print(f"CSV_ROWS={final_state['csv_rows']}")
    print(
        "FORBIDDEN_SITE_FILE_CHANGES="
        + ("YES" if any(item.startswith("Forbidden site files changed:") for item in final_state["critical_failures"]) else "NO")
    )
    print("CYRILLIC_ENCODING_ISSUES=" + ("YES" if any("Cyrillic encoding" in item for item in final_state["critical_failures"]) else "NO"))
    print(f"NOINDEX_IN_SITEMAP={final_state['noindex_pages_in_sitemap']}")
    print(f"INDEX_MISSING_FROM_SITEMAP={final_state['index_missing_from_sitemap']}")
    print(f"FINAL_DECISION={final_state['final_decision']}")
    return 0 if final_state["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())