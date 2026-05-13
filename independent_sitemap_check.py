from __future__ import annotations

import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parent
REPORT_PATH = ROOT / "independent-sitemap-check-report.md"
COMMIT = "8d7331f"
BASE_URL = "https://guide.youreco.com.ua"
IGNORED_DIRS = {".git", "node_modules", "dist", "build", "__pycache__"}
SERVICE_KEYWORDS = ("404", "error", "test", "draft", "debug")
ALLOWED_CHANGED_FILES = {
    "audit-url-map.csv",
    "audit-url-map.md",
    "sitemap-noindex-fix-report.md",
    "sitemap.xml",
    "validate_url_map.py",
    "validation-report.md",
}
IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".ico",
    ".bmp",
    ".avif",
}
MOJIBAKE_MARKERS = (
    "Ð",
    "Ñ",
    "Â",
    "Ã",
    "¤",
    "�",
    "â€",
    "â€™",
    "â€œ",
    "â€“",
    "Ñ–",
    "Ñ—",
    "Ñ”",
    "Ñ”",
)


@dataclass
class HtmlInfo:
    file_path: str
    page_url: str
    canonical_url: str | None
    meta_robots: str | None
    has_noindex: bool
    h1: str | None
    title: str | None
    meta_description: str | None
    encoding_warning: str | None = None

    @property
    def effective_url(self) -> str:
        return self.canonical_url or self.page_url


class SeoHtmlParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title: list[str] = []
        self.h1: list[str] = []
        self.canonical: str | None = None
        self.robots: str | None = None
        self.description: str | None = None
        self._capture_title = False
        self._capture_h1 = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {name.lower(): (value or "") for name, value in attrs}
        tag = tag.lower()
        if tag == "title":
            self._capture_title = True
        elif tag == "h1":
            self._capture_h1 = True
        elif tag == "link" and attrs_dict.get("rel", "").lower() == "canonical":
            href = attrs_dict.get("href", "").strip()
            if href:
                self.canonical = href
        elif tag == "meta":
            name = attrs_dict.get("name", "").strip().lower()
            content = attrs_dict.get("content", "").strip()
            if name == "robots":
                self.robots = content
            elif name == "description":
                self.description = content

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self._capture_title = False
        elif tag == "h1":
            self._capture_h1 = False

    def handle_data(self, data: str) -> None:
        if self._capture_title:
            self.title.append(data)
        if self._capture_h1:
            self.h1.append(data)


def normalize_url(url: str | None) -> str | None:
    if not url:
        return None
    value = unescape(url.strip())
    if not value:
        return None
    value = value.replace("\\", "/")
    if value.startswith(BASE_URL):
        value = BASE_URL + value[len(BASE_URL):]
    value = re.sub(r"(?<!:)/{2,}", "/", value)
    value = re.sub(r"^https:/([^/])", r"https://\1", value)
    value = re.sub(r"^http:/([^/])", r"http://\1", value)
    if value.endswith("/") and value not in {BASE_URL, BASE_URL + "/"}:
        value = value.rstrip("/")
    if value == BASE_URL + "/":
        value = BASE_URL
    return value


def file_to_page_url(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return BASE_URL
    return normalize_url(f"{BASE_URL}/{rel}") or f"{BASE_URL}/{rel}"


def read_text(path: Path) -> tuple[str, str | None]:
    try:
        return path.read_text(encoding="utf-8"), None
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace"), f"UTF-8 decode warning in {path.relative_to(ROOT).as_posix()}"


def detect_cyrillic_issue(value: str | None) -> bool:
    if not value:
        return False
    return any(marker in value for marker in MOJIBAKE_MARKERS)


def find_html_files() -> list[Path]:
    html_files: list[Path] = []
    for current_root, dirs, files in os.walk(ROOT):
        dirs[:] = [name for name in dirs if name not in IGNORED_DIRS]
        for filename in files:
            if filename.lower().endswith(".html"):
                html_files.append(Path(current_root) / filename)
    html_files.sort()
    return html_files


def parse_html(path: Path) -> HtmlInfo:
    html_text, encoding_warning = read_text(path)
    parser = SeoHtmlParser()
    parser.feed(html_text)
    robots = parser.robots.strip() if parser.robots else None
    canonical = normalize_url(parser.canonical)
    title = " ".join(part.strip() for part in parser.title if part.strip()) or None
    h1 = " ".join(part.strip() for part in parser.h1 if part.strip()) or None
    meta_description = parser.description.strip() if parser.description else None
    return HtmlInfo(
        file_path=path.relative_to(ROOT).as_posix(),
        page_url=file_to_page_url(path),
        canonical_url=canonical,
        meta_robots=robots,
        has_noindex=bool(robots and "noindex" in robots.lower()),
        h1=h1,
        title=title,
        meta_description=meta_description,
        encoding_warning=encoding_warning,
    )


def extract_sitemap_urls(xml_text: str) -> list[str]:
    root = ET.fromstring(xml_text)
    locs: list[str] = []
    for element in root.iter():
        if element.tag.endswith("loc") and element.text:
            loc = normalize_url(element.text)
            if loc:
                locs.append(loc)
    return locs


def run_git(*args: str) -> tuple[bool, str]:
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except FileNotFoundError:
        return False, "git executable not found"
    output = (completed.stdout or completed.stderr or "").strip()
    if completed.returncode != 0:
        return False, output or f"git {' '.join(args)} failed with code {completed.returncode}"
    return True, output


def is_service_like(url: str) -> bool:
    lowered = url.lower()
    return any(keyword in lowered for keyword in SERVICE_KEYWORDS)


def is_image_path(path: str) -> bool:
    return Path(path).suffix.lower() in IMAGE_EXTENSIONS


def quote_list(items: Iterable[str]) -> str:
    unique_items = list(items)
    if not unique_items:
        return "None."
    return "\n".join(f"- {item}" for item in unique_items)


def main() -> int:
    critical_failures: list[str] = []
    errors: list[str] = []
    warnings: list[str] = []

    html_infos = [parse_html(path) for path in find_html_files()]
    sitemap_path = ROOT / "sitemap.xml"
    if not sitemap_path.exists():
        critical_failures.append("sitemap.xml not found.")
        REPORT_PATH.write_text(
            "# Independent Sitemap Check Report\n\n## Result\nFAIL\n\n## Scope\nIndependent verification of sitemap/noindex fix after commit 8d7331f.\n\n## Critical failures\n- sitemap.xml not found.\n",
            encoding="utf-8",
        )
        return 1

    sitemap_text, sitemap_encoding_warning = read_text(sitemap_path)
    if sitemap_encoding_warning:
        warnings.append(sitemap_encoding_warning)

    try:
        sitemap_urls = extract_sitemap_urls(sitemap_text)
    except ET.ParseError as exc:
        critical_failures.append(f"Failed to parse sitemap.xml: {exc}")
        sitemap_urls = []

    unique_sitemap_urls = list(dict.fromkeys(sitemap_urls))
    sitemap_counter = Counter(sitemap_urls)
    duplicate_sitemap_urls = sorted(url for url, count in sitemap_counter.items() if count > 1)
    if duplicate_sitemap_urls:
        critical_failures.append("sitemap.xml contains duplicate <loc> entries.")

    url_to_files: dict[str, list[HtmlInfo]] = defaultdict(list)
    page_urls: set[str] = set()
    possible_cyrillic_issues: list[str] = []
    for info in html_infos:
        url_to_files[info.effective_url].append(info)
        page_urls.add(info.page_url)
        if info.encoding_warning:
            warnings.append(info.encoding_warning)
        fields = {
            "title": info.title,
            "h1": info.h1,
            "meta description": info.meta_description,
            "canonical": info.canonical_url,
        }
        for field_name, value in fields.items():
            if detect_cyrillic_issue(value):
                possible_cyrillic_issues.append(f"{info.file_path}: suspicious {field_name}: {value}")

    if detect_cyrillic_issue(sitemap_text):
        possible_cyrillic_issues.append("sitemap.xml: suspicious Cyrillic/mojibake markers found")

    if possible_cyrillic_issues:
        critical_failures.append("Possible Cyrillic encoding issues detected.")

    duplicate_canonical_urls: dict[str, list[str]] = {}
    noindex_unique_urls: set[str] = set()
    noindex_urls_in_sitemap: list[str] = []
    index_like_unique_urls: set[str] = set()
    index_like_missing_fail: list[str] = []
    index_like_missing_warning: list[str] = []

    for url, infos in sorted(url_to_files.items()):
        file_paths = [item.file_path for item in infos]
        if len(file_paths) > 1:
            duplicate_canonical_urls[url] = file_paths
            robots_states = sorted({(item.meta_robots or "").lower() for item in infos})
            warnings.append(
                f"Duplicate canonical/page URL {url} appears in {', '.join(file_paths)}; robots states: {robots_states or ['(none)']}"
            )

        all_noindex = all(item.has_noindex for item in infos)
        any_index_like = any(
            (not item.has_noindex) and item.canonical_url and not is_service_like(item.effective_url)
            for item in infos
        )
        if all_noindex:
            noindex_unique_urls.add(url)
        if any_index_like:
            index_like_unique_urls.add(url)

    sitemap_url_set = set(unique_sitemap_urls)
    known_html_url_set = set(url_to_files) | page_urls
    noindex_urls_in_sitemap = sorted(url for url in noindex_unique_urls if url in sitemap_url_set)
    if noindex_urls_in_sitemap:
        critical_failures.append("Found noindex URL(s) still present in sitemap.xml.")

    missing_index_like_urls = sorted(url for url in index_like_unique_urls if url not in sitemap_url_set)
    for url in missing_index_like_urls:
        if url in duplicate_canonical_urls or is_service_like(url):
            index_like_missing_warning.append(url)
            warnings.append(f"Index-like URL missing from sitemap but treated as warning: {url}")
        else:
            index_like_missing_fail.append(url)
            critical_failures.append(f"Index-like canonical URL missing from sitemap: {url}")

    sitemap_without_match = sorted(url for url in sitemap_url_set if url not in known_html_url_set)
    if sitemap_without_match:
        errors.extend(f"Sitemap loc has no matching HTML/canonical/page URL: {url}" for url in sitemap_without_match)

    commit_found, commit_stat_output = run_git("show", "--stat", "--oneline", COMMIT)
    if not commit_found:
        critical_failures.append(f"Git unavailable or commit {COMMIT} not found: {commit_stat_output}")
    commit_found_name, commit_name_output = run_git("show", "--name-only", "--oneline", COMMIT)
    if not commit_found_name:
        critical_failures.append(f"Unable to inspect file list for commit {COMMIT}: {commit_name_output}")
        changed_files: list[str] = []
    else:
        changed_files = [line.strip() for line in commit_name_output.splitlines()[1:] if line.strip()]

    status_ok, git_status_output = run_git("status", "--short")
    if not status_ok:
        critical_failures.append(f"Unable to read git status: {git_status_output}")
        git_status_output = "git status unavailable"

    diff_ok, sitemap_diff_output = run_git("diff", f"{COMMIT}^", COMMIT, "--", "sitemap.xml")
    if not diff_ok:
        critical_failures.append(f"Unable to inspect sitemap diff: {sitemap_diff_output}")

    old_sitemap_ok, old_sitemap_text = run_git("show", f"{COMMIT}^:sitemap.xml")
    new_sitemap_ok, new_sitemap_text = run_git("show", f"{COMMIT}:sitemap.xml")
    removed_urls: list[str] = []
    added_urls: list[str] = []
    if old_sitemap_ok and new_sitemap_ok:
        try:
            old_urls = extract_sitemap_urls(old_sitemap_text)
            new_urls = extract_sitemap_urls(new_sitemap_text)
            removed_urls = [url for url in old_urls if url not in set(new_urls)]
            added_urls = [url for url in new_urls if url not in set(old_urls)]
        except ET.ParseError as exc:
            critical_failures.append(f"Unable to parse historical sitemap.xml for diff verification: {exc}")
    else:
        critical_failures.append(f"Unable to read sitemap.xml from commit history for {COMMIT}.")

    suspicious_additions = bool(added_urls)
    if suspicious_additions:
        critical_failures.append("sitemap.xml gained new URL(s) in commit 8d7331f.")

    html_changed = any(path.lower().endswith((".html", ".htm")) for path in changed_files)
    css_changed = any(path.lower().endswith(".css") for path in changed_files)
    js_changed = any(path.lower().endswith(".js") for path in changed_files)
    robots_changed = any(path.lower() == "robots.txt" for path in changed_files)
    images_changed = any(is_image_path(path) for path in changed_files)
    sitemap_changed = any(path.lower() == "sitemap.xml" for path in changed_files)
    audit_files_changed = any(path in {"audit-url-map.csv", "audit-url-map.md"} for path in changed_files)
    only_allowed_files_changed = bool(changed_files) and set(changed_files).issubset(ALLOWED_CHANGED_FILES)

    if html_changed or css_changed or js_changed or robots_changed or images_changed:
        critical_failures.append("Commit 8d7331f changed forbidden asset types (HTML/CSS/JS/robots/images).")

    allowed_status_entries = {
        "?? independent_sitemap_check.py",
        "?? independent-sitemap-check-report.md",
    }
    status_lines = [line for line in git_status_output.splitlines() if line.strip()]
    unexpected_status_lines = [line for line in status_lines if line not in allowed_status_entries]
    if unexpected_status_lines:
        critical_failures.append("Git status contains changes beyond the two allowed new files.")

    result = "PASS"
    final_decision = "INDEPENDENT CHECK PASSED"
    if critical_failures:
        result = "FAIL"
        final_decision = "INDEPENDENT CHECK FAILED"
    elif errors:
        final_decision = "INDEPENDENT CHECK NEEDS REVIEW"

    counts = {
        "HTML files scanned": str(len(html_infos)),
        "Unique canonical/page URLs": str(len(url_to_files)),
        "Sitemap loc URLs": str(len(unique_sitemap_urls)),
        "Noindex HTML files": str(sum(1 for item in html_infos if item.has_noindex)),
        "Noindex unique URLs": str(len(noindex_unique_urls)),
        "Noindex URLs still in sitemap": str(len(noindex_urls_in_sitemap)),
        "Index-like unique URLs missing from sitemap": str(len(missing_index_like_urls)),
        "Duplicate sitemap loc entries": str(len(duplicate_sitemap_urls)),
        "Sitemap loc without matching HTML/canonical": str(len(sitemap_without_match)),
        "Duplicate canonical URLs": str(len(duplicate_canonical_urls)),
        "Possible Cyrillic encoding issues": str(len(possible_cyrillic_issues)),
    }

    duplicate_canonical_lines: list[str] = []
    for url, files in sorted(duplicate_canonical_urls.items()):
        duplicate_canonical_lines.append(f"- {url} -> {', '.join(files)}")

    report_lines = [
        "# Independent Sitemap Check Report",
        "",
        "## Result",
        result,
        "",
        "## Scope",
        f"Independent verification of sitemap/noindex fix after commit {COMMIT}.",
        "",
        "## Critical failures",
        quote_list(critical_failures),
        "",
        "## Errors",
        quote_list(errors),
        "",
        "## Warnings",
        quote_list(warnings),
        "",
        "## Counts",
    ]

    report_lines.extend(f"- {label}: {value}" for label, value in counts.items())
    report_lines.extend(
        [
            "",
            f"## Commit {COMMIT} verification",
            f"- Commit found: {'yes' if commit_found and commit_found_name else 'no'}",
            f"- Files changed in commit: {', '.join(changed_files) if changed_files else 'None'}",
            f"- HTML changed: {'yes' if html_changed else 'no'}",
            f"- CSS changed: {'yes' if css_changed else 'no'}",
            f"- JS changed: {'yes' if js_changed else 'no'}",
            f"- robots.txt changed: {'yes' if robots_changed else 'no'}",
            f"- images changed: {'yes' if images_changed else 'no'}",
            f"- sitemap.xml changed: {'yes' if sitemap_changed else 'no'}",
            f"- audit files changed: {'yes' if audit_files_changed else 'no'}",
            f"- only allowed files changed: {'yes' if only_allowed_files_changed else 'no'}",
            "",
            "## Sitemap diff verification",
            f"- URL blocks removed: {len(removed_urls)}",
            f"- URL blocks added: {len(added_urls)}",
            f"- Added URLs: {', '.join(added_urls) if added_urls else 'None'}",
            f"- Removed URLs: {', '.join(removed_urls) if removed_urls else 'None'}",
            f"- Suspicious additions: {'yes' if suspicious_additions else 'no'}",
            "",
            "## Remaining noindex URLs in sitemap",
            quote_list(noindex_urls_in_sitemap),
            "",
            "## Index-like URLs missing from sitemap",
            quote_list(missing_index_like_urls),
            "",
            "## Duplicate canonical URLs",
            "\n".join(duplicate_canonical_lines) if duplicate_canonical_lines else "None.",
            "",
            "## Git status",
            "```text",
            git_status_output or "",
            "```",
            "",
            "## Final decision",
            final_decision,
            "",
        ]
    )

    REPORT_PATH.write_text("\n".join(report_lines), encoding="utf-8")

    print(f"Result: {result}")
    print(f"Noindex URLs in sitemap: {len(noindex_urls_in_sitemap)}")
    print(f"Index-like URLs missing from sitemap: {len(missing_index_like_urls)}")
    print(f"Commit changed forbidden assets: {'yes' if (html_changed or css_changed or js_changed or robots_changed or images_changed) else 'no'}")
    print(f"Duplicate sitemap loc entries: {len(duplicate_sitemap_urls)}")
    print(f"Possible Cyrillic issues: {len(possible_cyrillic_issues)}")
    print(f"Final decision: {final_decision}")
    return 1 if result == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())