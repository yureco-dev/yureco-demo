# ЕТАП 8 — Schema JSON-LD, canonical, AI-friendly metadata

- HTML-сторінок перевірено: **244**
- Індексованих сторінок перевірено (canonical URL із sitemap): **51**
- JSON-LD блоків перевірено: **246**
- JSON-LD помилок до виправлення: **142**
- JSON-LD помилок після виправлення: **0**
- Canonical mismatch після виправлення: **0**
- Schema `url` / `mainEntityOfPage` mismatch після виправлення: **0**
- Сторінок із `FAQPage` без видимого FAQ після виправлення: **0**
- URL у sitemap після змін: **51**
- Noindex/redirect URL у sitemap: **ні (0)**
- UTF-8/BOM статус: **UTF-8, BOM не виявлено**
- Кирилиця: **не зіпсована**
- Фінальний статус: **ДОБРЕ**

## Що було зроблено

- Уніфіковано `canonical`, `robots`, `og:url`, `ai-content-url` для всіх HTML.
- Для індексованих сторінок canonical примусово звірено із URL із `sitemap.xml`.
- Для noindex/redirect-сторінок canonical приведено до цільового редирект-URL.
- Повністю нормалізовано JSON-LD:
  - валідний JSON;
  - `@context` = `https://schema.org`;
  - `url` і `mainEntityOfPage` узгоджені з canonical;
  - прибрано дубльовані/конфліктні схеми;
  - типи приведено до єдиної логіки (`CollectionPage` для хабів, `Article` для довідкових сторінок, `FAQPage` лише за наявності видимого FAQ).
- Перегенеровано `public/` командою збірки та повторно перевірено sitemap/кодування/mojibake.

## Перевірки після змін

- `python scripts/build_public.py` → `PUBLIC_BUILD_OK files=251 html=244`
- `python scripts/validate_utf8_mojibake.py` → успішно (0 помилок)
- Додаткова перевірка JSON-LD: `python scripts/step8_verify_jsonld.py` → `JSONLD_ISSUES=0`
- Пошук mojibake-маркерів у `public/*.html` (`Ð`, `Ñ`, `Р°`, `Р±`, `Р В`, `СЂ`, `вЂ`, `�`) → збігів не знайдено

## Змінені файли

- Масово оновлено HTML-сторінки сайту (довідникові, хаби, redirect/noindex): **254 HTML-файли**.
- Повний перелік HTML-файлів зафіксовано у `audits/_stage8_metrics.json` в полі `changed_files`.
- Додатково змінено/додано:
  - `scripts/step8_schema_ai_metadata.py`
  - `scripts/step8_verify_jsonld.py`
  - `audits/_stage8_metrics.json`
  - `audits/_stage8_jsonld_after_issues.txt`
  - `audits/step-8-schema-ai-metadata-report.md`
