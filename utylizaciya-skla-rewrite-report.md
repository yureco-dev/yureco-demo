# utylizaciya-skla rewrite report

- Date: 2026-05-21
- Source page: `utylizaciya-skla.html`
- Commercial page used in CTA: `https://youreco.com.ua/upakovky/`

## Preflight

- `git status --short --untracked-files=all` returned no output.
- Worktree was clean, so the rewrite proceeded.

## What changed

- Rewrote the body of `utylizaciya-skla.html` as a guide page about glass as a packaging material flow.
- Preserved the existing full sidebar.
- Replaced the routing/template-style structure with glass-specific sections focused on:
  - packaging glass versus non-packaging glass;
  - difference between glass containers, cullet, sheet/technical glass, and mixed glass flow;
  - why color, breakage, residues, caps, labels, and impurities matter;
  - how to prepare a glass batch before transfer;
  - when mixed or doubtful glass requires prior agreement.
- Updated robots to: `index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1`.
- Kept Article JSON-LD and updated its text to match the rewritten page.
- Did not add WebPage JSON-LD.
- Did not add FAQPage JSON-LD.
- Kept the CTA linked only to `https://youreco.com.ua/upakovky/`.

## Constraint check

- Only `utylizaciya-skla.html` was changed.
- Only one new file was created: `utylizaciya-skla-rewrite-report.md`.
- No other HTML files were touched.
- `public/`, `sitemap.xml`, build, commit, and push were not touched.
- Sidebar is present.
- CTA wording uses:
  - "уточнити можливість передачі скляної тари або скляного пакувального потоку";
  - "узгодити тип скла, обсяг, стан, наявність бою, залишки вмісту, формат накопичення і логістику".
- CTA does not promise acceptance of all glass types or automatic buyout.

## Validation

- HTML diagnostics for `utylizaciya-skla.html`: no errors found.
- Verified presence of:
  - required robots meta;
  - existing sidebar;
  - Article JSON-LD only;
  - single commercial CTA URL.