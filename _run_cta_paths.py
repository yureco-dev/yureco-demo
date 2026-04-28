"""Run CTA mismatch validator and output paths only, sorted."""
import sys, re
from html.parser import HTMLParser
from pathlib import Path

_STOP_WORDS = frozenset({
    "замовити","зробити","дізнатись","отримати","більше","послугу",
    "послуги","підприємство","підприємств","підприємствам","підприємства",
    "довідник","youreco","youreco.com.ua","https","http",
    "організувати","поводження","організація",
    "this","that","with","from","have","will","your","more",
    "about","what","when","where","which",
})

class _CTAExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.robots = None
        self.title = None
        self.h1 = None
        self.cta_block_tag = None
        self.cta_anchor = None
        self._in_title = False
        self._in_h1 = False
        self._in_cta = False
        self._in_cta_a = False
        self._buf = []

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "meta" and a.get("name","").lower() == "robots":
            self.robots = a.get("content","")
        if tag == "title":
            self._in_title = True; self._buf = []
        if tag == "h1" and self.h1 is None:
            self._in_h1 = True; self._buf = []
        if self.cta_block_tag is None:
            cid = a.get("id","").lower(); ccls = a.get("class","").lower()
            if "cta" in cid or "cta" in ccls:
                self.cta_block_tag = tag; self._in_cta = True
        if self._in_cta and tag == "a" and self.cta_anchor is None:
            self._in_cta_a = True; self._buf = []

    def handle_endtag(self, tag):
        if tag == "title" and self._in_title:
            self.title = "".join(self._buf).strip(); self._in_title = False
        if tag == "h1" and self._in_h1:
            self.h1 = "".join(self._buf).strip(); self._in_h1 = False
        if tag == "a" and self._in_cta_a:
            self.cta_anchor = "".join(self._buf).strip(); self._in_cta_a = False

    def handle_data(self, data):
        if self._in_title or self._in_h1 or self._in_cta_a:
            self._buf.append(data)

    def is_indexable(self):
        if self.robots is None: return True
        return "noindex" not in self.robots.lower()

def _content_words(text):
    words = re.findall(r"[а-яіїєґa-z]{4,}", text.lower())
    return {w for w in words if w not in _STOP_WORDS}

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
issues = []
for filepath in sorted(root.rglob("*.html")):
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except OSError:
        continue
    parser = _CTAExtractor()
    parser.feed(text)
    if not parser.is_indexable():
        continue
    reasons = []
    if parser.cta_block_tag is None:
        reasons.append("no-cta-block")
    elif not parser.cta_anchor:
        reasons.append("no-cta-anchor")
    else:
        h1w = _content_words(parser.h1 or "")
        ctaw = _content_words(parser.cta_anchor)
        if h1w and ctaw and not h1w.intersection(ctaw):
            reasons.append("topic-mismatch")
    if reasons:
        rel = str(filepath.relative_to(root))
        issues.append(rel)

for p in issues:
    print(p)
