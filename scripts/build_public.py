#!/usr/bin/env python3
"""
Build a clean static publish directory.

The repository root contains QA reports, validators, docs, and remediation
artifacts. This script copies only production-facing site files into public/.
"""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"

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
        copy_file(html, PUBLIC / html.name)

    for filename in sorted(ROOT_FILES):
        src = ROOT / filename
        if src.exists():
            copy_file(src, PUBLIC / filename)

    for dirname in sorted(ASSET_DIRS):
        copy_tree(ROOT / dirname, PUBLIC / dirname)

    for dirname in sorted(ROUTE_DIRS):
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


def main() -> None:
    reset_public()
    copy_production_files()
    assert_clean_public()

    files = [p for p in PUBLIC.rglob("*") if p.is_file()]
    html_files = [p for p in files if p.suffix.lower() == ".html"]
    print(f"PUBLIC_BUILD_OK files={len(files)} html={len(html_files)}")


if __name__ == "__main__":
    main()
