#!/usr/bin/env python3
"""
Post-build validator: self-referential metadata consistency check.

For each indexable HTML page, extracts and compares exactly 4 fields:
  1. canonical       — <link rel="canonical" href="...">
  2. og:url          — <meta property="og:url" content="...">
  3. ai-content-url  — <meta name="ai-content-url" content="...">
  4. schema/json-ld url — "url" field in a WebPage-typed JSON-LD block

A page PASSES only when all 4 values are present AND equal to each other.

Exit code 0  → no mismatches and no missing fields across all indexable pages
               stdout: SELF_REFERENTIAL_METADATA_OK
Exit code 1  → any mismatch or missing field detected
               stdout: per-file MISMATCH lines with repo-relative path

Usage:
    py -3 tools/validators/validate_self_referential_metadata.py [REPO_ROOT]
    REPO_ROOT defaults to the current working directory.
"""

import json
import os
import sys
from html.parser import HTMLParser
from pathlib import Path


class _MetadataExtractor(HTMLParser):
    """Single-pass HTML parser that extracts the 4 target metadata fields."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.robots: str | None = None
        self.canonical: str | None = None
        self.og_url: str | None = None
        self.ai_content_url: str | None = None
        # Collect all WebPage-typed JSON-LD "url" values; first one wins.
        self._webpage_jsonld_urls: list[str] = []
        self._in_jsonld_script: bool = False
        self._script_buffer: list[str] = []

    # ------------------------------------------------------------------
    # HTMLParser callbacks
    # ------------------------------------------------------------------

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = {k.lower(): (v or "") for k, v in attrs}

        if tag == "link":
            if a.get("rel", "").lower() == "canonical":
                self.canonical = a.get("href") or None

        elif tag == "meta":
            prop = a.get("property", "").lower()
            name = a.get("name", "").lower()
            content = a.get("content", "")
            if prop == "og:url":
                self.og_url = content or None
            elif name == "ai-content-url":
                self.ai_content_url = content or None
            elif name == "robots":
                self.robots = content

        elif tag == "script":
            if a.get("type", "").lower() == "application/ld+json":
                self._in_jsonld_script = True
                self._script_buffer = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._in_jsonld_script:
            self._in_jsonld_script = False
            raw = "".join(self._script_buffer).strip()
            if raw:
                self._parse_jsonld(raw)
            self._script_buffer = []

    def handle_data(self, data: str) -> None:
        if self._in_jsonld_script:
            self._script_buffer.append(data)

    # ------------------------------------------------------------------
    # JSON-LD helpers
    # ------------------------------------------------------------------

    def _parse_jsonld(self, raw: str) -> None:
        try:
            obj = json.loads(raw)
        except (json.JSONDecodeError, ValueError):
            return
        self._walk_jsonld(obj)

    def _walk_jsonld(self, node: object) -> None:
        if isinstance(node, list):
            for item in node:
                self._walk_jsonld(item)
            return
        if not isinstance(node, dict):
            return
        at_type = node.get("@type", "")
        if isinstance(at_type, list):
            at_type = " ".join(at_type)
        # Accept any JSON-LD block whose @type contains "WebPage"
        if "WebPage" in at_type:
            url_val = node.get("url")
            if url_val and isinstance(url_val, str):
                self._webpage_jsonld_urls.append(url_val)

    # ------------------------------------------------------------------
    # Derived properties
    # ------------------------------------------------------------------

    @property
    def is_indexable(self) -> bool:
        """True when the page carries no noindex directive."""
        if self.robots is None:
            return True  # absent robots meta → indexable by default
        return "noindex" not in self.robots.lower()

    @property
    def schema_url(self) -> str | None:
        """URL from the first matching WebPage JSON-LD block, or None."""
        return self._webpage_jsonld_urls[0] if self._webpage_jsonld_urls else None


# ---------------------------------------------------------------------------
# File helpers
# ---------------------------------------------------------------------------

def _extract(filepath: Path) -> _MetadataExtractor | None:
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    parser = _MetadataExtractor()
    parser.feed(text)
    return parser


def _find_html_files(root: Path) -> list[Path]:
    return sorted(root.rglob("*.html"))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

    html_files = _find_html_files(root)

    issues: list[str] = []

    for filepath in html_files:
        meta = _extract(filepath)
        if meta is None:
            continue
        if not meta.is_indexable:
            continue

        fields: dict[str, str | None] = {
            "canonical":          meta.canonical,
            "og:url":             meta.og_url,
            "ai-content-url":     meta.ai_content_url,
            "schema/json-ld url": meta.schema_url,
        }

        rel = str(filepath.relative_to(root))

        missing = [key for key, val in fields.items() if val is None]
        if missing:
            issues.append(f"MISMATCH {rel}  missing={missing}")
            continue

        unique_values = set(fields.values())
        if len(unique_values) > 1:
            issues.append(
                f"MISMATCH {rel}"
                f"  canonical={fields['canonical']}"
                f"  og:url={fields['og:url']}"
                f"  ai-content-url={fields['ai-content-url']}"
                f"  schema/json-ld url={fields['schema/json-ld url']}"
            )

    if issues:
        for line in issues:
            print(line)
        sys.exit(1)

    print("SELF_REFERENTIAL_METADATA_OK")
    sys.exit(0)


if __name__ == "__main__":
    main()
