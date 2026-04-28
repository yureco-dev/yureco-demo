import os
import re
import json
import sys

ROOT = os.getcwd()

TARGET_EXTENSIONS = (
    ".html",
    ".jinja",
    ".njk",
    ".liquid",
    ".tmpl",
    ".tpl"
)

OUTPUT_DIR = os.path.join(
    ROOT,
    "validation",
    "self_referential_metadata"
)

OUTPUT_FILE = os.path.join(
    OUTPUT_DIR,
    "source_map_metadata_urls.json"
)


canonical_pattern = re.compile(
    r'<link[^>]*rel=["\']canonical["\'][^>]*>',
    re.IGNORECASE
)

og_pattern = re.compile(
    r'<meta[^>]*property=["\']og:url["\'][^>]*>',
    re.IGNORECASE
)

ai_pattern = re.compile(
    r'<meta[^>]*name=["\']ai-content-url["\'][^>]*>',
    re.IGNORECASE
)

jsonld_pattern = re.compile(
    r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL
)

url_pattern = re.compile(
    r'"url"\s*:\s*"(.*?)"',
    re.IGNORECASE
)

template_var_pattern = re.compile(
    r'{{(.*?)}}|{%(.*?)%}'
)


def extract_source(expr):

    match = template_var_pattern.search(expr)

    if match:

        return (
            match.group(1)
            or match.group(2)
        ).strip()

    href_match = re.search(
        r'(href|content)\s*=\s*"([^"]+)"',
        expr
    )

    if href_match:

        return href_match.group(2)

    return "UNKNOWN"


results = {
    "canonical": [],
    "og_url": [],
    "ai_content_url": [],
    "schema_url": []
}


for root, _, files in os.walk(ROOT):

    for file in files:

        if not file.endswith(TARGET_EXTENSIONS):

            continue

        path = os.path.join(root, file)

        try:

            with open(path, "r", encoding="utf-8") as f:

                content = f.read()

        except Exception:

            continue

        for match in canonical_pattern.findall(content):

            results["canonical"].append({

                "template_path": path,

                "template_expression": match,

                "source_variable": extract_source(match)
            })


        for match in og_pattern.findall(content):

            results["og_url"].append({

                "template_path": path,

                "template_expression": match,

                "source_variable": extract_source(match)
            })


        for match in ai_pattern.findall(content):

            results["ai_content_url"].append({

                "template_path": path,

                "template_expression": match,

                "source_variable": extract_source(match)
            })


        for script in jsonld_pattern.findall(content):

            for url in url_pattern.findall(script):

                results["schema_url"].append({

                    "template_path": path,

                    "template_expression": url,

                    "source_variable": extract_source(url)
                })


os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        results,
        f,
        indent=2,
        ensure_ascii=False
    )


if all(k in results for k in ("canonical", "og_url", "ai_content_url", "schema_url")):

    sys.exit(0)

else:

    sys.exit(1)