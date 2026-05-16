# Food/Drinks CTA Clarity Audit

Scope: audit-only CTA clarity check for food/drinks pages. No source HTML changes, no build, no commit, no push.

## Summary

- pages checked: 7
- missing CTA id count: 4
- weak anchor count: 3
- missing rel/target count: 0
- noindex draft pages: utylizaciya-alkogolnyh-napoyiv.html
- pages needing CTA fix: utylizaciya-harchovyh-produktiv.html, utylizaciya-fruktiv-ta-ovochiv.html, utylizaciya-sokiv-ta-napoyiv.html, utylizaciya-energetychnyh-napoyiv.html

## utylizaciya-harchovyh-produktiv.html

- classification: missing CTA
- robots: index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1
- service CTA present: False
- commercial URL present: True
- rel noopener noreferrer: True
- target blank: True
- anchor text: утилізація харчових продуктів для бізнесу
- anchor specificity: ok for food umbrella; general anchor is acceptable here.
- nearby text clarity: ok; explains practical commercial request, contractor/logistics, transfer timing, party description.
- generic-without-topic risk: low, because the page is the umbrella food page and surrounding text mentions food/product parties.
- CTA lines:
  - L165: <p>Підрядник потрібен, коли підприємство має значний обсяг списаної продукції, партія швидко псується, є вимога до підтвердних документів або потрібна організована логістика з кількох точок. Перед зверненням варто підготувати базовий опис: тип продукції, орієнтовну вагу, кількість палет чи місць, стан тари, адресу зберігання, бажаний строк передачі та контакт відповідальної особи. Для практичного запиту щодо комерційної послуги можна перейти на сторінку <a href="https://youreco.com.ua/harchovy/" rel="noopener noreferrer" target="_blank">утилізація харчових продуктів для бізнесу</a>.</p>
- audit note: commercial CTA exists and is clear, but the required id="service-cta" block is missing.

## utylizaciya-fruktiv-ta-ovochiv.html

- classification: missing CTA; weak anchor
- robots: index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1
- service CTA present: False
- commercial URL present: True
- rel noopener noreferrer: True
- target blank: True
- anchor text: утилізація харчових продуктів для бізнесу
- anchor specificity: weak; expected anchor should directly mention фруктово-овочеві залишки or харчові партії.
- nearby text clarity: ok; surrounding text says practical organization of transfer and removal of fruit/vegetable residues.
- generic-without-topic risk: medium; text gives context, but the clickable anchor itself is umbrella-level.
- CTA lines:
  - L213: <h2>Що робити далі, якщо потрібна практична організація вивезення</h2>
  - L214: <p>Якщо підприємству потрібне не лише внутрішнє сортування, а й організація передачі та вивезення фруктово-овочевих залишків, можна перейти на сторінку <a href="https://youreco.com.ua/harchovy/" rel="noopener noreferrer" target="_blank">утилізація харчових продуктів для бізнесу</a>.</p>
- audit note: needs id="service-cta" and a more topical anchor.

## utylizaciya-sokiv-ta-napoyiv.html

- classification: missing CTA; weak anchor
- robots: index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1
- service CTA present: False
- commercial URL present: True
- rel noopener noreferrer: True
- target blank: True
- anchor text: утилізація харчових продуктів для бізнесу
- anchor specificity: weak; expected anchor should directly mention соки/напої or рідкі харчові партії.
- nearby text clarity: ok; surrounding text mentions transfer/removal of juice and drink party.
- generic-without-topic risk: medium; page context is clear, but anchor is too generic for the drinks page.
- CTA lines:
  - L221: <h2>Що робити далі</h2>
  - L222: <p>Якщо після внутрішньої підготовки потрібно організувати передачу або вивезення партії соків та напоїв, можна перейти на сторінку <a href="https://youreco.com.ua/harchovy/" rel="noopener noreferrer" target="_blank">утилізація харчових продуктів для бізнесу</a>.</p>
- audit note: needs id="service-cta" and a more topical anchor.

## utylizaciya-pyva.html

- classification: ok
- robots: index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1
- service CTA present: True
- commercial URL present: True
- rel noopener noreferrer: True
- target blank: True
- anchor text: утилізація пива та харчових партій для бізнесу
- anchor specificity: ok; directly mentions пиво.
- nearby text clarity: ok; explicitly says organize transfer or removal of expired/damaged/returned beer party.
- generic-without-topic risk: low.
- CTA lines:
  - L105: <section class="card" id="service-cta"><h2>Що робити далі</h2><p>Якщо потрібно організувати передачу або вивезення партії простроченого, пошкодженого чи поверненого пива, можна перейти на сторінку <a href="https://youreco.com.ua/harchovy/" rel="noopener noreferrer" target="_blank">утилізація пива та харчових партій для бізнесу</a>.</p></section>

## utylizaciya-energetychnyh-napoyiv.html

- classification: weak anchor
- robots: index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1
- service CTA present: True
- commercial URL present: True
- rel noopener noreferrer: True
- target blank: True
- anchor text: утилізація харчових продуктів для бізнесу
- anchor specificity: weak; expected anchor should directly mention енергетичні напої or SKU-партії енергетиків.
- nearby text clarity: partial; it says the party is collected/described and needs transfer/documents, but does not restate energy drinks in the CTA sentence.
- generic-without-topic risk: medium-high; CTA block can feel detached from the energy-drinks topic.
- CTA lines:
  - L105: <section class="card" id="service-cta"><h2>Що робити далі</h2><p>Якщо партія вже зібрана, описана й потрібна організація передачі або супровідних документів, перейдіть на сторінку <a href="https://youreco.com.ua/harchovy/" rel="noopener noreferrer" target="_blank">утилізація харчових продуктів для бізнесу</a>.</p></section>
- audit note: id/rel/target are fine; anchor and adjacent text should be more energy-drinks-specific.

## spysannya-produktiv.html

- classification: ok
- robots: index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1
- service CTA present: True
- commercial URL present: True
- rel noopener noreferrer: True
- target blank: True
- anchor text: утилізація харчових продуктів для бізнесу
- anchor specificity: ok for writeoff page; the topic is the document/accounting stage before physical handling.
- nearby text clarity: ok; explicitly says that after internal writeoff the party can be physically transferred further.
- generic-without-topic risk: low.
- CTA lines:
  - L215: <section class="card" id="service-cta">
  - L216: <h2>Що робити далі</h2>
  - L217: <p>Якщо після внутрішнього списання партію потрібно фактично передати далі, наступним кроком може бути сторінка <a href="https://youreco.com.ua/harchovy/" rel="noopener noreferrer" target="_blank">утилізація харчових продуктів для бізнесу</a>.</p>

## utylizaciya-alkogolnyh-napoyiv.html

- classification: noindex draft / leave for later
- robots: noindex, follow
- service CTA present: False
- commercial URL present: True
- rel noopener noreferrer: True
- target blank: True
- anchor text: Передати опис партії
- anchor specificity: weak/generic for alcohol, but acceptable to leave while draft remains noindex.
- nearby text clarity: partial; explains passing a description for preliminary assessment of wine/spirits/liquor parties, but does not frame it as actual transfer/removal strongly enough.
- generic-without-topic risk: medium; anchor itself is generic, surrounding paragraph provides alcohol context.
- CTA lines:
  - L207: <h2>Передача партії на оцінку</h2>
  - L208: <p>Якщо у вас є партія вина, міцного алкоголю або лікеро-горілчаних виробів, підготуйте короткий опис: тип продукції, кількість, тару, стан упаковки, наявність бою скла чи протікання. Ці дані можна передати для попередньої оцінки сценарію поводження з партією.</p>
  - L209: <p><a href="https://youreco.com.ua/harchovy/" target="_blank" rel="noopener noreferrer">Передати опис партії</a></p>
- audit note: noindex is present, so leave for later unless the draft is promoted.
