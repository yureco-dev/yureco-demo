# sitemap-add-evidence

## 1. git status --short
```txt
```

## 2. git log --oneline -5
```txt
fd601e1 add missing index urls to sitemap
3a5382e add duplicate and build structure audit reports
7e2f919 update fixed sitemap validation report
7dbff4b add independent sitemap validation checks
8d7331f fix sitemap noindex mismatch
```

## 3. git show --name-only --oneline HEAD
```txt
fd601e1 add missing index urls to sitemap
robots-canonical-audit.md
sitemap-add-index-report.md
sitemap.xml
```

## 4. git show --stat --oneline HEAD
```txt
fd601e1 add missing index urls to sitemap
 robots-canonical-audit.md   |  65 ++++++++++++++++++++++++
 sitemap-add-index-report.md |  56 +++++++++++++++++++++
 sitemap.xml                 | 120 ++++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 241 insertions(+)
```

## 5. git diff HEAD^ HEAD -- sitemap.xml
```diff
diff --git a/sitemap.xml b/sitemap.xml
index b608ff2..0e90bda 100644
--- a/sitemap.xml
+++ b/sitemap.xml
@@ -128,4 +128,124 @@
     <loc>https://guide.youreco.com.ua/zbir.html</loc>
     <lastmod>2026-04-28</lastmod>
   </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/logistyka.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/pererobka.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/sortuvannya.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-dokumentiv.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-gazovanyh-napoyiv.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-kabelyu-ta-drotiv.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-konserviv.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-kosmetyky-magazyniv.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-kosmetyky.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-li-ion-batarej.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-myasnyh-produktiv.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-napoyiv.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-nekondicijnoyi-sirovini.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-odyagu-vzuttya.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-ofisnih-mebliv-orgtehniki.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-paverbankiv-dbj.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-promyslovyh-vidhodiv.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-prostrochenyh-produktiv.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-rybnyh-produktiv.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-shyn.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-sonyachnih-panelij-vitryakiv.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-tary-upakovki.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-tovary-pid-mitnim-kontrolem.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-vidpracovanoi-olyvy.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-zamorozhenyh-produktiv.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya-zipsovanyh-produktiv.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
+  <url>
+    <loc>https://guide.youreco.com.ua/utylizaciya.html</loc>
+    <lastmod>2026-04-28</lastmod>
+  </url>
 </urlset>
```

## 6. git diff --name-only HEAD^ HEAD
```txt
robots-canonical-audit.md
sitemap-add-index-report.md
sitemap.xml
```

## 7. git diff --numstat HEAD^ HEAD
```txt
65	0	robots-canonical-audit.md
56	0	sitemap-add-index-report.md
120	0	sitemap.xml
```

## sitemap-add-index-report.md
```md
# Sitemap Add Index Report

## Summary
- URLs added: 30
- Existing URLs changed: 0
- HTML changed: no
- CSS changed: no
- JS changed: no
- robots.txt changed: no
- public changed: no
- dist changed: no

## Added URLs
- https://guide.youreco.com.ua/logistyka.html
- https://guide.youreco.com.ua/pererobka.html
- https://guide.youreco.com.ua/sortuvannya.html
- https://guide.youreco.com.ua/utylizaciya-dokumentiv.html
- https://guide.youreco.com.ua/utylizaciya-gazovanyh-napoyiv.html
- https://guide.youreco.com.ua/utylizaciya-kabelyu-ta-drotiv.html
- https://guide.youreco.com.ua/utylizaciya-konserviv.html
- https://guide.youreco.com.ua/utylizaciya-kosmetyky-magazyniv.html
- https://guide.youreco.com.ua/utylizaciya-kosmetyky.html
- https://guide.youreco.com.ua/utylizaciya-li-ion-batarej.html
- https://guide.youreco.com.ua/utylizaciya-myasnyh-produktiv.html
- https://guide.youreco.com.ua/utylizaciya-napoyiv.html
- https://guide.youreco.com.ua/utylizaciya-nekondicijnoyi-sirovini.html
- https://guide.youreco.com.ua/utylizaciya-odyagu-vzuttya.html
- https://guide.youreco.com.ua/utylizaciya-ofisnih-mebliv-orgtehniki.html
- https://guide.youreco.com.ua/utylizaciya-paverbankiv-dbj.html
- https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html
- https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html
- https://guide.youreco.com.ua/utylizaciya-promyslovyh-vidhodiv.html
- https://guide.youreco.com.ua/utylizaciya-prostrochenyh-produktiv.html
- https://guide.youreco.com.ua/utylizaciya-rybnyh-produktiv.html
- https://guide.youreco.com.ua/utylizaciya-shyn.html
- https://guide.youreco.com.ua/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
- https://guide.youreco.com.ua/utylizaciya-sonyachnih-panelij-vitryakiv.html
- https://guide.youreco.com.ua/utylizaciya-tary-upakovki.html
- https://guide.youreco.com.ua/utylizaciya-tovary-pid-mitnim-kontrolem.html
- https://guide.youreco.com.ua/utylizaciya-vidpracovanoi-olyvy.html
- https://guide.youreco.com.ua/utylizaciya-zamorozhenyh-produktiv.html
- https://guide.youreco.com.ua/utylizaciya-zipsovanyh-produktiv.html
- https://guide.youreco.com.ua/utylizaciya.html

## Validation
- index pages missing from sitemap after fix: 0
- noindex pages in sitemap after fix: 0
- duplicate loc entries: 0
- sitemap total URLs: 62

## Git Status
```txt
 M sitemap.xml
?? robots-canonical-audit.md
?? sitemap-add-index-report.md
```
```

## robots-canonical-audit.md
```md
# Robots Canonical Audit

## Summary
- root HTML files scanned: 241
- robots.txt found: true
- sitemap directive found: true
- sitemap URL correct: true
- canonical missing: 0
- canonical non-absolute: 0
- canonical wrong domain: 0
- canonical points to public: 0
- index pages missing from sitemap: 0
- noindex pages in sitemap: 0
- robots blocking indexed content: 0
- issues needing fix: 0

## Robots.txt
```txt
User-agent: *
Allow: /

Sitemap: https://guide.youreco.com.ua/sitemap.xml
```

## Canonical Issues
### Canonical missing
- none

### Canonical non-absolute
- none

### Canonical wrong domain
- none

### Canonical points to public
- none

### Canonical points to noindex URL
- none

### Meta robots missing
- none

## Index / Noindex Status
- index: 62
- noindex: 179

## Sitemap Consistency Issues
### Index pages missing from sitemap
- none

### Noindex pages in sitemap
- none

## Robots Blocking Indexed Content
- none

## Recommendation
- fixed

## Git Status
```txt
?? robots-canonical-audit.md
```
```
