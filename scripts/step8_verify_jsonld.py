#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://guide.youreco.com.ua"
MARKERS = ["Ð", "Ñ", "Р°", "Р±", "Р В", "СЂ", "вЂ", "�"]
EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAD6\U0001F1E0-\U0001F1FF\u2600-\u27BF]")
ROUTES = ("articles", "logistyka", "pererobka", "sortuvannya", "utylizaciya")


def files() -> list[Path]:
    result = sorted(ROOT.glob("*.html"))
    for d in ROUTES:
        p = ROOT / d / "index.html"
        if p.exists():
            result.append(p)
    return sorted(set(result))


def file_url(p: Path) -> str:
    rel = p.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return BASE
    if rel.endswith("/index.html"):
        return f"{BASE}/{rel[:-11]}"
    return f"{BASE}/{rel}"


def main() -> None:
    issues: list[str] = []
    count = 0
    for p in files():
        txt = p.read_text(encoding="utf-8")
        canonical_m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\'](.*?)["\']', txt, flags=re.I)
        canonical = canonical_m.group(1).strip() if canonical_m else file_url(p)
        blocks = re.findall(r"<script[^>]*type=[\"']application/ld\+json[\"'][^>]*>\s*(.*?)\s*</script>", txt, flags=re.I | re.S)
        for block in blocks:
            count += 1
            try:
                data = json.loads(block)
            except Exception as e:
                issues.append(f"{p.relative_to(ROOT).as_posix()} :: JSON parse error :: {e}")
                continue
            nodes = data if isinstance(data, list) else [data]
            for node in nodes:
                if not isinstance(node, dict):
                    issues.append(f"{p.relative_to(ROOT).as_posix()} :: node is not object")
                    continue
                if node.get("@context") != "https://schema.org":
                    issues.append(f"{p.relative_to(ROOT).as_posix()} :: wrong @context")
                url = node.get("url")
                meop = node.get("mainEntityOfPage")
                meop_val = meop.get("@id") if isinstance(meop, dict) else meop
                if url and url != canonical:
                    issues.append(f"{p.relative_to(ROOT).as_posix()} :: url mismatch")
                if meop_val and meop_val != canonical:
                    issues.append(f"{p.relative_to(ROOT).as_posix()} :: mainEntityOfPage mismatch")
                if any("/public/" in str(v) for v in (url, meop_val)):
                    issues.append(f"{p.relative_to(ROOT).as_posix()} :: /public/ in schema URL")
                for key in ("headline", "description", "name"):
                    v = str(node.get(key, ""))
                    if EMOJI_RE.search(v):
                        issues.append(f"{p.relative_to(ROOT).as_posix()} :: emoji in {key}")
                    if any(m in v for m in MARKERS):
                        issues.append(f"{p.relative_to(ROOT).as_posix()} :: mojibake in {key}")

    out = ROOT / "audits" / "_stage8_jsonld_after_issues.txt"
    out.write_text("\n".join(issues), encoding="utf-8")
    print(f"JSONLD_BLOCKS={count}")
    print(f"JSONLD_ISSUES={len(issues)}")


if __name__ == "__main__":
    main()
