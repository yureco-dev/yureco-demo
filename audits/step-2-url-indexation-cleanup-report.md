# ЕТАП 2. Очищення індексації та дублювання URL

Дата перевірки: 2026-04-28

## Production-output

Перевірено HTML-сторінок у `public/`: 244.

Перегенеровано `public/sitemap.xml` через `python3 scripts/build_public.py` після оновлення кореневого `sitemap.xml`.

## Знайдені дубль-групи та основні URL

1. `kudy-zdaty-*` / `utylizaciya-*`
   - Знайдено 67 паралельних `kudy-zdaty-*` URL.
   - Основними залишено відповідні `utylizaciya-[vidhodu].html` URL.
   - Усі `kudy-zdaty-*` дублікати мають 301 redirect у `.htaccess`, `noindex, follow` і canonical на основну сторінку.
   - Загальна сторінка `kudy-zdaty.html` не дублює конкретний B2B-intent і залишена індексованою.

2. Старі транслітераційні варіанти шин
   - `/kudy-zdaty-shin.html` -> `/utylizaciya-shyn.html`
   - `/kudy-zdaty-shyn.html` -> `/utylizaciya-shyn.html`
   - `/kudy-zdaty-shyny.html` -> `/utylizaciya-shyn.html`
   - `/shyny.html` -> `/utylizaciya-shyn.html`
   - `/utylizaciya-shin.html` -> `/utylizaciya-shyn.html`
   - Основний canonical URL: `/utylizaciya-shyn.html`.

3. `kosmetiki` / `kosmetyky`
   - `/kudy-zdaty-kosmetiki.html` -> `/utylizaciya-kosmetyky.html`
   - `/kudy-zdaty-kosmetyky.html` -> `/utylizaciya-kosmetyky.html`
   - `/utylizaciya-kosmetiki.html` -> `/utylizaciya-kosmetyky.html`
   - Основний canonical URL: `/utylizaciya-kosmetyky.html`.

4. Li-ion
   - `/li-ion.html` -> `/utylizaciya-li-ion-batarej.html`
   - `/kudy-zdaty-li-ion-batarej.html` -> `/utylizaciya-li-ion-batarej.html`
   - Основний canonical URL: `/utylizaciya-li-ion-batarej.html`.

5. `pererobka-*` / `utylizaciya-*` з однаковим B2B-intent
   - `/pererobka-metalu.html` переведено в `noindex + canonical` на `/utylizaciya-metalu.html`.
   - `/pererobka-shyn.html` переведено в `noindex + canonical` на `/utylizaciya-shyn.html`.
   - `/pererobka-skla.html` переведено в `noindex + canonical` на `/utylizaciya-skla.html`.
   - `/pererobka-vidpracovanyh-masel.html` переведено в `noindex + canonical` на `/utylizaciya-vidpracovanyh-masel.html`.

6. Дубль "Куди здати відпрацьовану оливу"
   - `/kudy-zdaty-vidpracovane-maslo.html` -> `/utylizaciya-vidpracovanoi-olyvy.html`
   - `/kudy-zdaty-vidpracovanoi-olyvy.html` -> `/utylizaciya-vidpracovanoi-olyvy.html`
   - Основний індексований URL: `/utylizaciya-vidpracovanoi-olyvy.html`.

## Зміни індексаційних сигналів

- 72 redirect/noindex HTML-сторінки отримали canonical на кінцевий основний URL замість self-canonical.
- 4 індексовані `pererobka-*` сторінки з паралельним B2B-intent переведено в `noindex + canonical`.
- Для кожної індексованої сторінки canonical вказує на саму себе.
- Для duplicate/noindex сторінок canonical вказує на основну сторінку.

## Sitemap

Результат перевірки `public/sitemap.xml`:
- URL у sitemap: 141
- noindex URL у sitemap: 0
- redirect URL у sitemap: 0
- індексованих URL з canonical не на себе: 0
- дубль-груп із кількома індексованими URL однакового intent: 0

У sitemap залишені тільки фінальні canonical URL.

## Змінені файли

- `sitemap.xml`
- `public/sitemap.xml`
- `public/.htaccess` оновлено як згенеровану копію
- 67 `kudy-zdaty-*.html` сторінок і їхні копії в `public/`
- `articles/index.html` і `public/articles/index.html`
- `li-ion.html` і `public/li-ion.html`
- `shyny.html` і `public/shyny.html`
- `utylizaciya-kosmetiki.html` і `public/utylizaciya-kosmetiki.html`
- `utylizaciya-shin.html` і `public/utylizaciya-shin.html`
- `pererobka-metalu.html` і `public/pererobka-metalu.html`
- `pererobka-shyn.html` і `public/pererobka-shyn.html`
- `pererobka-skla.html` і `public/pererobka-skla.html`
- `pererobka-vidpracovanyh-masel.html` і `public/pererobka-vidpracovanyh-masel.html`
- `audits/step-2-url-indexation-cleanup-report.md`

## Фінальний статус

ДОБРЕ
