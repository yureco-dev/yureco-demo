# utylizaciya-dokumentiv rewrite report

- Source page: `utylizaciya-dokumentiv.html`
- Commercial page used for CTA: `https://youreco.com.ua/dokumenty/`
- Rewrite scope: only the target page body and aligned head metadata/Article JSON-LD on the same page
- Files intentionally untouched: other HTML files, `public/`, `sitemap.xml`

## What changed

- Reframed the page into an umbrella/service guide for enterprises about organizing document disposal.
- Removed the confidential-only positioning and template sections like `Що це / Коли потрібно / Що перевірити`.
- Kept the existing full sidebar structure in place.
- Updated robots to `index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1`.
- Preserved Article JSON-LD and aligned it with the rewritten page.
- Removed FAQPage JSON-LD to avoid mismatch with the new non-FAQ body.
- Replaced generic related links with the required document-specific links.
- Rewrote the CTA around clarification of transfer feasibility, without promising unconditional destruction or automatic archival disposal.

## Content intent covered

- How a business organizes document disposal.
- Typical business document groups: archives, accounting, HR, contracts, service papers, drafts, internal materials.
- Why retention period, document status, confidentiality, volume, packaging and supporting paperwork matter.
- How to separate regular paper documents from confidential ones.
- How to prepare a batch for transfer.
- What data to capture before outreach.
- When separate approval is required.

## Validation notes

- Preflight `git status --short --untracked-files=all`: clean before edits.
- HTML structure repaired: yes.
- Cards div added: yes.
- Cards div closed: yes.
- Content changed: no.
- Title/meta/canonical/H1 changed: no.
- CTA changed: no.
- Build: not run.
- Commit/push: not done.
