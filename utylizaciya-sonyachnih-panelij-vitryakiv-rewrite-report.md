# Rewrite Report: utylizaciya-sonyachnih-panelij-vitryakiv.html

- Date: 2026-05-23
- Scope: one-pass rewrite of the source guide page only
- Commercial page used: https://youreco.com.ua/paneli/

## Preflight

- `git status --short --untracked-files=all` returned clean output before any edits.

## What changed

- Rewrote the page body into a renewable-assets service guide for enterprises.
- Preserved the existing full sidebar.
- Preserved Article JSON-LD and updated only `dateModified` to `2026-05-23`.
- Did not add WebPage JSON-LD.
- Did not add FAQPage JSON-LD.
- Updated robots to `index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1`.
- Kept the canonical URL unchanged.
- Kept the page focused on inventory, demolition context, component streams, damage state, storage, documents, logistics, and transfer approval.

## Anti-template checks

- Removed template-like sections such as FAQ and broad equipment framing.
- Avoided duplicating the routing intent of `/kudy-zdaty-sonyachnih-panelij-vitryakiv.html`.
- Avoided reusing generic equipment-block logic.
- Kept batteries only as adjacent components, not the main intent.
- Used a non-template CTA tied only to the approved commercial page.

## CTA checks

- CTA URL: https://youreco.com.ua/paneli/
- CTA phrasing used: `уточнити можливість утилізації сонячних панелей або лопатей ВЕС`.
- CTA copy includes: `узгодити тип обладнання, кількість, стан, демонтаж, габарити, місце зберігання, документи, доступ і логістику`.
- No promise of unconditional acceptance.
- No promise of automatic buyout.

## Validation

- `git diff -- utylizaciya-sonyachnih-panelij-vitryakiv.html` reviewed successfully.
- Search validation confirmed final robots tag, related link, and CTA URL.
- File diagnostics for `utylizaciya-sonyachnih-panelij-vitryakiv.html` reported no errors.

## Minor repair

- HTML structure repaired: yes.
- Restored the missing `<div class="cards">` wrapper inside `<main class="main">`.
- Added the closing `</div>` for `.cards` before `</main>`.
- Content changed: no.
- Title/meta/canonical/H1 changed: no.
- CTA changed: no.
- Build run: no.
- Commit done: no.

## Files changed

- `utylizaciya-sonyachnih-panelij-vitryakiv.html`
- `utylizaciya-sonyachnih-panelij-vitryakiv-rewrite-report.md`

## Not done

- Build not run.
- Commit not created.
- Push not performed.
