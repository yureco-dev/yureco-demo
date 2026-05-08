#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from bs4 import BeautifulSoup


STAMP_PHRASES = [
    "щоб вона не була порожньою",
    "коротку довідкову точку",
    "матеріал стисло пояснює",
]
BAD_TEXT_MARKERS = ["Ð", "Ñ", "Р°", "Р±", "Р В", "СЂ", "вЂ", "�", "в­•"]
ZERO_WIDTH_RE = re.compile(r"[\u200b-\u200f\u2060\ufeff]")
SOFT_HYPHEN = "\u00ad"


@dataclass
class PageAudit:
    url: str
    rel_path: str
    exists: bool
    is_html: bool
    noindex: bool
    is_redirect: bool
    canonical: str
    canonical_mismatch: bool
    word_count: int
    stamp_phrases: list[str]
    jsonld_errors: int
    has_bad_unicode: bool
    bad_unicode_hits: list[str]


def load_sitemap_urls(sitemap_path: Path) -> list[str]:
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.fromstring(sitemap_path.read_text(encoding="utf-8"))
    urls = [loc.text.strip() for loc in root.findall(".//sm:url/sm:loc", ns) if loc.text]
    return urls


def url_to_rel_path(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path or "/"
    if path.endswith("/"):
        path = f"{path}index.html"
    elif not Path(path).suffix:
        path = f"{path}/index.html"
    if path == "/":
        path = "/index.html"
    return path.lstrip("/")


def extract_canonical_path(href: str) -> str:
    parsed = urlparse(href)
    path = parsed.path or "/"
    if path.endswith("/"):
        path = f"{path}index.html"
    elif not Path(path).suffix:
        path = f"{path}/index.html"
    if path == "/":
        path = "/index.html"
    return path.lstrip("/")


def is_noindex(soup: BeautifulSoup) -> bool:
    for meta in soup.find_all("meta"):
        name = (meta.get("name") or "").strip().lower()
        if name == "robots":
            content = (meta.get("content") or "").lower()
            if "noindex" in content:
                return True
    return False


def is_redirect_page(soup: BeautifulSoup) -> bool:
    for meta in soup.find_all("meta"):
        equiv = (meta.get("http-equiv") or "").strip().lower()
        if equiv == "refresh":
            return True
    return False


def remove_noise_blocks(soup: BeautifulSoup) -> None:
    for sel in [
        "header",
        "nav",
        "aside",
        "footer",
        ".breadcrumbs",
        "[class*='breadcrumb']",
        "[id*='breadcrumb']",
        ".cta",
        "[class*='cta']",
        "[id*='cta']",
    ]:
        for node in soup.select(sel):
            node.decompose()

    for heading in soup.find_all(["h2", "h3", "h4"]):
        text = heading.get_text(" ", strip=True).lower()
        if "дивіться також" in text:
            parent = heading.find_parent(["section", "div", "aside"])
            if parent:
                parent.decompose()
            else:
                heading.decompose()


def main_content_word_count(soup: BeautifulSoup) -> int:
    working = BeautifulSoup(str(soup), "html.parser")
    remove_noise_blocks(working)
    main = working.select_one("main") or working.body or working
    text = main.get_text(" ", strip=True)
    words = re.findall(r"[A-Za-zА-Яа-яІіЇїЄєҐґ0-9'’`-]+", text)
    return len(words)


def scan_unicode_issues(text: str) -> list[str]:
    hits: list[str] = []
    for marker in BAD_TEXT_MARKERS:
        if marker in text:
            hits.append(marker)
    if SOFT_HYPHEN in text:
        hits.append("\\u00AD")
    if ZERO_WIDTH_RE.search(text):
        hits.append("zero-width")
    if "\ufffd" in text:
        hits.append("\\uFFFD")
    return sorted(set(hits))


def parse_jsonld_errors(soup: BeautifulSoup) -> int:
    errors = 0
    for script in soup.find_all("script", {"type": "application/ld+json"}):
        raw = script.string or script.get_text()
        if not raw or not raw.strip():
            continue
        try:
            json.loads(raw)
        except Exception:
            errors += 1
    return errors


def collect_internal_links(soup: BeautifulSoup, current_rel_path: str) -> list[str]:
    links: list[str] = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if not href or href.startswith(("http://", "https://", "mailto:", "tel:", "#", "javascript:")):
            continue
        if href.startswith("//"):
            continue
        if href.startswith("/"):
            links.append(url_to_rel_path(f"https://example.test{href}"))
        else:
            base = Path(current_rel_path).parent
            target = (base / href.split("#")[0].split("?")[0]).as_posix()
            if target.endswith("/"):
                target = f"{target}index.html"
            links.append(target.lstrip("/"))
    return links


def load_html(path: Path) -> BeautifulSoup:
    return BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")


def build_report(site_dir: Path) -> dict[str, Any]:
    sitemap_path = site_dir / "sitemap.xml"
    urls = load_sitemap_urls(sitemap_path)

    pages: list[PageAudit] = []
    paragraph_index: dict[str, set[str]] = defaultdict(set)
    all_html_files = sorted(site_dir.rglob("*.html"))

    link_map: dict[str, list[str]] = {}
    links_to_public = 0

    for url in urls:
        rel_path = url_to_rel_path(url)
        file_path = site_dir / rel_path
        if not file_path.exists():
            pages.append(
                PageAudit(url, rel_path, False, False, False, False, "", False, 0, [], 0, False, [])
            )
            continue
        soup = load_html(file_path)
        full_text = soup.get_text(" ", strip=True)
        canonical_tag = soup.find("link", rel="canonical")
        canonical = (canonical_tag.get("href") or "").strip() if canonical_tag else ""
        canonical_path = extract_canonical_path(canonical) if canonical else rel_path
        noindex = is_noindex(soup)
        redirect = is_redirect_page(soup)
        wc = main_content_word_count(soup)
        stamps = [phrase for phrase in STAMP_PHRASES if phrase in full_text]
        bad_hits = scan_unicode_issues(full_text)
        jsonld_errors = parse_jsonld_errors(soup)

        links = collect_internal_links(soup, rel_path)
        link_map[rel_path] = links
        links_to_public += sum(1 for a in soup.find_all("a", href=True) if "/public/" in a["href"])

        for p in soup.find_all("p"):
            text = re.sub(r"\s+", " ", p.get_text(" ", strip=True))
            if len(text) >= 140:
                paragraph_index[text].add(rel_path)

        pages.append(
            PageAudit(
                url=url,
                rel_path=rel_path,
                exists=True,
                is_html=True,
                noindex=noindex,
                is_redirect=redirect,
                canonical=canonical,
                canonical_mismatch=canonical_path != rel_path,
                word_count=wc,
                stamp_phrases=stamps,
                jsonld_errors=jsonld_errors,
                has_bad_unicode=bool(bad_hits),
                bad_unicode_hits=bad_hits,
            )
        )

    indexed_pages = [p for p in pages if p.exists and not p.noindex and not p.is_redirect]
    noindex_or_redirect = {p.rel_path for p in pages if p.noindex or p.is_redirect}
    broken_links: list[tuple[str, str]] = []
    links_to_noindex_redirect: list[tuple[str, str]] = []

    existing_paths = {p.relative_to(site_dir).as_posix() for p in all_html_files}
    existing_paths.update({"index.html"})

    for source, links in link_map.items():
        for target in links:
            if target not in existing_paths:
                broken_links.append((source, target))
            if target in noindex_or_redirect:
                links_to_noindex_redirect.append((source, target))

    dup_paragraph_groups = sorted(
        [{"paragraph": p, "pages": sorted(paths)} for p, paths in paragraph_index.items() if len(paths) > 1],
        key=lambda x: (-len(x["pages"]), -len(x["paragraph"])),
    )

    utf8_bom_files = []
    public_unicode_issues: dict[str, list[str]] = {}
    for html in all_html_files:
        raw = html.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            utf8_bom_files.append(html.relative_to(site_dir).as_posix())
        text = raw.decode("utf-8", errors="replace")
        hits = scan_unicode_issues(text)
        if hits:
            public_unicode_issues[html.relative_to(site_dir).as_posix()] = hits

    stamp_pages = [p.rel_path for p in pages if p.stamp_phrases]
    canonical_mismatch_indexed = [p.rel_path for p in indexed_pages if p.canonical_mismatch]
    jsonld_error_pages = [p.rel_path for p in pages if p.jsonld_errors > 0]
    under_300 = [p.rel_path for p in indexed_pages if p.word_count < 300]
    between_300_500 = [p.rel_path for p in indexed_pages if 300 <= p.word_count < 500]

    cyrillic_damaged = any(
        marker in "".join(sum(public_unicode_issues.values(), []))
        for marker in ["Ð", "Ñ", "Р°", "Р±", "Р В", "СЂ", "вЂ", "�"]
    )

    return {
        "sitemap_url_count": len(urls),
        "sitemap_urls": urls,
        "pages": [asdict(p) for p in pages],
        "indexed_url_count": len(indexed_pages),
        "indexed_under_300_count": len(under_300),
        "indexed_under_300_pages": under_300,
        "indexed_300_500_count": len(between_300_500),
        "indexed_300_500_pages": between_300_500,
        "stamp_phrase_pages": stamp_pages,
        "duplicate_paragraph_groups": dup_paragraph_groups[:100],
        "noindex_or_redirect_in_sitemap": sorted(noindex_or_redirect),
        "broken_internal_links_count": len(broken_links),
        "broken_internal_links_samples": broken_links[:200],
        "links_to_noindex_redirect_count": len(links_to_noindex_redirect),
        "links_to_noindex_redirect_samples": links_to_noindex_redirect[:200],
        "links_to_public_count": links_to_public,
        "jsonld_error_count": sum(p.jsonld_errors for p in pages),
        "jsonld_error_pages": jsonld_error_pages,
        "canonical_mismatch_indexed_count": len(canonical_mismatch_indexed),
        "canonical_mismatch_indexed_pages": canonical_mismatch_indexed,
        "utf8_bom_files": utf8_bom_files,
        "public_unicode_issue_files": public_unicode_issues,
        "contains_v_soft_hyphen_bullet": any("в­•" in "".join(v) for v in public_unicode_issues.values()),
        "hidden_unicode_found": any(
            "\\u00AD" in hits or "zero-width" in hits or "\\uFFFD" in hits
            for hits in public_unicode_issues.values()
        ),
        "cyrillic_status": "зіпсована" if cyrillic_damaged else "не зіпсована",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", default="public")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    site_dir = Path(args.site_dir).resolve()
    report = build_report(site_dir)
    out_path = Path(args.out).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"STAGE12_AUDIT_OK {out_path}")


if __name__ == "__main__":
    main()
