#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup

from stage12_control_check import build_report

FOOD_CLUSTER_PAGES = [
    "utylizaciya-napoyiv.html",
    "utylizaciya-gazovanyh-napoyiv.html",
    "utylizaciya-zipsovanyh-produktiv.html",
    "utylizaciya-zamorozhenyh-produktiv.html",
    "utylizaciya-myasnyh-produktiv.html",
    "utylizaciya-rybnyh-produktiv.html",
]

SERVICE_EXTENSIONS = {".md", ".txt", ".ps1", ".py", ".json", ".csv", ".sh", ".bat", ".log"}


def load_html(path: Path) -> BeautifulSoup:
    return BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def collect_html_files(site_dir: Path) -> list[Path]:
    return sorted(site_dir.rglob("*.html"))


def sidebar_issues(site_dir: Path, indexed_pages: list[str]) -> dict[str, Any]:
    missing_sidebar: list[str] = []
    broken_sidebar_links: list[list[str]] = []
    pages_with_sidebar = 0
    expected_paths = {p.relative_to(site_dir).as_posix() for p in collect_html_files(site_dir)}
    expected_paths.add("index.html")

    for rel_path in indexed_pages:
        file_path = site_dir / rel_path
        if not file_path.exists():
            continue
        soup = load_html(file_path)
        aside = soup.find("aside")
        if not aside:
            missing_sidebar.append(rel_path)
            continue

        pages_with_sidebar += 1
        for a in aside.find_all("a", href=True):
            href = a["href"].strip()
            if not href or href.startswith(("http://", "https://", "mailto:", "tel:", "#", "javascript:")):
                continue
            if href == "/":
                target = "index.html"
                if target not in expected_paths:
                    broken_sidebar_links.append([rel_path, href])
                continue
            if "/public/" in href:
                broken_sidebar_links.append([rel_path, href])
                continue
            target = href.split("#")[0].split("?")[0]
            if target.startswith("/"):
                target = target.lstrip("/")
            else:
                target = (Path(rel_path).parent / target).as_posix().lstrip("/")
            if target.endswith("/"):
                target += "index.html"
            if "." not in Path(target).name:
                target += "/index.html"
            if target not in expected_paths:
                broken_sidebar_links.append([rel_path, href])

    return {
        "pages_with_sidebar": pages_with_sidebar,
        "missing_sidebar_pages": missing_sidebar,
        "broken_sidebar_links": broken_sidebar_links[:200],
    }


def metadata_issues(site_dir: Path, indexed_pages: list[str]) -> dict[str, Any]:
    missing: list[dict[str, str]] = []
    schema_mismatch_pages: list[str] = []
    faq_schema_without_visible_faq: list[str] = []

    for rel_path in indexed_pages:
        soup = load_html(site_dir / rel_path)

        title = soup.find("title")
        h1 = soup.find("h1")
        description_meta = soup.find("meta", attrs={"name": re.compile("^description$", re.I)})
        canonical = soup.find("link", rel="canonical")

        if not title or not normalize_text(title.get_text(" ", strip=True)):
            missing.append({"page": rel_path, "field": "title"})
        if not h1 or not normalize_text(h1.get_text(" ", strip=True)):
            missing.append({"page": rel_path, "field": "h1"})
        if not description_meta or not normalize_text(description_meta.get("content", "")):
            missing.append({"page": rel_path, "field": "meta_description"})
        if not canonical or not normalize_text(canonical.get("href", "")):
            missing.append({"page": rel_path, "field": "canonical"})

        canonical_href = normalize_text(canonical.get("href", "")) if canonical else ""
        has_visible_faq = bool(
            soup.find(string=re.compile(r"faq|поширені питання|часті питання", re.I))
            or len(soup.find_all("details")) >= 2
        )
        for node in soup.find_all("script", {"type": "application/ld+json"}):
            raw = (node.string or node.get_text() or "").strip()
            if not raw:
                continue
            try:
                data = json.loads(raw)
            except Exception:
                continue
            items = data if isinstance(data, list) else [data]
            for item in items:
                if not isinstance(item, dict):
                    continue
                typ = item.get("@type")
                if typ == "FAQPage" and not has_visible_faq:
                    faq_schema_without_visible_faq.append(rel_path)
                for key in ("url", "mainEntityOfPage"):
                    value = item.get(key)
                    if isinstance(value, str) and canonical_href and value.strip() != canonical_href:
                        schema_mismatch_pages.append(rel_path)
                    if isinstance(value, dict) and "@" in value:
                        nested = str(value.get("@id", "")).strip()
                        if nested and canonical_href and nested != canonical_href:
                            schema_mismatch_pages.append(rel_path)

    return {
        "missing_title_h1_meta_canonical_count": len(missing),
        "missing_title_h1_meta_canonical": missing,
        "schema_mismatch_count": len(sorted(set(schema_mismatch_pages))),
        "schema_mismatch_pages": sorted(set(schema_mismatch_pages)),
        "faq_schema_without_visible_faq_count": len(sorted(set(faq_schema_without_visible_faq))),
        "faq_schema_without_visible_faq_pages": sorted(set(faq_schema_without_visible_faq)),
    }


def food_cluster_status(site_dir: Path) -> dict[str, Any]:
    first_paragraphs: dict[str, str] = {}
    paragraph_map: dict[str, list[str]] = {}

    for rel_path in FOOD_CLUSTER_PAGES:
        file_path = site_dir / rel_path
        if not file_path.exists():
            continue
        soup = load_html(file_path)
        paragraphs = [normalize_text(p.get_text(" ", strip=True)) for p in soup.find_all("p")]
        paragraphs = [p for p in paragraphs if len(p) >= 120]
        if paragraphs:
            first_paragraphs[rel_path] = paragraphs[0]
        for p in paragraphs:
            paragraph_map.setdefault(p, []).append(rel_path)

    duplicate_groups = [
        {"paragraph": p, "pages": sorted(paths)}
        for p, paths in paragraph_map.items()
        if len(set(paths)) > 1
    ]
    duplicate_groups.sort(key=lambda x: (-len(x["pages"]), -len(x["paragraph"])))
    unique_first = len(set(first_paragraphs.values())) == len(first_paragraphs)

    ok = unique_first and not duplicate_groups and len(first_paragraphs) == len(FOOD_CLUSTER_PAGES)
    return {
        "food_cluster_pages_checked": FOOD_CLUSTER_PAGES,
        "food_cluster_first_paragraph_unique": unique_first,
        "food_cluster_duplicate_paragraph_groups": duplicate_groups[:20],
        "food_cluster_duplicate_paragraph_status": "ok" if not duplicate_groups else "duplicates_found",
        "food_cluster_status": "ok" if ok else "needs_review",
    }


def service_files_in_public(site_dir: Path) -> list[str]:
    results: list[str] = []
    for p in site_dir.rglob("*"):
        if p.is_dir():
            continue
        rel = p.relative_to(site_dir).as_posix()
        if rel in {"robots.txt", "sitemap.xml"}:
            continue
        if p.suffix.lower() in SERVICE_EXTENSIONS:
            results.append(rel)
    return sorted(results)


def check_utf8_bom_repo(repo_root: Path) -> dict[str, Any]:
    files_with_bom: list[str] = []
    for p in repo_root.rglob("*"):
        if not p.is_file():
            continue
        if ".git" in p.parts or "__pycache__" in p.parts:
            continue
        if p.suffix.lower() not in {".html", ".xml", ".txt", ".css", ".js", ".json", ".md", ".py", ".htaccess"}:
            continue
        raw = p.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            files_with_bom.append(p.relative_to(repo_root).as_posix())
    return {"utf8_bom_files_repo": sorted(files_with_bom)}


def check_robots_status(repo_root: Path) -> dict[str, Any]:
    robots_path = repo_root / "public" / "robots.txt"
    if not robots_path.exists():
        return {"robots_txt_status": "missing"}
    text = robots_path.read_text(encoding="utf-8")
    expected = "Sitemap: https://guide.youreco.com.ua/sitemap.xml"
    return {"robots_txt_status": "ok" if expected in text else "invalid_sitemap_reference"}


def check_htaccess_status(repo_root: Path) -> dict[str, Any]:
    htaccess_path = repo_root / ".htaccess"
    if not htaccess_path.exists():
        return {"htaccess_status": "missing"}
    text = htaccess_path.read_text(encoding="utf-8")
    needed = [
        "RedirectMatch 403 (?i)^/(public|\\.git|\\.vscode)(/|$)",
        "RedirectMatch 403 (?i)^/(?!robots\\.txt$).+\\.txt$",
    ]
    status = "ok" if all(rule in text for rule in needed) else "missing_required_block_rules"
    return {"htaccess_status": status}


def build_final_report(repo_root: Path, site_dir: Path, build_command: str) -> dict[str, Any]:
    base = build_report(site_dir)
    indexed_pages = [p["rel_path"] for p in base["pages"] if p["exists"] and not p["noindex"] and not p["is_redirect"]]
    sitemap_duplicates = len(base["sitemap_urls"]) - len(set(base["sitemap_urls"]))
    sitemap_paths = [p["rel_path"] for p in base["pages"]]
    sitemap_files_missing = [p["rel_path"] for p in base["pages"] if not p["exists"]]

    sidebar = sidebar_issues(site_dir, indexed_pages)
    meta = metadata_issues(site_dir, indexed_pages)
    food = food_cluster_status(site_dir)
    service_files = service_files_in_public(site_dir)
    bom_status = check_utf8_bom_repo(repo_root)
    robots = check_robots_status(repo_root)
    htaccess = check_htaccess_status(repo_root)

    critical_fail = any(
        [
            base["indexed_under_300_count"] > 0,
            bool(base["stamp_phrase_pages"]),
            food["food_cluster_status"] != "ok",
            bool(sidebar["missing_sidebar_pages"]),
            bool(sidebar["broken_sidebar_links"]),
            base["contains_v_soft_hyphen_bullet"],
            base["hidden_unicode_found"],
            base["broken_internal_links_count"] > 0,
            base["links_to_noindex_redirect_count"] > 0,
            base["links_to_public_count"] > 0,
            len(base["noindex_or_redirect_in_sitemap"]) > 0,
            meta["missing_title_h1_meta_canonical_count"] > 0,
            base["canonical_mismatch_indexed_count"] > 0,
            base["jsonld_error_count"] > 0,
            meta["schema_mismatch_count"] > 0,
            meta["faq_schema_without_visible_faq_count"] > 0,
            len(service_files) > 0,
            len(bom_status["utf8_bom_files_repo"]) > 0,
            base["cyrillic_status"] != "не зіпсована",
            sitemap_duplicates > 0,
            len(sitemap_files_missing) > 0,
            robots["robots_txt_status"] != "ok",
            htaccess["htaccess_status"] != "ok",
        ]
    )

    return {
        "check_datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "build_command": build_command,
        "public_html_count": len(collect_html_files(site_dir)),
        "sitemap_url_count": base["sitemap_url_count"],
        "indexed_pages_count": base["indexed_url_count"],
        "noindex_redirect_pages_count": len(base["noindex_or_redirect_in_sitemap"]),
        "indexed_under_300_count": base["indexed_under_300_count"],
        "indexed_300_500_count": base["indexed_300_500_count"],
        "stamp_phrase_pages": base["stamp_phrase_pages"],
        "food_cluster_duplicate_paragraph_status": food["food_cluster_duplicate_paragraph_status"],
        "food_cluster_status": food["food_cluster_status"],
        "sidebar_status": "ok" if not sidebar["missing_sidebar_pages"] and not sidebar["broken_sidebar_links"] else "issues_found",
        "v_soft_hyphen_shyny_status": "absent" if not base["contains_v_soft_hyphen_bullet"] else "present",
        "hidden_unicode_status": "absent" if not base["hidden_unicode_found"] else "present",
        "broken_internal_links": base["broken_internal_links_count"],
        "links_to_noindex_redirect": base["links_to_noindex_redirect_count"],
        "links_to_public": base["links_to_public_count"],
        "noindex_redirect_urls_in_sitemap": base["noindex_or_redirect_in_sitemap"],
        "sitemap_duplicate_urls_count": sitemap_duplicates,
        "sitemap_missing_html_files": sitemap_files_missing,
        "missing_title_h1_meta_canonical": meta["missing_title_h1_meta_canonical"],
        "missing_title_h1_meta_canonical_count": meta["missing_title_h1_meta_canonical_count"],
        "indexed_canonical_mismatch_count": base["canonical_mismatch_indexed_count"],
        "jsonld_errors_count": base["jsonld_error_count"],
        "schema_mismatch_count": meta["schema_mismatch_count"],
        "faq_schema_without_visible_faq_count": meta["faq_schema_without_visible_faq_count"],
        "service_files_in_public": service_files,
        "robots_txt_status": robots["robots_txt_status"],
        "htaccess_status": htaccess["htaccess_status"],
        "utf8_bom_files_repo": bom_status["utf8_bom_files_repo"],
        "cyrillic_status": base["cyrillic_status"],
        "sidebar_missing_pages": sidebar["missing_sidebar_pages"],
        "sidebar_broken_links": sidebar["broken_sidebar_links"],
        "food_cluster_duplicate_groups": food["food_cluster_duplicate_paragraph_groups"],
        "final_status": "ДОБРЕ" if not critical_fail else "НЕ ДОБРЕ",
        "production_verdict": "готово до деплою" if not critical_fail else "не готово до деплою",
    }


def to_markdown(report: dict[str, Any]) -> str:
    def list_line(values: list[Any]) -> str:
        return ", ".join(str(v) for v in values) if values else "[]"

    lines = [
        "# ЕТАП 13: Фінальний контроль після ЕТАПУ 12",
        "",
        f"- дата перевірки: {report['check_datetime']}",
        f"- команда збірки: `{report['build_command']}`",
        f"- HTML у `public/`: {report['public_html_count']}",
        f"- URL у sitemap: {report['sitemap_url_count']}",
        f"- indexed pages: {report['indexed_pages_count']}",
        f"- noindex/redirect pages: {report['noindex_redirect_pages_count']}",
        f"- indexed_under_300_count: {report['indexed_under_300_count']}",
        f"- indexed_300_500_count: {report['indexed_300_500_count']}",
        f"- stamp_phrase_pages: {list_line(report['stamp_phrase_pages'])}",
        f"- food cluster duplicate paragraph status: {report['food_cluster_duplicate_paragraph_status']}",
        f"- sidebar status: {report['sidebar_status']}",
        f"- `в­• Шини` status: {report['v_soft_hyphen_shyny_status']}",
        f"- hidden Unicode status: {report['hidden_unicode_status']}",
        f"- broken internal links: {report['broken_internal_links']}",
        f"- links to noindex/redirect: {report['links_to_noindex_redirect']}",
        f"- links to `/public/`: {report['links_to_public']}",
        f"- noindex/redirect URL у sitemap: {list_line(report['noindex_redirect_urls_in_sitemap'])}",
        f"- missing title/H1/meta/canonical: {report['missing_title_h1_meta_canonical_count']}",
        f"- indexed canonical mismatch: {report['indexed_canonical_mismatch_count']}",
        f"- JSON-LD errors: {report['jsonld_errors_count']}",
        f"- schema mismatch: {report['schema_mismatch_count']}",
        f"- service files in `public`: {list_line(report['service_files_in_public'])}",
        f"- robots.txt status: {report['robots_txt_status']}",
        f"- `.htaccess` status: {report['htaccess_status']}",
        f"- UTF-8/BOM status: {'ok' if not report['utf8_bom_files_repo'] else 'BOM found'}",
        f"- Кирилиця: {report['cyrillic_status']}",
        f"- фінальний статус: {report['final_status']}",
        f"- production verdict: {report['production_verdict']}",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--site-dir", default="public")
    parser.add_argument("--json-out", required=True)
    parser.add_argument("--md-out", required=True)
    parser.add_argument("--build-command", default="python scripts/build_public.py")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    site_dir = (repo_root / args.site_dir).resolve() if not Path(args.site_dir).is_absolute() else Path(args.site_dir)
    report = build_final_report(repo_root, site_dir, args.build_command)

    json_out = Path(args.json_out).resolve()
    md_out = Path(args.md_out).resolve()
    json_out.parent.mkdir(parents=True, exist_ok=True)
    md_out.parent.mkdir(parents=True, exist_ok=True)

    json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    md_out.write_text(to_markdown(report), encoding="utf-8")
    print(f"FINAL_CONTROL_OK {json_out} {md_out}")


if __name__ == "__main__":
    main()
