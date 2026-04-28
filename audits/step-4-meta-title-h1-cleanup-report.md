# ЕТАП 4. Очищення title, meta description, H1 та базової SEO-розмітки

Дата перевірки: 2026-04-28

## Обсяг перевірки

- HTML-сторінок перевірено у `public/`: 244.
- Індексованих сторінок перевірено: 137.
- Source HTML, що відповідають production-виводу, перевірено та оновлено точково.
- `public/` перегенеровано командою `py -3 scripts/build_public.py` (`PUBLIC_BUILD_OK files=251 html=244`).
- `public/sitemap.xml` перевірено після збірки: 141 URL.

## Результати після виправлення

- Відсутніх `<title>` серед індексованих сторінок: 0.
- Відсутніх `<h1>` серед індексованих сторінок: 0.
- Сторінок з кількома `<h1>` серед індексованих сторінок: 0.
- Відсутніх meta description серед індексованих сторінок: 0.
- Дубльованих title серед індексованих сторінок: 0.
- Дубльованих meta description серед індексованих сторінок: 0.
- Noindex/redirect URL у sitemap: 0.

## Обов'язкові проблеми

- `articles/index.html`: виправлено. Додано унікальний meta description для службової noindex/redirect-сторінки.
- `kudy-zdaty-gipsokartonu.html`: коректно виключено. Сторінка має `noindex, follow`, refresh redirect, canonical на `utylizaciya-gipsokartonu.html` і не входить у sitemap.
- Дубль title `Куди здати відпрацьовану оливу — Довідник YOURECO`: конкуренцію прибрано. Noindex/redirect-сторінки отримали службові title/H1/description, основною індексованою лишилась `utylizaciya-vidpracovanoi-olyvy.html`.

## UTF-8 і кирилиця

- UTF-8: усі перевірені production source та `public/` файли читаються як UTF-8.
- BOM: не знайдено.
- Mojibake-патерни `Ð`, `Ñ`, `Р°`, `Р±`, `Р В`, `СЂ`, `вЂ`, `�`: не знайдено.
- Кирилиця: не зіпсована.

## Змінені файли

- `articles/index.html`
- `kudy-zdaty-vidpracovane-maslo.html`
- `kudy-zdaty-vidpracovanoi-olyvy.html`
- `utylizaciya-vidpracovanoi-olyvy.html`
- `dokumenty.html`
- `logistyka.html`
- `pererobka.html`
- `sortuvannya.html`
- `utylizaciya.html`
- `vidhody.html`
- `zbir.html`
- `logistyka/index.html`
- `pererobka/index.html`
- `sortuvannya/index.html`
- `utylizaciya/index.html`
- Відповідні згенеровані копії у `public/`
- `audits/step-4-meta-title-h1-cleanup-report.md`

## Фінальний статус

ДОБРЕ
