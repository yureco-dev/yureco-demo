# Build Structure Audit

## Summary
- package.json found: no
- build script found: yes (`render.yaml` runs `python3 scripts/build_public.py`)
- deploy config found: yes (`render.yaml`)
- public directory exists: yes
- dist directory exists: yes
- build directory exists: no
- sitemap location: `sitemap.xml`, `public/sitemap.xml`, `dist/sitemap.xml`
- robots location: `robots.txt`, `public/robots.txt`, `dist/robots.txt`, `guide/robots.txt`
- likely production source: `public/` is the deployed publish directory; root HTML files are the build input/source of truth
- confidence: high

## Evidence
- `render.yaml` defines a static Render service with `buildCommand: "python3 scripts/build_public.py"` and `staticPublishPath: ./public`.
- `scripts/build_public.py` says the repository root contains QA/docs/remediation artifacts and copies only production-facing site files into `public/`.
- `scripts/build_public.py` resets `public/`, copies selected root `*.html`, root files (`.htaccess`, `CNAME`, `robots.txt`, `sitemap.xml`, `styles.css`), `img/`, and selected route index files into `public/`.
- No `package.json` was found at repo root, so no npm build script is present.
- No README file was found by `rg --files -g "README*"`.
- `dist/` exists and contains HTML plus `robots.txt` and `sitemap.xml`, but `render.yaml` does not publish `dist/`.

## Root vs Public
- root HTML count: 241
- public HTML count: 174
- matching pairs: 32 exact root/public SHA256 matches
- differences suspected: yes; 138 root/public pairs differ, and 71 root HTML files are missing from `public/`. This matches the build script behavior: it excludes redirect-source pages and modifies some copied HTML by normalizing/inserting the `auto-active-nav` script.

## Recommendation
- use root as source of truth

## Git Status
```text
?? duplicate-canonical-audit.md
?? external-review-evidence.md
```
