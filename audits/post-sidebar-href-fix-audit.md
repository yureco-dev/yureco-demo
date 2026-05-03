# Post Sidebar Href Fix Audit

Generated after `python scripts/build_public.py`. Only this Markdown report and the paired JSON report were written.

## A. Summary Before/After

|Metric|Before|After|Delta|
|---|---:|---:|---:|
|sidebar WRONG_TOPIC `/utylizaciya.html`|594|0|-594|
|total wrong-topic links|676|94|-582|
|sleeping/stub links|875|1434|559|
|links to noindex|92|627|535|
|pages without sidebar|176|176|0|
|Cyrillic issue files|9|0|-9|

## Current Summary

|Metric|Value|
|---|---:|
|total_public_html|244|
|pages_with_sidebar|68|
|pages_without_sidebar|176|
|pages_with_active_item_0|50|
|pages_with_active_item_gt_1|0|
|pages_with_non_standard_sidebar|2|
|sidebar_wrong_topic_utylizaciya_html|0|
|broken_sidebar_links|0|
|sidebar_links_to_public|0|
|sidebar_links_to_noindex|552|
|sidebar_link_count_mismatch_vs_public_index|0|
|total_internal_links|4393|
|broken_links|0|
|links_to_noindex|627|
|links_to_redirect|0|
|links_to_public|0|
|sleeping_stub_links|1434|
|wrong_topic_links|94|
|cyrillic_issue_files|0|
|bom_files|0|

Cyrillic status: **не зіпсована**

## B. Remaining Issues Priority

### HIGH
- 627 internal links point to noindex pages (552 from sidebar).
- 94 wrong-topic links remain outside the fixed sidebar scope or in non-standard/sidebar residues.

### MEDIUM
- 1434 sleeping/stub links remain.
- 176 public HTML pages have no sidebar.
- 50 sidebar pages have no static active item.

### LOW
- 2 pages have non-standard sidebar compared with public/index.html.

## C. Next Recommended Stage

Fix internal links to noindex targets next, starting with sidebar links because their volume increased after the href correction.

## Sidebar Checks

- Remaining sidebar WRONG_TOPIC `/utylizaciya.html`: 0
- Broken sidebar links: 0
- Sidebar links to `/public/`: 0
- Sidebar links to noindex: 552
- Sidebar link count mismatch vs `public/index.html`: 0

## Cyrillic / Encoding Markers

No Cyrillic/encoding markers found.