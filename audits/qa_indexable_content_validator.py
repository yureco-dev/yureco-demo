#!/usr/bin/env python3
"""Deterministic read-only QA validator for indexable content in dist."""

from __future__ import annotations

import hashlib
import html
import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlparse
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
AUDITS = ROOT / "audits"
SITEMAP = DIST / "sitemap.xml"
HTACCESS = DIST / ".htaccess"
JSON_REPORT = AUDITS / "qa_indexable_content_validator_report.json"
TXT_REPORT = AUDITS / "qa_indexable_content_validator_report.txt"
EXPECTED_SITEMAP_URLS = 168

FIX_PAGES = {
    "reestr-partiyi.html",
    "scenarii-utilizaciyi.html",
    "vnutrishniy-akt-spysannya.html",
    "sortuvannya-plastyku.html",
    "transportuvannya-vidpracovanyh-masel.html",
    "vidy-kabelnyh-vidhodiv.html",
    "sortuvannya-budivelnyh-vidhodiv.html",
    "transportuvannya-vidpracovanyh-shyn.html",
    "logistyka-plastyku.html",
    "nebezpeka-vidpracovanogo-masla.html",
    "zberigannya-vidpracovanyh-masel.html",
    "vidy-plastykovyh-vidhodiv.html",
    "vidhody-polimeriv.html",
    "logistyka-kabelyu.html",
    "pererobka-pet.html",
    "vyviz-budivelnyh-vidhodiv.html",
    "logistyka-budivelnyh-vidhodiv.html",
    "plastykovi-vidhody.html",
    "pererobka-polistyrolu.html",
    "utylizaciya-materialiv.html",
    "pererobka-izolyaciyi-kabelyu.html",
    "spysannya-produktiv.html",
    "utylizaciya-budivelnyh-vidhodiv.html",
    "utylizaciya-avtoshyn.html",
    "utylizaciya-vantazhnyh-shyn.html",
    "pererobka-vidpracovanyh-masel.html",
    "utylizaciya-energetychnyh-napoyiv.html",
    "utylizaciya-derevyny-z-budivnyctva.html",
    "utylizaciya-fruktiv-ta-ovochiv.html",
    "utylizaciya-sokiv-ta-napoyiv.html",
    "utylizaciya-paperu-ta-kartonu.html",
    "utylizaciya-vody.html",
    "utylizaciya-upakovky-vid-kosmetyky.html",
    "vymogy-do-zberigannya-vidhodiv.html",
    "utylizaciya-harchovyh-produktiv.html",
    "utylizaciya-prostrochenoyi-kosmetyky.html",
    "shcho-take-promyslovi-vidhody.html",
    "shcho-take-znyshchennya-produkciyi.html",
    "shcho-take-pererobka-vidhodiv.html",
    "utylizaciya-rybnyh-produktiv.html",
    "utylizaciya-skladskyh-zalyshkiv-kosmetyky.html",
    "utylizaciya-myasnyh-produktiv.html",
    "shcho-take-utylizaciya.html",
    "utylizaciya-gazovanyh-napoyiv.html",
    "dokumenty.html",
    "utylizaciya-zamorozhenyh-produktiv.html",
    "fotozvit-utylizaciyi.html",
    "kudy-zdaty.html",
    "akt-utylizaciyi.html",
}

EXCLUDED_TAGS = {
    "title",
    "script",
    "style",
    "noscript",
    "header",
    "footer",
    "nav",
    "menu",
    "template",
    "svg",
    "canvas",
}

EXCLUDED_ATTR_SUBSTRINGS = {
    "breadcrumb",
    "breadcrumbs",
    "nav",
    "menu",
    "header",
    "footer",
    "cta",
    "service",
    "services",
    "bridge",
    "related",
    "law",
    "legal",
    "eeat",
    "author",
    "trust",
    "contact",
    "contacts",
    "form",
    "sidebar",
    "share",
    "social",
    "pagination",
}

AGGRESSIVE_BRIDGE_PHRASES = (
    "Замовити",
    "замовити",
    "Вивезення",
    "вивезення",
    "Послуги",
    "послуги",
    "Залишити заявку",
    "залишити заявку",
    "Отримати консультацію",
    "отримати консультацію",
    "Дізнатися вартість",
    "дізнатися вартість",
    "Розрахувати вартість",
    "розрахувати вартість",
    "Комерційна пропозиція",
    "комерційна пропозиція",
)

WORD_RE = re.compile(r"[^\W\d_]+(?:[-'’][^\W\d_]+)*", re.UNICODE)


@dataclass
class Node:
    tag: str
    attrs: dict[str, str] = field(default_factory=dict)
    children: list["Node"] = field(default_factory=list)
    text_parts: list[str] = field(default_factory=list)
    parent: "Node | None" = None


class TreeParser(HTMLParser):
    VOID_TAGS = {
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
        "param",
        "source",
        "track",
        "wbr",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Node("document")
        self.stack = [self.root]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        node = Node(tag=tag, attrs={k.lower(): v or "" for k, v in attrs}, parent=self.stack[-1])
        self.stack[-1].children.append(node)
        if tag not in self.VOID_TAGS:
            self.stack.append(node)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, data: str) -> None:
        if data:
            self.stack[-1].text_parts.append(data)


def parse_html_document(source: str) -> Node:
    parser = TreeParser()
    parser.feed(source)
    parser.close()
    return parser.root


def walk(node: Node) -> Iterable[Node]:
    yield node
    for child in node.children:
        yield from walk(child)


def node_text(node: Node) -> str:
    parts = list(node.text_parts)
    for child in node.children:
        parts.append(node_text(child))
    return html.unescape(" ".join(parts))


def norm_space(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value or "")).strip()


def norm_key(value: str) -> str:
    return norm_space(value).casefold()


def attr_has_excluded_keyword(node: Node) -> bool:
    value = " ".join(
        node.attrs.get(name, "")
        for name in ("class", "id", "role", "aria-label", "data-section", "data-role")
    ).casefold()
    return any(token in value for token in EXCLUDED_ATTR_SUBSTRINGS)


def is_hidden(node: Node) -> bool:
    if "hidden" in node.attrs:
        return True
    if node.attrs.get("aria-hidden", "").strip().casefold() == "true":
        return True
    if node.attrs.get("type", "").strip().casefold() == "hidden":
        return True
    style = re.sub(r"\s+", "", node.attrs.get("style", "").casefold())
    return "display:none" in style or "visibility:hidden" in style or "opacity:0" in style


def is_excluded(node: Node) -> bool:
    return node.tag in EXCLUDED_TAGS or attr_has_excluded_keyword(node) or is_hidden(node)


def visible_text(node: Node, excluded: bool = False) -> str:
    excluded = excluded or is_excluded(node)
    if excluded:
        return ""
    parts = list(node.text_parts)
    for child in node.children:
        parts.append(visible_text(child, excluded=False))
    return norm_space(" ".join(parts))


def find_nodes(root: Node, tags: set[str]) -> list[Node]:
    return [node for node in walk(root) if node.tag in tags and not is_excluded(node)]


def main_visible_text(root: Node) -> str:
    for tags in ({"main"}, {"article"}, {"section"}, {"body"}):
        nodes = find_nodes(root, tags)
        texts = [visible_text(node) for node in nodes]
        text = norm_space(" ".join(part for part in texts if part))
        if text:
            return text
    return visible_text(root)


def count_words(text: str) -> int:
    return len(WORD_RE.findall(html.unescape(text)))


def read_utf8(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dist_protected_hashes() -> dict[str, str]:
    patterns = ["*.html", "*.htm", "*.xml", "*.txt", "*.css"]
    files: set[Path] = set()
    for pattern in patterns:
        files.update(DIST.rglob(pattern))
    files.update(path for path in (HTACCESS, DIST / "robots.txt", SITEMAP) if path.exists())
    return {str(path.relative_to(DIST)).replace("\\", "/"): file_hash(path) for path in sorted(files)}


def parse_sitemap_urls() -> list[str]:
    tree = ElementTree.parse(SITEMAP)
    root = tree.getroot()
    urls = []
    for element in root.iter():
        if element.tag.endswith("loc") and element.text:
            urls.append(element.text.strip())
    return urls


def local_path_for_url(url: str) -> Path:
    parsed = urlparse(url)
    path = unquote(parsed.path or "/").lstrip("/")
    if not path:
        path = "index.html"
    elif path.endswith("/"):
        path += "index.html"
    elif "." not in Path(path).name:
        path += "/index.html"
    return DIST / path


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    scheme = parsed.scheme.lower()
    host = parsed.netloc.lower()
    path = parsed.path or "/"
    if path == "/index.html":
        path = "/"
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    return f"{scheme}://{host}{path}"


def page_name(path: Path) -> str:
    return path.name


def extract_title(root: Node) -> str:
    titles = [node_text(node) for node in walk(root) if node.tag == "title"]
    return norm_space(titles[0]) if titles else ""


def extract_meta(root: Node, name: str) -> str:
    wanted = name.casefold()
    for node in walk(root):
        if node.tag != "meta":
            continue
        meta_name = node.attrs.get("name", node.attrs.get("property", "")).casefold()
        if meta_name == wanted:
            return norm_space(node.attrs.get("content", ""))
    return ""


def extract_canonical(root: Node) -> str:
    for node in walk(root):
        if node.tag != "link":
            continue
        rel = node.attrs.get("rel", "").casefold().split()
        if "canonical" in rel:
            return norm_space(node.attrs.get("href", ""))
    return ""


def extract_first_h1(root: Node) -> str:
    for node in walk(root):
        if node.tag == "h1" and not is_excluded(node):
            value = norm_space(visible_text(node))
            if value:
                return value
    return ""


def is_noindex(root: Node) -> bool:
    robots_values = []
    for node in walk(root):
        if node.tag == "meta" and node.attrs.get("name", "").casefold() == "robots":
            robots_values.append(node.attrs.get("content", ""))
    return any("noindex" in value.casefold() for value in robots_values)


def extract_aggressive_bridge_anchors(root: Node, url: str, file_name: str) -> list[dict[str, str]]:
    findings = []
    for node in walk(root):
        if node.tag != "a":
            continue
        href = node.attrs.get("href", "").strip()
        if not href.startswith("https://youreco.com.ua/"):
            continue
        anchor = norm_space(node_text(node))
        matched = [phrase for phrase in AGGRESSIVE_BRIDGE_PHRASES if phrase in anchor]
        if matched:
            findings.append(
                {
                    "url": url,
                    "file": file_name,
                    "href": href,
                    "anchor": anchor,
                    "matched_phrases": matched,
                }
            )
    return findings


def parse_redirect_sources() -> set[str]:
    if not HTACCESS.exists():
        return set()
    sources = set()
    for line in read_utf8(HTACCESS).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.match(r"Redirect\s+\d{3}\s+(\S+)\s+\S+", line, flags=re.IGNORECASE)
        if match:
            sources.add(match.group(1))
    return sources


def duplicate_groups(items: list[dict[str, object]], key: str) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for item in items:
        value = str(item.get(key, ""))
        if value:
            grouped[norm_key(value)].append(item)
    groups = []
    for _, group in sorted(grouped.items(), key=lambda entry: entry[0]):
        if len(group) > 1:
            groups.append(
                {
                    "value": group[0][key],
                    "count": len(group),
                    "urls": [entry["url"] for entry in group],
                }
            )
    return groups


def validate() -> dict[str, object]:
    AUDITS.mkdir(exist_ok=True)
    before_hashes = dist_protected_hashes()
    urls = parse_sitemap_urls()
    redirect_sources = parse_redirect_sources()
    sitemap_url_set = {normalize_url(url) for url in urls}

    pages = []
    aggressive_bridge_anchors = []
    noindex_urls = []
    non_self_canonicals = []
    redirect_source_urls = []

    for url in urls:
        local_path = local_path_for_url(url)
        exists = local_path.exists() and local_path.is_file()
        parsed_path = urlparse(url).path or "/"
        if parsed_path in redirect_sources:
            redirect_source_urls.append(url)

        page = {
            "url": url,
            "file": str(local_path.relative_to(DIST)).replace("\\", "/"),
            "html_found": exists,
            "indexable": False,
            "word_count": 0,
            "threshold": 450,
            "is_fix_page": False,
            "title": "",
            "description": "",
            "h1": "",
            "canonical": "",
            "noindex": False,
            "non_self_canonical": False,
        }
        if not exists:
            pages.append(page)
            continue

        source = read_utf8(local_path)
        root = parse_html_document(source)
        file_name = page_name(local_path)
        noindex = is_noindex(root)
        is_fix = file_name in FIX_PAGES
        threshold = 950 if file_name == "kudy-zdaty.html" else 750 if is_fix else 450
        canonical = extract_canonical(root)
        non_self = bool(canonical) and normalize_url(canonical) != normalize_url(url)

        page.update(
            {
                "indexable": not noindex,
                "word_count": count_words(main_visible_text(root)) if not noindex else 0,
                "threshold": threshold,
                "is_fix_page": is_fix,
                "title": extract_title(root),
                "description": extract_meta(root, "description"),
                "h1": extract_first_h1(root),
                "canonical": canonical,
                "noindex": noindex,
                "non_self_canonical": non_self,
            }
        )
        if noindex:
            noindex_urls.append(url)
        if non_self and normalize_url(url) in sitemap_url_set:
            non_self_canonicals.append({"url": url, "canonical": canonical})
        aggressive_bridge_anchors.extend(extract_aggressive_bridge_anchors(root, url, file_name))
        pages.append(page)

    indexable_pages = [page for page in pages if page["html_found"] and page["indexable"]]
    pages_under_450 = [
        {"url": page["url"], "file": page["file"], "word_count": page["word_count"]}
        for page in indexable_pages
        if int(page["word_count"]) < 450
    ]
    fix_pages_under_750 = [
        {"url": page["url"], "file": page["file"], "word_count": page["word_count"]}
        for page in indexable_pages
        if page["is_fix_page"] and int(page["word_count"]) < 750
    ]
    kudy_page = next((page for page in pages if page["file"] == "kudy-zdaty.html"), None)
    kudy_ok = bool(kudy_page and kudy_page["html_found"] and kudy_page["indexable"] and int(kudy_page["word_count"]) >= 950)
    after_hashes = dist_protected_hashes()

    html_unchanged = all(
        before_hashes.get(name) == after_hashes.get(name)
        for name in before_hashes
        if name.lower().endswith((".html", ".htm"))
    )
    sitemap_unchanged = before_hashes.get("sitemap.xml") == after_hashes.get("sitemap.xml")
    robots_unchanged = before_hashes.get("robots.txt") == after_hashes.get("robots.txt")
    htaccess_unchanged = before_hashes.get(".htaccess") == after_hashes.get(".htaccess")
    css_unchanged = all(
        before_hashes.get(name) == after_hashes.get(name)
        for name in before_hashes
        if name.lower().endswith(".css")
    )
    utf8_ok = True
    cyrillic_ok = True
    try:
        for page in pages:
            if page["html_found"]:
                read_utf8(DIST / str(page["file"]))
    except UnicodeDecodeError:
        utf8_ok = False
        cyrillic_ok = False
    if utf8_ok:
        cyrillic_ok = any(
            re.search(r"[А-Яа-яІіЇїЄєҐґ]", read_utf8(DIST / str(page["file"])))
            for page in pages
            if page["html_found"]
        )

    duplicate_titles = duplicate_groups(indexable_pages, "title")
    duplicate_descriptions = duplicate_groups(indexable_pages, "description")
    duplicate_h1 = duplicate_groups(indexable_pages, "h1")

    summary = {
        "sitemap_url_count": len(urls),
        "expected_sitemap_url_count": EXPECTED_SITEMAP_URLS,
        "html_files_found_for_sitemap_urls": sum(1 for page in pages if page["html_found"]),
        "indexable_pages_checked": len(indexable_pages),
        "pages_under_450_count": len(pages_under_450),
        "fix_pages_under_750_count": len(fix_pages_under_750),
        "kudy_zdaty_has_950_plus_words": kudy_ok,
        "aggressive_bridge_anchors_count": len(aggressive_bridge_anchors),
        "noindex_urls_in_sitemap_count": len(noindex_urls),
        "redirect_source_urls_in_sitemap_count": len(redirect_source_urls),
        "duplicate_title_groups_count": len(duplicate_titles),
        "duplicate_description_groups_count": len(duplicate_descriptions),
        "duplicate_h1_groups_count": len(duplicate_h1),
        "non_self_canonicals_count": len(non_self_canonicals),
        "html_in_dist_unchanged": html_unchanged,
        "sitemap_xml_unchanged": sitemap_unchanged,
        "robots_txt_unchanged": robots_unchanged,
        "htaccess_unchanged": htaccess_unchanged,
        "css_unchanged": css_unchanged,
        "utf8_preserved": utf8_ok,
        "cyrillic_not_corrupted": cyrillic_ok,
    }

    blocking_ok = (
        len(urls) == EXPECTED_SITEMAP_URLS
        and summary["html_files_found_for_sitemap_urls"] == EXPECTED_SITEMAP_URLS
        and not pages_under_450
        and not fix_pages_under_750
        and kudy_ok
        and not noindex_urls
        and not redirect_source_urls
        and not duplicate_titles
        and not duplicate_descriptions
        and not duplicate_h1
        and not non_self_canonicals
        and html_unchanged
        and utf8_ok
        and cyrillic_ok
    )
    final_status = "ДОБРЕ" if blocking_ok else "НЕ ДОБРЕ"

    return {
        "summary": summary,
        "pages": pages,
        "pages_under_450": pages_under_450,
        "fix_pages_under_750": fix_pages_under_750,
        "kudy_zdaty_status": {
            "file": "kudy-zdaty.html",
            "word_count": int(kudy_page["word_count"]) if kudy_page else 0,
            "has_950_plus_words": kudy_ok,
        },
        "aggressive_bridge_anchors": aggressive_bridge_anchors,
        "bridge_link_note": "Bridge-link anchors потребують окремого пункту виправлення"
        if aggressive_bridge_anchors
        else "",
        "duplicate_titles": duplicate_titles,
        "duplicate_descriptions": duplicate_descriptions,
        "duplicate_h1": duplicate_h1,
        "non_self_canonicals": non_self_canonicals,
        "noindex_urls_in_sitemap": noindex_urls,
        "redirect_source_urls_in_sitemap": redirect_source_urls,
        "final_status": final_status,
    }


def yes_no(value: bool) -> str:
    return "так" if value else "ні"


def write_reports(report: dict[str, object]) -> None:
    JSON_REPORT.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    summary = report["summary"]
    status = report["final_status"]
    lines = [
        f"П.12.VALIDATOR Єдиний QA-валідатор — {status}",
        "",
        "Звіт:",
        f"- URL у sitemap.xml: {summary['sitemap_url_count']}",
        f"- HTML-файлів знайдено для sitemap URL: {summary['html_files_found_for_sitemap_urls']}",
        f"- indexable сторінок перевірено: {summary['indexable_pages_checked']}",
        f"- indexable сторінок <450 слів: {summary['pages_under_450_count']}",
        f"- FIX-сторінок <750 слів: {summary['fix_pages_under_750_count']}",
        f"- kudy-zdaty.html має 950+ слів: {yes_no(summary['kudy_zdaty_has_950_plus_words'])}",
        f"- агресивних bridge-link anchors: {summary['aggressive_bridge_anchors_count']}",
        f"- noindex URL у sitemap.xml: {summary['noindex_urls_in_sitemap_count']}",
        f"- redirect-source URL у sitemap.xml: {summary['redirect_source_urls_in_sitemap_count']}",
        f"- duplicate title groups: {summary['duplicate_title_groups_count']}",
        f"- duplicate description groups: {summary['duplicate_description_groups_count']}",
        f"- duplicate H1 groups: {summary['duplicate_h1_groups_count']}",
        f"- non-self canonical серед sitemap URL: {summary['non_self_canonicals_count']}",
        f"- HTML у dist не редагувався: {yes_no(summary['html_in_dist_unchanged'])}",
        f"- sitemap.xml не редагувався: {yes_no(summary['sitemap_xml_unchanged'])}",
        f"- robots.txt не редагувався: {yes_no(summary['robots_txt_unchanged'])}",
        f"- .htaccess не редагувався: {yes_no(summary['htaccess_unchanged'])}",
        f"- CSS не редагувався: {yes_no(summary['css_unchanged'])}",
        f"- UTF-8 збережено: {yes_no(summary['utf8_preserved'])}",
        f"- кирилиця не зіпсована: {yes_no(summary['cyrillic_not_corrupted'])}",
    ]
    if report.get("bridge_link_note"):
        lines.extend(["", str(report["bridge_link_note"])])
    TXT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    report = validate()
    write_reports(report)
    print(f"final_status={report['final_status']}")
    print(f"json_report={JSON_REPORT}")
    print(f"txt_report={TXT_REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
