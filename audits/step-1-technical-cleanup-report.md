# ЕТАП 1. Технічне очищення деплою

Дата перевірки: 2026-04-28

## Production-output

Залишено єдиний production-output: `public/`.

Поточний деплой налаштований на публікацію `./public`:
- `render.yaml`: `staticPublishPath: ./public`
- `deploy.sh`: перед деплоєм запускає `python3 scripts/build_public.py` і синхронізує `./public/`

HTML-файли з кореня репозиторію залишаються джерелом для збірки, але не є production-output і не синхронізуються в основний деплой напряму.

## Виключено з деплою

На рівні build-скрипта, rsync-деплою та серверних правил заблоковано або виключено:
- `.git/`
- `.vscode/`
- `.env.example`
- `*.ps1`
- `*.md`
- `*.txt`, крім `robots.txt`
- `*.csv`
- службові `*.json`-звіти
- `deploy.sh`
- `CHANGELOG.md`
- службові директорії `__pycache__/`, `docs/`, `scripts/`, `tools/`, `validation/`

Після production build у `public/` не знайдено службових файлів із цього списку.

## Блокування `/public/`

`/public/` заблоковано через `.htaccess`:

```apache
RedirectMatch 403 (?i)^/(public|\.git|\.vscode)(/|$)
```

Також після build не існує вкладеного шляху `public/public`, тому URL виду `/public/index.html` не має окремого production-файлу.

## Robots і Sitemap

`robots.txt` вказує на актуальний sitemap:

```txt
Sitemap: https://guide.youreco.com.ua/sitemap.xml
```

Результат перевірки `public/sitemap.xml`:
- URL у sitemap: 145
- Дублі: 0
- URL з `/public/`: 0
- `noindex` URL: 0
- meta refresh / redirect URL: 0
- missing / 4xx-кандидати за локальними файлами: 0
- placeholder / службові URL: 0

3xx/4xx/noindex URL у sitemap: немає.

## Змінені файли

- `.htaccess`
- `deploy.sh`
- `scripts/build_public.py`
- `audits/step-1-technical-cleanup-report.md`

`public/.htaccess` оновлюється як згенерована копія під час `python3 scripts/build_public.py`.

## Фінальний статус

ДОБРЕ
