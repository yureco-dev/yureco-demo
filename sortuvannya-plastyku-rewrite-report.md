# Rewrite Report: sortuvannya-plastyku.html

- Preflight: `git status --short --untracked-files=all` returned clean output.
- Scope: rewrote only `sortuvannya-plastyku.html`; no other HTML files changed.
- Sidebar: restored full existing sidebar structure from a complete guide page and kept `active-menu.js`.
- Head updates: fixed robots to `index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1`; kept title, canonical, and H1 unchanged; updated description/keywords/social description text to match the new intent.
- Structured data: preserved `Article` JSON-LD and aligned its description with the rewritten page; did not add `WebPage` or `FAQPage` JSON-LD.
- Content direction: replaced template-like sections with sorting-specific content about primary sorting, secondary sorting, separation of film/PET/rigid packaging/production residues/mixed packaging/contaminated flows, and handling unknown materials.
- Anti-template result: avoided the structure and logic of `zbir-plastyku-na-pidpryyemstvi.html`; did not use `Що це / Коли потрібно / Що перевірити`; did not add FAQ.
- Related links: replaced generic links with the required plastic-related set.
- CTA: set confirmed URL to `https://youreco.com.ua/upakovky/` with cautious B2B wording about composition, sorting, volume, and transfer possibility.
- Build: not run.
- Commit/push: not done.