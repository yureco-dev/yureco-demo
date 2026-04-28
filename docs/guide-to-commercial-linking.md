# Guide -> Commercial Linking

## Що зроблено

- На релевантних сторінках довідника оновлено блок `service-cta` із заголовком `Потрібна офіційна утилізація з актами?`.
- Додано посилання на релевантні галузеві сторінки commercial-сайту (1-2 на сторінку за контекстом).
- На кожне guide -> commercial посилання додано `data-analytics-event="commercial_site_click"`.
- Title/H1/canonical та основний інформаційний контент сторінок не змінювались.

## Мапінг сторінок

- `utylizaciya-prostrochenoyi-kosmetyky.html`
  - `утилізація для ритейлу` -> `https://youreco.com.ua/utylizatsiya-dlya-riteylu/`
- `spysannya-kosmetychnyh-tovariv.html`
  - `утилізація для ритейлу` -> `https://youreco.com.ua/utylizatsiya-dlya-riteylu/`
- `utylizaciya-harchovyh-produktiv.html`
  - `утилізація для ритейлу` -> `https://youreco.com.ua/utylizatsiya-dlya-riteylu/`
- `utylizaciya-tovariv.html`
  - `утилізація складських залишків` -> `https://youreco.com.ua/utylizatsiya-dlya-skladiv/`
- `utylizaciya-tary-upakovki.html`
  - `утилізація складських залишків` -> `https://youreco.com.ua/utylizatsiya-dlya-skladiv/`
- `dokumenty-dlya-utylizaciyi-vidhodiv.html`
  - `утилізація складських залишків` -> `https://youreco.com.ua/utylizatsiya-dlya-skladiv/`
  - `утилізація відходів для виробництв` -> `https://youreco.com.ua/utylizatsiya-dlya-vyrobnytstv/`
- `utylizaciya-skladskyh-zalyshkiv.html`
  - `утилізація складських залишків` -> `https://youreco.com.ua/utylizatsiya-dlya-skladiv/`
- `yak-peredaty-skladski-zalyshky.html`
  - `утилізація складських залишків` -> `https://youreco.com.ua/utylizatsiya-dlya-skladiv/`
- `vymogy-do-zberigannya-vidhodiv.html`
  - `утилізація складських залишків` -> `https://youreco.com.ua/utylizatsiya-dlya-skladiv/`
- `utylizaciya-promyslovyh-vidhodiv.html`
  - `утилізація відходів для виробництв` -> `https://youreco.com.ua/utylizatsiya-dlya-vyrobnytstv/`
- `utylizaciya-vyrobnychyh-vidhodiv.html`
  - `утилізація відходів для виробництв` -> `https://youreco.com.ua/utylizatsiya-dlya-vyrobnytstv/`
- `utylizaciya-nekondicijnoyi-sirovini.html`
  - `утилізація відходів для виробництв` -> `https://youreco.com.ua/utylizatsiya-dlya-vyrobnytstv/`
- `utylizaciya-vidpracovanoi-olyvy.html`
  - `утилізація відходів для виробництв` -> `https://youreco.com.ua/utylizatsiya-dlya-vyrobnytstv/`
- `utylizaciya-obladnannya.html`
  - `утилізація відходів для виробництв` -> `https://youreco.com.ua/utylizatsiya-dlya-vyrobnytstv/`
- `utylizaciya-tovary-pid-mitnim-kontrolem.html`
  - `утилізація списаних товарів для імпортерів` -> `https://youreco.com.ua/utylizatsiya-dlya-importeriv/`
- `utylizaciya-nekondyciynoyi-produkciyi.html`
  - `утилізація списаних товарів для імпортерів` -> `https://youreco.com.ua/utylizatsiya-dlya-importeriv/`

## Покриття сегментів

- Ритейл: `utylizaciya-prostrochenoyi-kosmetyky.html`, `spysannya-kosmetychnyh-tovariv.html`, `utylizaciya-harchovyh-produktiv.html`.
- Склади: `utylizaciya-skladskyh-zalyshkiv.html`, `yak-peredaty-skladski-zalyshky.html`, `vymogy-do-zberigannya-vidhodiv.html`, `utylizaciya-tary-upakovki.html`, `utylizaciya-tovariv.html`.
- Виробництва: `utylizaciya-promyslovyh-vidhodiv.html`, `utylizaciya-vyrobnychyh-vidhodiv.html`, `utylizaciya-nekondicijnoyi-sirovini.html`, `utylizaciya-vidpracovanoi-olyvy.html`, `utylizaciya-obladnannya.html`.
- Імпортери: `utylizaciya-tovary-pid-mitnim-kontrolem.html`, `utylizaciya-nekondyciynoyi-produkciyi.html`.

## Що потрібно створити пізніше

- Окрема guide-сторінка про `неліквідні товари` з посиланням на `https://youreco.com.ua/utylizatsiya-dlya-skladiv/`.
- Окрема guide-сторінка про `пошкоджену продукцію імпортерів` (окремо від митного контролю) з посиланням на `https://youreco.com.ua/utylizatsiya-dlya-importeriv/`.

## Перевірки канібалізації

- Не змінювалися title/H1/canonical.
- CTA розміщено внизу інформаційних сторінок у секції `service-cta`.
- Основний довідковий контент залишився інформаційним.

## Технічна перевірка

- `localhost` у `href`: не знайдено.
- `UTM`-параметри у `href`: не знайдено.
- Prepublish gate:
  - `SELF_REFERENTIAL_METADATA_GATE`: PASS
  - `SCHEMA_JSONLD_URL_GATE`: PASS
  - `PLACEHOLDER_DETECTION_GATE`: PASS
  - `REDIRECT_SITEMAP_GATE`: PASS
  - `MOJIBAKE_DETECTION_GATE`: FAIL (`akt-pryimannya-peredachi.html` містить символ `�`, не пов'язано з новими CTA)
  - `CTA_MISMATCH_DETECTION_GATE`: FAIL (7 semantic topic-mismatch попереджень через суворі внутрішні правила мапінгу CTA)
- Sitemap/robots не змінювалися.

## Prepublish fixes

- `akt-pryimannya-peredachi.html`:
  - знайдено масове пошкодження кирилиці (символ `�` по всьому документу), що блокувало `MOJIBAKE_DETECTION_GATE`;
  - виконано відновлення текстових блоків сторінки у коректному UTF-8 без зміни canonical URL;
  - фрагмент (до): `��� ���������-�������� ������`;
  - фрагмент (після): `Акт приймання-передачі відходів`.
- Виправлено 7 `CTA topic-mismatch` (anchor-тексти, без зміни commercial URL):
  - `utylizaciya-harchovyh-produktiv.html` -> `утилізація харчових продуктів для ритейлу`;
  - `utylizaciya-nekondyciynoyi-produkciyi.html` -> `утилізація некондиційної продукції для імпортерів`;
  - `utylizaciya-obladnannya.html` -> `утилізація обладнання для виробництв`;
  - `utylizaciya-prostrochenoyi-kosmetyky.html` -> `утилізація простроченої косметики для ритейлу`;
  - `utylizaciya-tovariv.html` -> `утилізація товарів і складських залишків`;
  - `utylizaciya-vidpracovanoi-olyvy.html` -> `утилізація відпрацьованої оливи для виробництв`;
  - `yak-peredaty-skladski-zalyshky.html` -> `утилізація складських залишків на утилізацію`.
- False positives після правок: не зафіксовано.
- Підсумок prepublish після повторного прогону: `PASS`.
