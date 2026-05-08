#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from html.parser import HTMLParser
import json


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"

SECTIONS = [
    "utylizaciya",
    "pererobka",
    "sortuvannya",
    "logistyka",
    "articles",
    "guide",
]


def decode_bytes(raw: bytes) -> tuple[str, str, bool]:
    has_bom = raw.startswith(b"\xef\xbb\xbf")
    payload = raw[3:] if has_bom else raw
    try:
        return payload.decode("utf-8"), "utf-8", has_bom
    except UnicodeDecodeError:
        return payload.decode("utf-8", errors="replace"), "invalid-utf8", has_bom


@dataclass
class LinkInfo:
    href: str
    active: bool
    aria_current: str


class SidebarParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_sidebar = False
        self.sidebar_depth = 0
        self.links: list[LinkInfo] = []
        self.robots_noindex = False
        self.redirect_links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k: (v or "") for k, v in attrs}
        if tag in {"aside", "nav"} and "sidebar" in attr.get("class", "").split():
            self.in_sidebar = True
            self.sidebar_depth = 1
            return

        if self.in_sidebar:
            self.sidebar_depth += 1
            if tag == "a":
                classes = set(attr.get("class", "").split())
                active = "active" in classes or "current" in classes
                aria_current = attr.get("aria-current", "")
                self.links.append(LinkInfo(attr.get("href", ""), active, aria_current))

        if tag == "meta" and attr.get("name", "").lower() == "robots":
            if "noindex" in attr.get("content", "").lower():
                self.robots_noindex = True

        if tag == "meta" and attr.get("http-equiv", "").lower() == "refresh":
            self.redirect_links.append("meta-refresh")

        if tag == "script" and "window.location.replace" in attr.get("src", ""):
            self.redirect_links.append(attr.get("src", ""))

    def handle_endtag(self, tag: str) -> None:
        if self.in_sidebar:
            self.sidebar_depth -= 1
            if self.sidebar_depth <= 0:
                self.in_sidebar = False
                self.sidebar_depth = 0


def normalize_runtime_path(value: str, *, is_current: bool) -> str:
    raw = (value or "").strip()
    lowered = raw.lower()

    if not is_current:
        if lowered.startswith(("mailto:", "tel:", "javascript:", "#")):
            return ""
        if "://" in raw:
            slash_pos = raw.find("/", raw.find("://") + 3)
            raw = "/" if slash_pos == -1 else raw[slash_pos:]

    raw = raw.replace("\\", "/")
    while "//" in raw:
        raw = raw.replace("//", "/")
    raw = raw.split("#", 1)[0].split("?", 1)[0]
    raw = raw.lstrip("/")

    if raw == "":
        return "index.html"
    if raw.endswith("/"):
        return raw + "index.html"
    if "." not in raw:
        return raw + "/index.html"
    return raw


def normalize_href(href: str) -> str:
    return normalize_runtime_path(href, is_current=False)


def fallback_target(normalized_current_path: str) -> str:
    if normalized_current_path == "index.html":
        return "index.html"
    if normalized_current_path == "kontakty.html":
        return "index.html"
    if normalized_current_path == "dokumenty.html" or normalized_current_path.startswith("dokumenty-"):
        return "dokumenty.html"
    if normalized_current_path == "zbir.html" or normalized_current_path.startswith("zbir-"):
        return "zbir.html"
    if (
        normalized_current_path == "vidhody.html"
        or normalized_current_path.startswith("vidhody-")
        or normalized_current_path.startswith("promyslovi-vidhody")
        or normalized_current_path.startswith("oblik-")
        or normalized_current_path.startswith("optymizaciya-")
        or normalized_current_path.startswith("skladuvannya-")
        or normalized_current_path.startswith("vtorynna-syrovyna-")
        or normalized_current_path.startswith("vymogy-do-zberigannya-")
        or normalized_current_path == "kabelni-vidhody.html"
    ):
        return "vidhody.html"
    if normalized_current_path == "kudy-zdaty.html" or normalized_current_path.startswith("kudy-zdaty-"):
        return "kudy-zdaty.html"
    if (
        normalized_current_path.startswith("sortuvannya/")
        or normalized_current_path.startswith("sortuvannya-")
        or normalized_current_path == "sortuvannya.html"
    ):
        return "sortuvannya/index.html"
    if (
        normalized_current_path.startswith("logistyka/")
        or normalized_current_path.startswith("logistyka-")
        or normalized_current_path == "logistyka.html"
    ):
        return "logistyka/index.html"
    if (
        normalized_current_path.startswith("pererobka/")
        or normalized_current_path.startswith("pererobka-")
        or normalized_current_path == "pererobka.html"
        or normalized_current_path == "chy-potribno-pererobyty-chy-utylizuvaty.html"
    ):
        return "pererobka/index.html"
    if (
        normalized_current_path.startswith("yak-")
        or normalized_current_path.startswith("spysannya-")
        or normalized_current_path.startswith("likvidaciya-")
        or normalized_current_path.startswith("povernennya-")
        or normalized_current_path.startswith("akt-")
        or normalized_current_path.startswith("fotozvit-")
    ):
        return "utylizaciya/index.html"
    if (
        normalized_current_path.startswith("utylizaciya/")
        or normalized_current_path.startswith("utylizaciya-")
        or normalized_current_path.startswith("utilizaciya-")
        or normalized_current_path == "utylizaciya.html"
    ):
        return "utylizaciya/index.html"
    return ""


def runtime_active_matches(links: list[LinkInfo], current_rel_path: str) -> list[LinkInfo]:
    current_norm = normalize_runtime_path(current_rel_path, is_current=True)
    matches = [link for link in links if normalize_runtime_path(link.href, is_current=False) == current_norm]
    if matches:
        return matches

    fallback_path = fallback_target(current_norm)
    if not fallback_path:
        return []

    fallback_matches = [
        link for link in links if normalize_runtime_path(link.href, is_current=False) == fallback_path
    ]
    return fallback_matches[:1]


def file_exists_for_href(href: str) -> bool:
    if not href or "://" in href:
        return True
    rel = normalize_href(href)
    if not rel:
        return True
    path = PUBLIC / rel
    if path.is_file():
        return True
    if path.is_dir() and (path / "index.html").is_file():
        return True
    return False


def gather_html_files() -> list[Path]:
    files = [p for p in PUBLIC.rglob("*.html") if p.is_file()]
    return sorted(files)


def main() -> None:
    all_html = gather_html_files()
    sidebar_pages_checked = 0
    pages_with_one_active = 0
    pages_with_non_one_active: list[str] = []
    broken_links: list[tuple[str, str]] = []
    links_to_public: list[tuple[str, str]] = []
    links_to_noindex_or_redirect: list[tuple[str, str]] = []
    invalid_utf8_files: list[str] = []
    bom_files: list[str] = []

    page_flags: dict[str, dict[str, int | bool]] = {}
    noindex_or_redirect_set: set[str] = set()

    parsed: dict[Path, SidebarParser] = {}
    for html_path in all_html:
        raw = html_path.read_bytes()
        text, encoding_status, has_bom = decode_bytes(raw)
        if encoding_status != "utf-8":
            invalid_utf8_files.append(str(html_path.relative_to(PUBLIC)).replace("\\", "/"))
        if has_bom:
            bom_files.append(str(html_path.relative_to(PUBLIC)).replace("\\", "/"))

        parser = SidebarParser()
        parser.feed(text)
        parsed[html_path] = parser

        rel = str(html_path.relative_to(PUBLIC)).replace("\\", "/")
        is_noindex_or_redirect = parser.robots_noindex or bool(parser.redirect_links)
        if is_noindex_or_redirect:
            noindex_or_redirect_set.add(rel)

    for html_path, parser in parsed.items():
        rel = str(html_path.relative_to(PUBLIC)).replace("\\", "/")

        if parser.links:
            sidebar_pages_checked += 1
            static_active_count = sum(1 for link in parser.links if link.active or link.aria_current == "page")
            runtime_matches = runtime_active_matches(parser.links, rel)
            runtime_active_count = 1 if runtime_matches else 0

            if runtime_active_count == 1:
                pages_with_one_active += 1
            else:
                pages_with_non_one_active.append(rel)
            page_flags[rel] = {
                "sidebar_links": len(parser.links),
                "static_active_count": static_active_count,
                "runtime_match_count": len(runtime_matches),
                "runtime_active_count": runtime_active_count,
                "exactly_one_active": runtime_active_count == 1,
            }

            for link in parser.links:
                href = link.href.strip()
                if "/public/" in href or href.startswith("/public/"):
                    links_to_public.append((rel, href))

                norm = normalize_href(href)
                if norm in noindex_or_redirect_set:
                    links_to_noindex_or_redirect.append((rel, href))

                if href and not file_exists_for_href(href):
                    broken_links.append((rel, href))

    section_hub_results: dict[str, dict[str, int | bool]] = {}
    for section in SECTIONS:
        hub_rel = f"{section}/index.html"
        hub_path = PUBLIC / hub_rel
        if hub_path.exists() and hub_path in parsed:
            parser = parsed[hub_path]
            runtime_matches = runtime_active_matches(parser.links, hub_rel)
            active_count = 1 if runtime_matches else 0
            section_hub_results[section] = {
                "exists": True,
                "runtime_match_count": len(runtime_matches),
                "active_count": active_count,
                "exactly_one_active": active_count == 1,
            }
        else:
            section_hub_results[section] = {
                "exists": False,
                "active_count": 0,
                "exactly_one_active": False,
            }

    report = {
        "public_html_pages": len(all_html),
        "sidebar_pages_checked": sidebar_pages_checked,
        "pages_with_one_active": pages_with_one_active,
        "pages_with_non_one_active": pages_with_non_one_active[:200],
        "broken_links_count": len(broken_links),
        "broken_links": broken_links[:200],
        "links_to_noindex_or_redirect_count": len(links_to_noindex_or_redirect),
        "links_to_noindex_or_redirect": links_to_noindex_or_redirect[:200],
        "links_to_public_count": len(links_to_public),
        "links_to_public": links_to_public[:200],
        "utf8_invalid_count": len(invalid_utf8_files),
        "utf8_invalid_files": invalid_utf8_files[:200],
        "bom_files_count": len(bom_files),
        "bom_files": bom_files[:200],
        "sections": section_hub_results,
        "page_flags_sample": dict(list(page_flags.items())[:30]),
    }

    out = ROOT / "audits" / "_step14_sidebar_active_audit.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"STEP14_AUDIT_OK report={out}")


if __name__ == "__main__":
    main()
