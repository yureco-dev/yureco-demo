1. git show --name-only --oneline d14d091
```
d14d091 add lead blocks after h1 on index pages
404.html
akt-pryimannya-peredachi.html
akt-utylizaciyi.html
chy-potribno-pererobyty-chy-utylizuvaty.html
dokumenty.html
fotozvit-utylizaciyi.html
index.html
kabelni-vidhody.html
kudy-zdaty.html
lead-block-fix-report.md
likvidaciya-skladskykh-zalyshkiv.html
logistyka-metalu.html
logistyka-skla.html
logistyka.html
pererobka-avtomobilnyh-shyn.html
pererobka-cegly.html
pererobka-skla.html
pererobka.html
povernennya-tovariv-z-merezhi.html
sortuvannya.html
spysannya-produkciyi.html
utilizaciya-brakovanoi-produkciyi.html
utilizaciya-dlya-bankiv.html
utilizaciya-dlya-data-centriv.html
utilizaciya-dlya-importeriv.html
utilizaciya-dlya-riteylu.html
utilizaciya-dlya-skladiv.html
utilizaciya-dlya-vyrobnyctva.html
utylizaciya-akumulyatoriv.html
utylizaciya-dokumentiv.html
utylizaciya-elektroniky.html
utylizaciya-gazovanyh-napoyiv.html
utylizaciya-importnyh-tovariv.html
utylizaciya-kabelyu-ta-drotiv.html
utylizaciya-konserviv.html
utylizaciya-kosmetyky-magazyniv.html
utylizaciya-kosmetyky.html
utylizaciya-li-ion-batarej.html
utylizaciya-myasnyh-produktiv.html
utylizaciya-napoyiv.html
utylizaciya-nekondicijnoyi-sirovini.html
utylizaciya-odyagu-vzuttya.html
utylizaciya-ofisnih-mebliv-orgtehniki.html
utylizaciya-paverbankiv-dbj.html
utylizaciya-plastyku-ta-polimeriv.html
utylizaciya-produktiv-harchuvannya-napoyiv.html
utylizaciya-promyslovyh-vidhodiv.html
utylizaciya-prostrochenyh-produktiv.html
utylizaciya-rybnyh-produktiv.html
utylizaciya-shyn.html
utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
utylizaciya-sonyachnih-panelij-vitryakiv.html
utylizaciya-tary-upakovki.html
utylizaciya-tovary-pid-mitnim-kontrolem.html
utylizaciya-vidpracovanoi-olyvy.html
utylizaciya-zamorozhenyh-produktiv.html
utylizaciya-zipsovanyh-produktiv.html
utylizaciya.html
vidhody.html
yak-oformyty-spysannya-partiyi.html
yak-peredaty-kosmetyku.html
yak-peredaty-li-ion-batarei.html
yak-peredaty-skladski-zalyshky.html
yak-vidbuvayetsya-utylizaciya-produkciyi.html
zbir.html
```

2. git diff d14d091^ d14d091 -- 404.html
```
diff --git a/404.html b/404.html
index 43c9785..c2baa1c 100644
--- a/404.html
+++ b/404.html
@@ -52,6 +52,7 @@
 </nav>
 
 <h1>Сторінку не знайдено</h1>
+<p class="lead">Ця сторінка повідомляє, що запитану адресу не знайдено в довіднику YOURECO. Вона допомагає повернутися до основних розділів і швидко знайти потрібну тему про поводження з відходами.</p>
 
 <section class="intro-card">
 <p>Можливо, адресу змінено або сторінку було переміщено. Перейдіть на головну сторінку або скористайтеся основними розділами довідника.</p>
```

3. git diff d14d091^ d14d091 --name-only
```
404.html
akt-pryimannya-peredachi.html
akt-utylizaciyi.html
chy-potribno-pererobyty-chy-utylizuvaty.html
dokumenty.html
fotozvit-utylizaciyi.html
index.html
kabelni-vidhody.html
kudy-zdaty.html
lead-block-fix-report.md
likvidaciya-skladskykh-zalyshkiv.html
logistyka-metalu.html
logistyka-skla.html
logistyka.html
pererobka-avtomobilnyh-shyn.html
pererobka-cegly.html
pererobka-skla.html
pererobka.html
povernennya-tovariv-z-merezhi.html
sortuvannya.html
spysannya-produkciyi.html
utilizaciya-brakovanoi-produkciyi.html
utilizaciya-dlya-bankiv.html
utilizaciya-dlya-data-centriv.html
utilizaciya-dlya-importeriv.html
utilizaciya-dlya-riteylu.html
utilizaciya-dlya-skladiv.html
utilizaciya-dlya-vyrobnyctva.html
utylizaciya-akumulyatoriv.html
utylizaciya-dokumentiv.html
utylizaciya-elektroniky.html
utylizaciya-gazovanyh-napoyiv.html
utylizaciya-importnyh-tovariv.html
utylizaciya-kabelyu-ta-drotiv.html
utylizaciya-konserviv.html
utylizaciya-kosmetyky-magazyniv.html
utylizaciya-kosmetyky.html
utylizaciya-li-ion-batarej.html
utylizaciya-myasnyh-produktiv.html
utylizaciya-napoyiv.html
utylizaciya-nekondicijnoyi-sirovini.html
utylizaciya-odyagu-vzuttya.html
utylizaciya-ofisnih-mebliv-orgtehniki.html
utylizaciya-paverbankiv-dbj.html
utylizaciya-plastyku-ta-polimeriv.html
utylizaciya-produktiv-harchuvannya-napoyiv.html
utylizaciya-promyslovyh-vidhodiv.html
utylizaciya-prostrochenyh-produktiv.html
utylizaciya-rybnyh-produktiv.html
utylizaciya-shyn.html
utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
utylizaciya-sonyachnih-panelij-vitryakiv.html
utylizaciya-tary-upakovki.html
utylizaciya-tovary-pid-mitnim-kontrolem.html
utylizaciya-vidpracovanoi-olyvy.html
utylizaciya-zamorozhenyh-produktiv.html
utylizaciya-zipsovanyh-produktiv.html
utylizaciya.html
vidhody.html
yak-oformyty-spysannya-partiyi.html
yak-peredaty-kosmetyku.html
yak-peredaty-li-ion-batarei.html
yak-peredaty-skladski-zalyshky.html
yak-vidbuvayetsya-utylizaciya-produkciyi.html
zbir.html
```

4. git diff d14d091^ d14d091 --numstat
```
1	0	404.html
1	0	akt-pryimannya-peredachi.html
1	0	akt-utylizaciyi.html
1	0	chy-potribno-pererobyty-chy-utylizuvaty.html
1	1	dokumenty.html
1	0	fotozvit-utylizaciyi.html
2	1	index.html
1	0	kabelni-vidhody.html
2	1	kudy-zdaty.html
160	0	lead-block-fix-report.md
1	0	likvidaciya-skladskykh-zalyshkiv.html
1	0	logistyka-metalu.html
1	0	logistyka-skla.html
2	1	logistyka.html
1	0	pererobka-avtomobilnyh-shyn.html
1	0	pererobka-cegly.html
1	0	pererobka-skla.html
2	1	pererobka.html
1	0	povernennya-tovariv-z-merezhi.html
2	1	sortuvannya.html
1	0	spysannya-produkciyi.html
1	0	utilizaciya-brakovanoi-produkciyi.html
1	0	utilizaciya-dlya-bankiv.html
1	0	utilizaciya-dlya-data-centriv.html
1	0	utilizaciya-dlya-importeriv.html
1	0	utilizaciya-dlya-riteylu.html
1	0	utilizaciya-dlya-skladiv.html
1	0	utilizaciya-dlya-vyrobnyctva.html
1	0	utylizaciya-akumulyatoriv.html
1	0	utylizaciya-dokumentiv.html
1	0	utylizaciya-elektroniky.html
1	0	utylizaciya-gazovanyh-napoyiv.html
1	0	utylizaciya-importnyh-tovariv.html
1	0	utylizaciya-kabelyu-ta-drotiv.html
1	0	utylizaciya-konserviv.html
1	0	utylizaciya-kosmetyky-magazyniv.html
1	0	utylizaciya-kosmetyky.html
1	0	utylizaciya-li-ion-batarej.html
1	0	utylizaciya-myasnyh-produktiv.html
1	0	utylizaciya-napoyiv.html
1	0	utylizaciya-nekondicijnoyi-sirovini.html
1	0	utylizaciya-odyagu-vzuttya.html
1	0	utylizaciya-ofisnih-mebliv-orgtehniki.html
1	0	utylizaciya-paverbankiv-dbj.html
1	0	utylizaciya-plastyku-ta-polimeriv.html
1	0	utylizaciya-produktiv-harchuvannya-napoyiv.html
1	0	utylizaciya-promyslovyh-vidhodiv.html
1	0	utylizaciya-prostrochenyh-produktiv.html
1	0	utylizaciya-rybnyh-produktiv.html
1	0	utylizaciya-shyn.html
1	0	utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
1	0	utylizaciya-sonyachnih-panelij-vitryakiv.html
1	0	utylizaciya-tary-upakovki.html
1	0	utylizaciya-tovary-pid-mitnim-kontrolem.html
1	0	utylizaciya-vidpracovanoi-olyvy.html
1	0	utylizaciya-zamorozhenyh-produktiv.html
1	0	utylizaciya-zipsovanyh-produktiv.html
2	1	utylizaciya.html
2	1	vidhody.html
1	0	yak-oformyty-spysannya-partiyi.html
1	0	yak-peredaty-kosmetyku.html
1	0	yak-peredaty-li-ion-batarei.html
1	0	yak-peredaty-skladski-zalyshky.html
1	0	yak-vidbuvayetsya-utylizaciya-produkciyi.html
2	1	zbir.html
```

5. git show --stat --oneline d14d091
```
d14d091 add lead blocks after h1 on index pages
 404.html                                        |   1 +
 akt-pryimannya-peredachi.html                   |   1 +
 akt-utylizaciyi.html                            |   1 +
 chy-potribno-pererobyty-chy-utylizuvaty.html    |   1 +
 dokumenty.html                                  |   2 +-
 fotozvit-utylizaciyi.html                       |   1 +
 index.html                                      |   3 +-
 kabelni-vidhody.html                            |   1 +
 kudy-zdaty.html                                 |   3 +-
 lead-block-fix-report.md                        | 160 ++++++++++++++++++++++++
 likvidaciya-skladskykh-zalyshkiv.html           |   1 +
 logistyka-metalu.html                           |   1 +
 logistyka-skla.html                             |   1 +
 logistyka.html                                  |   3 +-
 pererobka-avtomobilnyh-shyn.html                |   1 +
 pererobka-cegly.html                            |   1 +
 pererobka-skla.html                             |   1 +
 pererobka.html                                  |   3 +-
 povernennya-tovariv-z-merezhi.html              |   1 +
 sortuvannya.html                                |   3 +-
 spysannya-produkciyi.html                       |   1 +
 utilizaciya-brakovanoi-produkciyi.html          |   1 +
 utilizaciya-dlya-bankiv.html                    |   1 +
 utilizaciya-dlya-data-centriv.html              |   1 +
 utilizaciya-dlya-importeriv.html                |   1 +
 utilizaciya-dlya-riteylu.html                   |   1 +
 utilizaciya-dlya-skladiv.html                   |   1 +
 utilizaciya-dlya-vyrobnyctva.html               |   1 +
 utylizaciya-akumulyatoriv.html                  |   1 +
 utylizaciya-dokumentiv.html                     |   1 +
 utylizaciya-elektroniky.html                    |   1 +
 utylizaciya-gazovanyh-napoyiv.html              |   1 +
 utylizaciya-importnyh-tovariv.html              |   1 +
 utylizaciya-kabelyu-ta-drotiv.html              |   1 +
 utylizaciya-konserviv.html                      |   1 +
 utylizaciya-kosmetyky-magazyniv.html            |   1 +
 utylizaciya-kosmetyky.html                      |   1 +
 utylizaciya-li-ion-batarej.html                 |   1 +
 utylizaciya-myasnyh-produktiv.html              |   1 +
 utylizaciya-napoyiv.html                        |   1 +
 utylizaciya-nekondicijnoyi-sirovini.html        |   1 +
 utylizaciya-odyagu-vzuttya.html                 |   1 +
 utylizaciya-ofisnih-mebliv-orgtehniki.html      |   1 +
 utylizaciya-paverbankiv-dbj.html                |   1 +
 utylizaciya-plastyku-ta-polimeriv.html          |   1 +
 utylizaciya-produktiv-harchuvannya-napoyiv.html |   1 +
 utylizaciya-promyslovyh-vidhodiv.html           |   1 +
 utylizaciya-prostrochenyh-produktiv.html        |   1 +
 utylizaciya-rybnyh-produktiv.html               |   1 +
 utylizaciya-shyn.html                           |   1 +
 utylizaciya-skladskyh-zalyshkiv-kosmetyky.html  |   1 +
 utylizaciya-sonyachnih-panelij-vitryakiv.html   |   1 +
 utylizaciya-tary-upakovki.html                  |   1 +
 utylizaciya-tovary-pid-mitnim-kontrolem.html    |   1 +
 utylizaciya-vidpracovanoi-olyvy.html            |   1 +
 utylizaciya-zamorozhenyh-produktiv.html         |   1 +
 utylizaciya-zipsovanyh-produktiv.html           |   1 +
 utylizaciya.html                                |   3 +-
 vidhody.html                                    |   3 +-
 yak-oformyty-spysannya-partiyi.html             |   1 +
 yak-peredaty-kosmetyku.html                     |   1 +
 yak-peredaty-li-ion-batarei.html                |   1 +
 yak-peredaty-skladski-zalyshky.html             |   1 +
 yak-vidbuvayetsya-utylizaciya-produkciyi.html   |   1 +
 zbir.html                                       |   3 +-
 65 files changed, 232 insertions(+), 9 deletions(-)
```

