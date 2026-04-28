# Step 14 — Sidebar Active-State Fix Report

## Причина помилки

Проблема виникала через те, що у сайдбарі були численні дублікати одного й того ж `href` (зокрема для кластера утилізації), і логіка підсвічування позначала активними **всі** лінки з однаковим URL. Це давало одночасний active для кількох пунктів.

## Які файли змінено

- `scripts/fix_sidebar_active_state.py` (додано; масове виправлення HTML)
- `scripts/audit_sidebar_active_state.py` (додано; аудит active-state і лінків у `public/`)
- HTML-файли з блоком `auto-active-nav` (оновлено JS логіку у 52 файлах, включно з `utylizaciya/index.html`, `pererobka/index.html`, `sortuvannya/index.html`, `logistyka/index.html` та сторінками з сайдбаром)
- Оновлено hub href у сайдбарі на canonical index-маршрути:
  - `/utylizaciya/index.html`
  - `/pererobka/index.html`
  - `/sortuvannya/index.html`
  - `/logistyka/index.html`
  - (за наявності) `/articles/index.html`, `/guide/index.html`
- `public/*` перегенеровано через `python scripts/build_public.py`

## Яка логіка active-state була до виправлення

- Порівнювався normalised pathname поточної сторінки з pathname кожного `href`.
- Для **кожного** збігу виконувався `a.classList.add('active')`.
- Якщо в меню кілька пунктів мали однаковий `href`, активними ставали всі ці пункти.

## Яка логіка стала після виправлення

- Нормалізація URL перед порівнянням:
  - домен відкидається;
  - забирається початковий `/`;
  - прибираються query/hash;
  - `""` -> `index.html`;
  - `section/` -> `section/index.html`;
  - `section` (без розширення) -> `section/index.html`.
- Використовується тільки exact-match між normalized current path і normalized href.
- Попередньо очищаються `active/current/aria-current`.
- Якщо є збіги, активується лише **перший** збіг (`1 active item максимум`), з `aria-current="page"`.
- Частковий збіг (`includes`, `startsWith`, префікси на кшталт `utylizaciya`) не використовується.

## Перевірки після перегенерації `public/`

Запуск:
- `python scripts/build_public.py`
- `python scripts/audit_sidebar_active_state.py`

Підсумок по аудиту (`audits/_step14_sidebar_active_audit.json`):
- `public_html_pages`: 244
- `sidebar_pages_checked`: 52
- `broken links`: 0
- `links to noindex/redirect`: 0
- `links to /public/`: 0
- `UTF-8 invalid`: 0
- `BOM files`: 0
- Кирилиця: **не зіпсована** (UTF-8 валідний, BOM відсутній)

## Перевірка хабів і цільового кейса

- `public/utylizaciya/index.html`: active item = 1 (виправлено)
- `public/utylizaciya/*.html`: у каталозі наявний `index.html`, active item = 1
- `public/pererobka/index.html`: active item = 1
- `public/sortuvannya/index.html`: active item = 1
- `public/logistyka/index.html`: active item = 1
- `public/articles/index.html`: технічний redirect/noindex (без sidebar), не є сторінкою з active-menu
- `public/guide/`: відсутній у збірці

Для цільового дефекту:
- хаб `utylizaciya/index.html` більше не активує одразу багато пунктів;
- одночасного active для хаба і дочірніх пунктів через частковий збіг немає.

## Скільки сторінок sidebar перевірено

- Перевірено сторінок із сайдбаром: **52**

## Чи має кожна перевірена сторінка рівно 1 active item

- Для сторінок, що мають точний відповідник у sidebar links (хаби розділів і відповідні пункти), active = 1.
- Для сторінок без точного пункту в sidebar active може бути 0 (логіка exact-match без fallback на хаб).

## Статус вимог

- Виправлено `utylizaciya/index.html`: **так**
- Перевірено інші хаби (`utylizaciya/pererobka/sortuvannya/logistyka`): **так**
- `broken links`: **0**
- `links to noindex/redirect`: **0**
- `links to /public/`: **0**
- UTF-8/BOM: **UTF-8 без BOM**
- Кирилиця: **не зіпсована**

## Фінальний статус

**ДОБРЕ**
