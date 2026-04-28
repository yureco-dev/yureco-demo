#!/usr/bin/env python3
"""
Pre-publish validator: placeholder detection.

For each indexable HTML page, scans the raw text for known placeholder patterns:
  - TODO
  - TBD
  - PLACEHOLDER
  - lorem ipsum
  - {{ }}
  - %%%

Exit code 0  → no placeholders found across all indexable pages
               stdout: PLACEHOLDER_DETECTION_OK
Exit code 1  → at least one placeholder found
               stdout: per-file PLACEHOLDER_DETECTED lines with repo-relative path

Usage:
    py -3 tools/validators/validate_placeholder_detection.py [REPO_ROOT]
    REPO_ROOT defaults to the current working directory.
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


# ---------------------------------------------------------------------------
# Placeholder patterns (case-insensitive)
# ---------------------------------------------------------------------------

_PLACEHOLDER_PATTERNS: list[re.Pattern] = [
    re.compile(r'\bTODO\b', re.IGNORECASE),
    re.compile(r'\bTBD\b', re.IGNORECASE),
    re.compile(r'\bPLACEHOLDER\b', re.IGNORECASE),
    re.compile(r'lorem\s+ipsum', re.IGNORECASE),
    re.compile(r'\{\{\s*\}\}'),
    re.compile(r'%%%'),
]


# ---------------------------------------------------------------------------
# Minimal robots extractor to detect noindex
# ---------------------------------------------------------------------------

class _RobotsExtractor(HTMLParser):
    """Single-pass HTML parser that extracts only the robots meta tag."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.robots: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "meta":
            return
        a = {k.lower(): (v or "") for k, v in attrs}
        if a.get("name", "").lower() == "robots":
            self.robots = a.get("content", "")

    def is_indexable(self) -> bool:
        if self.robots is None:
            return True
        return "noindex" not in self.robots.lower()


# ---------------------------------------------------------------------------
# File helpers
# ---------------------------------------------------------------------------

def _is_indexable(text: str) -> bool:
    parser = _RobotsExtractor()
    parser.feed(text)
    return parser.is_indexable()


def _find_html_files(root: Path) -> list[Path]:
    return sorted(root.rglob("*.html"))


def _detect_placeholders(text: str) -> list[str]:
    """Return list of matched placeholder strings found in text."""
    found = []
    for pattern in _PLACEHOLDER_PATTERNS:
        match = pattern.search(text)
        if match:
            found.append(match.group(0))
    return found


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

    html_files = _find_html_files(root)

    issues: list[str] = []

    for filepath in html_files:
        try:
            text = filepath.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        if not _is_indexable(text):
            continue

        matches = _detect_placeholders(text)
        if matches:
            rel = str(filepath.relative_to(root))
            issues.append(f"PLACEHOLDER_DETECTED {rel}  patterns={matches}")

    if issues:
        for line in issues:
            print(line)
        sys.exit(1)

    print("PLACEHOLDER_DETECTION_OK")
    sys.exit(0)


if __name__ == "__main__":
    main()
