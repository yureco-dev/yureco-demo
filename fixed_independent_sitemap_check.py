from pathlib import Path
import re
import sys
import subprocess
from html import unescape
from collections import defaultdict, Counter

ROOT = Path(".")
SITEMAP_PATH = ROOT / "sitemap.xml"
REPORT_PATH = ROOT / "fixed-independent-sitemap-check-report.md"
TARGET_COMMIT = "8d7331f"

IGNORED_DIRS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "__pycache__",
}

ALLOWED_CHANGED_FILES = {
    "fixed_independent_sitemap_check.py",
    "fixed-independent-sitemap-check-report.md",
}

FORBIDDEN_CHANGED_SUFFIXES = {
    ".html",
    ".htm",
    ".css",
    ".js",
    ".xml",
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".svg",
    ".gif",
    ".ico",
}

MOJIBAKE_MARKERS = [
    "Ð",
    "Ñ",
    "�",
    "РЈ",
    "Р°",
    "С‚",
    "\\u043",
    "\\u044",
]

URL_PREFIX = "https://guide.youreco.com.ua/"


def run_cmd(args):
    try:
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except FileNotFoundError:
        return 127, "", f"Command not found: {args[0]}"


def should_ignore(path: Path) -> bool:
    return any(part in IGNORED_DIRS for part in path.parts)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value, flags=re.S)
    value = unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def first_match(pattern: str, text: str, flags=re.I | re.S) -> str:
    match = re.search(pattern, text, flags)
    if not match:
        return ""
    return unescape(match.group(1).strip())


def find_html_files():
    files = []
    for path in ROOT.rglob("*.html"):
        if should_ignore(path):
            continue
        files.append(path)
    return sorted(files, key=lambda p: p.as_posix())


def infer_url_from_path(path: Path) -> str:
    rel = path.as_posix()
    if rel == "index.html":
        return URL_PREFIX
    if rel.endswith("/index.html"):
        return URL_PREFIX + rel[:-len("index.html")]
    return URL_PREFIX + rel


def parse_html(path: Path):
    text = read_text(path)

    canonical = first_match(
        r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']',
        text,
    )
    if not canonical:
        canonical = first_match(
            r'<link[^>]+href=["\']([^"\']+)["\'][^>]+rel=["\']canonical["\']',
            text,
        )

    robots = first_match(
        r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']*)["\']',
        text,
    )
    if not robots:
        robots = first_match(
            r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+name=["\']robots["\']',
            text,
        )

    title = strip_tags(first_match(r"<title[^>]*>(.*?)</title>", text))
    h1 = strip_tags(first_match(r"<h1[^>]*>(.*?)</h1>", text))
    meta_description = first_match(
        r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)["\']',
        text,
    )
    if not meta_description:
        meta_description = first_match(
            r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+name=["\']description["\']',
            text,
        )

    page_url = canonical or infer_url_from_path(path)
    noindex = "noindex" in robots.lower()

    combined_for_encoding = " ".join([
        path.as_posix(),
        canonical,
        robots,
        title,
        h1,
        meta_description,
    ])

    return {
        "file_path": path.as_posix(),
        "canonical": canonical,
        "page_url": page_url,
        "robots": robots,
        "noindex": noindex,
        "title": title,
        "h1": h1,
        "meta_description": meta_description,
        "encoding_suspect": any(marker in combined_for_encoding for marker in MOJIBAKE_MARKERS),
    }


def parse_sitemap():
    if not SITEMAP_PATH.exists():
        return [], "sitemap.xml not found"

    text = read_text(SITEMAP_PATH)
    locs = re.findall(r"<loc>\s*(.*?)\s*</loc>", text, flags=re.I | re.S)
    locs = [unescape(loc.strip()) for loc in locs]
    return locs, ""


def verify_git_status():
    code, out, err = run_cmd(["git", "status", "--short"])
    if code != 0:
        return {
            "ok": False,
            "stdout": out,
            "stderr": err,
            "forbidden_changed": ["git status failed"],
        }

    forbidden = []
    for line in out.splitlines():
        if not line.strip():
            continue
        path = line[3:].strip()
        if " -> " in path:
            path = path.split(" -> ", 1)[1].strip()

        if path not in ALLOWED_CHANGED_FILES:
            forbidden.append(line)

    return {
        "ok": len(forbidden) == 0,
        "stdout": out,
        "stderr": err,
        "forbidden_changed": forbidden,
    }


def verify_commit():
    code, out, err = run_cmd(["git", "show", "--name-only", "--oneline", "--pretty=format:", TARGET_COMMIT])
    if code != 0:
        return {
            "commit_found": False,
            "files": [],
            "error": err or out,
            "html_changed": None,
            "css_changed": None,
            "js_changed": None,
            "robots_changed": None,
            "images_changed": None,
            "sitemap_changed": None,
            "forbidden_changed": True,
        }

    files = [line.strip() for line in out.splitlines() if line.strip()]

    def changed_suffix(*suffixes):
        return any(f.lower().endswith(suffixes) for f in files)

    html_changed = changed_suffix(".html", ".htm")
    css_changed = changed_suffix(".css")
    js_changed = changed_suffix(".js")
    robots_changed = any(Path(f).name.lower() == "robots.txt" for f in files)
    images_changed = changed_suffix(".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".ico")
    sitemap_changed = any(Path(f).name == "sitemap.xml" for f in files)

    forbidden_changed = html_changed or css_changed or js_changed or robots_changed or images_changed

    return {
        "commit_found": True,
        "files": files,
        "error": "",
        "html_changed": html_changed,
        "css_changed": css_changed,
        "js_changed": js_changed,
        "robots_changed": robots_changed,
        "images_changed": images_changed,
        "sitemap_changed": sitemap_changed,
        "forbidden_changed": forbidden_changed,
    }


def verify_sitemap_diff():
    code, out, err = run_cmd(["git", "diff", f"{TARGET_COMMIT}^", TARGET_COMMIT, "--", "sitemap.xml"])
    if code != 0:
        return {
            "ok": False,
            "error": err or out,
            "added_locs": [],
            "removed_locs": [],
            "raw_diff": out,
        }

    added_locs = []
    removed_locs = []

    for line in out.splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            match = re.search(r"<loc>\s*(.*?)\s*</loc>", line)
            if match:
                added_locs.append(unescape(match.group(1).strip()))
        elif line.startswith("-") and not line.startswith("---"):
            match = re.search(r"<loc>\s*(.*?)\s*</loc>", line)
            if match:
                removed_locs.append(unescape(match.group(1).strip()))

    return {
        "ok": True,
        "error": "",
        "added_locs": added_locs,
        "removed_locs": removed_locs,
        "raw_diff": out,
    }


def format_list(items, limit=200):
    if not items:
        return "None"
    lines = []
    for item in items[:limit]:
        lines.append(f"- {item}")
    if len(items) > limit:
        lines.append(f"- ... and {len(items) - limit} more")
    return "\n".join(lines)


def main():
    critical_failures = []
    errors = []
    warnings = []

    html_files = find_html_files()
    html_records = [parse_html(path) for path in html_files]

    sitemap_locs, sitemap_error = parse_sitemap()
    if sitemap_error:
        critical_failures.append(sitemap_error)

    sitemap_set = set(sitemap_locs)
    sitemap_counter = Counter(sitemap_locs)
    duplicate_sitemap_locs = [url for url, count in sitemap_counter.items() if count > 1]

    url_to_records = defaultdict(list)
    for record in html_records:
        key = record["canonical"] or record["page_url"]
        if key:
            url_to_records[key].append(record)

    unique_urls = set(url_to_records.keys())

    noindex_urls = set()
    index_like_urls = set()

    for url, records in url_to_records.items():
        has_noindex = any(r["noindex"] for r in records)
        has_index_like = any(not r["noindex"] for r in records)

        if has_noindex:
            noindex_urls.add(url)
        if has_index_like:
            index_like_urls.add(url)

        if has_noindex and has_index_like:
            warnings.append(f"Conflicting robots for duplicate URL: {url}")

    noindex_urls_in_sitemap = sorted(noindex_urls & sitemap_set)
    index_like_missing_from_sitemap = sorted(index_like_urls - sitemap_set)

    sitemap_without_matching_html = sorted(sitemap_set - unique_urls)

    duplicate_canonical_urls = []
    for url, records in url_to_records.items():
        if len(records) > 1:
            duplicate_canonical_urls.append(
                f"{url} :: " + " | ".join(r["file_path"] for r in records[:10])
            )

    encoding_issues = []
    for record in html_records:
        if record["encoding_suspect"]:
            encoding_issues.append(record["file_path"])

    sitemap_text = read_text(SITEMAP_PATH) if SITEMAP_PATH.exists() else ""
    if any(marker in sitemap_text for marker in MOJIBAKE_MARKERS):
        encoding_issues.append("sitemap.xml")

    git_status = verify_git_status()
    commit = verify_commit()
    sitemap_diff = verify_sitemap_diff()

    if not git_status["ok"]:
        critical_failures.append("Forbidden working tree changes detected or git status failed.")

    if not commit["commit_found"]:
        critical_failures.append(f"Commit {TARGET_COMMIT} not found.")
    elif commit["forbidden_changed"]:
        critical_failures.append(f"Commit {TARGET_COMMIT} changed forbidden file types.")

    if not commit["sitemap_changed"]:
        errors.append(f"Commit {TARGET_COMMIT} did not change sitemap.xml.")

    if not sitemap_diff["ok"]:
        errors.append(f"Could not inspect sitemap diff for {TARGET_COMMIT}: {sitemap_diff['error']}")

    if sitemap_diff["added_locs"]:
        errors.append("sitemap.xml diff contains added <loc> URLs.")

    if noindex_urls_in_sitemap:
        critical_failures.append("Noindex URLs still exist in sitemap.xml.")

    if duplicate_sitemap_locs:
        errors.append("Duplicate <loc> entries found in sitemap.xml.")

    if encoding_issues:
        critical_failures.append("Possible Cyrillic encoding corruption detected.")

    if sitemap_without_matching_html:
        warnings.append("Some sitemap <loc> URLs do not match any scanned HTML canonical/page URL.")

    if index_like_missing_from_sitemap:
        warnings.append("Some index-like URLs are missing from sitemap.xml. Review duplicates/service files manually.")

    result = "PASS" if not critical_failures and not errors else "FAIL"

    final_decision = (
        "INDEPENDENT CHECK PASSED"
        if result == "PASS"
        else "INDEPENDENT CHECK FAILED"
    )

    report = f"""# Fixed Independent Sitemap Check Report

## Result
{result}

## Scope
Fixed independent verification of sitemap/noindex fix after commit {TARGET_COMMIT}.
This script does not import or rely on validate_url_map.py.

## Critical failures
{format_list(critical_failures)}

## Errors
{format_list(errors)}

## Warnings
{format_list(warnings)}

## Counts
- HTML files scanned: {len(html_files)}
- Unique canonical/page URLs: {len(unique_urls)}
- Sitemap loc URLs: {len(sitemap_locs)}
- Noindex HTML files: {sum(1 for r in html_records if r["noindex"])}
- Noindex unique URLs: {len(noindex_urls)}
- Noindex URLs still in sitemap: {len(noindex_urls_in_sitemap)}
- Index-like unique URLs missing from sitemap: {len(index_like_missing_from_sitemap)}
- Duplicate sitemap loc entries: {len(duplicate_sitemap_locs)}
- Sitemap loc without matching HTML/canonical: {len(sitemap_without_matching_html)}
- Duplicate canonical URLs: {len(duplicate_canonical_urls)}
- Possible Cyrillic encoding issues: {len(encoding_issues)}

## Commit {TARGET_COMMIT} verification
- Commit found: {"yes" if commit["commit_found"] else "no"}
- Files changed in commit:
{format_list(commit["files"])}
- HTML changed: {commit["html_changed"]}
- CSS changed: {commit["css_changed"]}
- JS changed: {commit["js_changed"]}
- robots.txt changed: {commit["robots_changed"]}
- images changed: {commit["images_changed"]}
- sitemap.xml changed: {commit["sitemap_changed"]}
- forbidden files changed: {commit["forbidden_changed"]}

## Sitemap diff verification
- URL blocks removed: {len(sitemap_diff["removed_locs"])}
- URL blocks added: {len(sitemap_diff["added_locs"])}
- Added URLs:
{format_list(sitemap_diff["added_locs"])}
- Removed URLs:
{format_list(sitemap_diff["removed_locs"])}
- Suspicious additions: {"yes" if sitemap_diff["added_locs"] else "no"}

## Remaining noindex URLs in sitemap
{format_list(noindex_urls_in_sitemap)}

## Index-like URLs missing from sitemap
{format_list(index_like_missing_from_sitemap)}

## Duplicate sitemap loc entries
{format_list(duplicate_sitemap_locs)}

## Sitemap loc without matching HTML/canonical
{format_list(sitemap_without_matching_html)}

## Duplicate canonical URLs
{format_list(duplicate_canonical_urls)}

## Possible Cyrillic encoding issues
{format_list(encoding_issues)}

## Git status
```txt
{git_status["stdout"] or "clean"}
```

## Git status stderr
```txt
{git_status["stderr"] or "clean"}
```

## Final decision
{final_decision}
"""

    REPORT_PATH.write_text(report, encoding="utf-8")

    print(f"Result: {result}")
    print(f"Critical failures: {len(critical_failures)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    print(f"Final decision: {final_decision}")
    return 0 if result == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())