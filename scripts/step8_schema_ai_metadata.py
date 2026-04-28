#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://guide.youreco.com.ua"
ROUTE_DIRS = ("articles", "logistyka", "pererobka", "sortuvannya", "utylizaciya")
HUB_FILES = {
    "index.html",
    "dokumenty.html",
    "sortuvannya.html",
    "zbir.html",
    "logistyka.html",
    "vidhody.html",
    "kudy-zdaty.html",
    "pererobka.html",
    "utylizaciya.html",
    "articles/index.html",
    "logistyka/index.html",
    "pererobka/index.html",
    "sortuvannya/index.html",
    "utylizaciya/index.html",
}
MOJIBAKE_MARKERS = ["Ð", "Ñ", "Р°", "Р±", "Р В", "СЂ", "вЂ", "�"]
EMOJI_RE = re.compile(
    r"[\U0001F300-\U0001FAD6\U0001F1E0-\U0001F1FF\u2600-\u27BF]",
    flags=re.UNICODE,
)


@dataclass
class Stats:
    html_checked: int = 0
    indexed_checked: int = 0
    jsonld_checked_before: int = 0
    jsonld_errors_before: int = 0
    jsonld_errors_after: int = 0
    canonical_mismatch_after: int = 0
    schema_url_mismatch_after: int = 0
    faq_without_visible_after: int = 0
    sitemap_url_count_after: int = 0
    sitemap_noindex_redirect_count_after: int = 0
    bom_issues_after: int = 0
    mojibake_issues_after: int = 0
    changed_files: list[str] | None = None


def all_source_html_files() -> list[Path]:
    files = sorted(ROOT.glob("*.html"))
    for route_dir in ROUTE_DIRS:
        idx = ROOT / route_dir / "index.html"
        if idx.exists():
            files.append(idx)
    return sorted(set(files))


def parse_sitemap_urls(sitemap_path: Path) -> list[str]:
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.fromstring(sitemap_path.read_text(encoding="utf-8"))
    return [loc.text.strip() for loc in root.findall("sm:url/sm:loc", ns) if loc.text]


def file_to_url(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return BASE_URL
    if rel.endswith("/index.html"):
        return f"{BASE_URL}/{rel[:-11]}"
    return f"{BASE_URL}/{rel}"


def url_to_file(url: str) -> Path:
    if url == BASE_URL:
        return ROOT / "index.html"
    rest = url.replace(f"{BASE_URL}/", "", 1)
    if "/" in rest and not rest.endswith(".html"):
        return ROOT / rest / "index.html"
    if rest and not rest.endswith(".html"):
        return ROOT / rest / "index.html"
    return ROOT / rest


def find_tag_content(pattern: str, text: str) -> str:
    m = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
    if not m:
        return ""
    value = m.group(1).strip()
    return re.sub(r"\s+", " ", value)


def get_meta_content(text: str, meta_name: str) -> str:
    for m in re.finditer(r"<meta\b[^>]*>", text, flags=re.IGNORECASE):
        tag = m.group(0)
        name_m = re.search(r'name=["\']([^"\']+)["\']', tag, flags=re.IGNORECASE)
        if not name_m or name_m.group(1).strip().lower() != meta_name.lower():
            continue
        content_m = re.search(r'content=["\'](.*?)["\']', tag, flags=re.IGNORECASE | re.DOTALL)
        if content_m:
            return re.sub(r"\s+", " ", content_m.group(1).strip())
    return ""


def get_refresh_redirect_url(content: str) -> str | None:
    refresh = re.search(r"<meta\b[^>]*http-equiv=[\"']refresh[\"'][^>]*>", content, flags=re.IGNORECASE)
    if not refresh:
        return None
    tag = refresh.group(0)
    content_m = re.search(r'content=["\'](.*?)["\']', tag, flags=re.IGNORECASE)
    if not content_m:
        return None
    raw = content_m.group(1)
    url_m = re.search(r"url\s*=\s*([^;]+)$", raw, flags=re.IGNORECASE)
    if not url_m:
        url_m = re.search(r"url\s*=\s*(.+)", raw, flags=re.IGNORECASE)
    if not url_m:
        return None
    target = url_m.group(1).strip().strip("'\"")
    if target.startswith("http://") or target.startswith("https://"):
        return target
    if target.startswith("/"):
        return f"{BASE_URL}{target}"
    return f"{BASE_URL}/{target}"


def has_visible_faq(content: str) -> bool:
    return bool(re.search(r"<h2[^>]*>\s*(FAQ|Часті запитання)", content, flags=re.IGNORECASE))


def extract_faq_items(content: str) -> list[dict[str, Any]]:
    section = re.search(
        r"<h2[^>]*>\s*(FAQ|Часті запитання).*?</h2>(.*?)</(section|div|main)>",
        content,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if not section:
        return []
    block = section.group(2)
    items: list[dict[str, Any]] = []
    for q, a in re.findall(
        r"<li>\s*<strong>(.*?)</strong>\s*<br\s*/?>\s*(.*?)</li>",
        block,
        flags=re.IGNORECASE | re.DOTALL,
    ):
        q_clean = strip_html(q)
        a_clean = strip_html(a)
        if q_clean and a_clean:
            items.append(
                {
                    "@type": "Question",
                    "name": q_clean,
                    "acceptedAnswer": {"@type": "Answer", "text": a_clean},
                }
            )
    return items[:10]


def strip_html(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def no_emoji(value: str) -> str:
    return EMOJI_RE.sub("", value).strip()


def schema_blocks(content: str) -> list[str]:
    return re.findall(
        r"<script[^>]*type=[\"']application/ld\+json[\"'][^>]*>\s*(.*?)\s*</script>",
        content,
        flags=re.IGNORECASE | re.DOTALL,
    )


def jsonld_before_errors(content: str, canonical: str) -> tuple[int, int]:
    blocks = schema_blocks(content)
    total = 0
    errors = 0
    for block in blocks:
        total += 1
        try:
            data = json.loads(block)
        except Exception:
            errors += 1
            continue
        nodes = data if isinstance(data, list) else [data]
        for node in nodes:
            if not isinstance(node, dict):
                errors += 1
                continue
            if node.get("@context") != "https://schema.org":
                errors += 1
            url = node.get("url")
            meop = node.get("mainEntityOfPage")
            meop_val = meop.get("@id") if isinstance(meop, dict) else meop
            if url and url != canonical:
                errors += 1
            if meop_val and meop_val != canonical:
                errors += 1
            text_fields = [
                str(node.get("headline", "")),
                str(node.get("description", "")),
                str(node.get("name", "")),
            ]
            if any(EMOJI_RE.search(v) for v in text_fields):
                errors += 1
            if any("/public/" in str(v) for v in (url, meop_val)):
                errors += 1
            if any(any(marker in v for marker in MOJIBAKE_MARKERS) for v in text_fields):
                errors += 1
    return total, errors


def build_schema(content: str, file_path: Path, canonical: str, title: str, h1: str, description: str) -> list[dict[str, Any]]:
    rel = file_path.relative_to(ROOT).as_posix()
    is_hub = rel in HUB_FILES
    page_type = "CollectionPage" if is_hub else "Article"
    headline = no_emoji(h1 or title)
    name = no_emoji(title or h1)
    descr = no_emoji(description)

    page_schema: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": page_type,
        "headline": headline,
        "name": name,
        "description": descr,
        "url": canonical,
        "mainEntityOfPage": canonical,
        "inLanguage": "uk-UA",
    }

    schemas: list[dict[str, Any]] = [page_schema]
    if has_visible_faq(content):
        faq_items = extract_faq_items(content)
        if faq_items:
            schemas.append(
                {
                    "@context": "https://schema.org",
                    "@type": "FAQPage",
                    "url": canonical,
                    "mainEntity": faq_items,
                    "inLanguage": "uk-UA",
                }
            )
    return schemas


def replace_or_add(pattern: str, replacement: str, text: str) -> str:
    if re.search(pattern, text, flags=re.IGNORECASE):
        return re.sub(pattern, replacement, text, count=1, flags=re.IGNORECASE)
    return text


def upsert_head_metadata(content: str, canonical: str, indexed: bool) -> str:
    robots_value = "index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" if indexed else "noindex, follow"

    if re.search(r'<meta[^>]+name=["\']robots["\']', content, flags=re.IGNORECASE):
        content = re.sub(
            r'<meta[^>]+name=["\']robots["\'][^>]*>',
            f'<meta name="robots" content="{robots_value}"/>',
            content,
            count=1,
            flags=re.IGNORECASE,
        )
    else:
        content = re.sub(r"</head>", f'<meta name="robots" content="{robots_value}"/>\n</head>', content, count=1, flags=re.IGNORECASE)

    if re.search(r'<link[^>]+rel=["\']canonical["\']', content, flags=re.IGNORECASE):
        content = re.sub(
            r'<link[^>]+rel=["\']canonical["\'][^>]*>',
            f'<link rel="canonical" href="{canonical}"/>',
            content,
            count=1,
            flags=re.IGNORECASE,
        )
    else:
        content = re.sub(r"</head>", f'<link rel="canonical" href="{canonical}"/>\n</head>', content, count=1, flags=re.IGNORECASE)

    if re.search(r'<meta[^>]+property=["\']og:url["\']', content, flags=re.IGNORECASE):
        content = re.sub(
            r'<meta[^>]+property=["\']og:url["\'][^>]*>',
            f'<meta property="og:url" content="{canonical}"/>',
            content,
            count=1,
            flags=re.IGNORECASE,
        )

    if re.search(r'<meta[^>]+name=["\']ai-content-url["\']', content, flags=re.IGNORECASE):
        content = re.sub(
            r'<meta[^>]+name=["\']ai-content-url["\'][^>]*>',
            f'<meta name="ai-content-url" content="{canonical}"/>',
            content,
            count=1,
            flags=re.IGNORECASE,
        )
    return content


def upsert_schema(content: str, schemas: list[dict[str, Any]]) -> str:
    content = re.sub(
        r"<script[^>]*type=[\"']application/ld\+json[\"'][^>]*>.*?</script>\s*",
        "",
        content,
        flags=re.IGNORECASE | re.DOTALL,
    )
    blocks = []
    for schema in schemas:
        blocks.append(
            '<script type="application/ld+json">'
            + json.dumps(schema, ensure_ascii=False, separators=(",", ":"))
            + "</script>"
        )
    insert = "\n".join(blocks) + "\n"
    return re.sub(r"</head>", insert + "</head>", content, count=1, flags=re.IGNORECASE)


def check_bom(path: Path) -> bool:
    return path.read_bytes().startswith(b"\xef\xbb\xbf")


def contains_mojibake(content: str) -> bool:
    return any(marker in content for marker in MOJIBAKE_MARKERS)


def main() -> None:
    stats = Stats(changed_files=[])
    sitemap_urls = parse_sitemap_urls(ROOT / "sitemap.xml")
    indexed_map = {url_to_file(url).resolve(): url for url in sitemap_urls}

    for file_path in all_source_html_files():
        stats.html_checked += 1
        content = file_path.read_text(encoding="utf-8")
        resolved = file_path.resolve()
        indexed = resolved in indexed_map
        refresh_target = get_refresh_redirect_url(content)
        is_noindex = "noindex" in get_meta_content(content, "robots").lower()
        canonical_target = indexed_map.get(resolved, file_to_url(file_path))
        if (is_noindex or refresh_target) and refresh_target:
            canonical_target = refresh_target

        if indexed:
            stats.indexed_checked += 1

        before_total, before_err = jsonld_before_errors(content, canonical_target)
        stats.jsonld_checked_before += before_total
        stats.jsonld_errors_before += before_err

        title = find_tag_content(r"<title>(.*?)</title>", content)
        h1 = find_tag_content(r"<h1[^>]*>(.*?)</h1>", content)
        description = get_meta_content(content, "description")

        updated = upsert_head_metadata(content, canonical_target, indexed=indexed)
        schemas = build_schema(updated, file_path, canonical_target, title, h1, description)
        updated = upsert_schema(updated, schemas)

        if updated != content:
            file_path.write_text(updated, encoding="utf-8", newline="\n")
            stats.changed_files.append(file_path.relative_to(ROOT).as_posix())

    # Post-checks after changes on source files
    for file_path in all_source_html_files():
        content = file_path.read_text(encoding="utf-8")
        resolved = file_path.resolve()
        indexed = resolved in indexed_map
        refresh_target = get_refresh_redirect_url(content)
        is_noindex = "noindex" in get_meta_content(content, "robots").lower()
        canonical_target = indexed_map.get(resolved, file_to_url(file_path))
        if (is_noindex or refresh_target) and refresh_target:
            canonical_target = refresh_target

        canonical = find_tag_content(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\'](.*?)["\']', content)
        if not canonical:
            canonical = find_tag_content(r'<link[^>]+href=["\'](.*?)["\'][^>]+rel=["\']canonical["\']', content)

        if indexed and canonical != canonical_target:
            stats.canonical_mismatch_after += 1

        if has_visible_faq(content):
            blocks = schema_blocks(content)
            has_faq_schema = False
            for block in blocks:
                try:
                    data = json.loads(block)
                except Exception:
                    stats.jsonld_errors_after += 1
                    continue
                nodes = data if isinstance(data, list) else [data]
                for node in nodes:
                    if not isinstance(node, dict):
                        stats.jsonld_errors_after += 1
                        continue
                    if node.get("@context") != "https://schema.org":
                        stats.jsonld_errors_after += 1
                    url = node.get("url")
                    meop = node.get("mainEntityOfPage")
                    meop_val = meop.get("@id") if isinstance(meop, dict) else meop
                    if url and url != canonical:
                        stats.schema_url_mismatch_after += 1
                    if meop_val and meop_val != canonical:
                        stats.schema_url_mismatch_after += 1
                    if node.get("@type") == "FAQPage":
                        has_faq_schema = True
                    text_fields = [str(node.get("headline", "")), str(node.get("description", "")), str(node.get("name", ""))]
                    if any(EMOJI_RE.search(v) for v in text_fields):
                        stats.jsonld_errors_after += 1
                    if any("/public/" in str(v) for v in (url, meop_val)):
                        stats.jsonld_errors_after += 1
                    if any(any(marker in v for marker in MOJIBAKE_MARKERS) for v in text_fields):
                        stats.jsonld_errors_after += 1
            if not has_faq_schema:
                # Visible FAQ without FAQ schema is acceptable by requirements.
                pass
        else:
            for block in schema_blocks(content):
                try:
                    data = json.loads(block)
                except Exception:
                    stats.jsonld_errors_after += 1
                    continue
                nodes = data if isinstance(data, list) else [data]
                for node in nodes:
                    if isinstance(node, dict) and node.get("@type") == "FAQPage":
                        stats.faq_without_visible_after += 1

        if check_bom(file_path):
            stats.bom_issues_after += 1
        if contains_mojibake(content):
            stats.mojibake_issues_after += 1

    # sitemap checks
    stats.sitemap_url_count_after = len(sitemap_urls)
    for url in sitemap_urls:
        p = url_to_file(url)
        if p.exists():
            txt = p.read_text(encoding="utf-8")
            robots = find_tag_content(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\']', txt).lower()
            if "noindex" in robots or re.search(r"http-equiv=[\"']refresh[\"']", txt, flags=re.IGNORECASE):
                stats.sitemap_noindex_redirect_count_after += 1

    out = ROOT / "audits" / "_stage8_metrics.json"
    out.write_text(json.dumps(stats.__dict__, ensure_ascii=False, indent=2), encoding="utf-8")
    print("STAGE8_OK")
    print(json.dumps(stats.__dict__, ensure_ascii=False))


if __name__ == "__main__":
    main()
