# SOURCE-OF-TRUTH DISCOVERY — P0.3
## Self-Referential Metadata: canonical / og:url / ai-content-url / schema/json-ld url

---

## SOURCE_OF_TRUTH

**Literal absolute URL hardcoded in `<link rel="canonical" href="...">` inside each individual `.html` file.**

There is no template engine (no Jinja, Nunjucks, Liquid, or equivalent), no build-time variable, and no code-level URL generator. Every HTML page contains its own canonical URL as a literal string directly authored in the `<head>` block. The `<link rel="canonical">` tag is the leading field; the remaining three fields are authored to match it verbatim in the same file.

---

## AFFECTED_TEMPLATES

No separate template files exist in the repository (zero `.jinja`, `.njk`, `.liquid`, `.tmpl`, `.tpl` files detected). The 4 fields are authored directly in each deployed HTML file.

Affected files — every indexable `.html` file in the repository root and subdirectories, for example:

- `akt-pryimannya-peredachi.html`
- `kabelni-vidhody.html`
- `articles/index.html`
- `logistyka/index.html`
- `pererobka/index.html`
- `sortuvannya/index.html`
- `utylizaciya/index.html`
- ... (145 indexable pages total per validator run)

The validation pipeline scripts (`validation/self_referential_metadata/discover_metadata_sources.py`, `validation/self_referential_metadata/validate_metadata_url_consistency.py`, `validation/run_p0_3.py`) are post-build read-only scanners — they do not generate or inject any of the 4 fields.

---

## FIELD_MAPPING

| Field | Location in each HTML file | Attribute carrying the URL |
|---|---|---|
| canonical | `<head>` — `<link rel="canonical" href="ABSOLUTE_URL"/>` | `href` |
| og:url | `<head>` — `<meta property="og:url" content="ABSOLUTE_URL"/>` | `content` |
| ai-content-url | `<head>` — `<meta name="ai-content-url" content="ABSOLUTE_URL"/>` | `content` |
| schema/json-ld url | `<head>` — `<script type="application/ld+json">` block with `"@type":"WebPage"`, field `"url":"ABSOLUTE_URL"` | `"url"` key in JSON-LD object |

**Note on schema/json-ld url:** Pages with `"@type":"Article"` in their JSON-LD block use `mainEntityOfPage.@id` to reference the page URL — they do **not** carry a top-level `"url"` key. As a result, the `schema/json-ld url` field is absent (missing) on all Article-typed pages. Only pages with a dedicated `"@type":"WebPage"` JSON-LD block expose the `"url"` field for this check.

---

## EVIDENCE

**canonical:**
```
kabelni-vidhody.html, line 12:
<link href="https://guide.youreco.com.ua/kabelni-vidhody.html" rel="canonical"/>

akt-pryimannya-peredachi.html, line 12:
<link href="https://guide.youreco.com.ua/akt-pryimannya-peredachi.html" rel="canonical"/>
```

**og:url:**
```
kabelni-vidhody.html, line 20:
<meta content="https://guide.youreco.com.ua/kabelni-vidhody.html" property="og:url"/>

akt-pryimannya-peredachi.html, line 20:
<meta content="https://guide.youreco.com.ua/akt-pryimannya-peredachi.html" property="og:url"/>
```

**ai-content-url:**
```
kabelni-vidhody.html, line 25:
<meta content="https://guide.youreco.com.ua/kabelni-vidhody.html" name="ai-content-url"/>

akt-pryimannya-peredachi.html, line 25:
<meta content="https://guide.youreco.com.ua/akt-pryimannya-peredachi.html" name="ai-content-url"/>
```

**schema/json-ld url — present (WebPage @type):**
```
articles/index.html, line 11:
<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage",
"name":"...","url":"https://guide.youreco.com.ua/articles",
"mainEntityOfPage":{"@type":"WebPage","@id":"https://guide.youreco.com.ua/articles"}}</script>
```

**schema/json-ld url — absent (Article @type, missing field):**
```
kabelni-vidhody.html, line 199:
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article",
"headline":"...","mainEntityOfPage":{"@type":"WebPage",
"@id":"https://guide.youreco.com.ua/kabelni-vidhody.html"},...}</script>
```
→ No top-level `"url"` key. The validator reports `schema/json-ld url` as missing for this page.

**No template engine / no build-time URL generator:**
```
scripts/  — contains only prepublish_validate_encoding.cmd and validate_utf8_mojibake.py
deploy.sh — rsync only, no URL injection
```
`validation/self_referential_metadata/discover_metadata_sources.py` line 8–13:
scans `(".html", ".jinja", ".njk", ".liquid", ".tmpl", ".tpl")` — zero matches on non-html extensions.

**source_map_metadata_urls.json confirms all `source_variable` values are literal absolute URLs** (no `{{ }}` template expressions):
```
validation/self_referential_metadata/source_map_metadata_urls.json:
{
  "canonical": [
    { "source_variable": "https://guide.youreco.com.ua/akt-pryimannya-peredachi.html" },
    { "source_variable": "https://guide.youreco.com.ua/kabelni-vidhody.html" },
    ...
  ]
}
```

---

## DECISION

**All 4 fields (canonical, og:url, ai-content-url, schema/json-ld url) must be taken from the literal URL value of `<link rel="canonical" href="...">` authored in each individual HTML file.**

The `<link rel="canonical" href="...">` is the single source of truth. Any correction or generation of the other three fields must use the canonical href value of the same page as its authoritative input. No external config, no build variable, and no shared template currently centralize this value.
