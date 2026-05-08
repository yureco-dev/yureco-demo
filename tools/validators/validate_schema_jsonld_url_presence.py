#!/usr/bin/env python3
"""
Validator: JSON-LD schema "url" key presence check.

For each indexable HTML page, verifies:
  1. A <script type="application/ld+json"> block exists.
  2. That block contains a top-level "url" key.

Output per-file (to stdout):
  MISSING_SCHEMA_JSONLD_BLOCK <repo-relative-path>  — no JSON-LD block at all
  MISSING_SCHEMA_JSONLD_URL   <repo-relative-path>  — block exists, "url" key absent

Exit code 0 → all indexable pages have a JSON-LD block with "url" key;
              stdout: SCHEMA_JSONLD_URL_PRESENT_OK
Exit code 1 → at least one page has a missing block or missing "url" key.

Usage:
    py -3 tools/validators/validate_schema_jsonld_url_presence.py [REPO_ROOT]
    REPO_ROOT defaults to the current working directory.
"""

import json
import re
import sys
from pathlib import Path

_JSONLD_BLOCK = re.compile(
    r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL,
)
_ROBOTS_NOINDEX = re.compile(
    r'<meta[^>]*name=["\']robots["\'][^>]*content=["\'][^"\']*noindex',
    re.IGNORECASE,
)
_HTML_TAG = re.compile(r'<html', re.IGNORECASE)


def _is_indexable(text: str) -> bool:
    if not _HTML_TAG.search(text):
        return False
    return not _ROBOTS_NOINDEX.search(text)


def _jsonld_blocks(text: str) -> list[str]:
    """Return raw JSON text of every JSON-LD script block in the page."""
    return _JSONLD_BLOCK.findall(text)


def _has_url_key(raw: str) -> bool:
    """Return True if the JSON-LD object (or any object in an array) has a top-level 'url' key."""
    try:
        obj = json.loads(raw.strip())
    except (json.JSONDecodeError, ValueError):
        return False
    if isinstance(obj, list):
        return any(isinstance(item, dict) and "url" in item for item in obj)
    if isinstance(obj, dict):
        return "url" in obj
    return False


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

    issues: list[str] = []

    for filepath in sorted(root.rglob("*.html")):
        try:
            text = filepath.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        if not _is_indexable(text):
            continue

        rel = str(filepath.relative_to(root))
        blocks = _jsonld_blocks(text)

        if not blocks:
            issues.append(f"MISSING_SCHEMA_JSONLD_BLOCK {rel}")
            continue

        if not any(_has_url_key(b) for b in blocks):
            issues.append(f"MISSING_SCHEMA_JSONLD_URL {rel}")

    if issues:
        for line in issues:
            print(line)
        sys.exit(1)

    print("SCHEMA_JSONLD_URL_PRESENT_OK")
    sys.exit(0)


if __name__ == "__main__":
    main()
