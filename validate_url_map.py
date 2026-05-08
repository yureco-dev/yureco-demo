from __future__ import annotations

import csv
import subprocess
from pathlib import Path
from typing import Iterable
import xml.etree.ElementTree as ET


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
REQUIRED_MD_SNIPPETS = [
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
    "Noindex pages found in sitemap",
    "Index pages missing from sitemap",
    "Pages missing canonical",
    "Pages missing H1",
    "Pages with JSON-LD parse errors",
    "Pages with possible encoding problems",
]
ENCODING_MARKERS = ["Ð", "Ñ", "�", "РЈ", "Р°", "С‚", "\\u043", "\\u044"]
ALLOWED_GIT_PATHS = {
    "audit-url-map.csv",
    "audit-url-map.md",
    "validate_url_map.py",
    "validation-report.md",
}
SITE_FILE_SUFFIXES = {".html", ".css", ".js"}
SITE_FILE_NAMES = {"sitemap.xml", "robots.txt"}


def normalize_rel_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def iter_html_files() -> list[Path]:
    html_files: list[Path] = []
    for path in ROOT.rglob("*.html"):
        if any(part in EXCLUDED_DIRS for part in path.relative_to(ROOT).parts):
            continue
        html_files.append(path)
    return sorted(html_files)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def run_git_status() -> tuple[list[str], str | None]:
    command = ["git", "-C", str(ROOT), "status", "--short"]
    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except FileNotFoundError:
        return [], "git executable not found"

    stdout = completed.stdout.strip()
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


def parse_csv(errors: list[str]) -> tuple[list[dict[str, str]], int, list[str]]:
    if not CSV_PATH.exists():
        return [], 0, []

    rows: list[dict[str, str]] = []
    raw_file_paths: list[str] = []
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        try:
            header = next(reader)
        except StopIteration:
            errors.append("audit-url-map.csv is empty.")
            return [], 0, []

        if header != REQUIRED_COLUMNS:
            errors.append(
                "CSV header does not match the required columns exactly."
            )

        total_rows = 0
        for index, raw_row in enumerate(reader, start=2):
            if not raw_row or not any(cell.strip() for cell in raw_row):
                continue
            total_rows += 1
            if len(raw_row) != len(REQUIRED_COLUMNS):
                errors.append(
                    f"CSV row {index} has {len(raw_row)} columns instead of {len(REQUIRED_COLUMNS)}."
                )
                continue

            row = dict(zip(REQUIRED_COLUMNS, raw_row))
            rows.append(row)
            raw_file_paths.append(row["file_path"].replace("\\", "/").strip())

    return rows, total_rows, raw_file_paths


def parse_sitemap(errors: list[str]) -> set[str]:
    if not SITEMAP_PATH.exists():
        return set()
    try:
        root = ET.fromstring(SITEMAP_PATH.read_text(encoding="utf-8-sig", errors="replace"))
    except ET.ParseError as exc:
        errors.append(f"sitemap.xml could not be parsed: {exc}.")
        return set()

    urls: set[str] = set()
    for elem in root.iter():
        if elem.tag.endswith("loc") and elem.text:
            urls.add(elem.text.strip())
    return urls


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


def has_noindex(meta_robots: str) -> bool:
    return "noindex" in meta_robots.lower()


def find_encoding_issues(content: str) -> list[str]:
    return [marker for marker in ENCODING_MARKERS if marker in content]


def main() -> int:
    critical_failures: list[str] = []
    errors: list[str] = []
    warnings: list[str] = []

    git_status_lines, git_error = run_git_status()
    changed_paths = parse_git_changed_paths(git_status_lines)
    if git_error:
        errors.append(f"Git status unavailable: {git_error}.")
        git_status_rendered = f"git status --short unavailable: {git_error}"
    else:
        git_status_rendered = "\n".join(git_status_lines) if git_status_lines else "(clean)"

        unexpected_paths = [path for path in changed_paths if path not in ALLOWED_GIT_PATHS]
        forbidden_paths = [
            path
            for path in unexpected_paths
            if Path(path).suffix.lower() in SITE_FILE_SUFFIXES or Path(path).name.lower() in SITE_FILE_NAMES
        ]
        if forbidden_paths:
            critical_failures.append(
                "Forbidden site files changed: " + ", ".join(sorted(forbidden_paths))
            )
        if unexpected_paths:
            errors.append(
                "Unexpected changed/created files found: " + ", ".join(sorted(unexpected_paths))
            )

    for path in (CSV_PATH, MD_PATH, ROOT / "validate_url_map.py"):
        if not path.exists():
            errors.append(f"Required file missing: {path.name}.")

    csv_rows, csv_row_count, csv_file_paths = parse_csv(errors)
    html_files = iter_html_files()
    html_rel_paths = {normalize_rel_path(path) for path in html_files}

    if csv_row_count != len(html_files):
        errors.append(
            f"CSV row count mismatch: {csv_row_count} rows vs {len(html_files)} HTML files."
        )

    csv_path_set = set(csv_file_paths)
    missing_from_csv = sorted(html_rel_paths - csv_path_set)
    missing_in_project = sorted(csv_path_set - html_rel_paths)
    if missing_from_csv:
        errors.append(
            f"HTML files missing from CSV file_path: {len(missing_from_csv)}."
        )
    if missing_in_project:
        errors.append(
            f"CSV contains non-existent file_path values: {len(missing_in_project)}."
        )

    sitemap_urls = parse_sitemap(errors)

    pages_in_sitemap = 0
    noindex_pages = 0
    index_like_pages = 0
    noindex_pages_in_sitemap = 0
    index_missing_from_sitemap = 0
    missing_canonical = 0
    missing_h1 = 0
    missing_meta_description = 0
    missing_updated_date = 0
    json_ld_parse_errors = 0

    for row_number, row in enumerate(csv_rows, start=2):
        for column in YES_NO_COLUMNS:
            if row[column] not in YES_NO_VALUES:
                errors.append(
                    f"CSV row {row_number} has invalid {column} value: {row[column]!r}."
                )

        if row["target_status_suggestion"] not in STATUS_VALUES:
            errors.append(
                f"CSV row {row_number} has invalid target_status_suggestion: {row['target_status_suggestion']!r}."
            )

        url_candidates = [value.strip() for value in (row["canonical_url"], row["page_url"]) if value.strip()]
        in_actual_sitemap = any(url in sitemap_urls for url in url_candidates)
        declared_in_sitemap = row["in_sitemap"] == "YES"
        if declared_in_sitemap:
            pages_in_sitemap += 1
            if sitemap_urls and not in_actual_sitemap:
                errors.append(
                    f"CSV row {row_number} is marked in_sitemap=YES but page_url/canonical_url is absent from sitemap.xml."
                )
        elif in_actual_sitemap:
            errors.append(
                f"CSV row {row_number} is present in sitemap.xml but marked in_sitemap=NO."
            )

        is_noindex = has_noindex(row["meta_robots"])
        if is_noindex:
            noindex_pages += 1
            if in_actual_sitemap:
                noindex_pages_in_sitemap += 1
        else:
            index_like_pages += 1
            if sitemap_urls and not in_actual_sitemap:
                index_missing_from_sitemap += 1

        if not row["canonical_url"].strip():
            missing_canonical += 1
        if not row["h1"].strip():
            missing_h1 += 1
        if not row["meta_description"].strip():
            missing_meta_description += 1
        if row["has_visible_updated_date"] == "NO":
            missing_updated_date += 1
        if "parse error" in row["schema_types"].lower() or "parse error" in row["notes"].lower():
            json_ld_parse_errors += 1

    if noindex_pages_in_sitemap:
        warnings.append(
            f"SEO/AIO issue: {noindex_pages_in_sitemap} noindex pages are present in sitemap.xml."
        )
    if index_missing_from_sitemap:
        warnings.append(
            f"SEO/AIO issue: {index_missing_from_sitemap} index-like pages are missing from sitemap.xml."
        )

    md_text = read_text(MD_PATH) if MD_PATH.exists() else ""
    csv_text = read_text(CSV_PATH) if CSV_PATH.exists() else ""
    md_metrics = parse_md_metrics(md_text)

    for snippet in REQUIRED_MD_SNIPPETS:
        if snippet not in md_text:
            errors.append(f"audit-url-map.md is missing required content: {snippet}.")

    expected_metrics = {
        "total_html_files": len(html_files),
        "total_noindex": noindex_pages,
        "total_in_sitemap": pages_in_sitemap,
    }
    for key, expected in expected_metrics.items():
        actual = md_metrics.get(key)
        if actual is None:
            errors.append(f"audit-url-map.md is missing numeric metric: {key}.")
        elif actual != expected:
            errors.append(
                f"audit-url-map.md metric mismatch for {key}: {actual} vs expected {expected}."
            )

    encoding_issue_files: list[str] = []
    csv_markers = find_encoding_issues(csv_text)
    md_markers = find_encoding_issues(md_text)
    if csv_markers:
        critical_failures.append(
            "Possible Cyrillic encoding corruption in audit-url-map.csv: " + ", ".join(sorted(set(csv_markers)))
        )
        encoding_issue_files.append("audit-url-map.csv")
    if md_markers:
        critical_failures.append(
            "Possible Cyrillic encoding corruption in audit-url-map.md: " + ", ".join(sorted(set(md_markers)))
        )
        encoding_issue_files.append("audit-url-map.md")

    result = "PASS" if not critical_failures and not errors else "FAIL"
    if critical_failures and any("Forbidden site files changed" in item for item in critical_failures):
        final_decision = "VALIDATION FAILED BECAUSE SITE FILES WERE MODIFIED"
    elif result == "PASS":
        final_decision = "AUDIT IS VALID"
    else:
        final_decision = "AUDIT NEEDS FIXES"

    report_lines = [
        "# Validation Report",
        "",
        "## Result",
        result,
        "",
        "## Critical Failures",
    ]
    report_lines.extend(f"- {item}" for item in critical_failures) if critical_failures else report_lines.append("None")
    report_lines.extend([
        "",
        "## Errors",
    ])
    report_lines.extend(f"- {item}" for item in errors) if errors else report_lines.append("None")
    report_lines.extend([
        "",
        "## Warnings",
    ])
    report_lines.extend(f"- {item}" for item in warnings) if warnings else report_lines.append("None")
    report_lines.extend([
        "",
        "## Counts",
        f"- HTML files found: {len(html_files)}",
        f"- CSV rows: {csv_row_count}",
        f"- Sitemap URLs: {len(sitemap_urls)}",
        f"- Index-like pages: {index_like_pages}",
        f"- Noindex pages: {noindex_pages}",
        f"- Pages in sitemap: {pages_in_sitemap}",
        f"- Noindex pages in sitemap: {noindex_pages_in_sitemap}",
        f"- Index pages missing from sitemap: {index_missing_from_sitemap}",
        f"- Missing canonical: {missing_canonical}",
        f"- Missing H1: {missing_h1}",
        f"- Missing meta description: {missing_meta_description}",
        f"- Missing visible updated date: {missing_updated_date}",
        f"- JSON-LD parse errors: {json_ld_parse_errors}",
        f"- Possible encoding issues: {len(encoding_issue_files)}",
        "",
        "## Files changed or created",
        "```text",
        git_status_rendered,
        "```",
        "",
        "## Final decision",
        final_decision,
        "",
    ])

    REPORT_PATH.write_text("\n".join(report_lines), encoding="utf-8", newline="\n")

    print(f"RESULT={result}")
    print(f"HTML_FILES={len(html_files)}")
    print(f"CSV_ROWS={csv_row_count}")
    print(f"FORBIDDEN_SITE_FILE_CHANGES={'YES' if any('Forbidden site files changed' in item for item in critical_failures) else 'NO'}")
    print(f"CYRILLIC_ENCODING_ISSUES={'YES' if encoding_issue_files else 'NO'}")
    print(f"FINAL_DECISION={final_decision}")
    return 0 if result == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())