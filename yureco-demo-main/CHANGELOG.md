CHANGELOG — guide.youreco.com.ua (deploy ZIP rebuild)

User URL standard enforced:
- shyn
- kosmetyky

Changes (single-pass):
1) Duplicate-title canonization (6 pairs):
   - Converted non-canonical pages to HTML redirect pages (meta refresh + JS) with:
     - meta robots: noindex,follow
     - rel=canonical to the canonical target
   - Canonical targets (kept as content pages):
     - .../kudy-zdaty-kosmetyky.html
     - .../yak-pereroblyayut-kosmetyky.html
     - .../kudy-zdaty-sokiv-ta-napoyiv.html
     - .../yak-pereroblyayut-sokiv-ta-napoyiv.html
     - .../kudy-zdaty-shyn.html
     - .../yak-pereroblyayut-shyn.html

2) Redirect pages handled:
   - guide/li-ion.html and guide/shyny.html are kept (already redirect pages) but:
     - removed from sitemap
     - internal links normalized to point directly to:
       - /utylizaciya-li-ion-batarej.html
       - /utylizaciya-shyn.html

3) Internal link normalization:
   - Updated hrefs across all HTML so internal navigation links point to canonical URLs only.

4) Sitemap cleanup:
   - Removed:
     - 6 non-canonical duplicate URLs
     - li-ion.html and shyny.html
   - Preserved all other URLs.

Artifacts included:
- redirect-map.csv
- validation-report.txt
- sitemap-before.xml
- sitemap-after.xml