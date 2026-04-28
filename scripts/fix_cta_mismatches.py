"""Normalize CTA blocks so CTA text shares content words with the page H1."""

from __future__ import annotations

import html
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


_STOP_WORDS: frozenset[str] = frozenset({
    "замовити",
    "зробити",
    "дізнатись",
    "отримати",
    "більше",
    "послугу",
    "послуги",
    "підприємство",
    "підприємств",
    "підприємствам",
    "підприємства",
    "довідник",
    "youreco",
    "youreco.com.ua",
    "https",
    "http",
    "організувати",
    "поводження",
    "організація",
    "this",
    "that",
    "with",
    "from",
    "have",
    "will",
    "your",
    "more",
    "about",
    "what",
    "when",
    "where",
    "which",
})


class _CTAExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.robots: str | None = None
        self.h1: str | None = None
        self.cta_block_tag: str | None = None
        self.cta_anchor: str | None = None
        self._in_h1 = False
        self._in_cta = False
        self._in_cta_a = False
        self._buf: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "meta" and a.get("name", "").lower() == "robots":
            self.robots = a.get("content", "")
        if tag == "h1" and self.h1 is None:
            self._in_h1 = True
            self._buf = []
        if self.cta_block_tag is None:
            cid = a.get("id", "").lower()
            ccls = a.get("class", "").lower()
            if "cta" in cid or "cta" in ccls:
                self.cta_block_tag = tag
                self._in_cta = True
        if self._in_cta and tag == "a" and self.cta_anchor is None:
            self._in_cta_a = True
            self._buf = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "h1" and self._in_h1:
            self.h1 = "".join(self._buf).strip()
            self._in_h1 = False
        if tag == "a" and self._in_cta_a:
            self.cta_anchor = "".join(self._buf).strip()
            self._in_cta_a = False

    def handle_data(self, data: str) -> None:
        if self._in_h1 or self._in_cta_a:
            self._buf.append(data)

    def is_indexable(self) -> bool:
        if self.robots is None:
            return True
        return "noindex" not in self.robots.lower()


def _content_words(text: str) -> set[str]:
    words = re.findall(r"[а-яіїєґa-z]{4,}", text.lower())
    return {w for w in words if w not in _STOP_WORDS}


def _build_cta_block(anchor_text: str) -> str:
    safe_anchor = html.escape(anchor_text, quote=False)
    return (
        '<section class="card" id="service-cta">'
        "<h2>Потрібна послуга YOURECO?</h2>"
        "<p>Дивіться релевантну комерційну сторінку з умовами, вивозом та документальним супроводом.</p>"
        '<ul class="related-list"><li><a href="https://youreco.com.ua/" rel="noopener" target="_blank">'
        f"{safe_anchor}"
        "</a></li></ul></section>"
    )


def _extract_h1(text: str) -> str:
    match = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.IGNORECASE | re.DOTALL)
    if not match:
        return ""
    h1 = re.sub(r"<[^>]+>", "", match.group(1))
    return re.sub(r"\s+", " ", h1).strip()


def _find_cta_block_bounds(text: str) -> tuple[int, int] | None:
    start_re = re.compile(
        r'<(?P<tag>section|div)\b(?=[^>]*(?:id="[^"]*cta[^"]*"|class="[^"]*cta[^"]*"))[^>]*>',
        re.IGNORECASE | re.DOTALL,
    )
    match = start_re.search(text)
    if not match:
        return None
    tag = match.group("tag").lower()
    close = f"</{tag}>"
    end = text.find(close, match.end())
    if end == -1:
        return None
    return match.start(), end + len(close)


def _fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="replace")
    parser = _CTAExtractor()
    parser.feed(text)
    if not parser.is_indexable():
        return False

    h1 = _extract_h1(text) or path.stem
    h1_words = _content_words(parser.h1 or "")
    cta_words = _content_words(parser.cta_anchor or "")
    no_issue = (
        parser.cta_block_tag is not None
        and parser.cta_anchor
        and bool(h1_words.intersection(cta_words))
    )
    if no_issue:
        return False

    new_block = _build_cta_block(h1)
    bounds = _find_cta_block_bounds(text)
    if bounds is not None:
        start, end = bounds
        updated = text[:start] + new_block + text[end:]
    else:
        insertion = text.rfind("</main>")
        if insertion == -1:
            insertion = text.rfind("</body>")
        if insertion == -1:
            updated = text + "\n" + new_block + "\n"
        else:
            updated = text[:insertion] + "\n" + new_block + "\n" + text[insertion:]

    if updated != text:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    changed: list[str] = []
    for path in sorted(root.rglob("*.html")):
        try:
            if _fix_file(path):
                changed.append(str(path.relative_to(root)))
        except OSError:
            continue

    for rel in changed:
        print(rel)
    print(f"CTA_FIXED_COUNT={len(changed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
