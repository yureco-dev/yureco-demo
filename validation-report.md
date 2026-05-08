# Validation Report

## Result
FAIL

## Critical Failures
None

## Errors
- Git status unavailable: fatal: not a git repository (or any of the parent directories): .git.
- CSV row 2 has 23 columns instead of 15.
- CSV row 3 has 22 columns instead of 15.
- CSV row 4 has 18 columns instead of 15.
- CSV row 5 has 20 columns instead of 15.
- CSV row 6 has 22 columns instead of 15.
- CSV row count mismatch: 5 rows vs 420 HTML files.
- HTML files missing from CSV file_path: 420.
- audit-url-map.md metric mismatch for total_html_files: 5 vs expected 420.
- audit-url-map.md metric mismatch for total_noindex: 2 vs expected 0.
- audit-url-map.md metric mismatch for total_in_sitemap: 5 vs expected 0.

## Warnings
None

## Counts
- HTML files found: 420
- CSV rows: 5
- Sitemap URLs: 62
- Index-like pages: 0
- Noindex pages: 0
- Pages in sitemap: 0
- Noindex pages in sitemap: 0
- Index pages missing from sitemap: 0
- Missing canonical: 0
- Missing H1: 0
- Missing meta description: 0
- Missing visible updated date: 0
- JSON-LD parse errors: 0
- Possible encoding issues: 0

## Files changed or created
```text
git status --short unavailable: fatal: not a git repository (or any of the parent directories): .git
```

## Final decision
AUDIT NEEDS FIXES
