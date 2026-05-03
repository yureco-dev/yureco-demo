# SEO Risk Diff Audit

Forensic audit of current `git diff` from `HEAD` to working tree. No build was run. No HTML, sitemap, or source files were changed by this audit.

## Executive summary

- Status: НЕ ДОБРЕ
- Changed tracked files in diff: 69
- Changed HTML files: 68
- Sitemap URL added count: 11
- Sitemap URL removed count: 0
- Meta robots changed count: 11
- Canonical changed count: 0
- Internal href changed count: 757 anchor-preserving href changes
- Sidebar href changed count: 672
- Main content href changed count: 85
- Sidebar item removed count: 1 unique item, 56 occurrences
- Cyrillic integrity: не зіпсована

## 1. sitemap.xml

Added URLs:

| URL | lastmod |
|---|---|
| `https://guide.youreco.com.ua/utylizaciya-budivelnyh-vidhodiv.html` | `2026-04-28` |
| `https://guide.youreco.com.ua/utylizaciya-kabelyu-ta-drotiv.html` | `2026-04-28` |
| `https://guide.youreco.com.ua/utylizaciya-li-ion-batarej.html` | `2026-04-28` |
| `https://guide.youreco.com.ua/utylizaciya-odyagu-vzuttya.html` | `2026-04-28` |
| `https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html` | `2026-04-28` |
| `https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html` | `2026-04-28` |
| `https://guide.youreco.com.ua/utylizaciya-shyn.html` | `2026-04-28` |
| `https://guide.youreco.com.ua/utylizaciya-sonyachnih-panelij-vitryakiv.html` | `2026-04-28` |
| `https://guide.youreco.com.ua/utylizaciya-tary-upakovki.html` | `2026-04-28` |
| `https://guide.youreco.com.ua/utylizaciya-ofisnih-mebliv-orgtehniki.html` | `2026-04-28` |
| `https://guide.youreco.com.ua/utylizaciya-vidpracovanoi-olyvy.html` | `2026-04-28` |

Removed URLs: none.

Existing URL order: unchanged for common URLs.

Existing `lastmod`: unchanged for common URLs.

Risk: HIGH because new indexable URLs were added to sitemap.

## 2. Meta robots

All robots changes are `noindex → index`.

| File | Old value | New value |
|---|---|---|
| `utylizaciya-budivelnyh-vidhodiv.html` | `noindex, follow` | `index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1` |
| `utylizaciya-kabelyu-ta-drotiv.html` | `noindex, follow` | `index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1` |
| `utylizaciya-li-ion-batarej.html` | `noindex, follow` | `index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1` |
| `utylizaciya-odyagu-vzuttya.html` | `noindex, follow` | `index, follow` |
| `utylizaciya-ofisnih-mebliv-orgtehniki.html` | `noindex, follow` | `index, follow` |
| `utylizaciya-plastyku-ta-polimeriv.html` | `noindex, follow` | `index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1` |
| `utylizaciya-produktiv-harchuvannya-napoyiv.html` | `noindex, follow` | `index, follow` |
| `utylizaciya-shyn.html` | `noindex, follow` | `index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1` |
| `utylizaciya-sonyachnih-panelij-vitryakiv.html` | `noindex, follow` | `index, follow` |
| `utylizaciya-tary-upakovki.html` | `noindex, follow` | `index, follow` |
| `utylizaciya-vidpracovanoi-olyvy.html` | `noindex, follow` | `index, follow` |

Files changed `index → noindex`: none.

Risk: HIGH because 11 pages were made indexable.

## 3. Canonical

Canonical changes: none detected.

Risk: none for canonical.

## 4. Internal href

Method: counted anchor-preserving internal link changes where the same anchor text exists before and after, but `href` changed.

- Total internal href changes: 757
- Sidebar href changes: 672
- Main content href changes: 85

Sitewide sidebar href changes:

| Anchor text | Old href | New href | Occurrences |
|---|---|---|---:|
| `♻️ Пластик та полімери` | `/utylizaciya.html` | `/utylizaciya-plastyku-ta-polimeriv.html` | 56 |
| `⚡ Сонячні панелі та лопаті ВЕС` | `/utylizaciya.html` | `/utylizaciya-sonyachnih-panelij-vitryakiv.html` | 56 |
| `⭕ Шини` | `/utylizaciya.html` | `/utylizaciya-shyn.html` | 56 |
| `🏗️ Будівельні відходи` | `/utylizaciya.html` | `/utylizaciya-budivelnyh-vidhodiv.html` | 56 |
| `👕 Одяг та взуття` | `/utylizaciya.html` | `/utylizaciya-odyagu-vzuttya.html` | 56 |
| `📄 Конфіденційні документи` | `/utylizaciya.html` | `/utylizaciya-konfidenciynykh-dokumentiv.html` | 56 |
| `📦 Тара та упаковка` | `/utylizaciya.html` | `/utylizaciya-tary-upakovki.html` | 56 |
| `🔋 Li-ion батареї` | `/utylizaciya.html` | `/utylizaciya-li-ion-batarej.html` | 56 |
| `🔌 Кабель та дроти` | `/utylizaciya.html` | `/utylizaciya-kabelyu-ta-drotiv.html` | 56 |
| `🖥️ Офісні меблі та оргтехніка` | `/utylizaciya.html` | `/utylizaciya-ofisnih-mebliv-orgtehniki.html` | 56 |
| `🛢️ Відпрацьована моторна олива` | `/utylizaciya.html` | `/utylizaciya-vidpracovanoi-olyvy.html` | 56 |
| `🥫 Продукти харчування та напої` | `/utylizaciya.html` | `/utylizaciya-produktiv-harchuvannya-napoyiv.html` | 56 |

Main content href changes are concentrated in `index.html`, `utylizaciya/index.html`, and other hub-like content where links moved from `/utylizaciya.html` to more specific target URLs. Some new main-content targets appear broader than the 11 sitemap additions and need separate existence/indexability validation before release.

Risk: MEDIUM for sitewide internal link redistribution.

## 5. Sidebar

Removed sidebar items:

| Anchor text | Old href | Occurrences |
|---|---|---:|
| `🧪 Некондиційна сировина` | `/utylizaciya.html` | 56 |

Added sidebar items as net-new anchors: none for the stable sidebar set. Some files appear to have a full sidebar block added in the diff; those are structural additions, not new unique sidebar menu concepts.

Changed sidebar hrefs: the 12 sitewide rows listed in section 4.

Changed sidebar anchor text: no anchor text changes detected for the 12 changed href rows. The removed item is a true sidebar item removal.

Active state / visual sidebar changes:

- `aria-current="page"` and `class="active"` were added on hub links in hub pages.
- `script id="auto-active-nav"` was removed from `logistyka/index.html` and `sortuvannya/index.html`.
- Risk: LOW by itself, but should be reviewed with navigation behavior.

## 6. SEO-risk classification

HIGH:

- `sitemap.xml`: 11 new URL entries.
- `utylizaciya-budivelnyh-vidhodiv.html`: `noindex → index`.
- `utylizaciya-kabelyu-ta-drotiv.html`: `noindex → index`.
- `utylizaciya-li-ion-batarej.html`: `noindex → index`.
- `utylizaciya-odyagu-vzuttya.html`: `noindex → index`.
- `utylizaciya-ofisnih-mebliv-orgtehniki.html`: `noindex → index`.
- `utylizaciya-plastyku-ta-polimeriv.html`: `noindex → index`.
- `utylizaciya-produktiv-harchuvannya-napoyiv.html`: `noindex → index`.
- `utylizaciya-shyn.html`: `noindex → index`.
- `utylizaciya-sonyachnih-panelij-vitryakiv.html`: `noindex → index`.
- `utylizaciya-tary-upakovki.html`: `noindex → index`.
- `utylizaciya-vidpracovanoi-olyvy.html`: `noindex → index`.

MEDIUM:

- Sitewide sidebar href changes from `/utylizaciya.html` to 12 specific URLs across 56 occurrences each.
- Main content href changes from `/utylizaciya.html` to many specific URLs, including targets outside the 11 sitemap additions.

LOW:

- Active sidebar state changes.
- Removal of auto-active-nav script on selected hub pages.

## 7. Recommendation

Rollback first:

1. Restore `sitemap.xml` additions until each added URL is intentionally approved for indexation.
2. Restore robots `noindex, follow` on the 11 pages unless the noindex-to-index release is intentional.
3. Pause the sitewide sidebar href rollout until target pages are verified for existence, canonical consistency, status code, indexability, and content quality.

Can remain pending additional verification:

- Active sidebar visual state changes.
- Canonical state, because no canonical changes were detected.
- Main content href refinements only after validating every target URL.

Suggested partial rollback commands:

```powershell
git restore --source=HEAD -- sitemap.xml
```

```powershell
git restore --source=HEAD -- utylizaciya-budivelnyh-vidhodiv.html utylizaciya-kabelyu-ta-drotiv.html utylizaciya-li-ion-batarej.html utylizaciya-odyagu-vzuttya.html utylizaciya-ofisnih-mebliv-orgtehniki.html utylizaciya-plastyku-ta-polimeriv.html utylizaciya-produktiv-harchuvannya-napoyiv.html utylizaciya-shyn.html utylizaciya-sonyachnih-panelij-vitryakiv.html utylizaciya-tary-upakovki.html utylizaciya-vidpracovanoi-olyvy.html
```

For selective sidebar/main-content href rollback without touching the whole files:

```powershell
git restore -p --source=HEAD -- '*.html'
```

For a broad rollback of all tracked HTML changes only:

```powershell
git restore --source=HEAD -- '*.html'
```

## Cyrillic check

Кирилиця у diff і в цьому звіті читається коректно: приклади `Конфіденційні документи`, `Будівельні відходи`, `Відпрацьована моторна олива`, `Некондиційна сировина`.

