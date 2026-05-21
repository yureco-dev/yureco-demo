# Rewrite Report: kudy-zdaty-dokumentiv.html

- Date: 2026-05-21
- Scope: one-pass rewrite of `kudy-zdaty-dokumentiv.html` only
- Commercial page used: `https://youreco.com.ua/dokumenty/`

## What changed

- Replaced redirect/noindex stub with a full HTML routing page.
- Preserved the existing page identity around title, H1 and Article JSON-LD, while correcting canonical and metadata URLs to `kudy-zdaty-dokumentiv.html`.
- Added the existing full-page sidebar pattern from the guide so the page matches the site layout.
- Rewrote body content around document-routing logic for businesses: where to apply, why the route depends on document type/status/confidentiality/logistics, when prior approval is needed, and what data to prepare before contact.
- Kept CTA limited to the allowed commercial URL and used the required wording about clarifying the route and agreeing type, volume, confidentiality, packaging, documents and logistics.
- Added only the required related links:
  - `/utylizaciya-dokumentiv.html`
  - `/utylizaciya-konfidenciynykh-dokumentiv.html`

## Constraint check

- Only changed file: `kudy-zdaty-dokumentiv.html`
- Only created file: `kudy-zdaty-dokumentiv-rewrite-report.md`
- No other HTML touched
- `public/` untouched
- `sitemap.xml` untouched
- No build run
- No commit
- No push

## Metadata and structured data

- Final robots set to: `index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1`
- Article JSON-LD preserved and updated to the correct page URL
- No WebPage JSON-LD added because it was not present before
- No FAQPage JSON-LD added

## Anti-template outcome

- The page is no longer a redirect stub.
- The content is routing-specific, not a generic waste page.
- The structure does not clone the umbrella/service page section-for-section.
- The page does not collapse into a confidentiality-only scenario.
- CTA is custom to the routing intent and does not promise unconditional destruction or automatic archive disposal.