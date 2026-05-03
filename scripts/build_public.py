#!/usr/bin/env python3
"""
Build a clean static publish directory.

The repository root contains QA reports, validators, docs, and remediation
artifacts. This script copies only production-facing site files into public/.
"""

from __future__ import annotations

import shutil
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"

AUTO_ACTIVE_NAV_RE = re.compile(
    r'<script id="auto-active-nav">[\s\S]*?</script>',
    flags=re.IGNORECASE,
)

AUTO_ACTIVE_NAV_SCRIPT = """<script id="auto-active-nav">
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

  function fallbackTarget(normalizedCurrentPath) {
    if (normalizedCurrentPath === "index.html") return "index.html";
    if (normalizedCurrentPath === "kontakty.html") return "index.html";
    if (normalizedCurrentPath === "dokumenty.html" || normalizedCurrentPath.indexOf("dokumenty-") === 0) return "dokumenty.html";
    if (normalizedCurrentPath === "zbir.html" || normalizedCurrentPath.indexOf("zbir-") === 0) return "zbir.html";
    if (normalizedCurrentPath === "vidhody.html" || normalizedCurrentPath.indexOf("vidhody-") === 0 || normalizedCurrentPath.indexOf("promyslovi-vidhody") === 0 || normalizedCurrentPath.indexOf("oblik-") === 0 || normalizedCurrentPath.indexOf("optymizaciya-") === 0 || normalizedCurrentPath.indexOf("skladuvannya-") === 0 || normalizedCurrentPath.indexOf("vtorynna-syrovyna-") === 0 || normalizedCurrentPath.indexOf("vymogy-do-zberigannya-") === 0 || normalizedCurrentPath === "kabelni-vidhody.html") return "vidhody.html";
    if (normalizedCurrentPath === "kudy-zdaty.html" || normalizedCurrentPath.indexOf("kudy-zdaty-") === 0) return "kudy-zdaty.html";
    if (normalizedCurrentPath.indexOf("sortuvannya/") === 0 || normalizedCurrentPath.indexOf("sortuvannya-") === 0 || normalizedCurrentPath === "sortuvannya.html") return "sortuvannya.html";
    if (normalizedCurrentPath.indexOf("logistyka/") === 0 || normalizedCurrentPath.indexOf("logistyka-") === 0 || normalizedCurrentPath === "logistyka.html") return "logistyka.html";
    if (normalizedCurrentPath.indexOf("pererobka/") === 0 || normalizedCurrentPath.indexOf("pererobka-") === 0 || normalizedCurrentPath === "pererobka.html" || normalizedCurrentPath === "chy-potribno-pererobyty-chy-utylizuvaty.html") return "pererobka.html";
    if (normalizedCurrentPath.indexOf("yak-") === 0 || normalizedCurrentPath.indexOf("spysannya-") === 0 || normalizedCurrentPath.indexOf("likvidaciya-") === 0 || normalizedCurrentPath.indexOf("povernennya-") === 0 || normalizedCurrentPath.indexOf("akt-") === 0 || normalizedCurrentPath.indexOf("fotozvit-") === 0) return "utylizaciya.html";
    if (normalizedCurrentPath.indexOf("utylizaciya/") === 0 || normalizedCurrentPath.indexOf("utylizaciya-") === 0 || normalizedCurrentPath.indexOf("utilizaciya-") === 0 || normalizedCurrentPath === "utylizaciya.html") return "utylizaciya.html";
    return "";
  }

  var currentPath = normalizePath("", true);
  var links = document.querySelectorAll("nav a[href], .sidebar a[href]");
  var allSidebarLinks = [];
  var matches = [];

  links.forEach(function (a) {
    a.classList.remove("active", "current");
    a.removeAttribute("aria-current");
    var normalizedHref = normalizePath(a.getAttribute("href"), false);
    allSidebarLinks.push({ node: a, path: normalizedHref });
    if (normalizedHref && normalizedHref === currentPath) {
      matches.push(a);
    }
  });

  if (matches.length === 0) {
    var fallbackPath = fallbackTarget(currentPath);
    if (fallbackPath) {
      allSidebarLinks.forEach(function (item) {
        if (!matches.length && item.path === fallbackPath) {
          matches.push(item.node);
        }
      });
    }
  }

  if (matches.length > 0) {
    matches[0].classList.add("active");
    matches[0].setAttribute("aria-current", "page");
  }
})();
</script>"""

ROOT_FILES = {
    ".htaccess",
    "CNAME",
    "robots.txt",
    "sitemap.xml",
    "styles.css",
}

ROUTE_DIRS = {
    "articles",
    "logistyka",
    "pererobka",
    "sortuvannya",
    "utylizaciya",
}

ASSET_DIRS = {
    "img",
}

FORBIDDEN_DIRS = {
    ".git",
    ".github",
    ".vscode",
    "__pycache__",
    "docs",
    "scripts",
    "tools",
    "validation",
}

FORBIDDEN_SUFFIXES = {
    ".bat",
    ".cmd",
    ".csv",
    ".json",
    ".md",
    ".ps1",
    ".py",
    ".sh",
    ".txt",
    ".tsv",
}

FORBIDDEN_FILENAMES = {
    ".env.example",
    "CHANGELOG.md",
    "deploy.sh",
}

ALLOWED_TEXT_FILES = {
    "robots.txt",
}

RENDER_REDIRECT_SOURCE_FILES = {
    "li-ion.html",
    "shyny.html",
    "utylizaciya-kosmetiki.html",
    "utylizaciya-shin.html",
}

RENDER_REDIRECT_SOURCE_DIRS = {
    "articles",
}


def is_render_redirect_source(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if rel in RENDER_REDIRECT_SOURCE_FILES:
        return True
    if path.name.startswith("kudy-zdaty-") and path.suffix.lower() == ".html":
        return True
    return any(rel == f"{dirname}/index.html" for dirname in RENDER_REDIRECT_SOURCE_DIRS)


def reset_public() -> None:
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir()


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def copy_tree(src: Path, dst: Path) -> None:
    if src.exists():
        shutil.copytree(src, dst)


def copy_production_files() -> None:
    for html in sorted(ROOT.glob("*.html")):
        if is_render_redirect_source(html):
            continue
        copy_file(html, PUBLIC / html.name)

    for filename in sorted(ROOT_FILES):
        src = ROOT / filename
        if src.exists():
            copy_file(src, PUBLIC / filename)

    for dirname in sorted(ASSET_DIRS):
        copy_tree(ROOT / dirname, PUBLIC / dirname)

    for dirname in sorted(ROUTE_DIRS):
        if dirname in RENDER_REDIRECT_SOURCE_DIRS:
            continue
        index = ROOT / dirname / "index.html"
        if index.exists():
            copy_file(index, PUBLIC / dirname / "index.html")


def assert_clean_public() -> None:
    issues: list[str] = []

    for path in PUBLIC.rglob("*"):
        rel = path.relative_to(PUBLIC)
        if any(part in FORBIDDEN_DIRS for part in rel.parts):
            issues.append(f"forbidden directory copied: {rel}")
            continue

        if path.is_file():
            if path.name in FORBIDDEN_FILENAMES:
                issues.append(f"forbidden file copied: {rel}")
                continue
            if path.name in ALLOWED_TEXT_FILES:
                continue
            if path.suffix.lower() in FORBIDDEN_SUFFIXES:
                issues.append(f"forbidden file copied: {rel}")

    if issues:
        for issue in issues:
            print(f"PUBLIC_BUILD_ERROR {issue}")
        raise SystemExit(1)


def normalize_sidebar_active_state() -> None:
    for html_path in sorted(PUBLIC.rglob("*.html")):
        original = html_path.read_text(encoding="utf-8")
        if 'class="sidebar"' not in original and "class='sidebar'" not in original:
            continue

        if '<script id="auto-active-nav">' in original:
            updated = AUTO_ACTIVE_NAV_RE.sub(AUTO_ACTIVE_NAV_SCRIPT, original)
        elif "</body>" in original:
            updated = original.replace("</body>", f"{AUTO_ACTIVE_NAV_SCRIPT}\n</body>", 1)
        else:
            updated = f"{original}\n{AUTO_ACTIVE_NAV_SCRIPT}\n"

        if updated != original:
            html_path.write_text(updated, encoding="utf-8", newline="\n")


def main() -> None:
    reset_public()
    copy_production_files()
    normalize_sidebar_active_state()
    assert_clean_public()

    files = [p for p in PUBLIC.rglob("*") if p.is_file()]
    html_files = [p for p in files if p.suffix.lower() == ".html"]
    print(f"PUBLIC_BUILD_OK files={len(files)} html={len(html_files)}")


if __name__ == "__main__":
    main()
