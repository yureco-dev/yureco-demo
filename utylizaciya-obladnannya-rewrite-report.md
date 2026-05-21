# utylizaciya-obladnannya rewrite report

## Scope
- Rewritten only `utylizaciya-obladnannya.html`
- Added only `utylizaciya-obladnannya-rewrite-report.md`
- No other HTML files changed
- No build run
- No commit or push

## Preflight
- `git status --short --untracked-files=all` returned clean output before edits

## What changed in `utylizaciya-obladnannya.html`
- Replaced the template-like body with a full source page focused on enterprise equipment disposal workflow
- Preserved the existing full-page sidebar pattern
- Removed `noindex` and set final robots to `index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1`
- Kept canonical, `og:url`, `ai-content-url`, and page URL aligned to `utylizaciya-obladnannya.html`
- Preserved existing `Article` JSON-LD
- Did not add `WebPage` JSON-LD because it was not present in HEAD
- Did not add `FAQPage` JSON-LD
- Kept the existing title, canonical, and H1
- Used only the allowed commercial CTA URL: `https://youreco.com.ua/obladnannya/`

## Content decisions
- Positioned the page as an umbrella/service guide for enterprises about organizing equipment disposal
- Focused on preparation, composition assessment, disconnection, dismantling, accumulation, documents, logistics, and handoff
- Covered business equipment flows as production, warehouse, retail, service, auxiliary, and dismantled equipment
- Explained why routing depends on equipment type, condition, completeness, materials, dimensions, weight, electronics, liquids, oils, batteries, and hazardous modules
- Added guidance on what should be disconnected, dismantled, or separated before handoff
- Added a data-capture table for pre-contact coordination
- Added explicit separate-approval logic for mixed, hazardous, oversized, heavy, or not-yet-disconnected batches
- Avoided promising acceptance of all equipment types or any automatic buyout
- Included only the required related links list

## Anti-template check
- Removed generic headings such as `Що це`, `Коли потрібно`, and `Що перевірити`
- Avoided routing-page framing and avoided turning the page into a generic industrial-waste article
- Avoided duplicating the office equipment page and the industrial-mechanisms page
- CTA wording is specific to clarifying transfer feasibility for equipment disposal
- Final body is a coherent one-pass rewrite, not a mix of old template sections and new copy

## Validation
- `get_errors` on `utylizaciya-obladnannya.html`: no errors found
- Spot-check confirmed:
  - final robots present
  - no `noindex`
  - `Article` JSON-LD present
  - no `WebPage` JSON-LD added
  - no `FAQPage` JSON-LD added
  - CTA points to `https://youreco.com.ua/obladnannya/`
  - sidebar present

## Minor repair
- html structure repaired: так
- cards div added: так
- cards div closed: так
- content changed: ні
- title/meta/canonical/H1 changed: ні
- CTA changed: ні
- build run: ні
- commit done: ні
