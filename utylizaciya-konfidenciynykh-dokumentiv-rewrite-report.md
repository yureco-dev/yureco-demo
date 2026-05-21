# Rewrite Report: utylizaciya-konfidenciynykh-dokumentiv.html

## Scope
- Rewritten only `utylizaciya-konfidenciynykh-dokumentiv.html`
- Created only `utylizaciya-konfidenciynykh-dokumentiv-rewrite-report.md`
- No other HTML files changed
- No build run
- No commit or push

## What Changed
- Reworked the page around a dedicated sensitive-document flow for confidential documents.
- Preserved the existing sidebar from the full page layout.
- Kept the Article JSON-LD and updated its text fields to match the rewritten page.
- Removed the existing FAQPage JSON-LD because the page should not introduce FAQ structured data.
- Updated robots to `index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1`.
- Replaced template-like sections with page-specific sections about:
  - confidential documents as a separate document stream;
  - personal data, HR files, financial records, contracts, service materials, commercial papers;
  - access level, retention period, batch control, packaging, marking and sealing when needed;
  - avoiding mixing confidential documents with normal paper flow;
  - preparing the batch for transfer;
  - agreeing confirmations and supporting documents;
  - cases that require separate approval.
- Replaced the CTA with the approved commercial destination and wording.

## CTA Check
- URL: `https://youreco.com.ua/dokumenty/`
- CTA text: `уточнити можливість передачі конфіденційних документів на утилізацію`
- CTA copy includes: `узгодити тип документів, рівень конфіденційності, обсяг, пакування, доступ, підтвердження і логістику`
- No promise of unconditional destruction or automatic archive disposal.

## Anti-Template Check
- No `Що це` block
- No `Коли потрібно` block
- No FAQ section/schema carried over as page template
- No routing-page structure
- No umbrella-page duplication

## Validation
- HTML file check: no errors found
- Targeted search confirmed:
  - final robots meta present;
  - CTA URL present;
  - no `noindex`;
  - no `FAQPage`.
