# Thin Content Audit Report

## Scope
- source HTML checked: 246
- public HTML checked: 246
- index/follow pages checked: 62
- noindex pages checked: 184
- build run: no
- files changed: this report only
- excluded: `dist/`, `node_modules/`, `.git/`, service caches; `public/` excluded from source pass and checked separately
- source/public parity: public HTML mirrors source metrics for checked paths

## Summary
- critical thin indexable pages: 3
- warning thin indexable pages: 8
- thin noindex/service pages: 77
- pages with low word count: 78 in source, 78 mirrored in public
- pages with weak section depth: 4 in source, 4 mirrored in public
- pages with template-like content: 72 explicit template-style pages in source, 72 mirrored in public
- pages containing `Розділ доповнюється`: 0
- FAQ/JSON-LD missing on critical pages: 3

## Critical Thin Pages
Only `index/follow` pages that should be expanded first.

| path | H1 | title | meta description | word count | H2/H3 count | paragraphs | lists | read-also/internal links | FAQ/JSON-LD | issue | recommended action |
|---|---|---|---|---:|---:|---:|---:|---|---|---|---|
| `pererobka-cegly.html` | Як передають на переробку цеглу | Як передають на переробку цеглу - Довідник YOURECO | Переробка цегли: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника YOURECO. | 331 | 8 | 8 | 5 | yes | no | below 350 words; several repeated guide blocks; useful skeleton but not enough practical depth | expand handling scenarios, acceptance limits, contamination cases, logistics, document examples, and add FAQ |
| `logistyka-skla.html` | Логістика скла | Логістика скла - Довідник YOURECO | Довідка для підприємств про «логістику скла»: що включає, як підготувати партію, правила зберігання, логістика, документи та типові помилки. | 335 | 8 | 8 | 5 | yes | no | below 350 words; topic needs practical packaging/loading guidance | add sections for safe storage, тарування, loading risks, route planning, photo checklist, and FAQ |
| `kabelni-vidhody.html` | Кабельні відходи: класифікація та зберігання | Кабельні відходи: класифікація та зберігання - Довідник YOURECO | Кабельні відходи: класифікація, зберігання, підготовка до передачі, організація вивезення та документи для підприємств. | 340 | 8 | 9 | 5 | yes | no | below 350 words; has structure but little concrete classification depth | add cable-type classification, separation rules, storage mistakes, document checklist, and FAQ |

## Warning Pages
Indexable pages that are not below the hard 350-word threshold, but remain thin or borderline because of low depth, short blocks, or template-like phrasing.

| path | index status | word count | H2/H3 count | issue | recommended action |
|---|---|---:|---:|---|---|
| `logistyka-metalu.html` | index/follow | 352 | 8 | barely above 350 words; similar logistics template to other material pages | expand with metal-specific loading, sorting, contamination, weighing, and document details |
| `utylizaciya-zipsovanyh-produktiv.html` | index/follow | 396 | 6 | short blocks dominate; no FAQ; practical answer is shallow for food waste | add spoilage categories, quarantine/storage, odor/liquid handling, decision flow, and FAQ |
| `utylizaciya-napoyiv.html` | index/follow | 399 | 7 | short blocks dominate; broad topic needs clearer practical scenarios | add sections for bottled/canned/bulk drinks, leaking packaging, depackaging, documents, and FAQ |
| `utylizaciya-kosmetyky-magazyniv.html` | index/follow | 403 | 8 | template-like guide page; no FAQ; thin for a concrete retail scenario | add retail return flows, mixed SKUs, packaging state, evidence/photo report, and FAQ |
| `akt-pryimannya-peredachi.html` | index/follow | 474 | 10 | acceptable structure but still short for a document explainer; no FAQ | add sample fields, common mistakes, when act differs from utilization act, and FAQ |
| `povernennya-tovariv-z-merezhi.html` | index/follow | 537 | 8 | borderline; topic has practical business workflow but limited detail | add reverse-logistics stages, responsibility split, warehouse decision table, and FAQ/checklist |
| `utilizaciya-brakovanoi-produkciyi.html` | index/follow | 549 | 8 | borderline; broad topic almost at threshold for usefulness but needs more practical examples | add defect-type scenarios, approval chain, evidence package, and FAQ/checklist |
| `dokumenty.html` | index/follow | 636 | 15 | enough words, but many short blocks; hub-like page may feel fragmented | strengthen with table of documents, when each is needed, and links to concrete document pages |

## Noindex / Service Thin Pages
These are not critical because they are `noindex, follow`, redirect-like, service-like, or navigation pages. They should remain intentionally noindex or be expanded before making indexable.

| path | word count | H2/H3 count | reason not critical |
|---|---:|---:|---|
| `404.html` | 44 | 1 | technical 404 page; intentionally noindex |
| `utylizaciya-shin.html` | 106 | 3 | noindex redirect/service-style page with very short template blocks |
| `utylizaciya-kosmetiki.html` | 113 | 3 | noindex alias/redirect-style page with very short template blocks |
| `kudy-zdaty-gipsokartonu.html` | 119 | 3 | noindex redirect-style page |
| `kudy-zdaty-avtoshyn.html` | 124 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-ovochiv.html` | 128 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-obladnannya.html` | 129 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-produktiv-na-skladi.html` | 129 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-fruktiv.html` | 130 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-derevyny-z-budivnyctva.html` | 131 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-dokumentiv.html` | 131 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-gazovanyh-napoyiv.html` | 131 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-parfumeriyi.html` | 132 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-napoyiv.html` | 133 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-budivelnyh-vidhodiv.html` | 134 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-partiyi-produktiv.html` | 134 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-fruktiv-ta-ovochiv.html` | 135 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-nekondicijnoyi-sirovini.html` | 136 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-metalu.html` | 137 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-nekondyciynoyi-produkciyi.html` | 138 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-energetychnyh-napoyiv.html` | 139 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-napivfabrykatyv.html` | 139 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-produktiv-harchuvannya-napoyiv.html` | 139 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-shyn-pidpryyemstvamy.html` | 139 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-kosmetyky.html` | 140 | 4 | noindex legacy redirect-style page |
| `kudy-zdaty-plastyku-ta-polimeriv.html` | 140 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-materialiv.html` | 141 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-shyn.html` | 141 | 4 | noindex legacy redirect-style page |
| `kudy-zdaty-vantazhnyh-shyn.html` | 141 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-harchovyh-produktiv.html` | 142 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-kosmetiki.html` | 142 | 4 | noindex legacy redirect-style page |
| `kudy-zdaty-metalevoyi-strushky.html` | 142 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-paperu-ta-kartonu.html` | 142 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-promyslovogo-obladnannya-mehanizmiv.html` | 142 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-rybnyh-produktiv.html` | 142 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-skladskyh-zalyshkiv-kosmetyky.html` | 142 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-sokiv.html` | 142 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-kondyterskyh-vyrobiv.html` | 143 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-molochnyh-produktiv.html` | 143 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-promyslovyh-vidhodiv.html` | 143 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-skladskyh-zalyshkiv.html` | 143 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-tovariv.html` | 143 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-li-ion-batarej.html` | 144 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-myasnyh-produktiv.html` | 144 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-ofisnih-mebliv-orgtehniki.html` | 144 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-pyva.html` | 144 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-shin.html` | 144 | 4 | noindex legacy redirect-style page |
| `kudy-zdaty-shyny.html` | 144 | 4 | noindex legacy redirect-style page |
| `kudy-zdaty-paverbankiv-dbj.html` | 145 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-prostrochenyh-produktiv.html` | 145 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-upakovky-vid-kosmetyky.html` | 145 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-kabelyu-ta-drotiv.html` | 146 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-konserviv.html` | 146 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-kosmetyky-magazyniv.html` | 146 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-skla.html` | 146 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-prostrochenoyi-kosmetyky.html` | 147 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-tary-upakovki.html` | 147 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-sokiv-ta-napoyiv.html` | 149 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-odyagu-vzuttya.html` | 150 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-tovary-pid-mitnim-kontrolem.html` | 150 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-vidpracovane-maslo.html` | 150 | 4 | noindex redirect-style page |
| `kudy-zdaty-sonyachnih-panelij-vitryakiv.html` | 152 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-vyrobnychyh-vidhodiv.html` | 152 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-zamorozhenyh-produktiv.html` | 152 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-yagid.html` | 153 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-upakovky-na-pidpryyemstvi.html` | 154 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-vody.html` | 154 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-vidpracovanoi-olyvy.html` | 155 | 4 | noindex redirect-style page |
| `kudy-zdaty-vidpracovanyh-masel.html` | 155 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `kudy-zdaty-zipsovanyh-produktiv.html` | 156 | 4 | noindex `kudy-zdaty` helper page; short template blocks |
| `articles/index.html` | 189 | 4 | noindex redirect/navigation page |
| `kontakty.html` | 265 | 8 | noindex contact/service page; short but not a content article |
| `sortuvannya/index.html` | 338 | 6 | noindex category index; thin but intentionally navigational |
| `utylizaciya/index.html` | 340 | 5 | noindex category index; thin but intentionally navigational |
| `logistyka/index.html` | 347 | 6 | noindex category index; thin but intentionally navigational |
| `li-ion.html` | 429 | 14 | noindex redirect/alias page; not low word count but template-like |
| `shyny.html` | 462 | 14 | noindex redirect/alias page; not low word count but template-like |

## Recommended Content Expansion Plan

### `pererobka-cegly.html`
- Add or expand sections: what brick waste is accepted, what is not accepted, how to separate brick from concrete/plaster/insulation, when crushing is useful, how to estimate volume and weight.
- Practical content needed: contamination examples, storage before pickup, loading requirements, what photos to prepare, how the business confirms transfer.
- Internal links: `/utylizaciya-budivelnyh-vidhodiv.html`, `/sortuvannya-budivelnyh-vidhodiv.html`, `/logistyka-budivelnyh-vidhodiv.html`, `/dokumenty.html`.
- Add table/checklist/FAQ: yes; table for accepted/not accepted materials, checklist for preparing a construction-waste batch, 3-4 FAQ items.

### `logistyka-skla.html`
- Add or expand sections: separate glass types, broken-glass safety, container choice, loading/access requirements, how to prevent mixing with ceramics and packaging.
- Practical content needed: pallet/container guidance, handling of wet/contaminated glass, route planning for enterprise sites, photo evidence and handover notes.
- Internal links: `/utylizaciya-skla.html`, `/pererobka-skla.html`, `/zbir-sklyanoyi-tary.html`, `/dokumenty.html`.
- Add table/checklist/FAQ: yes; checklist for safe storage and pickup, table of glass streams, FAQ about broken glass and mixed packaging.

### `kabelni-vidhody.html`
- Add or expand sections: cable waste categories, copper/aluminum/mixed cable, insulation types, sorting before transfer, what lowers recovery value or complicates handling.
- Practical content needed: examples of enterprise cable batches, storage and labeling, weighing/volume notes, when to link to utilization vs recycling.
- Internal links: `/utylizaciya-kabelyu-ta-drotiv.html`, `/pererobka-midnogo-kabelyu.html`, `/pererobka-alyuminiyevogo-kabelyu.html`, `/zbir-kabelyu.html`, `/dokumenty.html`.
- Add table/checklist/FAQ: yes; classification table, preparation checklist, FAQ about mixed cable, insulation, and documents.

## Method Notes
- Main/content word count was estimated from text inside `<main>` when present.
- Section depth counted `H2` and `H3` headings.
- Template-like pages were flagged when they repeated short helper-page patterns such as `Основний маршрут`, `Що перевірити`, `Дивіться також`, and `Практичне виконання робіт`.
- `noindex, follow` pages were not treated as critical unless they later become indexable.
- Public HTML was checked separately and did not show metric mismatches against source.

## Guardrails
- HTML changed: no
- CSS changed: no
- JS changed: no
- sitemap/robots changed: no
- public changed: no
- build run: no
- commit done: no
- push done: no
- Cyrillic/UTF-8 issues: none observed while reading HTML with UTF-8/UTF-8 BOM fallback
