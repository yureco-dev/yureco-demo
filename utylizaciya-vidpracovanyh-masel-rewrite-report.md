# Rewrite Report: utylizaciya-vidpracovanyh-masel.html

- Date: 2026-05-20
- Scope: one-pass rewrite of `utylizaciya-vidpracovanyh-masel.html` only
- Commercial page used for fit: `https://youreco.com.ua/olyvy/`

## Preflight

- `git status --short --untracked-files=all` returned clean output before any changes.

## What was changed

- Replaced template-like body content with a category page about used oils / lubricants for business.
- Kept the existing full sidebar structure in place.
- Updated robots to `index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1`.
- Preserved Article JSON-LD and updated its text fields to match the rewritten page.
- Did not add WebPage JSON-LD.
- Did not add FAQPage JSON-LD.
- Replaced the CTA with the required commercial URL only: `https://youreco.com.ua/olyvy/`.
- Kept related links limited to the required list.

## Intent handling

- Positioned the page as a broader category page for used oils / lubricants, not just motor oil.
- Covered the difference between motor, transmission, hydraulic, industrial, and compressor oils.
- Explained why `масла` is broader than a single motor oil flow.
- Focused the page on describing the flow by source, type, impurities, packaging, and volume.
- Included a dedicated section on why oils should not be mixed with antifreeze, fuel, emulsions, or solvents.
- Included a dedicated section on when separate agreement is needed.

## Anti-template check

- Removed generic headings like `Що це`, `Коли потрібно`, and `Що перевірити`.
- Avoided turning the page into a routing page, storage page, transport page, or generic waste page.
- Avoided duplicating the dedicated motor-oil page by keeping this page at category level.
- Used a non-template CTA aligned to preliminary agreement rather than a generic service prompt.

## Validation

- `get_errors` on `utylizaciya-vidpracovanyh-masel.html`: no errors found.
- Manual readback confirmed:
  - sidebar present;
  - required robots meta present;
  - Article JSON-LD present;
  - CTA URL correct;
  - related links match the requested set.

## Not done by design

- No build run.
- No commit.
- No push.
- No edits to other HTML files, `public/`, or `sitemap.xml`.