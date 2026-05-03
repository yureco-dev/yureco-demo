# Sidebar Noindex Link Plan

Diagnostics only. Source: `audits/post-sidebar-href-fix-audit.json`. No HTML/CSS/JS, build, sitemap, robots/meta, or page creation changes were made.

## A. Summary

|Metric|Value|
|---|---:|
|total sidebar links to noindex|552|
|unique noindex target URLs|12|
|targets that are redirect/meta-refresh|0|
|targets with canonical to another page|0|
|targets not in public sitemap|12|

Key finding: 544 of 552 links are the same 8 standard sidebar targets repeated across all 68 sidebar pages. The remaining 8 links are 4 targets that appear only in `utylizaciya.html` and `utylizaciya/index.html`.

## B. Unique Noindex Sidebar Targets

|anchor text|href|target title/H1|canonical|in sitemap|redirect|occurrences|recommended action|reason|
|---|---|---|---|---|---|---:|---|---|
|🏗️ Будівельні відходи|/utylizaciya-budivelnyh-vidhodiv.html|Порядок утилізації будівельних відходів для підприємств / Порядок утилізації будівельних відходів для підприємств — Довідник YOURECO|https://guide.youreco.com.ua/utylizaciya-budivelnyh-vidhodiv.html|no|no|68|MAKE_TARGET_INDEXABLE|Пункт присутній у стандартному sidebar на всіх 68 сторінках; target має self-canonical, не є redirect і виглядає як важлива сторінка меню, але закритий noindex та відсутній у public sitemap.|
|🔌 Кабель та дроти|/utylizaciya-kabelyu-ta-drotiv.html|Як оформлюється утилізація кабелю та дротів / Як оформлюється утилізація кабелю та дротів — Довідник YOURECO|https://guide.youreco.com.ua/utylizaciya-kabelyu-ta-drotiv.html|no|no|68|MAKE_TARGET_INDEXABLE|Пункт присутній у стандартному sidebar на всіх 68 сторінках; target має self-canonical, не є redirect і виглядає як важлива сторінка меню, але закритий noindex та відсутній у public sitemap.|
|🔋 Li-ion батареї|/utylizaciya-li-ion-batarej.html|Як оформлюється утилізація літій-іонних батарей / Як оформлюється утилізація літій-іонних батарей — Довідник YOURECO|https://guide.youreco.com.ua/utylizaciya-li-ion-batarej.html|no|no|68|MAKE_TARGET_INDEXABLE|Пункт присутній у стандартному sidebar на всіх 68 сторінках; target має self-canonical, не є redirect і виглядає як важлива сторінка меню, але закритий noindex та відсутній у public sitemap.|
|🖥️ Офісні меблі та оргтехніка|/utylizaciya-ofisnih-mebliv-orgtehniki.html|Порядок утилізації офісних меблів та оргтехніки / Порядок утилізації офісних меблів та оргтехніки — Довідник YOURECO|https://guide.youreco.com.ua/utylizaciya-ofisnih-mebliv-orgtehniki.html|no|no|68|MAKE_TARGET_INDEXABLE|Пункт присутній у стандартному sidebar на всіх 68 сторінках; target має self-canonical, не є redirect і виглядає як важлива сторінка меню, але закритий noindex та відсутній у public sitemap.|
|♻️ Пластик та полімери|/utylizaciya-plastyku-ta-polimeriv.html|Порядок утилізації пластику та полімерів для підприємств / Порядок утилізації пластику та полімерів для підприємств — Довідник YOURECO|https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html|no|no|68|MAKE_TARGET_INDEXABLE|Пункт присутній у стандартному sidebar на всіх 68 сторінках; target має self-canonical, не є redirect і виглядає як важлива сторінка меню, але закритий noindex та відсутній у public sitemap.|
|⭕ Шини|/utylizaciya-shyn.html|Як оформлюється утилізація шин / Як оформлюється утилізація шин — Довідник YOURECO|https://guide.youreco.com.ua/utylizaciya-shyn.html|no|no|68|MAKE_TARGET_INDEXABLE|Пункт присутній у стандартному sidebar на всіх 68 сторінках; target має self-canonical, не є redirect і виглядає як важлива сторінка меню, але закритий noindex та відсутній у public sitemap.|
|📦 Тара та упаковка|/utylizaciya-tary-upakovki.html|Як оформлюється утилізація тари та упаковки / Як оформлюється утилізація тари та упаковки — Довідник YOURECO|https://guide.youreco.com.ua/utylizaciya-tary-upakovki.html|no|no|68|MAKE_TARGET_INDEXABLE|Пункт присутній у стандартному sidebar на всіх 68 сторінках; target має self-canonical, не є redirect і виглядає як важлива сторінка меню, але закритий noindex та відсутній у public sitemap.|
|🛢️ Відпрацьована моторна олива|/utylizaciya-vidpracovanoi-olyvy.html|Утилізація відпрацьованої оливи для бізнесу / Утилізація відпрацьованої оливи для бізнесу — YOURECO|https://guide.youreco.com.ua/utylizaciya-vidpracovanoi-olyvy.html|no|no|68|MAKE_TARGET_INDEXABLE|Пункт присутній у стандартному sidebar на всіх 68 сторінках; target має self-canonical, не є redirect і виглядає як важлива сторінка меню, але закритий noindex та відсутній у public sitemap.|
|🧪 Некондиційна сировина|/utylizaciya-nekondyciynoyi-produkciyi.html|Порядок утилізації некондиційної продукції / Порядок утилізації некондиційної продукції — Довідник YOURECO|https://guide.youreco.com.ua/utylizaciya-nekondyciynoyi-produkciyi.html|no|no|2|NEEDS_DECISION|Пункт трапляється тільки у sidebar сторінок utylizaciya.html та utylizaciya/index.html; target self-canonical, не redirect, але noindex і не в sitemap. Потрібно вирішити, чи це частина меню, чи зайвий hub-residue.|
|👕 Одяг та взуття|/utylizaciya-odyagu-vzuttya.html|Куди передають одяг та взуття на утилізацію / Куди передають одяг та взуття на утилізацію — Довідник YOURECO|https://guide.youreco.com.ua/utylizaciya-odyagu-vzuttya.html|no|no|2|NEEDS_DECISION|Пункт трапляється тільки у sidebar сторінок utylizaciya.html та utylizaciya/index.html; target self-canonical, не redirect, але noindex і не в sitemap. Потрібно вирішити, чи це частина меню, чи зайвий hub-residue.|
|🥫 Продукти харчування та напої|/utylizaciya-produktiv-harchuvannya-napoyiv.html|Порядок утилізації продуктів харчування та напоїв / Порядок утилізації продуктів харчування та напоїв — Довідник YOURECO|https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html|no|no|2|NEEDS_DECISION|Пункт трапляється тільки у sidebar сторінок utylizaciya.html та utylizaciya/index.html; target self-canonical, не redirect, але noindex і не в sitemap. Потрібно вирішити, чи це частина меню, чи зайвий hub-residue.|
|⚡ Сонячні панелі та лопаті ВЕС|/utylizaciya-sonyachnih-panelij-vitryakiv.html|Як оформлюється утилізація сонячних панелей та лопатей ВЕС / Як оформлюється утилізація сонячних панелей та лопатей ВЕС — Довідник YOURECO|https://guide.youreco.com.ua/utylizaciya-sonyachnih-panelij-vitryakiv.html|no|no|2|NEEDS_DECISION|Пункт трапляється тільки у sidebar сторінок utylizaciya.html та utylizaciya/index.html; target self-canonical, не redirect, але noindex і не в sitemap. Потрібно вирішити, чи це частина меню, чи зайвий hub-residue.|

## Main Navigation Points To Noindex

|sidebar item|href|recommendation|
|---|---|---|
|🏗️ Будівельні відходи|/utylizaciya-budivelnyh-vidhodiv.html|Краще індексувати target: прибрати `noindex`, перевірити якість/CTA, додати URL у sitemap.|
|🔌 Кабель та дроти|/utylizaciya-kabelyu-ta-drotiv.html|Краще індексувати target: прибрати `noindex`, перевірити якість/CTA, додати URL у sitemap.|
|🔋 Li-ion батареї|/utylizaciya-li-ion-batarej.html|Краще індексувати target: прибрати `noindex`, перевірити якість/CTA, додати URL у sitemap.|
|🖥️ Офісні меблі та оргтехніка|/utylizaciya-ofisnih-mebliv-orgtehniki.html|Краще індексувати target: прибрати `noindex`, перевірити якість/CTA, додати URL у sitemap.|
|♻️ Пластик та полімери|/utylizaciya-plastyku-ta-polimeriv.html|Краще індексувати target: прибрати `noindex`, перевірити якість/CTA, додати URL у sitemap.|
|⭕ Шини|/utylizaciya-shyn.html|Краще індексувати target: прибрати `noindex`, перевірити якість/CTA, додати URL у sitemap.|
|📦 Тара та упаковка|/utylizaciya-tary-upakovki.html|Краще індексувати target: прибрати `noindex`, перевірити якість/CTA, додати URL у sitemap.|
|🛢️ Відпрацьована моторна олива|/utylizaciya-vidpracovanoi-olyvy.html|Краще індексувати target: прибрати `noindex`, перевірити якість/CTA, додати URL у sitemap.|
|🧪 Некондиційна сировина|/utylizaciya-nekondyciynoyi-produkciyi.html|Краще прийняти окреме рішення: або індексувати як hub-menu пункт, або прибрати з sidebar `utylizaciya`-хабів; автоматично замінювати нічим за даними аудиту.|
|👕 Одяг та взуття|/utylizaciya-odyagu-vzuttya.html|Краще прийняти окреме рішення: або індексувати як hub-menu пункт, або прибрати з sidebar `utylizaciya`-хабів; автоматично замінювати нічим за даними аудиту.|
|🥫 Продукти харчування та напої|/utylizaciya-produktiv-harchuvannya-napoyiv.html|Краще прийняти окреме рішення: або індексувати як hub-menu пункт, або прибрати з sidebar `utylizaciya`-хабів; автоматично замінювати нічим за даними аудиту.|
|⚡ Сонячні панелі та лопаті ВЕС|/utylizaciya-sonyachnih-panelij-vitryakiv.html|Краще прийняти окреме рішення: або індексувати як hub-menu пункт, або прибрати з sidebar `utylizaciya`-хабів; автоматично замінювати нічим за даними аудиту.|

## C. Priorities

### HIGH
- Індексувати або свідомо замінити 8 стандартних sidebar targets з 68 входженнями кожен: `/utylizaciya-li-ion-batarej.html`, `/utylizaciya-shyn.html`, `/utylizaciya-plastyku-ta-polimeriv.html`, `/utylizaciya-budivelnyh-vidhodiv.html`, `/utylizaciya-kabelyu-ta-drotiv.html`, `/utylizaciya-tary-upakovki.html`, `/utylizaciya-ofisnih-mebliv-orgtehniki.html`, `/utylizaciya-vidpracovanoi-olyvy.html`.
- Перед зміною індексації перевірити, що ці сторінки не були залишені `noindex` через якість контенту, CTA або попередні self-referential/CTA issues.

### MEDIUM
- Розібрати 4 hub-sidebar targets із 2 входженнями кожен у `utylizaciya.html` та `utylizaciya/index.html`: некондиційна продукція, одяг та взуття, продукти харчування та напої, сонячні панелі та лопаті ВЕС.
- Для пункту “Некондиційна сировина” окремо перевірити відповідність anchor text до href: зараз anchor веде на `/utylizaciya-nekondyciynoyi-produkciyi.html`, а не на сторінку сировини.

### LOW
- Після рішення щодо індексації повторно прогнати аудит noindex links і окремо перевірити 50 сторінок без статичного active item.
- Якщо якісь target лишаються `noindex`, прибрати їх із основного меню або зафіксувати свідому політику `noindex, follow`.

## D. Batch 1 Proposal

Maximum 5 target URLs. Recommended first batch: targets with highest repeated sidebar impact and no alternate canonical/index target shown by the audit.

|target URL|recommended action|source files if this becomes replace|meta robots/sitemap needed if make indexable|
|---|---|---|---|
|/utylizaciya-li-ion-batarej.html|MAKE_TARGET_INDEXABLE|Replace is not preferred. If replace is chosen, update the standard sidebar in all 68 source HTML files that currently contain this href.|Yes: remove `noindex` from `utylizaciya-li-ion-batarej.html` and add the URL to public sitemap/source sitemap flow.|
|/utylizaciya-shyn.html|MAKE_TARGET_INDEXABLE|Replace is not preferred. If replace is chosen, update the standard sidebar in all 68 source HTML files that currently contain this href.|Yes: remove `noindex` from `utylizaciya-shyn.html` and add the URL to public sitemap/source sitemap flow.|
|/utylizaciya-plastyku-ta-polimeriv.html|MAKE_TARGET_INDEXABLE|Replace is not preferred. If replace is chosen, update the standard sidebar in all 68 source HTML files that currently contain this href.|Yes: remove `noindex` from `utylizaciya-plastyku-ta-polimeriv.html` and add the URL to public sitemap/source sitemap flow.|
|/utylizaciya-budivelnyh-vidhodiv.html|MAKE_TARGET_INDEXABLE|Replace is not preferred. If replace is chosen, update the standard sidebar in all 68 source HTML files that currently contain this href.|Yes: remove `noindex` from `utylizaciya-budivelnyh-vidhodiv.html` and add the URL to public sitemap/source sitemap flow.|
|/utylizaciya-kabelyu-ta-drotiv.html|MAKE_TARGET_INDEXABLE|Replace is not preferred. If replace is chosen, update the standard sidebar in all 68 source HTML files that currently contain this href.|Yes: remove `noindex` from `utylizaciya-kabelyu-ta-drotiv.html` and add the URL to public sitemap/source sitemap flow.|

Replace source-file scope for standard sidebar targets: all 68 sidebar source files copied by `scripts/build_public.py` from root HTML and route index files. The highest-value places to check first are `index.html`, `logistyka/index.html`, `pererobka/index.html`, `sortuvannya/index.html`, and then the remaining root HTML pages with the standard sidebar.

## E. Source Scope Notes

- Standard repeated targets occur on 68 sidebar pages; because `scripts/build_public.py` copies root `*.html` plus route `index.html` files into `public/`, fixes should be made in source HTML, not in `public/`.
- The 4 low-occurrence targets occur only in source files `utylizaciya.html` and `utylizaciya/index.html`.
- No target is a meta-refresh redirect, and no target canonical points to a different URL according to the audit fields.

## Cyrillic / Encoding

Кирилиця: не зіпсована.
