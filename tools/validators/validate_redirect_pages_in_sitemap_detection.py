#!/usr/bin/env python3
"""
Pre-publish validator: redirect pages in sitemap detection.

Reads:
  - sitemap.xml      — extracts all <loc> URLs
  - docs/qa/p2.1/page_type_inventory.txt — extracts redirect-page filenames

Checks whether any redirect-page URL appears in sitemap.xml.

Exit code 0  → no redirect pages found in sitemap
               stdout: REDIRECT_PAGES_NOT_PRESENT_IN_SITEMAP_OK
Exit code 1  → at least one redirect page found in sitemap
               stdout: per-URL REDIRECT_PAGE_PRESENT_IN_SITEMAP lines

Usage:
    py -3 tools/validators/validate_redirect_pages_in_sitemap_detection.py [REPO_ROOT]
    REPO_ROOT defaults to the current working directory.
"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------

def _parse_sitemap_urls(sitemap_path: Path) -> set[str]:
    """Extract all <loc> URL values from sitemap.xml."""
    text = sitemap_path.read_text(encoding="utf-8")
    # Match both namespaced <ns0:loc> and plain <loc>
    return set(re.findall(r"<(?:\w+:)?loc>\s*(https?://[^\s<]+)\s*</(?:\w+:)?loc>", text))


def _url_path(url: str) -> str:
    """Return a normalized path without a leading slash."""
    path = unquote(urlparse(url).path)
    return path.lstrip("/")


def _parse_redirect_pages(inventory_path: Path) -> list[str]:
    """Extract filenames of redirect-page entries from page_type_inventory.txt."""
    raw = inventory_path.read_bytes()
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        raise ValueError(
            f"{inventory_path} must be UTF-8, but it looks like UTF-16. "
            "Re-save page_type_inventory.txt as UTF-8."
        )

    redirect_files = []
    for line in raw.decode("utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) >= 2 and parts[1].lower() == "redirect-page":
            redirect_files.append(parts[0])
    return redirect_files


def _parse_redirect_rule_sources(htaccess_path: Path) -> list[str]:
    """Extract source paths from Apache Redirect 301 rules."""
    if not htaccess_path.exists():
        return []

    sources: list[str] = []
    text = htaccess_path.read_text(encoding="utf-8")
    for line in text.splitlines():
        match = re.match(r"\s*Redirect\s+301\s+(\S+)\s+\S+", line)
        if match:
            sources.append(match.group(1).lstrip("/"))
    return sources


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

    sitemap_path = root / "sitemap.xml"
    inventory_path = root / "docs" / "qa" / "p2.1" / "page_type_inventory.txt"
    htaccess_path = root / ".htaccess"

    if not sitemap_path.exists():
        print(f"ERROR: sitemap.xml not found at {sitemap_path}")
        sys.exit(2)

    if not inventory_path.exists():
        print(f"ERROR: page_type_inventory.txt not found at {inventory_path}")
        sys.exit(2)

    try:
        sitemap_urls = _parse_sitemap_urls(sitemap_path)
        redirect_files = _parse_redirect_pages(inventory_path)
        redirect_rule_sources = _parse_redirect_rule_sources(htaccess_path)
    except UnicodeError as exc:
        print(f"ERROR: expected UTF-8 input: {exc}")
        sys.exit(2)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        sys.exit(2)

    if redirect_rule_sources and not redirect_files:
        print(
            "ERROR: page_type_inventory.txt produced 0 redirect-page entries, "
            f"but .htaccess contains {len(redirect_rule_sources)} Redirect 301 rule(s)."
        )
        print("ERROR: inventory parsing failed or the inventory is stale.")
        sys.exit(2)

    sitemap_paths = {_url_path(url): url for url in sitemap_urls}
    issues: list[str] = []

    for filename in redirect_files:
        url = sitemap_paths.get(filename)
        if url:
            issues.append(f"REDIRECT_PAGE_PRESENT_IN_SITEMAP {filename}  url={url}")

    for source in redirect_rule_sources:
        url = sitemap_paths.get(source)
        if url:
            issues.append(f"REDIRECT_RULE_SOURCE_PRESENT_IN_SITEMAP {source}  url={url}")

    if issues:
        for line in sorted(set(issues)):
            print(line)
        sys.exit(1)

    print("REDIRECT_PAGES_NOT_PRESENT_IN_SITEMAP_OK")
    sys.exit(0)


if __name__ == "__main__":
    main()
