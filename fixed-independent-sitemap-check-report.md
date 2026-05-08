# Fixed Independent Sitemap Check Report

## Result
FAIL

## Scope
Fixed independent verification of sitemap/noindex fix after commit 8d7331f.
This script does not import or rely on validate_url_map.py.

## Critical failures
- Forbidden working tree changes detected or git status failed.

## Errors
None

## Warnings
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-dokumentiv.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-gazovanyh-napoyiv.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-kabelyu-ta-drotiv.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-konserviv.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-kosmetyky.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-kosmetyky-magazyniv.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-li-ion-batarej.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-myasnyh-produktiv.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-napoyiv.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-nekondicijnoyi-sirovini.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-odyagu-vzuttya.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-ofisnih-mebliv-orgtehniki.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-paverbankiv-dbj.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-promyslovyh-vidhodiv.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-prostrochenyh-produktiv.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-rybnyh-produktiv.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-shyn.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-sonyachnih-panelij-vitryakiv.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-tary-upakovki.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-tovary-pid-mitnim-kontrolem.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-vidpracovanoi-olyvy.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-zamorozhenyh-produktiv.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya-zipsovanyh-produktiv.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/logistyka.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/pererobka.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/sortuvannya.html
- Conflicting robots for duplicate URL: https://guide.youreco.com.ua/utylizaciya.html
- Some index-like URLs are missing from sitemap.xml. Review duplicates/service files manually.

## Counts
- HTML files scanned: 420
- Unique canonical/page URLs: 171
- Sitemap loc URLs: 32
- Noindex HTML files: 296
- Noindex unique URLs: 139
- Noindex URLs still in sitemap: 0
- Index-like unique URLs missing from sitemap: 30
- Duplicate sitemap loc entries: 0
- Sitemap loc without matching HTML/canonical: 0
- Duplicate canonical URLs: 170
- Possible Cyrillic encoding issues: 0

## Commit 8d7331f verification
- Commit found: yes
- Files changed in commit:
- audit-url-map.csv
- audit-url-map.md
- sitemap-noindex-fix-report.md
- sitemap.xml
- validate_url_map.py
- validation-report.md
- HTML changed: False
- CSS changed: False
- JS changed: False
- robots.txt changed: False
- images changed: False
- sitemap.xml changed: True
- forbidden files changed: False

## Sitemap diff verification
- URL blocks removed: 30
- URL blocks added: 0
- Added URLs:
None
- Removed URLs:
- https://guide.youreco.com.ua/logistyka.html
- https://guide.youreco.com.ua/pererobka.html
- https://guide.youreco.com.ua/sortuvannya.html
- https://guide.youreco.com.ua/utylizaciya-gazovanyh-napoyiv.html
- https://guide.youreco.com.ua/utylizaciya-kosmetyky-magazyniv.html
- https://guide.youreco.com.ua/utylizaciya-kosmetyky.html
- https://guide.youreco.com.ua/utylizaciya-li-ion-batarej.html
- https://guide.youreco.com.ua/utylizaciya-shyn.html
- https://guide.youreco.com.ua/utylizaciya-promyslovyh-vidhodiv.html
- https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html
- https://guide.youreco.com.ua/utylizaciya-kabelyu-ta-drotiv.html
- https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html
- https://guide.youreco.com.ua/utylizaciya-prostrochenyh-produktiv.html
- https://guide.youreco.com.ua/utylizaciya-paverbankiv-dbj.html
- https://guide.youreco.com.ua/utylizaciya-ofisnih-mebliv-orgtehniki.html
- https://guide.youreco.com.ua/utylizaciya-sonyachnih-panelij-vitryakiv.html
- https://guide.youreco.com.ua/utylizaciya-vidpracovanoi-olyvy.html
- https://guide.youreco.com.ua/utylizaciya-tary-upakovki.html
- https://guide.youreco.com.ua/utylizaciya-tovary-pid-mitnim-kontrolem.html
- https://guide.youreco.com.ua/utylizaciya-nekondicijnoyi-sirovini.html
- https://guide.youreco.com.ua/utylizaciya-dokumentiv.html
- https://guide.youreco.com.ua/utylizaciya-konserviv.html
- https://guide.youreco.com.ua/utylizaciya-odyagu-vzuttya.html
- https://guide.youreco.com.ua/utylizaciya-myasnyh-produktiv.html
- https://guide.youreco.com.ua/utylizaciya-napoyiv.html
- https://guide.youreco.com.ua/utylizaciya-rybnyh-produktiv.html
- https://guide.youreco.com.ua/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
- https://guide.youreco.com.ua/utylizaciya-zamorozhenyh-produktiv.html
- https://guide.youreco.com.ua/utylizaciya-zipsovanyh-produktiv.html
- https://guide.youreco.com.ua/utylizaciya.html
- Suspicious additions: no

## Remaining noindex URLs in sitemap
None

## Index-like URLs missing from sitemap
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

## Duplicate sitemap loc entries
None

## Sitemap loc without matching HTML/canonical
None

## Duplicate canonical URLs
- https://guide.youreco.com.ua/404.html :: 404.html | public/404.html
- https://guide.youreco.com.ua/akt-pryimannya-peredachi.html :: akt-pryimannya-peredachi.html | public/akt-pryimannya-peredachi.html
- https://guide.youreco.com.ua/akt-utylizaciyi.html :: akt-utylizaciyi.html | public/akt-utylizaciyi.html
- https://guide.youreco.com.ua/chy-potribno-pererobyty-chy-utylizuvaty.html :: chy-potribno-pererobyty-chy-utylizuvaty.html | public/chy-potribno-pererobyty-chy-utylizuvaty.html
- https://guide.youreco.com.ua/dokumenty-dlya-utylizaciyi-vidhodiv.html :: dokumenty-dlya-utylizaciyi-vidhodiv.html | public/dokumenty-dlya-utylizaciyi-vidhodiv.html
- https://guide.youreco.com.ua/dokumenty.html :: dokumenty.html | public/dokumenty.html
- https://guide.youreco.com.ua/fotozvit-utylizaciyi.html :: fotozvit-utylizaciyi.html | public/fotozvit-utylizaciyi.html
- https://guide.youreco.com.ua :: index.html | public/index.html
- https://guide.youreco.com.ua/kabelni-vidhody.html :: kabelni-vidhody.html | public/kabelni-vidhody.html
- https://guide.youreco.com.ua/kontakty.html :: kontakty.html | public/kontakty.html
- https://guide.youreco.com.ua/utylizaciya-avtoshyn.html :: kudy-zdaty-avtoshyn.html | public/utylizaciya-avtoshyn.html | utylizaciya-avtoshyn.html
- https://guide.youreco.com.ua/utylizaciya-budivelnyh-vidhodiv.html :: kudy-zdaty-budivelnyh-vidhodiv.html | public/utylizaciya-budivelnyh-vidhodiv.html | utylizaciya-budivelnyh-vidhodiv.html
- https://guide.youreco.com.ua/utylizaciya-derevyny-z-budivnyctva.html :: kudy-zdaty-derevyny-z-budivnyctva.html | public/utylizaciya-derevyny-z-budivnyctva.html | utylizaciya-derevyny-z-budivnyctva.html
- https://guide.youreco.com.ua/utylizaciya-dokumentiv.html :: kudy-zdaty-dokumentiv.html | public/utylizaciya-dokumentiv.html | utylizaciya-dokumentiv.html
- https://guide.youreco.com.ua/utylizaciya-energetychnyh-napoyiv.html :: kudy-zdaty-energetychnyh-napoyiv.html | public/utylizaciya-energetychnyh-napoyiv.html | utylizaciya-energetychnyh-napoyiv.html
- https://guide.youreco.com.ua/utylizaciya-fruktiv-ta-ovochiv.html :: kudy-zdaty-fruktiv-ta-ovochiv.html | public/utylizaciya-fruktiv-ta-ovochiv.html | utylizaciya-fruktiv-ta-ovochiv.html
- https://guide.youreco.com.ua/utylizaciya-fruktiv.html :: kudy-zdaty-fruktiv.html | public/utylizaciya-fruktiv.html | utylizaciya-fruktiv.html
- https://guide.youreco.com.ua/utylizaciya-gazovanyh-napoyiv.html :: kudy-zdaty-gazovanyh-napoyiv.html | public/utylizaciya-gazovanyh-napoyiv.html | utylizaciya-gazovanyh-napoyiv.html
- https://guide.youreco.com.ua/utylizaciya-gipsokartonu.html :: kudy-zdaty-gipsokartonu.html | public/utylizaciya-gipsokartonu.html | utylizaciya-gipsokartonu.html
- https://guide.youreco.com.ua/utylizaciya-harchovyh-produktiv.html :: kudy-zdaty-harchovyh-produktiv.html | public/utylizaciya-harchovyh-produktiv.html | utylizaciya-harchovyh-produktiv.html
- https://guide.youreco.com.ua/utylizaciya-kabelyu-ta-drotiv.html :: kudy-zdaty-kabelyu-ta-drotiv.html | public/utylizaciya-kabelyu-ta-drotiv.html | utylizaciya-kabelyu-ta-drotiv.html
- https://guide.youreco.com.ua/utylizaciya-kondyterskyh-vyrobiv.html :: kudy-zdaty-kondyterskyh-vyrobiv.html | public/utylizaciya-kondyterskyh-vyrobiv.html | utylizaciya-kondyterskyh-vyrobiv.html
- https://guide.youreco.com.ua/utylizaciya-konserviv.html :: kudy-zdaty-konserviv.html | public/utylizaciya-konserviv.html | utylizaciya-konserviv.html
- https://guide.youreco.com.ua/utylizaciya-kosmetyky.html :: kudy-zdaty-kosmetiki.html | kudy-zdaty-kosmetyky.html | public/utylizaciya-kosmetyky.html | utylizaciya-kosmetiki.html | utylizaciya-kosmetyky.html
- https://guide.youreco.com.ua/utylizaciya-kosmetyky-magazyniv.html :: kudy-zdaty-kosmetyky-magazyniv.html | public/utylizaciya-kosmetyky-magazyniv.html | utylizaciya-kosmetyky-magazyniv.html
- https://guide.youreco.com.ua/utylizaciya-li-ion-batarej.html :: kudy-zdaty-li-ion-batarej.html | li-ion.html | public/utylizaciya-li-ion-batarej.html | utylizaciya-li-ion-batarej.html
- https://guide.youreco.com.ua/utylizaciya-materialiv.html :: kudy-zdaty-materialiv.html | public/utylizaciya-materialiv.html | utylizaciya-materialiv.html
- https://guide.youreco.com.ua/utylizaciya-metalevoyi-strushky.html :: kudy-zdaty-metalevoyi-strushky.html | public/utylizaciya-metalevoyi-strushky.html | utylizaciya-metalevoyi-strushky.html
- https://guide.youreco.com.ua/utylizaciya-metalu.html :: kudy-zdaty-metalu.html | public/utylizaciya-metalu.html | utylizaciya-metalu.html
- https://guide.youreco.com.ua/utylizaciya-molochnyh-produktiv.html :: kudy-zdaty-molochnyh-produktiv.html | public/utylizaciya-molochnyh-produktiv.html | utylizaciya-molochnyh-produktiv.html
- https://guide.youreco.com.ua/utylizaciya-myasnyh-produktiv.html :: kudy-zdaty-myasnyh-produktiv.html | public/utylizaciya-myasnyh-produktiv.html | utylizaciya-myasnyh-produktiv.html
- https://guide.youreco.com.ua/utylizaciya-napivfabrykatyv.html :: kudy-zdaty-napivfabrykatyv.html | public/utylizaciya-napivfabrykatyv.html | utylizaciya-napivfabrykatyv.html
- https://guide.youreco.com.ua/utylizaciya-napoyiv.html :: kudy-zdaty-napoyiv.html | public/utylizaciya-napoyiv.html | utylizaciya-napoyiv.html
- https://guide.youreco.com.ua/utylizaciya-nekondicijnoyi-sirovini.html :: kudy-zdaty-nekondicijnoyi-sirovini.html | public/utylizaciya-nekondicijnoyi-sirovini.html | utylizaciya-nekondicijnoyi-sirovini.html
- https://guide.youreco.com.ua/utylizaciya-nekondyciynoyi-produkciyi.html :: kudy-zdaty-nekondyciynoyi-produkciyi.html | public/utylizaciya-nekondyciynoyi-produkciyi.html | utylizaciya-nekondyciynoyi-produkciyi.html
- https://guide.youreco.com.ua/utylizaciya-obladnannya.html :: kudy-zdaty-obladnannya.html | public/utylizaciya-obladnannya.html | utylizaciya-obladnannya.html
- https://guide.youreco.com.ua/utylizaciya-odyagu-vzuttya.html :: kudy-zdaty-odyagu-vzuttya.html | public/utylizaciya-odyagu-vzuttya.html | utylizaciya-odyagu-vzuttya.html
- https://guide.youreco.com.ua/utylizaciya-ofisnih-mebliv-orgtehniki.html :: kudy-zdaty-ofisnih-mebliv-orgtehniki.html | public/utylizaciya-ofisnih-mebliv-orgtehniki.html | utylizaciya-ofisnih-mebliv-orgtehniki.html
- https://guide.youreco.com.ua/utylizaciya-ovochiv.html :: kudy-zdaty-ovochiv.html | public/utylizaciya-ovochiv.html | utylizaciya-ovochiv.html
- https://guide.youreco.com.ua/utylizaciya-paperu-ta-kartonu.html :: kudy-zdaty-paperu-ta-kartonu.html | public/utylizaciya-paperu-ta-kartonu.html | utylizaciya-paperu-ta-kartonu.html
- https://guide.youreco.com.ua/utylizaciya-parfumeriyi.html :: kudy-zdaty-parfumeriyi.html | public/utylizaciya-parfumeriyi.html | utylizaciya-parfumeriyi.html
- https://guide.youreco.com.ua/utylizaciya-partiyi-produktiv.html :: kudy-zdaty-partiyi-produktiv.html | public/utylizaciya-partiyi-produktiv.html | utylizaciya-partiyi-produktiv.html
- https://guide.youreco.com.ua/utylizaciya-paverbankiv-dbj.html :: kudy-zdaty-paverbankiv-dbj.html | public/utylizaciya-paverbankiv-dbj.html | utylizaciya-paverbankiv-dbj.html
- https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html :: kudy-zdaty-plastyku-ta-polimeriv.html | public/utylizaciya-plastyku-ta-polimeriv.html | utylizaciya-plastyku-ta-polimeriv.html
- https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html :: kudy-zdaty-produktiv-harchuvannya-napoyiv.html | public/utylizaciya-produktiv-harchuvannya-napoyiv.html | utylizaciya-produktiv-harchuvannya-napoyiv.html
- https://guide.youreco.com.ua/utylizaciya-produktiv-na-skladi.html :: kudy-zdaty-produktiv-na-skladi.html | public/utylizaciya-produktiv-na-skladi.html | utylizaciya-produktiv-na-skladi.html
- https://guide.youreco.com.ua/utylizaciya-promyslovogo-obladnannya-mehanizmiv.html :: kudy-zdaty-promyslovogo-obladnannya-mehanizmiv.html | public/utylizaciya-promyslovogo-obladnannya-mehanizmiv.html | utylizaciya-promyslovogo-obladnannya-mehanizmiv.html
- https://guide.youreco.com.ua/utylizaciya-promyslovyh-vidhodiv.html :: kudy-zdaty-promyslovyh-vidhodiv.html | public/utylizaciya-promyslovyh-vidhodiv.html | utylizaciya-promyslovyh-vidhodiv.html
- https://guide.youreco.com.ua/utylizaciya-prostrochenoyi-kosmetyky.html :: kudy-zdaty-prostrochenoyi-kosmetyky.html | public/utylizaciya-prostrochenoyi-kosmetyky.html | utylizaciya-prostrochenoyi-kosmetyky.html
- https://guide.youreco.com.ua/utylizaciya-prostrochenyh-produktiv.html :: kudy-zdaty-prostrochenyh-produktiv.html | public/utylizaciya-prostrochenyh-produktiv.html | utylizaciya-prostrochenyh-produktiv.html
- https://guide.youreco.com.ua/utylizaciya-pyva.html :: kudy-zdaty-pyva.html | public/utylizaciya-pyva.html | utylizaciya-pyva.html
- https://guide.youreco.com.ua/utylizaciya-rybnyh-produktiv.html :: kudy-zdaty-rybnyh-produktiv.html | public/utylizaciya-rybnyh-produktiv.html | utylizaciya-rybnyh-produktiv.html
- https://guide.youreco.com.ua/utylizaciya-shyn.html :: kudy-zdaty-shin.html | kudy-zdaty-shyn.html | kudy-zdaty-shyny.html | public/utylizaciya-shyn.html | shyny.html | utylizaciya-shin.html | utylizaciya-shyn.html
- https://guide.youreco.com.ua/utylizaciya-shyn-pidpryyemstvamy.html :: kudy-zdaty-shyn-pidpryyemstvamy.html | public/utylizaciya-shyn-pidpryyemstvamy.html | utylizaciya-shyn-pidpryyemstvamy.html
- https://guide.youreco.com.ua/utylizaciya-skla.html :: kudy-zdaty-skla.html | public/utylizaciya-skla.html | utylizaciya-skla.html
- https://guide.youreco.com.ua/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html :: kudy-zdaty-skladskyh-zalyshkiv-kosmetyky.html | public/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html | utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
- https://guide.youreco.com.ua/utylizaciya-skladskyh-zalyshkiv.html :: kudy-zdaty-skladskyh-zalyshkiv.html | public/utylizaciya-skladskyh-zalyshkiv.html | utylizaciya-skladskyh-zalyshkiv.html
- https://guide.youreco.com.ua/utylizaciya-sokiv-ta-napoyiv.html :: kudy-zdaty-sokiv-ta-napoyiv.html | public/utylizaciya-sokiv-ta-napoyiv.html | utylizaciya-sokiv-ta-napoyiv.html
- https://guide.youreco.com.ua/utylizaciya-sokiv.html :: kudy-zdaty-sokiv.html | public/utylizaciya-sokiv.html | utylizaciya-sokiv.html
- https://guide.youreco.com.ua/utylizaciya-sonyachnih-panelij-vitryakiv.html :: kudy-zdaty-sonyachnih-panelij-vitryakiv.html | public/utylizaciya-sonyachnih-panelij-vitryakiv.html | utylizaciya-sonyachnih-panelij-vitryakiv.html
- https://guide.youreco.com.ua/utylizaciya-tary-upakovki.html :: kudy-zdaty-tary-upakovki.html | public/utylizaciya-tary-upakovki.html | utylizaciya-tary-upakovki.html
- https://guide.youreco.com.ua/utylizaciya-tovariv.html :: kudy-zdaty-tovariv.html | public/utylizaciya-tovariv.html | utylizaciya-tovariv.html
- https://guide.youreco.com.ua/utylizaciya-tovary-pid-mitnim-kontrolem.html :: kudy-zdaty-tovary-pid-mitnim-kontrolem.html | public/utylizaciya-tovary-pid-mitnim-kontrolem.html | utylizaciya-tovary-pid-mitnim-kontrolem.html
- https://guide.youreco.com.ua/utylizaciya-upakovky-na-pidpryyemstvi.html :: kudy-zdaty-upakovky-na-pidpryyemstvi.html | public/utylizaciya-upakovky-na-pidpryyemstvi.html | utylizaciya-upakovky-na-pidpryyemstvi.html
- https://guide.youreco.com.ua/utylizaciya-upakovky-vid-kosmetyky.html :: kudy-zdaty-upakovky-vid-kosmetyky.html | public/utylizaciya-upakovky-vid-kosmetyky.html | utylizaciya-upakovky-vid-kosmetyky.html
- https://guide.youreco.com.ua/utylizaciya-vantazhnyh-shyn.html :: kudy-zdaty-vantazhnyh-shyn.html | public/utylizaciya-vantazhnyh-shyn.html | utylizaciya-vantazhnyh-shyn.html
- https://guide.youreco.com.ua/utylizaciya-vidpracovanoi-olyvy.html :: kudy-zdaty-vidpracovane-maslo.html | kudy-zdaty-vidpracovanoi-olyvy.html | public/utylizaciya-vidpracovanoi-olyvy.html | utylizaciya-vidpracovanoi-olyvy.html
- https://guide.youreco.com.ua/utylizaciya-vidpracovanyh-masel.html :: kudy-zdaty-vidpracovanyh-masel.html | public/utylizaciya-vidpracovanyh-masel.html | utylizaciya-vidpracovanyh-masel.html
- https://guide.youreco.com.ua/utylizaciya-vody.html :: kudy-zdaty-vody.html | public/utylizaciya-vody.html | utylizaciya-vody.html
- https://guide.youreco.com.ua/utylizaciya-vyrobnychyh-vidhodiv.html :: kudy-zdaty-vyrobnychyh-vidhodiv.html | public/utylizaciya-vyrobnychyh-vidhodiv.html | utylizaciya-vyrobnychyh-vidhodiv.html
- https://guide.youreco.com.ua/utylizaciya-yagid.html :: kudy-zdaty-yagid.html | public/utylizaciya-yagid.html | utylizaciya-yagid.html
- https://guide.youreco.com.ua/utylizaciya-zamorozhenyh-produktiv.html :: kudy-zdaty-zamorozhenyh-produktiv.html | public/utylizaciya-zamorozhenyh-produktiv.html | utylizaciya-zamorozhenyh-produktiv.html
- https://guide.youreco.com.ua/utylizaciya-zipsovanyh-produktiv.html :: kudy-zdaty-zipsovanyh-produktiv.html | public/utylizaciya-zipsovanyh-produktiv.html | utylizaciya-zipsovanyh-produktiv.html
- https://guide.youreco.com.ua/kudy-zdaty.html :: kudy-zdaty.html | public/kudy-zdaty.html
- https://guide.youreco.com.ua/likvidaciya-skladskykh-zalyshkiv.html :: likvidaciya-skladskykh-zalyshkiv.html | public/likvidaciya-skladskykh-zalyshkiv.html
- https://guide.youreco.com.ua/logistyka-budivelnyh-vidhodiv.html :: logistyka-budivelnyh-vidhodiv.html | public/logistyka-budivelnyh-vidhodiv.html
- https://guide.youreco.com.ua/logistyka-kabelyu.html :: logistyka-kabelyu.html | public/logistyka-kabelyu.html
- https://guide.youreco.com.ua/logistyka-metalu.html :: logistyka-metalu.html | public/logistyka-metalu.html
- https://guide.youreco.com.ua/logistyka-paperu-ta-kartonu.html :: logistyka-paperu-ta-kartonu.html | public/logistyka-paperu-ta-kartonu.html
- https://guide.youreco.com.ua/logistyka-plastyku.html :: logistyka-plastyku.html | public/logistyka-plastyku.html
- https://guide.youreco.com.ua/logistyka-promyslovyh-vidhodiv.html :: logistyka-promyslovyh-vidhodiv.html | public/logistyka-promyslovyh-vidhodiv.html
- https://guide.youreco.com.ua/logistyka-shyn.html :: logistyka-shyn.html | public/logistyka-shyn.html
- https://guide.youreco.com.ua/logistyka-skla.html :: logistyka-skla.html | public/logistyka-skla.html
- https://guide.youreco.com.ua/logistyka.html :: logistyka.html | logistyka/index.html | public/logistyka.html | public/logistyka/index.html
- https://guide.youreco.com.ua/nebezpeka-vidpracovanogo-masla.html :: nebezpeka-vidpracovanogo-masla.html | public/nebezpeka-vidpracovanogo-masla.html
- https://guide.youreco.com.ua/oblik-promyslovyh-vidhodiv.html :: oblik-promyslovyh-vidhodiv.html | public/oblik-promyslovyh-vidhodiv.html
- https://guide.youreco.com.ua/optymizaciya-vidhodiv-na-vyrobnyctvi.html :: optymizaciya-vidhodiv-na-vyrobnyctvi.html | public/optymizaciya-vidhodiv-na-vyrobnyctvi.html
- https://guide.youreco.com.ua/pererobka-alyuminiyevogo-kabelyu.html :: pererobka-alyuminiyevogo-kabelyu.html | public/pererobka-alyuminiyevogo-kabelyu.html
- https://guide.youreco.com.ua/pererobka-avtomobilnyh-shyn.html :: pererobka-avtomobilnyh-shyn.html | public/pererobka-avtomobilnyh-shyn.html
- https://guide.youreco.com.ua/pererobka-betonu.html :: pererobka-betonu.html | public/pererobka-betonu.html
- https://guide.youreco.com.ua/pererobka-cegly.html :: pererobka-cegly.html | public/pererobka-cegly.html
- https://guide.youreco.com.ua/pererobka-gumovyh-vyrobiv.html :: pererobka-gumovyh-vyrobiv.html | public/pererobka-gumovyh-vyrobiv.html
- https://guide.youreco.com.ua/pererobka-izolyaciyi-kabelyu.html :: pererobka-izolyaciyi-kabelyu.html | public/pererobka-izolyaciyi-kabelyu.html
- https://guide.youreco.com.ua/pererobka-kartonu.html :: pererobka-kartonu.html | public/pererobka-kartonu.html
- https://guide.youreco.com.ua/pererobka-makulatury.html :: pererobka-makulatury.html | public/pererobka-makulatury.html
- https://guide.youreco.com.ua/pererobka-metalu.html :: pererobka-metalu.html | public/pererobka-metalu.html
- https://guide.youreco.com.ua/pererobka-midnogo-kabelyu.html :: pererobka-midnogo-kabelyu.html | public/pererobka-midnogo-kabelyu.html
- https://guide.youreco.com.ua/pererobka-pet.html :: pererobka-pet.html | public/pererobka-pet.html
- https://guide.youreco.com.ua/pererobka-plastykovoyi-upakovky.html :: pererobka-plastykovoyi-upakovky.html | public/pererobka-plastykovoyi-upakovky.html
- https://guide.youreco.com.ua/pererobka-polietylenu.html :: pererobka-polietylenu.html | public/pererobka-polietylenu.html
- https://guide.youreco.com.ua/pererobka-polipropylenu.html :: pererobka-polipropylenu.html | public/pererobka-polipropylenu.html
- https://guide.youreco.com.ua/pererobka-polistyrolu.html :: pererobka-polistyrolu.html | public/pererobka-polistyrolu.html
- https://guide.youreco.com.ua/pererobka-shyn.html :: pererobka-shyn.html | public/pererobka-shyn.html
- https://guide.youreco.com.ua/pererobka-skla.html :: pererobka-skla.html | public/pererobka-skla.html
- https://guide.youreco.com.ua/pererobka-vidpracovanyh-masel.html :: pererobka-vidpracovanyh-masel.html | public/pererobka-vidpracovanyh-masel.html
- https://guide.youreco.com.ua/pererobka.html :: pererobka.html | pererobka/index.html | public/pererobka.html | public/pererobka/index.html
- https://guide.youreco.com.ua/plastyk-yak-vtorynna-syrovyna.html :: plastyk-yak-vtorynna-syrovyna.html | public/plastyk-yak-vtorynna-syrovyna.html
- https://guide.youreco.com.ua/plastykovi-vidhody.html :: plastykovi-vidhody.html | public/plastykovi-vidhody.html
- https://guide.youreco.com.ua/podribnennya-shyn-gumova-kryshka.html :: podribnennya-shyn-gumova-kryshka.html | public/podribnennya-shyn-gumova-kryshka.html
- https://guide.youreco.com.ua/povernennya-tovariv-z-merezhi.html :: povernennya-tovariv-z-merezhi.html | public/povernennya-tovariv-z-merezhi.html
- https://guide.youreco.com.ua/promyslovi-vidhody-na-pidpryyemstvi.html :: promyslovi-vidhody-na-pidpryyemstvi.html | public/promyslovi-vidhody-na-pidpryyemstvi.html
- https://guide.youreco.com.ua/promyslovi-vidhody.html :: promyslovi-vidhody.html | public/promyslovi-vidhody.html
- https://guide.youreco.com.ua/pryjom-kabelyu-na-utylizaciyu.html :: pryjom-kabelyu-na-utylizaciyu.html | public/pryjom-kabelyu-na-utylizaciyu.html
- https://guide.youreco.com.ua/reestr-partiyi.html :: public/reestr-partiyi.html | reestr-partiyi.html
- https://guide.youreco.com.ua/scenarii-utilizaciyi.html :: public/scenarii-utilizaciyi.html | scenarii-utilizaciyi.html
- https://guide.youreco.com.ua/shcho-take-pererobka-vidhodiv.html :: public/shcho-take-pererobka-vidhodiv.html | shcho-take-pererobka-vidhodiv.html
- https://guide.youreco.com.ua/shcho-take-promyslovi-vidhody.html :: public/shcho-take-promyslovi-vidhody.html | shcho-take-promyslovi-vidhody.html
- https://guide.youreco.com.ua/shcho-take-utylizaciya.html :: public/shcho-take-utylizaciya.html | shcho-take-utylizaciya.html
- https://guide.youreco.com.ua/shcho-take-znyshchennya-produkciyi.html :: public/shcho-take-znyshchennya-produkciyi.html | shcho-take-znyshchennya-produkciyi.html
- https://guide.youreco.com.ua/skilky-koshtuye-pererobka-kabelyu.html :: public/skilky-koshtuye-pererobka-kabelyu.html | skilky-koshtuye-pererobka-kabelyu.html
- https://guide.youreco.com.ua/skladuvannya-promyslovyh-vidhodiv.html :: public/skladuvannya-promyslovyh-vidhodiv.html | skladuvannya-promyslovyh-vidhodiv.html
- https://guide.youreco.com.ua/sortuvannya-budivelnyh-vidhodiv.html :: public/sortuvannya-budivelnyh-vidhodiv.html | sortuvannya-budivelnyh-vidhodiv.html
- https://guide.youreco.com.ua/sortuvannya-plastyku.html :: public/sortuvannya-plastyku.html | sortuvannya-plastyku.html
- https://guide.youreco.com.ua/sortuvannya-promyslovyh-vidhodiv.html :: public/sortuvannya-promyslovyh-vidhodiv.html | sortuvannya-promyslovyh-vidhodiv.html
- https://guide.youreco.com.ua/sortuvannya.html :: public/sortuvannya.html | public/sortuvannya/index.html | sortuvannya.html | sortuvannya/index.html
- https://guide.youreco.com.ua/spysannya-kosmetychnyh-tovariv.html :: public/spysannya-kosmetychnyh-tovariv.html | spysannya-kosmetychnyh-tovariv.html
- https://guide.youreco.com.ua/spysannya-produkciyi.html :: public/spysannya-produkciyi.html | spysannya-produkciyi.html
- https://guide.youreco.com.ua/spysannya-produktiv.html :: public/spysannya-produktiv.html | spysannya-produktiv.html
- https://guide.youreco.com.ua/transportuvannya-vidpracovanyh-masel.html :: public/transportuvannya-vidpracovanyh-masel.html | transportuvannya-vidpracovanyh-masel.html
- https://guide.youreco.com.ua/transportuvannya-vidpracovanyh-shyn.html :: public/transportuvannya-vidpracovanyh-shyn.html | transportuvannya-vidpracovanyh-shyn.html
- https://guide.youreco.com.ua/utilizaciya-brakovanoi-produkciyi.html :: public/utilizaciya-brakovanoi-produkciyi.html | utilizaciya-brakovanoi-produkciyi.html
- https://guide.youreco.com.ua/utilizaciya-dlya-bankiv.html :: public/utilizaciya-dlya-bankiv.html | utilizaciya-dlya-bankiv.html
- https://guide.youreco.com.ua/utilizaciya-dlya-data-centriv.html :: public/utilizaciya-dlya-data-centriv.html | utilizaciya-dlya-data-centriv.html
- https://guide.youreco.com.ua/utilizaciya-dlya-importeriv.html :: public/utilizaciya-dlya-importeriv.html | utilizaciya-dlya-importeriv.html
- https://guide.youreco.com.ua/utilizaciya-dlya-riteylu.html :: public/utilizaciya-dlya-riteylu.html | utilizaciya-dlya-riteylu.html
- https://guide.youreco.com.ua/utilizaciya-dlya-skladiv.html :: public/utilizaciya-dlya-skladiv.html | utilizaciya-dlya-skladiv.html
- https://guide.youreco.com.ua/utilizaciya-dlya-vyrobnyctva.html :: public/utilizaciya-dlya-vyrobnyctva.html | utilizaciya-dlya-vyrobnyctva.html
- https://guide.youreco.com.ua/utylizaciya-akumulyatoriv.html :: public/utylizaciya-akumulyatoriv.html | utylizaciya-akumulyatoriv.html
- https://guide.youreco.com.ua/utylizaciya-elektroniky.html :: public/utylizaciya-elektroniky.html | utylizaciya-elektroniky.html
- https://guide.youreco.com.ua/utylizaciya-importnyh-tovariv.html :: public/utylizaciya-importnyh-tovariv.html | utylizaciya-importnyh-tovariv.html
- https://guide.youreco.com.ua/utylizaciya-konfidenciynykh-dokumentiv.html :: public/utylizaciya-konfidenciynykh-dokumentiv.html | utylizaciya-konfidenciynykh-dokumentiv.html
- https://guide.youreco.com.ua/utylizaciya.html :: public/utylizaciya.html | public/utylizaciya/index.html | utylizaciya.html | utylizaciya/index.html
- https://guide.youreco.com.ua/vidhody-demontazhu.html :: public/vidhody-demontazhu.html | vidhody-demontazhu.html
- https://guide.youreco.com.ua/vidhody-gumy.html :: public/vidhody-gumy.html | vidhody-gumy.html
- https://guide.youreco.com.ua/vidhody-polimeriv.html :: public/vidhody-polimeriv.html | vidhody-polimeriv.html
- https://guide.youreco.com.ua/vidhody-vyrobnyctva.html :: public/vidhody-vyrobnyctva.html | vidhody-vyrobnyctva.html
- https://guide.youreco.com.ua/vidhody.html :: public/vidhody.html | vidhody.html
- https://guide.youreco.com.ua/vidy-kabelnyh-vidhodiv.html :: public/vidy-kabelnyh-vidhodiv.html | vidy-kabelnyh-vidhodiv.html
- https://guide.youreco.com.ua/vidy-plastykovyh-vidhodiv.html :: public/vidy-plastykovyh-vidhodiv.html | vidy-plastykovyh-vidhodiv.html
- https://guide.youreco.com.ua/vnutrishniy-akt-spysannya.html :: public/vnutrishniy-akt-spysannya.html | vnutrishniy-akt-spysannya.html
- https://guide.youreco.com.ua/vtorynna-syrovyna-z-budivelnyh-vidhodiv.html :: public/vtorynna-syrovyna-z-budivelnyh-vidhodiv.html | vtorynna-syrovyna-z-budivelnyh-vidhodiv.html
- https://guide.youreco.com.ua/vtorynna-syrovyna-z-vidhodiv.html :: public/vtorynna-syrovyna-z-vidhodiv.html | vtorynna-syrovyna-z-vidhodiv.html
- https://guide.youreco.com.ua/vymogy-do-zberigannya-vidhodiv.html :: public/vymogy-do-zberigannya-vidhodiv.html | vymogy-do-zberigannya-vidhodiv.html
- https://guide.youreco.com.ua/vyviz-budivelnyh-vidhodiv.html :: public/vyviz-budivelnyh-vidhodiv.html | vyviz-budivelnyh-vidhodiv.html
- https://guide.youreco.com.ua/yak-oformyty-spysannya-partiyi.html :: public/yak-oformyty-spysannya-partiyi.html | yak-oformyty-spysannya-partiyi.html
- https://guide.youreco.com.ua/yak-peredaty-kosmetyku.html :: public/yak-peredaty-kosmetyku.html | yak-peredaty-kosmetyku.html
- https://guide.youreco.com.ua/yak-peredaty-li-ion-batarei.html :: public/yak-peredaty-li-ion-batarei.html | yak-peredaty-li-ion-batarei.html
- https://guide.youreco.com.ua/yak-peredaty-skladski-zalyshky.html :: public/yak-peredaty-skladski-zalyshky.html | yak-peredaty-skladski-zalyshky.html
- https://guide.youreco.com.ua/yak-vidbuvayetsya-utylizaciya-produkciyi.html :: public/yak-vidbuvayetsya-utylizaciya-produkciyi.html | yak-vidbuvayetsya-utylizaciya-produkciyi.html
- https://guide.youreco.com.ua/zberigannya-vidpracovanyh-masel.html :: public/zberigannya-vidpracovanyh-masel.html | zberigannya-vidpracovanyh-masel.html
- https://guide.youreco.com.ua/zbir-kabelyu.html :: public/zbir-kabelyu.html | zbir-kabelyu.html
- https://guide.youreco.com.ua/zbir-kartonu-na-pidpryyemstvi.html :: public/zbir-kartonu-na-pidpryyemstvi.html | zbir-kartonu-na-pidpryyemstvi.html
- https://guide.youreco.com.ua/zbir-metalu-na-pidpryyemstvi.html :: public/zbir-metalu-na-pidpryyemstvi.html | zbir-metalu-na-pidpryyemstvi.html
- https://guide.youreco.com.ua/zbir-plastyku-na-pidpryyemstvi.html :: public/zbir-plastyku-na-pidpryyemstvi.html | zbir-plastyku-na-pidpryyemstvi.html
- https://guide.youreco.com.ua/zbir-promyslovyh-vidhodiv.html :: public/zbir-promyslovyh-vidhodiv.html | zbir-promyslovyh-vidhodiv.html
- https://guide.youreco.com.ua/zbir-shyn-na-pidpryyemstvi.html :: public/zbir-shyn-na-pidpryyemstvi.html | zbir-shyn-na-pidpryyemstvi.html
- https://guide.youreco.com.ua/zbir-sklyanoyi-tary.html :: public/zbir-sklyanoyi-tary.html | zbir-sklyanoyi-tary.html
- https://guide.youreco.com.ua/zbir-vidpracovanoyi-olyvy.html :: public/zbir-vidpracovanoyi-olyvy.html | zbir-vidpracovanoyi-olyvy.html
- https://guide.youreco.com.ua/zbir.html :: public/zbir.html | zbir.html
- https://guide.youreco.com.ua/znyshchennya-kosmetyky.html :: public/znyshchennya-kosmetyky.html | znyshchennya-kosmetyky.html

## Possible Cyrillic encoding issues
None

## Git status
```txt
?? fixed_independent_sitemap_check.py
?? independent-sitemap-check-report.md
?? independent_sitemap_check.py
```

## Git status stderr
```txt
clean
```

## Final decision
INDEPENDENT CHECK FAILED
