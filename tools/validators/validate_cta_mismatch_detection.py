#!/usr/bin/env python3
"""
Pre-publish validator: CTA mismatch detection.

For each indexable HTML page, checks consistency between:
  1. title
  2. H1
  3. first CTA block (element with id or class containing "cta")
  4. first CTA anchor text (first <a> inside the CTA block)

A CTA_MISMATCH is reported when any of the following is true:
  - CTA block is absent
  - CTA anchor text is absent (CTA block exists but contains no <a>)
  - No content-word overlap between H1 and CTA anchor text
    (words ≥4 chars, excluding common Ukrainian/English stop words)

Exit code 0  → no mismatches found across all indexable pages
               stdout: CTA_MISMATCH_DETECTION_OK
Exit code 1  → at least one mismatch found
               stdout: per-file CTA_MISMATCH_DETECTED lines with repo-relative path

Usage:
    py -3 tools/validators/validate_cta_mismatch_detection.py [REPO_ROOT]
    REPO_ROOT defaults to the current working directory.
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


# ---------------------------------------------------------------------------
# Stop words to exclude from overlap check (Ukrainian + English common words)
# ---------------------------------------------------------------------------

_STOP_WORDS: frozenset[str] = frozenset({
    # Ukrainian
    "замовити", "зробити", "дізнатись", "отримати", "більше", "послугу",
    "послуги", "підприємство", "підприємств", "підприємствам", "підприємства",
    "довідник", "youreco", "youreco.com.ua", "https", "http",
    "організувати", "поводження", "організація",
    # English
    "this", "that", "with", "from", "have", "will", "your", "more",
    "about", "what", "when", "where", "which",
})


# ---------------------------------------------------------------------------
# HTML parser: extracts robots, title, H1, first CTA block tag, first CTA anchor
# ---------------------------------------------------------------------------

class _CTAExtractor(HTMLParser):
    """Single-pass HTML parser extracting all 4 CTA consistency fields."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.robots: str | None = None
        self.title: str | None = None
        self.h1: str | None = None
        self.cta_block_tag: str | None = None   # tag name of first CTA element
        self.cta_anchor: str | None = None       # text of first <a> inside CTA

        self._in_title = False
        self._in_h1 = False
        self._in_cta = False
        self._in_cta_a = False
        self._buf: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = {k.lower(): (v or "") for k, v in attrs}

        # robots meta
        if tag == "meta" and a.get("name", "").lower() == "robots":
            self.robots = a.get("content", "")

        # <title>
        if tag == "title":
            self._in_title = True
            self._buf = []

        # <h1> — first occurrence only
        if tag == "h1" and self.h1 is None:
            self._in_h1 = True
            self._buf = []

        # CTA block — first element with id or class containing "cta"
        if self.cta_block_tag is None:
            cid = a.get("id", "").lower()
            ccls = a.get("class", "").lower()
            if "cta" in cid or "cta" in ccls:
                self.cta_block_tag = tag
                self._in_cta = True

        # First <a> inside CTA block
        if self._in_cta and tag == "a" and self.cta_anchor is None:
            self._in_cta_a = True
            self._buf = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self._in_title:
            self.title = "".join(self._buf).strip()
            self._in_title = False

        if tag == "h1" and self._in_h1:
            self.h1 = "".join(self._buf).strip()
            self._in_h1 = False

        if tag == "a" and self._in_cta_a:
            self.cta_anchor = "".join(self._buf).strip()
            self._in_cta_a = False

    def handle_data(self, data: str) -> None:
        if self._in_title or self._in_h1 or self._in_cta_a:
            self._buf.append(data)

    def is_indexable(self) -> bool:
        if self.robots is None:
            return True
        return "noindex" not in self.robots.lower()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _content_words(text: str) -> set[str]:
    """Extract lowercase content words (≥4 chars, not stop words) from text."""
    words = re.findall(r"[а-яіїєґa-z]{4,}", text.lower())
    return {w for w in words if w not in _STOP_WORDS}


def _find_html_files(root: Path) -> list[Path]:
    return sorted(root.rglob("*.html"))


def _check_cta(meta: _CTAExtractor) -> list[str]:
    """Return list of mismatch reasons, or empty list if OK."""
    reasons = []

    if meta.cta_block_tag is None:
        reasons.append("no-cta-block")
        return reasons  # no point checking anchor if block absent

    if not meta.cta_anchor:
        reasons.append("no-cta-anchor")
        return reasons

    # Topic alignment: H1 and CTA anchor must share ≥1 content word
    h1_words = _content_words(meta.h1 or "")
    cta_words = _content_words(meta.cta_anchor)
    if h1_words and cta_words and not h1_words.intersection(cta_words):
        reasons.append(
            f"topic-mismatch  h1={repr(meta.h1)}  cta={repr(meta.cta_anchor)}"
        )

    return reasons


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

        parser = _CTAExtractor()
        parser.feed(text)

        if not parser.is_indexable():
            continue

        reasons = _check_cta(parser)
        if reasons:
            rel = str(filepath.relative_to(root))
            issues.append(f"CTA_MISMATCH_DETECTED {rel} reasons={reasons}")

    if issues:
        for line in issues:
            print(line)
        sys.exit(1)

    print("CTA_MISMATCH_DETECTION_OK")
    sys.exit(0)


if __name__ == "__main__":
    main()
