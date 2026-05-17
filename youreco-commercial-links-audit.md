# YOURECO Commercial Links Audit

## Scope
- Audit only. No source HTML was modified.
- Scanned source `*.html` files excluding `public`, `dist`, `node_modules`, `.git`.
- Focus: external `href` values pointing to `https://youreco.com.ua/`.

## Summary
- external YOURECO links count: 176
- unique external YOURECO URLs: 22
- suspicious links count: 38
- cosmetics wrong URL count: 14
- files with suspicious links: 37

## Known correct mappings
- cosmetics commercial page: https://youreco.com.ua/kosmetyky/
- food commercial page currently used in food/drinks block: https://youreco.com.ua/harchovy/

## Priority URL check
- `https://youreco.com.ua/utylizaciya-kosmetyky.html` -> found 14 times in source HTML; should not be treated as correct without replacement.
- `https://youreco.com.ua/utylizaciya-kosmetyky.html/` -> found 0 times in source HTML; should not be treated as correct.
- `https://youreco.com.ua/kosmetyky/` -> found 0 times in source HTML; verified live and matches the known-correct cosmetics commercial URL.
- `https://youreco.com.ua/harchovy/` -> found 45 times in source HTML; verified live and looks correct.
- `https://youreco.com.ua/utylizatsiya-dlya-riteylu/` -> found 1 time in source HTML; verified live and looks correct.

## Cosmetics URL fix
- wrong URL replaced: `https://youreco.com.ua/utylizaciya-kosmetyky.html`
- correct URL: `https://youreco.com.ua/kosmetyky/`
- source files changed: 13 (`kudy-zdaty-kosmetiki.html`, `kudy-zdaty-kosmetyky-magazyniv.html`, `kudy-zdaty-kosmetyky.html`, `kudy-zdaty-parfumeriyi.html`, `kudy-zdaty-prostrochenoyi-kosmetyky.html`, `kudy-zdaty-skladskyh-zalyshkiv-kosmetyky.html`, `kudy-zdaty-upakovky-vid-kosmetyky.html`, `utylizaciya-kosmetyky-magazyniv.html`, `utylizaciya-kosmetyky.html`, `utylizaciya-parfumeriyi.html`, `utylizaciya-prostrochenoyi-kosmetyky.html`, `utylizaciya-skladskyh-zalyshkiv-kosmetyky.html`, `znyshchennya-kosmetyky.html`)
- remaining wrong cosmetics URL in real source HTML: 0
- internal guide links preserved: yes; `href="/utylizaciya-kosmetyky.html"` still found in real source HTML

## Existing / likely correct URLs
These are slash-based commercial URLs that either were verified live or align with the apparent commercial-site navigation.

- https://youreco.com.ua/harchovy/ (count: 45) - verified live
- https://youreco.com.ua/kosmetyky/ (count: 0) - verified live; known correct cosmetics URL
- https://youreco.com.ua/utylizatsiya-dlya-riteylu/ (count: 1) - verified live
- https://youreco.com.ua/promyslovi/ (count: 46)
- https://youreco.com.ua/upakovky/ (count: 21)
- https://youreco.com.ua/utylizatsiya-dlya-vyrobnytstv/ (count: 5)
- https://youreco.com.ua/li-ion-batarei/ (count: 4)
- https://youreco.com.ua/utylizatsiya-dlya-skladiv/ (count: 3)
- https://youreco.com.ua/paneli/ (count: 2)
- https://youreco.com.ua/orgtehniky/ (count: 2)
- https://youreco.com.ua/odyag/ (count: 2)
- https://youreco.com.ua/paverbanki/ (count: 2)
- https://youreco.com.ua/olyvy/ (count: 1)
- https://youreco.com.ua/obladnannya/ (count: 1)
- https://youreco.com.ua/utylizatsiya-dlya-importeriv/ (count: 1)
- https://youreco.com.ua/pid-mytnym/ (count: 1)

## Suspicious or invented URLs
These should not be assumed correct for the commercial site.

- https://youreco.com.ua/utylizaciya-kosmetyky.html (count: 14)
  - probable replacement: https://youreco.com.ua/kosmetyky/
  - reason: `.html` guide-like slug on the commercial domain; cosmetics has a known-correct landing page.
- https://youreco.com.ua/dokumenty.html (count: 3)
  - probable replacement: https://youreco.com.ua/dokumenty/
  - reason: `.html` URL on the commercial site; commercial navigation pattern is slash-based.
- https://youreco.com.ua/kontakty.html (count: 3)
  - probable replacement: https://youreco.com.ua/kontakty/
  - reason: `.html` URL on the commercial site; commercial navigation pattern is slash-based.
- https://youreco.com.ua/utylizaciya-shyn.html (count: 12)
  - probable replacement: https://youreco.com.ua/shyn/
  - reason: `.html` URL on the commercial site; live navigation references the slash URL.
- https://youreco.com.ua/utylizaciya-obladnannya.html (count: 3)
  - probable replacement: https://youreco.com.ua/obladnannya/
  - reason: `.html` URL on the commercial site; live navigation references the slash URL.
- https://youreco.com.ua/utylizaciya-tovariv.html (count: 3)
  - probable replacement: https://youreco.com.ua/tovary/
  - reason: `.html` URL on the commercial site; live navigation references the slash URL.

## URL normalization issue
- https://youreco.com.ua/syrovyny (count: 1)
  - probable replacement: https://youreco.com.ua/syrovyny/
  - reason: looks nav-aligned, but the source uses a non-canonical no-trailing-slash form.

## Commercial URLs with `.html`
- https://youreco.com.ua/dokumenty.html (count: 3)
- https://youreco.com.ua/kontakty.html (count: 3)
- https://youreco.com.ua/utylizaciya-kosmetyky.html (count: 14)
- https://youreco.com.ua/utylizaciya-obladnannya.html (count: 3)
- https://youreco.com.ua/utylizaciya-shyn.html (count: 12)
- https://youreco.com.ua/utylizaciya-tovariv.html (count: 3)

## URLs that should be replaced first
- https://youreco.com.ua/utylizaciya-kosmetyky.html -> https://youreco.com.ua/kosmetyky/
- https://youreco.com.ua/dokumenty.html -> https://youreco.com.ua/dokumenty/
- https://youreco.com.ua/kontakty.html -> https://youreco.com.ua/kontakty/
- https://youreco.com.ua/utylizaciya-shyn.html -> https://youreco.com.ua/shyn/
- https://youreco.com.ua/utylizaciya-obladnannya.html -> https://youreco.com.ua/obladnannya/
- https://youreco.com.ua/utylizaciya-tovariv.html -> https://youreco.com.ua/tovary/
- https://youreco.com.ua/syrovyny -> https://youreco.com.ua/syrovyny/

## CTA anchors that need clarification
These anchors either point to a suspicious URL or over-promise a specific landing page while the commercial target appears broader.

- `utylizaciya-kosmetyky-magazyniv.html:L245` -> `Передати на утилізацію retail-партію косметики`
- `utylizaciya-parfumeriyi.html:L236` -> `Передати партію парфумерії на утилізацію з документами`
- `utylizaciya-prostrochenoyi-kosmetyky.html:L233` -> `Передати прострочену косметику на утилізацію з документами`
- `utylizaciya-prostrochenoyi-kosmetyky-main-draft.html:L157` -> `Передати прострочену косметику на утилізацію з документами`
- `utylizaciya-skladskyh-zalyshkiv-kosmetyky.html:L246` -> `Передати на утилізацію складські залишки косметики`
- `utylizaciya-dokumentiv.html:L112` -> `Перейти до послуги`
- `pererobka-avtomobilnyh-shyn.html:L100` -> `Перейти до послуги`
- `kontakty.html:L142` -> `Сторінка контактів YOURECO`
- `kontakty.html:L147` -> `Відкрити контакти YOURECO`

## Files with suspicious links
- kontakty.html
- kudy-zdaty-avtoshyn.html
- kudy-zdaty-dokumentiv.html
- kudy-zdaty-kosmetiki.html
- kudy-zdaty-kosmetyky-magazyniv.html
- kudy-zdaty-kosmetyky.html
- kudy-zdaty-obladnannya.html
- kudy-zdaty-parfumeriyi.html
- kudy-zdaty-promyslovogo-obladnannya-mehanizmiv.html
- kudy-zdaty-prostrochenoyi-kosmetyky.html
- kudy-zdaty-shin.html
- kudy-zdaty-shyn-pidpryyemstvamy.html
- kudy-zdaty-shyn.html
- kudy-zdaty-shyny.html
- kudy-zdaty-skladskyh-zalyshkiv-kosmetyky.html
- kudy-zdaty-tovariv.html
- kudy-zdaty-tovary-pid-mitnim-kontrolem.html
- kudy-zdaty-upakovky-vid-kosmetyky.html
- kudy-zdaty-vantazhnyh-shyn.html
- logistyka-shyn.html
- pererobka-avtomobilnyh-shyn.html
- pererobka-gumovyh-vyrobiv.html
- shyny.html
- utylizaciya-avtoshyn.html
- utylizaciya-dokumentiv.html
- utylizaciya-konfidenciynykh-dokumentiv.html
- utylizaciya-kosmetyky-magazyniv.html
- utylizaciya-kosmetyky.html
- utylizaciya-parfumeriyi.html
- utylizaciya-promyslovogo-obladnannya-mehanizmiv.html
- utylizaciya-prostrochenoyi-kosmetyky-main-draft.html
- utylizaciya-prostrochenoyi-kosmetyky.html
- utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
- utylizaciya.html
- zbir-shyn-na-pidpryyemstvi.html
- znyshchennya-kosmetyky.html

## All external YOURECO links in source HTML
This section inventories every unique external commercial URL found in source HTML, with total occurrence count.

- https://youreco.com.ua/promyslovi/ (46)
- https://youreco.com.ua/harchovy/ (45)
- https://youreco.com.ua/upakovky/ (21)
- https://youreco.com.ua/utylizaciya-kosmetyky.html (14)
- https://youreco.com.ua/utylizaciya-shyn.html (12)
- https://youreco.com.ua/utylizatsiya-dlya-vyrobnytstv/ (5)
- https://youreco.com.ua/li-ion-batarei/ (4)
- https://youreco.com.ua/dokumenty.html (3)
- https://youreco.com.ua/kontakty.html (3)
- https://youreco.com.ua/utylizaciya-obladnannya.html (3)
- https://youreco.com.ua/utylizaciya-tovariv.html (3)
- https://youreco.com.ua/utylizatsiya-dlya-skladiv/ (3)
- https://youreco.com.ua/odyag/ (2)
- https://youreco.com.ua/orgtehniky/ (2)
- https://youreco.com.ua/paneli/ (2)
- https://youreco.com.ua/paverbanki/ (2)
- https://youreco.com.ua/obladnannya/ (1)
- https://youreco.com.ua/olyvy/ (1)
- https://youreco.com.ua/pid-mytnym/ (1)
- https://youreco.com.ua/syrovyny (1)
- https://youreco.com.ua/utylizatsiya-dlya-importeriv/ (1)
- https://youreco.com.ua/utylizatsiya-dlya-riteylu/ (1)

## Detailed suspicious entries
- kontakty.html:L88 -> https://youreco.com.ua/kontakty.html -> `youreco.com.ua/kontakty`
- kontakty.html:L142 -> https://youreco.com.ua/kontakty.html -> `Сторінка контактів YOURECO`
- kontakty.html:L147 -> https://youreco.com.ua/kontakty.html -> `Відкрити контакти YOURECO`
- kudy-zdaty-avtoshyn.html:L39 -> https://youreco.com.ua/utylizaciya-shyn.html -> `Замовити утилізацію шин`
- kudy-zdaty-dokumentiv.html:L39 -> https://youreco.com.ua/dokumenty.html -> `Замовити знищення конфіденційних документів`
- kudy-zdaty-kosmetiki.html:L39 -> https://youreco.com.ua/utylizaciya-kosmetyky.html -> `Замовити утилізацію косметики`
- kudy-zdaty-kosmetyky-magazyniv.html:L39 -> https://youreco.com.ua/utylizaciya-kosmetyky.html -> `Замовити утилізацію косметики`
- kudy-zdaty-kosmetyky.html:L39 -> https://youreco.com.ua/utylizaciya-kosmetyky.html -> `Замовити утилізацію косметики`
- kudy-zdaty-obladnannya.html:L40 -> https://youreco.com.ua/utylizaciya-obladnannya.html -> `Замовити утилізацію обладнання`
- kudy-zdaty-parfumeriyi.html:L39 -> https://youreco.com.ua/utylizaciya-kosmetyky.html -> `Замовити утилізацію косметики`
- kudy-zdaty-promyslovogo-obladnannya-mehanizmiv.html:L39 -> https://youreco.com.ua/utylizaciya-obladnannya.html -> `Замовити утилізацію обладнання`
- kudy-zdaty-prostrochenoyi-kosmetyky.html:L39 -> https://youreco.com.ua/utylizaciya-kosmetyky.html -> `Замовити утилізацію косметики`
- kudy-zdaty-shin.html:L39 -> https://youreco.com.ua/utylizaciya-shyn.html -> `Замовити утилізацію шин`
- kudy-zdaty-shyn-pidpryyemstvamy.html:L39 -> https://youreco.com.ua/utylizaciya-shyn.html -> `Замовити утилізацію шин`
- kudy-zdaty-shyn.html:L39 -> https://youreco.com.ua/utylizaciya-shyn.html -> `Замовити утилізацію шин`
- kudy-zdaty-shyny.html:L39 -> https://youreco.com.ua/utylizaciya-shyn.html -> `Замовити утилізацію шин`
- kudy-zdaty-skladskyh-zalyshkiv-kosmetyky.html:L39 -> https://youreco.com.ua/utylizaciya-kosmetyky.html -> `Замовити утилізацію косметики`
- kudy-zdaty-tovariv.html:L39 -> https://youreco.com.ua/utylizaciya-tovariv.html -> `Замовити утилізацію списаних товарів`
- kudy-zdaty-tovary-pid-mitnim-kontrolem.html:L39 -> https://youreco.com.ua/utylizaciya-tovariv.html -> `Замовити утилізацію списаних товарів`
- kudy-zdaty-upakovky-vid-kosmetyky.html:L39 -> https://youreco.com.ua/utylizaciya-kosmetyky.html -> `Замовити утилізацію косметики`
- kudy-zdaty-vantazhnyh-shyn.html:L39 -> https://youreco.com.ua/utylizaciya-shyn.html -> `Замовити утилізацію шин`
- logistyka-shyn.html:L96 -> https://youreco.com.ua/utylizaciya-shyn.html -> `Замовити вивезення та передання шин`
- pererobka-avtomobilnyh-shyn.html:L100 -> https://youreco.com.ua/utylizaciya-shyn.html -> `Перейти до послуги`
- pererobka-gumovyh-vyrobiv.html:L96 -> https://youreco.com.ua/utylizaciya-shyn.html -> `Замовити переробку гумових виробів`
- shyny.html:L46 -> https://youreco.com.ua/utylizaciya-shyn.html -> `Замовити утилізацію шин`
- utylizaciya-avtoshyn.html:L98 -> https://youreco.com.ua/utylizaciya-shyn.html -> `Замовити утилізацію шин`
- utylizaciya-dokumentiv.html:L112 -> https://youreco.com.ua/dokumenty.html -> `Перейти до послуги`
- utylizaciya-konfidenciynykh-dokumentiv.html:L156 -> https://youreco.com.ua/dokumenty.html -> `Замовити знищення конфіденційних документів`
- utylizaciya-kosmetyky-magazyniv.html:L245 -> https://youreco.com.ua/utylizaciya-kosmetyky.html -> `Передати на утилізацію retail-партію косметики`
- utylizaciya-kosmetyky.html:L142 -> https://youreco.com.ua/utylizaciya-kosmetyky.html -> `Замовити утилізацію косметики`
- utylizaciya-parfumeriyi.html:L236 -> https://youreco.com.ua/utylizaciya-kosmetyky.html -> `Передати партію парфумерії на утилізацію з документами`
- utylizaciya-promyslovogo-obladnannya-mehanizmiv.html:L102 -> https://youreco.com.ua/utylizaciya-obladnannya.html -> `Замовити утилізацію обладнання`
- utylizaciya-prostrochenoyi-kosmetyky-main-draft.html:L157 -> https://youreco.com.ua/utylizaciya-kosmetyky.html -> `Передати прострочену косметику на утилізацію з документами`
- utylizaciya-prostrochenoyi-kosmetyky.html:L233 -> https://youreco.com.ua/utylizaciya-kosmetyky.html -> `Передати прострочену косметику на утилізацію з документами`
- utylizaciya-skladskyh-zalyshkiv-kosmetyky.html:L246 -> https://youreco.com.ua/utylizaciya-kosmetyky.html -> `Передати на утилізацію складські залишки косметики`
- utylizaciya.html:L151 -> https://youreco.com.ua/utylizaciya-tovariv.html -> `Замовити утилізацію списаних товарів`
- zbir-shyn-na-pidpryyemstvi.html:L97 -> https://youreco.com.ua/utylizaciya-shyn.html -> `Замовити утилізацію шин`
- znyshchennya-kosmetyky.html:L65 -> https://youreco.com.ua/utylizaciya-kosmetyky.html -> `Замовити утилізацію косметики`

## Notable exact target counts
- https://youreco.com.ua/utylizaciya-kosmetyky.html -> 14
- https://youreco.com.ua/utylizaciya-kosmetyky.html/ -> 0
- https://youreco.com.ua/kosmetyky/ -> 0
- https://youreco.com.ua/harchovy/ -> 45
- https://youreco.com.ua/utylizatsiya-dlya-riteylu/ -> 1
- https://youreco.com.ua/dokumenty.html -> 3
- https://youreco.com.ua/kontakty.html -> 3
- https://youreco.com.ua/utylizaciya-shyn.html -> 12
- https://youreco.com.ua/utylizaciya-obladnannya.html -> 3
- https://youreco.com.ua/utylizaciya-tovariv.html -> 3
- https://youreco.com.ua/syrovyny -> 1

## Manual classification template
- file:
- current URL:
- correct URL:
- anchor:
- action: replace / keep / verify manually
