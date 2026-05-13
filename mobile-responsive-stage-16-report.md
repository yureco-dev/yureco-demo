files changed:
- styles.css
- mobile-responsive-stage-16-report.md

media queries added:
- @media (max-width: 1024px)
- @media (max-width: 768px)
- @media (max-width: 430px)
- @media (max-width: 390px)

sidebar mobile behavior:
- On mobile widths, .layout switches to a single column.
- .sidebar becomes a full-width top block with position: static and no fixed column sizing.
- .sidebar no longer overlaps .main.

main/content overlap protection:
- .main, main, .card, .intro-card, .links-card, .content, .breadcrumbs, .read-also-grid, and .read-also-item receive max-width/min-width safeguards where relevant.
- Mobile .main/main resets margin-left to 0 and keeps width/max-width at 100%.

table horizontal scroll:
- table has max-width: 100%.
- At max-width 768px, table uses display: block, width: 100%, overflow-x: auto, and -webkit-overflow-scrolling: touch.
- th and td use white-space: nowrap at mobile width so table overflow is controlled by table scroll.
- Global overflow-x: hidden was removed from html/body so responsive issues are not hidden.
- Controlled horizontal overflow remains only on tables.

checked widths:
- 390 px: yes, CSS breakpoint added for overflow protection.
- 430 px: yes, CSS breakpoint added for tighter spacing.
- 768 px: yes, CSS breakpoint added for mobile/tablet layout and table scroll.
- 1024 px: yes, CSS breakpoint added to protect main width.

HTML changed:
- no

JS changed:
- no

sitemap/robots changed:
- no

public/dist changed:
- no

build run:
- no

commit done:
- no

Cyrillic/UTF-8 issues:
- no
