import os
import re
import json
import sys

ROOT = os.getcwd()

TARGET_EXTENSIONS = (".html", ".htm")

OUTPUT_DIR = os.path.join(ROOT, "validation", "self_referential_metadata")

OUTPUT_FILE = os.path.join(
    OUTPUT_DIR,
    "metadata_url_mismatch_report.json"
)

canonical_tag_pattern = re.compile(
    r'<link[^>]*rel=["\']canonical["\'][^>]*>',
    re.IGNORECASE
)

og_tag_pattern = re.compile(
    r'<meta[^>]*property=["\']og:url["\'][^>]*>',
    re.IGNORECASE
)

ai_tag_pattern = re.compile(
    r'<meta[^>]*name=["\']ai-content-url["\'][^>]*>',
    re.IGNORECASE
)

jsonld_block_pattern = re.compile(
    r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL
)

canonical_value_pattern = re.compile(
    r'href=["\']([^"\']+)["\']',
    re.IGNORECASE
)

meta_content_pattern = re.compile(
    r'content=["\']([^"\']+)["\']',
    re.IGNORECASE
)

jsonld_url_pattern = re.compile(
    r'"url"\s*:\s*"([^"]+)"',
    re.IGNORECASE
)

robots_noindex_pattern = re.compile(
    r'<meta[^>]*name=["\']robots["\'][^>]*content=["\'][^"\']*noindex[^"\']*["\']',
    re.IGNORECASE
)

html_tag_pattern = re.compile(
    r'<html',
    re.IGNORECASE
)


def extract(pattern, text):
    m = pattern.search(text)
    if m:
        return m.group(1).strip()
    return None


def is_indexable(content):
    if not html_tag_pattern.search(content):
        return False
    if robots_noindex_pattern.search(content):
        return False
    return True


def schema_urls(content):
    urls = []
    for block in jsonld_block_pattern.findall(content):
        urls.extend(jsonld_url_pattern.findall(block))
    return urls


results = {
    "checked_files": 0,
    "indexable_files": 0,
    "valid_files": 0,
    "mismatch_files": 0,
    "missing_files": 0,
    "files": []
}


for root, _, files in os.walk(ROOT):
    for file in files:

        if not file.lower().endswith(TARGET_EXTENSIONS):
            continue

        path = os.path.join(root, file)

        results["checked_files"] += 1

        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            continue

        if not is_indexable(content):
            continue

        results["indexable_files"] += 1

        canonical_tag = canonical_tag_pattern.search(content)
        og_tag = og_tag_pattern.search(content)
        ai_tag = ai_tag_pattern.search(content)

        canonical = extract(canonical_value_pattern, canonical_tag.group(0)) if canonical_tag else None
        og = extract(meta_content_pattern, og_tag.group(0)) if og_tag else None
        ai = extract(meta_content_pattern, ai_tag.group(0)) if ai_tag else None

        schemas = schema_urls(content)

        missing = []

        if not canonical:
            missing.append("canonical")

        if not og:
            missing.append("og_url")

        if not ai:
            missing.append("ai_content_url")

        if not schemas:
            missing.append("schema_url")

        mismatches = []

        if canonical and og and canonical != og:
            mismatches.append("canonical!=og_url")

        if canonical and ai and canonical != ai:
            mismatches.append("canonical!=ai_content_url")

        if canonical and schemas:
            for s in schemas:
                if s != canonical:
                    mismatches.append("canonical!=schema_url")
                    break

        status = "PASS"

        if missing or mismatches:
            status = "FAIL"

        if status == "PASS":
            results["valid_files"] += 1
        else:
            if missing:
                results["missing_files"] += 1
            if mismatches:
                results["mismatch_files"] += 1

        results["files"].append({
            "file_path": path,
            "status": status,
            "canonical": canonical,
            "og_url": og,
            "ai_content_url": ai,
            "schema_urls": schemas,
            "missing_fields": missing,
            "mismatches": mismatches
        })


os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)


has_fail = any(x["status"] == "FAIL" for x in results["files"])

sys.exit(1 if has_fail else 0)
