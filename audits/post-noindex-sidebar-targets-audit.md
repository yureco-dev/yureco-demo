# Post Noindex Sidebar Targets Audit

Read-only audit of current `public/**/*.html`. Build was not run; `public` was audited as-is.

## A. Summary

|Metric|Value|
|---|---:|
|total_public_html|244|
|pages_without_sidebar|176|
|pages_with_active_item_0|50|
|sidebar_links_to_noindex|2|
|unique_sidebar_noindex_targets|1|
|broken_sidebar_links|0|
|links_to_noindex|54|
|wrong_topic_links|272|
|sleeping_stub_links|987|
|cyrillic_issue_files|0|

Cyrillic status: **не зіпсована**

## B. Comparison With Previous Audit

Previous file: `audits/post-sidebar-href-fix-audit.json`.

|Metric|Previous|Current|Delta|
|---|---:|---:|---:|
|sidebar links to noindex|552|2|-550|
|links to noindex|627|54|-573|
|wrong-topic links|94|272|178|
|sleeping/stub links|1434|987|-447|

## Sidebar

- total_public_html: 244
- pages_with_sidebar: 68
- pages_without_sidebar: 176
- pages_with_active_item_0: 50
- pages_with_active_item_gt_1: 0
- pages_with_non_standard_sidebar: 2

## Sidebar Links

- sidebar_wrong_topic_utylizaciya_html: 264
- broken_sidebar_links: 0
- sidebar_links_to_noindex: 2
- unique_sidebar_noindex_targets: 1
- sidebar_links_to_public: 0
- sidebar_link_count_mismatch: 0

Unique sidebar noindex targets:
- `/utylizaciya-nekondyciynoyi-produkciyi.html`

## All Internal Links

- total_internal_links: 4394
- broken_links: 1
- links_to_noindex: 54
- wrong_topic_links: 272
- sleeping_stub_links: 987
- links_to_redirect: 0
- links_to_public: 0

## Specific Check

- target: `/utylizaciya-nekondyciynoyi-produkciyi.html`
- target exists: True
- target noindex: True
- total occurrences: 4
- sidebar occurrences: 2
- mismatch anchor text `Некондиційна сировина` -> target `nekondyciynoyi-produkciyi`: 2

Occurrences:
- `public/index.html` [main content]: `Утилізація некондиційної продукції` -> `/utylizaciya-nekondyciynoyi-produkciyi.html`
- `public/utylizaciya/index.html` [sidebar]: `🧪 Некондиційна сировина` -> `/utylizaciya-nekondyciynoyi-produkciyi.html`
- `public/utylizaciya.html` [sidebar]: `🧪 Некондиційна сировина` -> `/utylizaciya-nekondyciynoyi-produkciyi.html`
- `public/utylizaciya.html` [main content]: `Утилізація некондиційної продукції` -> `/utylizaciya-nekondyciynoyi-produkciyi.html`

## Cyrillic / Encoding

Forbidden marker scan is reported by safe marker IDs to avoid emitting the raw control tokens in this report.
- marker_01: 0
- marker_02: 0
- marker_03: 0
- marker_04: 0
- marker_05: 0
- marker_06: 0
- marker_07: 0
- marker_08: 0
- marker_09: 0
- BOM files: 0

## C. Remaining Priority

### HIGH
- 54 internal links point to noindex targets; 2 are sidebar links.
- /utylizaciya-nekondyciynoyi-produkciyi.html remains noindex and is linked 4 times (2 from sidebar).
- Broken links found: 1 total, 0 sidebar.

### MEDIUM
- 272 wrong-topic / anchor-target mismatches remain.
- 987 links point to sleeping/stub-like targets (noindex, redirect, or not in sitemap).

### LOW
- 176 pages without sidebar; 50 sidebar pages have no static active item.

## D. Recommendation

Прибрати noindex із пріоритетних sidebar targets у згенерованому public, почавши з /utylizaciya-nekondyciynoyi-produkciyi.html, потім повторити цей контрольний аудит.
