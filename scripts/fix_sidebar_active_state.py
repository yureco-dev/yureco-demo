#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

SCRIPT_RE = re.compile(
    r'<script id="auto-active-nav">[\s\S]*?</script>',
    flags=re.IGNORECASE,
)

NEW_SCRIPT = """<script id="auto-active-nav">
(function () {
  function normalizePath(value, isCurrent) {
    var raw = String(value || "");
    if (!isCurrent) {
      if (/^(mailto:|tel:|javascript:|#)/i.test(raw)) return "";
      try {
        raw = new URL(raw, window.location.origin).pathname;
      } catch (e) {
        return "";
      }
    } else {
      raw = window.location.pathname;
    }

    raw = raw.replace(/\\\\/g, "/").replace(/\\/+/g, "/");
    raw = raw.split("#")[0].split("?")[0];
    raw = raw.replace(/^\\//, "");

    if (raw === "") return "index.html";
    if (raw.endsWith("/")) return raw + "index.html";
    if (!raw.includes(".")) return raw + "/index.html";
    return raw;
  }

  var currentPath = normalizePath("", true);
  var links = document.querySelectorAll("nav a[href], .sidebar a[href]");
  var matches = [];

  links.forEach(function (a) {
    a.classList.remove("active", "current");
    a.removeAttribute("aria-current");
    var normalizedHref = normalizePath(a.getAttribute("href"), false);
    if (normalizedHref && normalizedHref === currentPath) {
      matches.push(a);
    }
  });

  if (matches.length > 0) {
    matches[0].classList.add("active");
    matches[0].setAttribute("aria-current", "page");
  }
})();
</script>"""

HUB_REPLACEMENTS = {
    'href="/articles.html">📰 Статті (хаб)</a>': 'href="/articles/index.html">📰 Статті (хаб)</a>',
    'href="/guide.html">📘 Гайд (хаб)</a>': 'href="/guide/index.html">📘 Гайд (хаб)</a>',
    'href="/logistyka.html">🚚 Логістика (хаб)</a>': 'href="/logistyka/index.html">🚚 Логістика (хаб)</a>',
    'href="/pererobka.html">🔄 Переробка (хаб)</a>': 'href="/pererobka/index.html">🔄 Переробка (хаб)</a>',
    'href="/sortuvannya.html">🧹 Сортування (хаб)</a>': 'href="/sortuvannya/index.html">🧹 Сортування (хаб)</a>',
    'href="/utylizaciya.html">🧭 Утилізація (хаб)</a>': 'href="/utylizaciya/index.html">🧭 Утилізація (хаб)</a>',
}


def main() -> None:
    changed = 0
    for html_path in sorted(ROOT.rglob("*.html")):
        if "public" in html_path.parts:
            continue

        original = html_path.read_text(encoding="utf-8")
        updated = original

        if '<script id="auto-active-nav">' in updated:
            updated = SCRIPT_RE.sub(NEW_SCRIPT, updated)

        for old, new in HUB_REPLACEMENTS.items():
            updated = updated.replace(old, new)

        if updated != original:
            html_path.write_text(updated, encoding="utf-8", newline="\n")
            changed += 1

    print(f"SIDEBAR_ACTIVE_FIX_OK files_changed={changed}")


if __name__ == "__main__":
    main()
