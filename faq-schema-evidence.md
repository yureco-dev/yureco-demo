## 1. git status --short
```
?? faq-schema-audit.md
```

## 2. git log --oneline -5
```
992570f add faqpage schema for visible faq blocks
1bace37 add meta schema audit evidence reports
0dc0e9f fix remaining meta schema mismatches
01e903a align json-ld descriptions with meta descriptions
fd601e1 add missing index urls to sitemap
```

## 3. git show --name-only --oneline HEAD
```
992570f add faqpage schema for visible faq blocks
akt-utylizaciyi.html
dokumenty.html
faq-schema-fix-report.md
fotozvit-utylizaciyi.html
index.html
kudy-zdaty.html
pererobka-avtomobilnyh-shyn.html
pererobka-skla.html
pererobka.html
sortuvannya.html
utylizaciya-dokumentiv.html
utylizaciya-gazovanyh-napoyiv.html
utylizaciya-kabelyu-ta-drotiv.html
utylizaciya-konserviv.html
utylizaciya-li-ion-batarej.html
utylizaciya-myasnyh-produktiv.html
utylizaciya-nekondicijnoyi-sirovini.html
utylizaciya-odyagu-vzuttya.html
utylizaciya-plastyku-ta-polimeriv.html
utylizaciya-produktiv-harchuvannya-napoyiv.html
utylizaciya-promyslovyh-vidhodiv.html
utylizaciya-rybnyh-produktiv.html
utylizaciya-shyn.html
utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
utylizaciya-sonyachnih-panelij-vitryakiv.html
utylizaciya-tary-upakovki.html
utylizaciya-tovary-pid-mitnim-kontrolem.html
utylizaciya-vidpracovanoi-olyvy.html
utylizaciya-zamorozhenyh-produktiv.html
utylizaciya.html
vidhody.html
zbir.html
```

## 4. git show --stat --oneline HEAD
```
992570f add faqpage schema for visible faq blocks
 akt-utylizaciyi.html                            |  1 +
 dokumenty.html                                  |  1 +
 faq-schema-fix-report.md                        | 91 +++++++++++++++++++++++++
 fotozvit-utylizaciyi.html                       |  1 +
 index.html                                      |  2 +-
 kudy-zdaty.html                                 |  1 +
 pererobka-avtomobilnyh-shyn.html                |  1 +
 pererobka-skla.html                             |  1 +
 pererobka.html                                  |  1 +
 sortuvannya.html                                |  1 +
 utylizaciya-dokumentiv.html                     |  1 +
 utylizaciya-gazovanyh-napoyiv.html              |  1 +
 utylizaciya-kabelyu-ta-drotiv.html              |  1 +
 utylizaciya-konserviv.html                      |  1 +
 utylizaciya-li-ion-batarej.html                 |  1 +
 utylizaciya-myasnyh-produktiv.html              |  1 +
 utylizaciya-nekondicijnoyi-sirovini.html        |  1 +
 utylizaciya-odyagu-vzuttya.html                 |  1 +
 utylizaciya-plastyku-ta-polimeriv.html          |  3 +-
 utylizaciya-produktiv-harchuvannya-napoyiv.html |  3 +-
 utylizaciya-promyslovyh-vidhodiv.html           |  3 +-
 utylizaciya-rybnyh-produktiv.html               |  1 +
 utylizaciya-shyn.html                           |  1 +
 utylizaciya-skladskyh-zalyshkiv-kosmetyky.html  |  1 +
 utylizaciya-sonyachnih-panelij-vitryakiv.html   |  1 +
 utylizaciya-tary-upakovki.html                  |  1 +
 utylizaciya-tovary-pid-mitnim-kontrolem.html    |  1 +
 utylizaciya-vidpracovanoi-olyvy.html            |  1 +
 utylizaciya-zamorozhenyh-produktiv.html         |  1 +
 utylizaciya.html                                |  1 +
 vidhody.html                                    |  1 +
 zbir.html                                       |  1 +
 32 files changed, 125 insertions(+), 4 deletions(-)
```

## 5. git diff HEAD^ HEAD -- "*.html"
```diff
diff --git a/akt-utylizaciyi.html b/akt-utylizaciyi.html
index dc98daf..2be9dd0 100644
--- a/akt-utylizaciyi.html
+++ b/akt-utylizaciyi.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Акт утилізації відходів: що підтверджує цей документ","name":"Акт утилізації відходів: що підтверджує цей документ — Довідник YOURECO","description":"Акт утилізації відходів: що підтверджує документ, коли його оформлюють і як він фіксує завершення утилізації, переробки чи знищення.","url":"https://guide.youreco.com.ua/akt-utylizaciyi.html","mainEntityOfPage":"https://guide.youreco.com.ua/akt-utylizaciyi.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/akt-utylizaciyi.html","mainEntity":[{"@type":"Question","name":"Чи акт утилізації замінює акт приймання-передачі?","acceptedAnswer":{"@type":"Answer","text":"Ні. Це різні документи: один фіксує передачу, інший описує завершення операції з партією."}},{"@type":"Question","name":"Чи завжди акт має однакову форму?","acceptedAnswer":{"@type":"Answer","text":"Ні. Форма залежить від документообігу, типу матеріалу та домовленого способу опису партії."}},{"@type":"Question","name":"Навіщо зберігати опис партії?","acceptedAnswer":{"@type":"Answer","text":"Опис допомагає пов'язати акт із конкретними матеріалами, кількістю, станом і підставою вибуття."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/dokumenty.html b/dokumenty.html
index cdbd929..3d2af35 100644
--- a/dokumenty.html
+++ b/dokumenty.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","headline":"Документи для утилізації відходів","name":"Документи для утилізації відходів — Довідник YOURECO","description":"Які акти, реєстри та підтвердження потрібні підприємству для передачі, утилізації або переробки відходів.","url":"https://guide.youreco.com.ua/dokumenty.html","mainEntityOfPage":"https://guide.youreco.com.ua/dokumenty.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/dokumenty.html","mainEntity":[{"@type":"Question","name":"Чи замінює довідник юридичну перевірку?","acceptedAnswer":{"@type":"Answer","text":"Ні, довідник пояснює облікову логіку і не надає юридичних гарантій."}},{"@type":"Question","name":"Навіщо потрібен реєстр партії?","acceptedAnswer":{"@type":"Answer","text":"Він деталізує склад, кількість, тару, маркування і допомагає пов'язати внутрішні записи з переданням."}},{"@type":"Question","name":"Чим відрізняється списання від передачі?","acceptedAnswer":{"@type":"Answer","text":"Списання фіксує внутрішнє вибуття, а передача підтверджує рух партії до іншого учасника процесу."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 
diff --git a/fotozvit-utylizaciyi.html b/fotozvit-utylizaciyi.html
index a8f18c3..5245c84 100644
--- a/fotozvit-utylizaciyi.html
+++ b/fotozvit-utylizaciyi.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Фотозвіт утилізації: коли використовується і що підтверджує","name":"Фотозвіт утилізації: коли використовується і що підтверджує — Довідник YOURECO","description":"Фотозвіт утилізації: коли його додають до акта, що він підтверджує і як допомагає зафіксувати оброблення або знищення партії.","url":"https://guide.youreco.com.ua/fotozvit-utylizaciyi.html","mainEntityOfPage":"https://guide.youreco.com.ua/fotozvit-utylizaciyi.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/fotozvit-utylizaciyi.html","mainEntity":[{"@type":"Question","name":"Чи достатньо тільки фотографій?","acceptedAnswer":{"@type":"Answer","text":"Ні. Фотографії є додатковим матеріалом і мають розглядатися разом з актами, реєстрами або описом партії."}},{"@type":"Question","name":"Що варто показати на фото?","acceptedAnswer":{"@type":"Answer","text":"Загальний вигляд, маркування, кількість місць, стан тари, характерні пошкодження та різні типи матеріалів у змішаній партії."}},{"@type":"Question","name":"Чи фотозвіт має однакову силу для всіх ситуацій?","acceptedAnswer":{"@type":"Answer","text":"Ні. Його значення залежить від контексту, якості фіксації та зв'язку з іншими документами."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/index.html b/index.html
index 20f6181..817699f 100644
--- a/index.html
+++ b/index.html
@@ -160,7 +160,7 @@
 <!-- Schema.org (AboutPage) -->
 <!-- Schema.org (ItemList: structure of the guide) -->
 <link href="https://guide.youreco.com.ua/" hreflang="uk" rel="alternate"/><script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","headline":"Довідник YOURECO про поводження з відходами для підприємств","name":"Довідник YOURECO | як підприємствам організувати поводження з відходами — Довідник YOURECO","description":"Довідник YOURECO про відходи для підприємств України: утилізація, переробка, сортування, логістика, документи та типові ризики.","url":"https://guide.youreco.com.ua","mainEntityOfPage":"https://guide.youreco.com.ua","inLanguage":"uk-UA"}</script>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua","mainEntity":[{"@type":"Question","name":"Чим відрізняється переробка від утилізації та знешкодження?","acceptedAnswer":{"@type":"Answer","text":"Переробка повертає матеріали у вторинний обіг. Утилізація — ширше поняття, яке може включати переробку. Знешкодження застосовують, коли переробка неможлива або є небезпека."}},{"@type":"Question","name":"Чому важливо мати документи на утилізацію?","acceptedAnswer":{"@type":"Answer","text":"Документи підтверджують факт передачі відходів та коректне поводження з ними для внутрішнього обліку, контрагентів і перевірок."}},{"@type":"Question","name":"Що найчастіше “ламає” приймання відходів?","acceptedAnswer":{"@type":"Answer","text":"Змішування несумісних фракцій, відсутність маркування, протікання тари, наявність сторонніх домішок або небезпечних компонентів без попередження."}},{"@type":"Question","name":"Чи можна підготувати відходи заздалегідь, щоб зменшити вартість?","acceptedAnswer":{"@type":"Answer","text":"Так: сортування, зняття зайвого пакування, правильна тара й компактне складування майже завжди зменшують витрати на логістику та обробку."}},{"@type":"Question","name":"Де знайти практичні інструкції щодо конкретного виду відходів?","acceptedAnswer":{"@type":"Answer","text":"Оберіть розділ зліва. У кожному матеріалі є короткі правила підготовки, типові ризики та базовий комплект документів."}}],"inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua","mainEntity":[{"@type":"Question","name":"Чим відрізняється переробка від утилізації та знешкодження?","acceptedAnswer":{"@type":"Answer","text":"Переробка повертає матеріали у вторинний обіг. Утилізація — ширше поняття, яке може включати переробку. Знешкодження застосовують, коли переробка неможлива або є небезпека."}},{"@type":"Question","name":"Чому важливо мати документи на утилізацію?","acceptedAnswer":{"@type":"Answer","text":"Документи підтверджують факт передачі відходів та коректне поводження з ними для внутрішнього обліку, контрагентів і перевірок."}},{"@type":"Question","name":"Що найчастіше “ламає” приймання відходів?","acceptedAnswer":{"@type":"Answer","text":"Змішування несумісних фракцій, відсутність маркування, протікання тари, наявність сторонніх домішок або небезпечних компонентів без попередження."}},{"@type":"Question","name":"Чи можна підготувати відходи заздалегідь, щоб зменшити вартість?","acceptedAnswer":{"@type":"Answer","text":"Так: сортування, зняття зайвого пакування, правильна тара й компактне складування майже завжди зменшують витрати на логістику та обробку."}},{"@type":"Question","name":"Де знайти практичні інструкції щодо конкретного виду відходів?","acceptedAnswer":{"@type":"Answer","text":"Оберіть розділ зліва. У кожному матеріалі є короткі правила підготовки, типові ризики та базовий комплект документів."}},{"@type":"Question","name":"Для кого створено довідник?","acceptedAnswer":{"@type":"Answer","text":"Для користувачів, яким потрібно швидко розібратися в термінах, типах відходів, документах і базових процесах поводження."}},{"@type":"Question","name":"Чи довідник замінює профільні документи підприємства?","acceptedAnswer":{"@type":"Answer","text":"Ні. Він пояснює поняття та контекст, але не замінює внутрішні правила, договори або спеціалізовану оцінку ситуації."}},{"@type":"Question","name":"Як швидко знайти потрібну тему?","acceptedAnswer":{"@type":"Answer","text":"Спочатку визначте тип матеріалу або процес, а потім переходьте до розділів про утилізацію, переробку, сортування, логістику чи документи."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/kudy-zdaty.html b/kudy-zdaty.html
index 9e09a1e..70dc031 100644
--- a/kudy-zdaty.html
+++ b/kudy-zdaty.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","headline":"Куди здати","name":"Куди здати — Довідник YOURECO","description":"Практичний розділ: куди і як здати конкретні види відходів, що підготувати та які є вимоги.","url":"https://guide.youreco.com.ua/kudy-zdaty.html","mainEntityOfPage":"https://guide.youreco.com.ua/kudy-zdaty.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/kudy-zdaty.html","mainEntity":[{"@type":"Question","name":"З чого почати, якщо матеріал змішаний?","acceptedAnswer":{"@type":"Answer","text":"Почніть з опису найбільших фракцій, стану упаковки, наявності органічних залишків і приблизного обсягу."}},{"@type":"Question","name":"Чи достатньо знати тільки назву товару?","acceptedAnswer":{"@type":"Answer","text":"Не завжди. Для вибору сторінки важливі також стан, тара, домішки, причина вибуття і тип матеріалу."}},{"@type":"Question","name":"Навіщо розділяти харчові та пакувальні потоки?","acceptedAnswer":{"@type":"Answer","text":"Органічні залишки можуть забруднювати тару, тому чисте пакування і змішане пакування мають різний довідковий контекст."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 
diff --git a/pererobka-avtomobilnyh-shyn.html b/pererobka-avtomobilnyh-shyn.html
index 9e0c6d8..45d2f5f 100644
--- a/pererobka-avtomobilnyh-shyn.html
+++ b/pererobka-avtomobilnyh-shyn.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як передають на переробку автомобільні шини","name":"Як передають на переробку автомобільні шини — Довідник YOURECO","description":"Переробка автомобільних шин: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника YOURECO.","url":"https://guide.youreco.com.ua/pererobka-avtomobilnyh-shyn.html","mainEntityOfPage":"https://guide.youreco.com.ua/pererobka-avtomobilnyh-shyn.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/pererobka-avtomobilnyh-shyn.html","mainEntity":[{"@type":"Question","name":"Чим переробка шин відрізняється від утилізації шин?","acceptedAnswer":{"@type":"Answer","text":"Для підприємства різниця зазвичай полягає в подальшому маршруті матеріалу після передачі. Утилізація означає загальну організацію поводження зі списаними шинами, а переробка передбачає можливість сортування, подрібнення або підготовки матеріалу до повторного використання в інших процесах."}},{"@type":"Question","name":"Чи можна передати шини з дисками?","acceptedAnswer":{"@type":"Answer","text":"Це потрібно зазначити окремо під час попередньої оцінки. Шини з дисками можуть потребувати іншого формату приймання або підготовки."}},{"@type":"Question","name":"Які дані потрібні для попередньої оцінки?","acceptedAnswer":{"@type":"Answer","text":"Потрібні тип шин, приблизна кількість або вага, місто, місце зберігання, наявність дисків, нестандартних розмірів, забруднення та інформація про те, чи потрібні документи після передачі."}},{"@type":"Question","name":"Чи потрібно самостійно різати або подрібнювати шини?","acceptedAnswer":{"@type":"Answer","text":"Ні, без потреби цього робити не варто. Для передачі достатньо відокремити шини від інших відходів, згрупувати їх за типом і описати партію."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/pererobka-skla.html b/pererobka-skla.html
index 98d4f54..c44d71b 100644
--- a/pererobka-skla.html
+++ b/pererobka-skla.html
@@ -200,6 +200,7 @@
 .breadcrumbs a:hover{text-decoration:underline}
 .breadcrumbs span{opacity:.8}</style>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як передають скло на переробку","name":"Як передають скло на переробку — Довідник YOURECO","description":"Довідка для підприємств про «переробку скла»: що включає, як підготувати партію, правила зберігання, логістика, документи та типові помилки.","url":"https://guide.youreco.com.ua/pererobka-skla.html","mainEntityOfPage":"https://guide.youreco.com.ua/pererobka-skla.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/pererobka-skla.html","mainEntity":[{"@type":"Question","name":"Чи можна передати змішану партію скла?","acceptedAnswer":{"@type":"Answer","text":"Іноді це можливо, але для оцінки краще окремо описати склотару, пляшки, банки, листове скло, бій скла та наявність домішок. Так простіше визначити формат приймання."}},{"@type":"Question","name":"Чи потрібно самостійно дробити скло перед передачею?","acceptedAnswer":{"@type":"Answer","text":"Ні, без потреби цього робити не варто. Для передачі достатньо безпечно зібрати скло, відокремити його від інших відходів і описати партію."}},{"@type":"Question","name":"Які дані потрібні для попередньої оцінки?","acceptedAnswer":{"@type":"Answer","text":"Потрібні тип скла, приблизна кількість або вага, стан, наявність бою, ступінь забруднення, місто, місце зберігання, пакування та інформація про те, чи потрібні документи після передачі."}},{"@type":"Question","name":"Що робити зі склом із залишками продуктів або технічних речовин?","acceptedAnswer":{"@type":"Answer","text":"Таке скло потрібно виділити окремо й описати, чим саме воно забруднене, якщо ця інформація відома. Не варто змішувати його з чистою склотарою без потреби."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/pererobka.html b/pererobka.html
index e68bcca..eeb5c29 100644
--- a/pererobka.html
+++ b/pererobka.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","headline":"Порядок передання відходів на переробку","name":"Порядок передання відходів на переробку — Довідник YOURECO","description":"Що підприємству знати про передання відходів на переробку: підготовка партій, вимоги до сировини й підтвердження.","url":"https://guide.youreco.com.ua/pererobka.html","mainEntityOfPage":"https://guide.youreco.com.ua/pererobka.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/pererobka.html","mainEntity":[{"@type":"Question","name":"Чи вся вторсировина приймається однаково?","acceptedAnswer":{"@type":"Answer","text":"Ні. Умови залежать від чистоти, однорідності, вологості, наявності домішок і формату накопичення."}},{"@type":"Question","name":"Коли матеріал втрачає придатність до переробки?","acceptedAnswer":{"@type":"Answer","text":"Коли його змішують з іншими потоками, забруднюють, накопичують без контролю або не захищають від пошкодження та вологи."}},{"@type":"Question","name":"Що дає підприємству системна переробка?","acceptedAnswer":{"@type":"Answer","text":"Вона зменшує частку проблемних потоків, підвищує керованість відходів і допомагає будувати стабільні маршрути поводження з матеріалами."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 
diff --git a/sortuvannya.html b/sortuvannya.html
index ff2e2d9..9cae399 100644
--- a/sortuvannya.html
+++ b/sortuvannya.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","headline":"Сортування відходів перед передачею","name":"Сортування відходів перед передачею — Довідник YOURECO","description":"Як розділяти потоки відходів перед передачею: базові правила сортування, підготовка партій і типові помилки.","url":"https://guide.youreco.com.ua/sortuvannya.html","mainEntityOfPage":"https://guide.youreco.com.ua/sortuvannya.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/sortuvannya.html","mainEntity":[{"@type":"Question","name":"З чого починати сортування на підприємстві?","acceptedAnswer":{"@type":"Answer","text":"З ключових потоків, які утворюються найчастіше, та з чітко позначених місць їх накопичення."}},{"@type":"Question","name":"Чому схема сортування перестає працювати?","acceptedAnswer":{"@type":"Answer","text":"Через складні правила, відсутність маркування, незручну тару або відрив сортування від реальної логістики об'єкта."}},{"@type":"Question","name":"Що робити зі змішаними партіями?","acceptedAnswer":{"@type":"Answer","text":"Виділяти окремо і погоджувати для них окремий маршрут, а не домішувати до чистих фракцій."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 
diff --git a/utylizaciya-dokumentiv.html b/utylizaciya-dokumentiv.html
index e80383f..75f7f11 100644
--- a/utylizaciya-dokumentiv.html
+++ b/utylizaciya-dokumentiv.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як оформлюється утилізація конфіденційних документів","name":"Як оформлюється утилізація конфіденційних документів — Довідник YOURECO","description":"Утилізація конфіденційних документів: папір, архіви, бухгалтерські й юридичні документи, носії даних та підтвердження знищення.","url":"https://guide.youreco.com.ua/utylizaciya-dokumentiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-dokumentiv.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-dokumentiv.html","mainEntity":[{"@type":"Question","name":"Чи можна викинути старі документи як макулатуру?","acceptedAnswer":{"@type":"Answer","text":"Якщо документи не містять чутливої інформації та підприємство погодило їх списання, це може бути простішим випадком. Але документи з персональними, фінансовими, комерційними або внутрішніми даними краще передавати контрольовано з підтвердними документами."}},{"@type":"Question","name":"Чи потрібно складати перелік документів перед передачею?","acceptedAnswer":{"@type":"Answer","text":"Бажано сформувати хоча б загальний опис партії: тип документів, період, підрозділ, кількість коробок або орієнтовна вага. Це допомагає уникнути випадкової передачі потрібних матеріалів."}},{"@type":"Question","name":"Які дані потрібні для попередньої оцінки?","acceptedAnswer":{"@type":"Answer","text":"Потрібні тип документів, орієнтовний обсяг, кількість коробок або вага, місто, місце зберігання, поверх, доступ до приміщення та інформація про те, які документи потрібні після передачі."}},{"@type":"Question","name":"Чи можна передати документи разом з офісним папером і поліграфією?","acceptedAnswer":{"@type":"Answer","text":"Іноді це можливо, але конфіденційні документи краще описувати окремо від звичайного паперу, рекламної поліграфії або пакувальних матеріалів."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-gazovanyh-napoyiv.html b/utylizaciya-gazovanyh-napoyiv.html
index f800112..768a04f 100644
--- a/utylizaciya-gazovanyh-napoyiv.html
+++ b/utylizaciya-gazovanyh-napoyiv.html
@@ -200,6 +200,7 @@
 .breadcrumbs a:hover{text-decoration:underline}
 .breadcrumbs span{opacity:.8}</style>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Куди передають газовані напої на утилізацію","name":"Куди передають газовані напої на утилізацію — Довідник YOURECO","description":"Довідка для підприємств про «утилізацію газованих напоїв»: що включає, як підготувати партію, правила зберігання, логістика, документи та типові помилки.","url":"https://guide.youreco.com.ua/utylizaciya-gazovanyh-napoyiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-gazovanyh-napoyiv.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-gazovanyh-napoyiv.html","mainEntity":[{"@type":"Question","name":"Чому не можна зливати газовані напої будь-де?","acceptedAnswer":{"@type":"Answer","text":"Через тиск у тарі та ризик неконтрольованих викидів рідини і упаковки."}},{"@type":"Question","name":"Чи потрібна окрема фотофіксація?","acceptedAnswer":{"@type":"Answer","text":"Так, якщо партія брендована або є високий ризик претензій щодо повторного потрапляння товару в обіг."}},{"@type":"Question","name":"Чому газовані напої описують окремо від інших напоїв?","acceptedAnswer":{"@type":"Answer","text":"Через тиск у закритій тарі, ризик протікання, змішані формати упаковки та наявність органічних залишків."}},{"@type":"Question","name":"Чи варто самостійно відкривати пошкоджену тару?","acceptedAnswer":{"@type":"Answer","text":"Ні. Довідковий підхід полягає в описі стану партії, а не в виконанні небезпечних дій із закритою упаковкою."}},{"@type":"Question","name":"Що фіксувати у змішаній партії?","acceptedAnswer":{"@type":"Answer","text":"Типи напоїв, види тари, стан коробів, наявність протікання, кількість місць і причину втрати придатності."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-kabelyu-ta-drotiv.html b/utylizaciya-kabelyu-ta-drotiv.html
index 1acaddb..71ff315 100644
--- a/utylizaciya-kabelyu-ta-drotiv.html
+++ b/utylizaciya-kabelyu-ta-drotiv.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як оформлюється утилізація кабелю та дротів","name":"Як оформлюється утилізація кабелю та дротів — Довідник YOURECO","description":"Утилізація кабелю та дротів: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника YOURECO.","url":"https://guide.youreco.com.ua/utylizaciya-kabelyu-ta-drotiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-kabelyu-ta-drotiv.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-kabelyu-ta-drotiv.html","mainEntity":[{"@type":"Question","name":"Чи можна самостійно випалювати ізоляцію з кабелю?","acceptedAnswer":{"@type":"Answer","text":"Ні, цього не варто робити. Самостійне випалювання ізоляції є небезпечним способом поводження з кабельними відходами та може створювати ризики для людей, майданчика й довкілля."}},{"@type":"Question","name":"Чи потрібно сортувати кабель перед передачею?","acceptedAnswer":{"@type":"Answer","text":"Бажано хоча б відокремити силовий кабель, слабкострумові дроти, мідні, алюмінієві та змішані залишки, якщо це можна зробити безпечно. Це спрощує оцінку партії та подальше приймання."}},{"@type":"Question","name":"Які дані потрібні для попередньої оцінки?","acceptedAnswer":{"@type":"Answer","text":"Потрібні тип кабелю, приблизна кількість або вага, місто, місце зберігання, стан, походження партії, наявність ізоляції, домішок або забруднення."}},{"@type":"Question","name":"Чи можна передати кабель разом з електронікою або обладнанням?","acceptedAnswer":{"@type":"Answer","text":"Іноді це можливо, але для оцінки потрібно окремо описати кабель, обладнання та інші матеріали в партії. Якщо кабель уже демонтований, його краще обліковувати окремо."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-konserviv.html b/utylizaciya-konserviv.html
index a01f449..40aae47 100644
--- a/utylizaciya-konserviv.html
+++ b/utylizaciya-konserviv.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Куди передають консерви на утилізацію","name":"Куди передають консерви на утилізацію — Довідник YOURECO","description":"Утилізація консервів: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника YOURECO.","url":"https://guide.youreco.com.ua/utylizaciya-konserviv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-konserviv.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-konserviv.html","mainEntity":[{"@type":"Question","name":"Чи можна просто викинути списані консерви у звичайний контейнер?","acceptedAnswer":{"@type":"Answer","text":"Для підприємства це небажаний варіант. Списана продукція потребує обліку, відокремлення від придатних товарів і документального підтвердження передачі."}},{"@type":"Question","name":"Що робити зі здутими або пошкодженими банками?","acceptedAnswer":{"@type":"Answer","text":"Їх потрібно виділити окремо, не відкривати без потреби та описати стан партії під час попередньої оцінки. Такі позиції краще не змішувати з непошкодженою продукцією."}},{"@type":"Question","name":"Які дані потрібні для попередньої оцінки?","acceptedAnswer":{"@type":"Answer","text":"Потрібні найменування або тип продукції, кількість одиниць, вага або об'єм, строк придатності, причина списання, стан пакування, місто, місце зберігання та інформація про те, чи потрібні документи після передачі."}},{"@type":"Question","name":"Чи можна передати змішану партію консервів?","acceptedAnswer":{"@type":"Answer","text":"Іноді це можливо, але для оцінки потрібно розуміти склад змішаної партії. Краще окремо описати типи продукції, тару, пошкоджені позиції, здуття, протікання та причину списання."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-li-ion-batarej.html b/utylizaciya-li-ion-batarej.html
index 1fce268..1bf6f46 100644
--- a/utylizaciya-li-ion-batarej.html
+++ b/utylizaciya-li-ion-batarej.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle про Li-ion батареї -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як оформлюється утилізація літій-іонних батарей","name":"Як оформлюється утилізація літій-іонних батарей — Довідник YOURECO","description":"Утилізація Li-ion батарей для підприємств: ризики, підготовка, тимчасове зберігання, етапи передачі та документи.","url":"https://guide.youreco.com.ua/utylizaciya-li-ion-batarej.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-li-ion-batarej.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-li-ion-batarej.html","mainEntity":[{"@type":"Question","name":"Чи можна викидати Li-ion батареї у звичайний контейнер?","acceptedAnswer":{"@type":"Answer","text":"Для підприємства це небажаний і ризиковий варіант. Такі батареї краще збирати окремо та передавати організації, яка може прийняти їх для подальшого поводження."}},{"@type":"Question","name":"Що робити зі здутими або пошкодженими батареями?","acceptedAnswer":{"@type":"Answer","text":"Їх потрібно відокремити від непошкоджених, не розбирати, не стискати, не проколювати та не зберігати поруч із матеріалами, які можуть посилити ризик займання. Для передачі варто окремо повідомити про стан таких батарей."}},{"@type":"Question","name":"Чи потрібно знімати батареї з обладнання?","acceptedAnswer":{"@type":"Answer","text":"Якщо батареї знімні та це можна зробити безпечним штатним способом, їх зручно обліковувати окремо. Якщо батарея вбудована або демонтаж потребує втручання в конструкцію, краще не розбирати обладнання самостійно без відповідної компетенції."}},{"@type":"Question","name":"Які дані потрібні для попередньої оцінки?","acceptedAnswer":{"@type":"Answer","text":"Потрібні тип батарей, кількість або приблизна вага, стан, місто, походження партії та інформація про те, чи батареї вже списані на підприємстві."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-myasnyh-produktiv.html b/utylizaciya-myasnyh-produktiv.html
index 8dbe97b..557d51e 100644
--- a/utylizaciya-myasnyh-produktiv.html
+++ b/utylizaciya-myasnyh-produktiv.html
@@ -200,6 +200,7 @@
 .breadcrumbs a:hover{text-decoration:underline}
 .breadcrumbs span{opacity:.8}</style>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Куди передають м’ясні продукти на утилізацію","name":"Куди передають м’ясні продукти на утилізацію — Довідник YOURECO","description":"Довідка для підприємств про «утилізацію м’ясних продуктів»: що включає, як підготувати партію, правила зберігання, логістика, документи та типові помилки.","url":"https://guide.youreco.com.ua/utylizaciya-myasnyh-produktiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-myasnyh-produktiv.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-myasnyh-produktiv.html","mainEntity":[{"@type":"Question","name":"Що вказувати для м'ясної партії?","acceptedAnswer":{"@type":"Answer","text":"Назву, кількість, стан, тип тари, температуру зберігання, наявність пошкоджень, запаху або рідини."}},{"@type":"Question","name":"Чи потрібно описувати змішані матеріали?","acceptedAnswer":{"@type":"Answer","text":"Так, лотки, плівку, картон, піддони і мокре пакування бажано виділяти в описі окремо."}},{"@type":"Question","name":"Чому санітарний контекст важливий?","acceptedAnswer":{"@type":"Answer","text":"Він пояснює ризики запаху, протікання і забруднення сусідніх матеріалів без надання юридичних висновків."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-nekondicijnoyi-sirovini.html b/utylizaciya-nekondicijnoyi-sirovini.html
index 2117b50..685faac 100644
--- a/utylizaciya-nekondicijnoyi-sirovini.html
+++ b/utylizaciya-nekondicijnoyi-sirovini.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації некондиційної сировини та продукції","name":"Порядок утилізації некондиційної сировини та продукції — Довідник YOURECO","description":"Утилізація некондиційної сировини та продукції: прострочені партії, брак, порушення зберігання, рекламації й документи.","url":"https://guide.youreco.com.ua/utylizaciya-nekondicijnoyi-sirovini.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-nekondicijnoyi-sirovini.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-nekondicijnoyi-sirovini.html","mainEntity":[{"@type":"Question","name":"Чи можна повернути некондиційну сировину у виробництво?","acceptedAnswer":{"@type":"Answer","text":"Це залежить від внутрішнього рішення підприємства, статусу партії та причин некондиційності. Якщо сировина вже списана як непридатна, її не варто повертати в процес без окремого рішення відповідальних осіб."}},{"@type":"Question","name":"Що робити зі змішаною партією сировини?","acceptedAnswer":{"@type":"Answer","text":"Для оцінки потрібно окремо описати склад змішаної партії, типи матеріалів, приблизну кількість, стан пакування та причину списання. Якщо можливо, різні групи матеріалів краще розділити."}},{"@type":"Question","name":"Які дані потрібні для попередньої оцінки?","acceptedAnswer":{"@type":"Answer","text":"Потрібні назва або тип сировини, кількість, вага або об’єм, причина списання, стан пакування, місто, місце зберігання та інформація про те, чи потрібні документи після передачі."}},{"@type":"Question","name":"Чи можна передати сировину без маркування?","acceptedAnswer":{"@type":"Answer","text":"Іноді це можливо, але відсутність маркування потрібно окремо зазначити. Для оцінки важливо максимально описати походження, склад або процес, у якому ця сировина використовувалась."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-odyagu-vzuttya.html b/utylizaciya-odyagu-vzuttya.html
index 01f3b2a..36d1d84 100644
--- a/utylizaciya-odyagu-vzuttya.html
+++ b/utylizaciya-odyagu-vzuttya.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Куди передають одяг та взуття на утилізацію","name":"Куди передають одяг та взуття на утилізацію — Довідник YOURECO","description":"Утилізація одягу та взуття для підприємств: списання, брак, надлишки, корпоративна форма, контроль повторного обігу й документи.","url":"https://guide.youreco.com.ua/utylizaciya-odyagu-vzuttya.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-odyagu-vzuttya.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-odyagu-vzuttya.html","mainEntity":[{"@type":"Question","name":"Чи можна передати списаний одяг і взуття однією партією?","acceptedAnswer":{"@type":"Answer","text":"Іноді це можливо, але для оцінки краще окремо описати одяг, взуття, текстиль, спецодяг, уніформу, брендовані позиції, брак і повернення."}},{"@type":"Question","name":"Що робити з брендованим одягом або уніформою?","acceptedAnswer":{"@type":"Answer","text":"Такі позиції варто виділити окремо та зазначити наявність логотипів, маркування або вимоги щодо унеможливлення повторного використання."}},{"@type":"Question","name":"Які дані потрібні для попередньої оцінки?","acceptedAnswer":{"@type":"Answer","text":"Потрібні тип матеріалів, кількість одиниць, приблизна вага або об'єм, причина списання, стан, місто, місце зберігання, наявність брендування та інформація про те, чи потрібні документи після передачі."}},{"@type":"Question","name":"Чи можна передати забруднений або вологий текстиль?","acceptedAnswer":{"@type":"Answer","text":"Це потрібно зазначити окремо під час попередньої оцінки. Забруднення, вологість або запах можуть впливати на умови приймання, пакування та вивезення."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-plastyku-ta-polimeriv.html b/utylizaciya-plastyku-ta-polimeriv.html
index 31a193f..da565dc 100644
--- a/utylizaciya-plastyku-ta-polimeriv.html
+++ b/utylizaciya-plastyku-ta-polimeriv.html
@@ -204,7 +204,8 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації пластику та полімерів для підприємств","name":"Порядок утилізації пластику та полімерів для підприємств — Довідник YOURECO","description":"Утилізація пластику та полімерів: що приймають, як організувати збір, вивезення та документи для підприємств.","url":"https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html","inLanguage":"uk-UA"}</script>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","url":"https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html"}</script></head>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","url":"https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html","mainEntity":[{"@type":"Question","name":"Чи можна змішувати різні види пластику?","acceptedAnswer":{"@type":"Answer","text":"Для попереднього накопичення іноді це можливо, але для оцінки й приймання краще розділяти плівку, тверду тару, каністри, ящики, біг-беги, чистий і забруднений пластик. Так легше визначити подальший формат передачі."}},{"@type":"Question","name":"Що робити із забрудненими каністрами або тарою?","acceptedAnswer":{"@type":"Answer","text":"Їх потрібно виділити окремо та описати, чим саме вони забруднені, якщо ця інформація відома. Не варто змішувати таку тару з чистою плівкою або іншим пластиком без потреби."}},{"@type":"Question","name":"Які дані потрібні для попередньої оцінки?","acceptedAnswer":{"@type":"Answer","text":"Потрібні тип пластику, приблизна кількість або вага, стан, ступінь забруднення, місто, місце зберігання, пакування та інформація про те, чи потрібні документи після передачі."}},{"@type":"Question","name":"Чи можна передати браковані пластикові вироби?","acceptedAnswer":{"@type":"Answer","text":"Так, але для оцінки потрібно розуміти тип матеріалу, обсяг партії, причину списання, чи є забруднення та чи потрібно оформити підтвердні документи після передачі."}}],"inLanguage":"uk-UA"}</script></head>
 <body>
 <div class="layout">
 <!-- SIDEBAR -->
diff --git a/utylizaciya-produktiv-harchuvannya-napoyiv.html b/utylizaciya-produktiv-harchuvannya-napoyiv.html
index 3c72006..586bafc 100644
--- a/utylizaciya-produktiv-harchuvannya-napoyiv.html
+++ b/utylizaciya-produktiv-harchuvannya-napoyiv.html
@@ -204,7 +204,8 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації продуктів харчування та напоїв","name":"Порядок утилізації продуктів харчування та напоїв — Довідник YOURECO","description":"Утилізація продуктів харчування, напоїв і жирів: причини списання, класифікація, підготовка, логістика та документи.","url":"https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html","inLanguage":"uk-UA"}</script>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","url":"https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html"}</script></head>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","url":"https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html","mainEntity":[{"@type":"Question","name":"Чи можна просто викинути списані продукти у звичайний контейнер?","acceptedAnswer":{"@type":"Answer","text":"Для підприємства це небажаний варіант. Списана продукція потребує обліку, контролю та документального підтвердження передачі, особливо якщо йдеться про партії зі складу, магазину або виробництва."}},{"@type":"Question","name":"Що робити з напоями або рідкою продукцією?","acceptedAnswer":{"@type":"Answer","text":"Їх потрібно описати окремо: тип продукції, об’єм, тара, стан пакування, наявність протікань і причина списання. Не варто самостійно зливати такі партії без узгодженого порядку поводження."}},{"@type":"Question","name":"Які дані потрібні для попередньої оцінки?","acceptedAnswer":{"@type":"Answer","text":"Потрібні найменування або тип продукції, кількість, вага або об’єм, причина списання, стан пакування, місто, місце зберігання та інформація про те, чи потрібні документи після передачі."}},{"@type":"Question","name":"Чи можна передати змішані партії продуктів і напоїв?","acceptedAnswer":{"@type":"Answer","text":"Іноді це можливо, але для оцінки потрібно розуміти склад змішаної партії. Краще окремо описати сухі продукти, рідини, напої, заморожену продукцію, тару та пошкоджене пакування."}}],"inLanguage":"uk-UA"}</script></head>
 <body>
 <div class="layout">
 <!-- SIDEBAR -->
diff --git a/utylizaciya-promyslovyh-vidhodiv.html b/utylizaciya-promyslovyh-vidhodiv.html
index 49f356a..2fd64ea 100644
--- a/utylizaciya-promyslovyh-vidhodiv.html
+++ b/utylizaciya-promyslovyh-vidhodiv.html
@@ -204,7 +204,8 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації промислових відходів для підприємств","name":"Порядок утилізації промислових відходів для підприємств — Довідник YOURECO","description":"Утилізація промислових відходів: що приймають, як організувати збір, вивезення та документи для підприємств.","url":"https://guide.youreco.com.ua/utylizaciya-promyslovyh-vidhodiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-promyslovyh-vidhodiv.html","inLanguage":"uk-UA"}</script>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","url":"https://guide.youreco.com.ua/utylizaciya-promyslovyh-vidhodiv.html"}</script></head>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","url":"https://guide.youreco.com.ua/utylizaciya-promyslovyh-vidhodiv.html"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-promyslovyh-vidhodiv.html","mainEntity":[{"@type":"Question","name":"Чи можна змішувати промислові відходи зі звичайним сміттям?","acceptedAnswer":{"@type":"Answer","text":"Для підприємства це небажаний варіант. Промислові відходи можуть мати різний склад, рівень забруднення та вимоги до подальшого поводження, тому їх краще обліковувати й передавати окремо."}},{"@type":"Question","name":"Що робити, якщо склад відходів невідомий?","acceptedAnswer":{"@type":"Answer","text":"Спочатку потрібно описати походження матеріалів, процес, у якому вони утворилися, зовнішній стан, пакування та доступну інформацію від відповідальних працівників. Якщо склад неочевидний, це потрібно окремо зазначити під час попередньої оцінки."}},{"@type":"Question","name":"Які дані потрібні для попередньої оцінки?","acceptedAnswer":{"@type":"Answer","text":"Потрібні типи відходів, приблизна кількість або вага, джерело утворення, місто, місце зберігання, стан, пакування та інформація про те, чи потрібні документи після передачі."}},{"@type":"Question","name":"Чи можна передати змішану партію?","acceptedAnswer":{"@type":"Answer","text":"Іноді це можливо, але для оцінки потрібно розуміти склад змішаної партії. Краще заздалегідь відокремити різні типи матеріалів, якщо це можна зробити безпечно та без додаткового забруднення."}}],"inLanguage":"uk-UA"}</script></head>
 <body>
 <div class="layout">
 <aside class="sidebar">
diff --git a/utylizaciya-rybnyh-produktiv.html b/utylizaciya-rybnyh-produktiv.html
index df75e9c..e207a9b 100644
--- a/utylizaciya-rybnyh-produktiv.html
+++ b/utylizaciya-rybnyh-produktiv.html
@@ -200,6 +200,7 @@
 .breadcrumbs a:hover{text-decoration:underline}
 .breadcrumbs span{opacity:.8}</style>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Куди передають рибні продукти на утилізацію","name":"Куди передають рибні продукти на утилізацію — Довідник YOURECO","description":"Довідка для підприємств про «утилізацію рибних продуктів»: що включає, як підготувати партію, правила зберігання, логістика, документи та типові помилки.","url":"https://guide.youreco.com.ua/utylizaciya-rybnyh-produktiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-rybnyh-produktiv.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-rybnyh-produktiv.html","mainEntity":[{"@type":"Question","name":"Що фіксувати для рибної партії?","acceptedAnswer":{"@type":"Answer","text":"Зазвичай зазначають вид продукції, стан, температуру зберігання, тару, наявність запаху, рідини або пошкоджень."}},{"@type":"Question","name":"Чи потрібно відокремлювати пакування?","acceptedAnswer":{"@type":"Answer","text":"Так, якщо це можливо в межах внутрішнього процесу; принаймні пакування варто описати окремо."}},{"@type":"Question","name":"Чому важливий температурний режим?","acceptedAnswer":{"@type":"Answer","text":"Він пояснює стан продукції на момент списання і допомагає відтворити логіку поводження з партією."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-shyn.html b/utylizaciya-shyn.html
index d9feed4..836bed6 100644
--- a/utylizaciya-shyn.html
+++ b/utylizaciya-shyn.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як оформлюється утилізація шин","name":"Як оформлюється утилізація шин — Довідник YOURECO","description":"Утилізація шин: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника YOURECO.","url":"https://guide.youreco.com.ua/utylizaciya-shyn.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-shyn.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-shyn.html","mainEntity":[{"@type":"Question","name":"Чи можна викидати відпрацьовані шини у звичайний контейнер?","acceptedAnswer":{"@type":"Answer","text":"Для підприємства це небажаний варіант. Шини займають значний об’єм, потребують окремого обліку та мають передаватися окремо від звичайних побутових або офісних відходів."}},{"@type":"Question","name":"Чи приймаються шини з дисками?","acceptedAnswer":{"@type":"Answer","text":"Це потрібно уточнювати окремо під час попередньої оцінки. Шини з дисками краще вказати як окрему позицію, тому що умови приймання та підготовки можуть відрізнятися."}},{"@type":"Question","name":"Які дані потрібні для попередньої оцінки?","acceptedAnswer":{"@type":"Answer","text":"Потрібні тип шин, приблизна кількість або вага, місто, місце зберігання, наявність дисків, нестандартних розмірів або сильного забруднення."}},{"@type":"Question","name":"Чи потрібно сортувати шини перед передачею?","acceptedAnswer":{"@type":"Answer","text":"Бажано хоча б розділити легкові, вантажні, індустріальні та нестандартні шини. Це спрощує оцінку партії, погодження умов вивезення та подальше приймання."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html b/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
index d6c3179..3ed5ceb 100644
--- a/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
+++ b/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
@@ -200,6 +200,7 @@
 .breadcrumbs a:hover{text-decoration:underline}
 .breadcrumbs span{opacity:.8}</style>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації складських залишків косметики","name":"Порядок утилізації складських залишків косметики — Довідник YOURECO","description":"Утилізація складських залишків косметики: підготовка партії, правила зберігання, логістика, документи та типові помилки.","url":"https://guide.youreco.com.ua/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html","mainEntity":[{"@type":"Question","name":"Що належить до складських залишків косметики?","acceptedAnswer":{"@type":"Answer","text":"Це продукція і пакування, що залишилися після інвентаризації, повернень, пошкоджень або завершення строку придатності."}},{"@type":"Question","name":"Чому важливо розділяти рідини і тару?","acceptedAnswer":{"@type":"Answer","text":"Рідини та креми можуть забруднювати упаковку, змінювати її стан і впливати на опис партії."}},{"@type":"Question","name":"Що фіксувати під час групування?","acceptedAnswer":{"@type":"Answer","text":"Категорію товару, тару, стан упаковки, кількість, маркування, наявність протікань і змішаних матеріалів."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-sonyachnih-panelij-vitryakiv.html b/utylizaciya-sonyachnih-panelij-vitryakiv.html
index 163e939..ba07a9e 100644
--- a/utylizaciya-sonyachnih-panelij-vitryakiv.html
+++ b/utylizaciya-sonyachnih-panelij-vitryakiv.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як оформлюється утилізація сонячних панелей та лопатей ВЕС","name":"Як оформлюється утилізація сонячних панелей та лопатей ВЕС — Довідник YOURECO","description":"Утилізація сонячних панелей і лопатей ВЕС: компоненти, демонтаж, логістика, переробка композитів та документи.","url":"https://guide.youreco.com.ua/utylizaciya-sonyachnih-panelij-vitryakiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-sonyachnih-panelij-vitryakiv.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-sonyachnih-panelij-vitryakiv.html","mainEntity":[{"@type":"Question","name":"Чи можна передати сонячні панелі разом з інверторами та кабелем?","acceptedAnswer":{"@type":"Answer","text":"Іноді це можливо, але для оцінки краще окремо описати панелі, інвертори, кабель, кріплення, акумулятори та інші компоненти. Так простіше визначити формат приймання і вивезення."}},{"@type":"Question","name":"Чи потрібно самостійно розбирати сонячні панелі або інвертори?","acceptedAnswer":{"@type":"Answer","text":"Ні, без потреби цього робити не варто. Якщо демонтаж або розбирання потребує спеціальної компетенції, краще передати обладнання як окрему позицію та описати його стан."}},{"@type":"Question","name":"Які дані потрібні для попередньої оцінки?","acceptedAnswer":{"@type":"Answer","text":"Потрібні тип обладнання, кількість одиниць, орієнтовна вага або габарити, місто, місце зберігання, стан, наявність пошкоджень, умови доступу та інформація про те, чи потрібні документи після передачі."}},{"@type":"Question","name":"Що робити з акумуляторними модулями від енергетичної системи?","acceptedAnswer":{"@type":"Answer","text":"Їх потрібно описати окремо від панелей, кріплень і кабелю. Не варто самостійно розбирати або пошкоджувати акумуляторні блоки, особливо якщо є здуття, перегрів або інші ознаки несправності."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-tary-upakovki.html b/utylizaciya-tary-upakovki.html
index 6921af2..d16040c 100644
--- a/utylizaciya-tary-upakovki.html
+++ b/utylizaciya-tary-upakovki.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як оформлюється утилізація тари та упаковки","name":"Як оформлюється утилізація тари та упаковки — Довідник YOURECO","description":"Утилізація тари й упаковки: етикетки, плівка, картон, контейнери, піддони, біг-беги, розділення фракцій і документи.","url":"https://guide.youreco.com.ua/utylizaciya-tary-upakovki.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-tary-upakovki.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-tary-upakovki.html","mainEntity":[{"@type":"Question","name":"Чи можна передати змішану тару й упаковку?","acceptedAnswer":{"@type":"Answer","text":"Іноді це можливо, але для оцінки краще окремо описати картон, плівку, пластик, каністри, дерево, скло, метал і забруднену тару. Так простіше визначити формат приймання."}},{"@type":"Question","name":"Що робити із забрудненою тарою?","acceptedAnswer":{"@type":"Answer","text":"Її потрібно виділити окремо та описати, чим саме вона забруднена, якщо ця інформація відома. Не варто змішувати таку тару з чистим картоном, плівкою або іншими матеріалами без потреби."}},{"@type":"Question","name":"Які дані потрібні для попередньої оцінки?","acceptedAnswer":{"@type":"Answer","text":"Потрібні тип тари, приблизна кількість, вага або об’єм, стан, ступінь забруднення, місто, місце зберігання, пакування та інформація про те, чи потрібні документи після передачі."}},{"@type":"Question","name":"Чи можна повторно використовувати тару після списання?","acceptedAnswer":{"@type":"Answer","text":"Це залежить від її стану, походження та внутрішнього рішення підприємства. Якщо тара забруднена, пошкоджена або вже списана як відхід, її краще не повертати в обіг без окремої оцінки."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-tovary-pid-mitnim-kontrolem.html b/utylizaciya-tovary-pid-mitnim-kontrolem.html
index 905bbcd..c5c58e0 100644
--- a/utylizaciya-tovary-pid-mitnim-kontrolem.html
+++ b/utylizaciya-tovary-pid-mitnim-kontrolem.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації товарів під митним контролем","name":"Порядок утилізації товарів під митним контролем — Довідник YOURECO","description":"Утилізація товарів під митним контролем: контрафакт, брак, повернення, конфіскат, методи знищення та пакет документів.","url":"https://guide.youreco.com.ua/utylizaciya-tovary-pid-mitnim-kontrolem.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-tovary-pid-mitnim-kontrolem.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-tovary-pid-mitnim-kontrolem.html","mainEntity":[{"@type":"Question","name":"Чи можна просто вивезти товари під митним контролем як звичайні відходи?","acceptedAnswer":{"@type":"Answer","text":"Ні, без попереднього визначення статусу партії цього робити не варто. Потрібно врахувати документи, облік, відповідальних учасників процесу та підтвердження фактичної передачі."}},{"@type":"Question","name":"Які дані потрібні для попередньої оцінки?","acceptedAnswer":{"@type":"Answer","text":"Потрібні найменування товару, кількість, вага або об’єм, причина списання, стан пакування, місце зберігання, наявність супровідних документів і інформація про те, чи потрібні документи після передачі."}},{"@type":"Question","name":"Чи можна передати змішану партію товарів?","acceptedAnswer":{"@type":"Answer","text":"Іноді це можливо, але для оцінки краще окремо описати групи товарів, кількість, стан, пакування та причину списання для кожної групи."}},{"@type":"Question","name":"Чи замінює передача на утилізацію митне оформлення?","acceptedAnswer":{"@type":"Answer","text":"Ні. Передача на утилізацію не повинна підміняти митну або внутрішню юридичну процедуру. Підприємству потрібно діяти відповідно до статусу товару та погодженого порядку."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-vidpracovanoi-olyvy.html b/utylizaciya-vidpracovanoi-olyvy.html
index 5472a63..e46d95a 100644
--- a/utylizaciya-vidpracovanoi-olyvy.html
+++ b/utylizaciya-vidpracovanoi-olyvy.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Утилізація відпрацьованої оливи для бізнесу","name":"Утилізація відпрацьованої оливи для бізнесу — YOURECO","description":"Дізнайтеся, як підприємству зібрати, передати й документально оформити утилізацію відпрацьованої моторної оливи.","url":"https://guide.youreco.com.ua/utylizaciya-vidpracovanoi-olyvy.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-vidpracovanoi-olyvy.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-vidpracovanoi-olyvy.html","mainEntity":[{"@type":"Question","name":"Чи можна зливати відпрацьовану оливу в каналізацію або на землю?","acceptedAnswer":{"@type":"Answer","text":"Ні, цього не варто робити. Для підприємства це ризиковий спосіб поводження з технічними рідинами. Відпрацьовану оливу потрібно накопичувати окремо та передавати з підтвердними документами."}},{"@type":"Question","name":"Чи можна змішувати оливу з антифризом, водою або паливом?","acceptedAnswer":{"@type":"Answer","text":"Без потреби цього робити не варто. Змішування різних рідин ускладнює оцінку, приймання та подальше поводження з партією."}},{"@type":"Question","name":"Які дані потрібні для попередньої оцінки?","acceptedAnswer":{"@type":"Answer","text":"Потрібні тип оливи, приблизний об’єм або вага, походження, місто, місце зберігання, тип тари, наявність домішок і інформація про те, чи потрібні документи після передачі."}},{"@type":"Question","name":"У якій тарі зберігати відпрацьовану оливу до передачі?","acceptedAnswer":{"@type":"Answer","text":"Найкраще використовувати герметичну, стійку та підписану тару, яка не протікає й дозволяє безпечно накопичувати матеріал до моменту передачі."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-zamorozhenyh-produktiv.html b/utylizaciya-zamorozhenyh-produktiv.html
index 999f95a..8e2c27f 100644
--- a/utylizaciya-zamorozhenyh-produktiv.html
+++ b/utylizaciya-zamorozhenyh-produktiv.html
@@ -200,6 +200,7 @@
 .breadcrumbs a:hover{text-decoration:underline}
 .breadcrumbs span{opacity:.8}</style>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Куди передають заморожені продукти на утилізацію","name":"Куди передають заморожені продукти на утилізацію — Довідник YOURECO","description":"Довідка для підприємств про «утилізацію заморожених продуктів»: що включає, як підготувати партію, правила зберігання, логістика, документи та типові помилки.","url":"https://guide.youreco.com.ua/utylizaciya-zamorozhenyh-produktiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-zamorozhenyh-produktiv.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya-zamorozhenyh-produktiv.html","mainEntity":[{"@type":"Question","name":"Чи обов'язково вказувати температурну подію в документах?","acceptedAnswer":{"@type":"Answer","text":"Так, це ключова підстава, чому партія не може повернутися в реалізацію."}},{"@type":"Question","name":"Чи можна передавати змішані заморожені групи в одному рейсі?","acceptedAnswer":{"@type":"Answer","text":"Можна, але в реєстрі їх варто розділити за категоріями і станом."}},{"@type":"Question","name":"Чи заморожені продукти завжди безпечні до моменту розморожування?","acceptedAnswer":{"@type":"Answer","text":"Ні. Стан залежить від температурної історії, цілісності упаковки, строків зберігання та умов транспортування."}},{"@type":"Question","name":"Чому важливо описувати тару?","acceptedAnswer":{"@type":"Answer","text":"Тара може бути окремою фракцією або змішаною з органічними залишками, тому її стан впливає на загальний опис партії."}},{"@type":"Question","name":"Що робити зі змішаною партією?","acceptedAnswer":{"@type":"Answer","text":"Її зазвичай описують як змішаний потік із зазначенням основних груп продуктів, упаковки, стану та приблизного обсягу."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya.html b/utylizaciya.html
index 65b465b..8d68d95 100644
--- a/utylizaciya.html
+++ b/utylizaciya.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","headline":"Порядок утилізації відходів для підприємств","name":"Порядок утилізації відходів для підприємств — Довідник YOURECO","description":"Огляд утилізації відходів для підприємств: як підготувати партію, оформити документи й обрати правильний сценарій.","url":"https://guide.youreco.com.ua/utylizaciya.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/utylizaciya.html","mainEntity":[{"@type":"Question","name":"Чи будь-які відходи треба одразу вважати такими, що підлягають утилізації?","acceptedAnswer":{"@type":"Answer","text":"Ні. Спочатку треба оцінити склад, домішки, стан партії та можливість відокремити придатні до переробки фракції."}},{"@type":"Question","name":"Коли погоджувати вивезення з підрядником?","acceptedAnswer":{"@type":"Answer","text":"Тоді, коли підприємство вже може описати фактичний стан партії, її орієнтовний обсяг і умови доступу до місця завантаження."}},{"@type":"Question","name":"Що найчастіше ускладнює утилізацію?","acceptedAnswer":{"@type":"Answer","text":"Змішування різних потоків, відсутність маркування, неточний опис складу та підготовка документів уже після фактичного вивезення."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 
diff --git a/vidhody.html b/vidhody.html
index bc08819..99e7a6c 100644
--- a/vidhody.html
+++ b/vidhody.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","headline":"Види відходів і поводження з ними","name":"Види відходів і поводження з ними — Довідник YOURECO","description":"Довідник за видами відходів: як визначити потік, оцінити ризики змішування та підготувати партію до передачі.","url":"https://guide.youreco.com.ua/vidhody.html","mainEntityOfPage":"https://guide.youreco.com.ua/vidhody.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/vidhody.html","mainEntity":[{"@type":"Question","name":"Чи достатньо знати лише назву матеріалу?","acceptedAnswer":{"@type":"Answer","text":"Ні. Потрібно враховувати походження потоку, домішки, стан партії і спосіб накопичення."}},{"@type":"Question","name":"Коли потік треба виділяти окремо?","acceptedAnswer":{"@type":"Answer","text":"Коли він має інший маршрут поводження, інший склад або окремі умови зберігання і передачі."}},{"@type":"Question","name":"Що найчастіше заважає правильній класифікації?","acceptedAnswer":{"@type":"Answer","text":"Змішування різних матеріалів ще на етапі первинного збору та відсутність опису місця утворення."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 
diff --git a/zbir.html b/zbir.html
index ec4589f..ae4075f 100644
--- a/zbir.html
+++ b/zbir.html
@@ -204,6 +204,7 @@
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","headline":"Збір відходів на підприємстві","name":"Збір відходів на підприємстві — Довідник YOURECO","description":"Як організувати збір відходів на підприємстві: місця накопичення, сортування, підготовка партії та передача підряднику.","url":"https://guide.youreco.com.ua/zbir.html","mainEntityOfPage":"https://guide.youreco.com.ua/zbir.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua/zbir.html","mainEntity":[{"@type":"Question","name":"Чи обов'язково мати багато контейнерів?","acceptedAnswer":{"@type":"Answer","text":"Ні. Важливіше визначити ключові потоки, правильні точки їх утворення і зрозуміле маркування."}},{"@type":"Question","name":"Що робити зі змішаними залишками?","acceptedAnswer":{"@type":"Answer","text":"Виділяти окремо й погоджувати їхній маршрут окремо, а не домішувати до чистих фракцій."}},{"@type":"Question","name":"Коли збір можна вважати контрольованим?","acceptedAnswer":{"@type":"Answer","text":"Коли для кожного основного потоку є місце, відповідальна особа і зрозумілий порядок подальшого переміщення."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
 
```

## 6. git diff --name-only HEAD^ HEAD
```
akt-utylizaciyi.html
dokumenty.html
faq-schema-fix-report.md
fotozvit-utylizaciyi.html
index.html
kudy-zdaty.html
pererobka-avtomobilnyh-shyn.html
pererobka-skla.html
pererobka.html
sortuvannya.html
utylizaciya-dokumentiv.html
utylizaciya-gazovanyh-napoyiv.html
utylizaciya-kabelyu-ta-drotiv.html
utylizaciya-konserviv.html
utylizaciya-li-ion-batarej.html
utylizaciya-myasnyh-produktiv.html
utylizaciya-nekondicijnoyi-sirovini.html
utylizaciya-odyagu-vzuttya.html
utylizaciya-plastyku-ta-polimeriv.html
utylizaciya-produktiv-harchuvannya-napoyiv.html
utylizaciya-promyslovyh-vidhodiv.html
utylizaciya-rybnyh-produktiv.html
utylizaciya-shyn.html
utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
utylizaciya-sonyachnih-panelij-vitryakiv.html
utylizaciya-tary-upakovki.html
utylizaciya-tovary-pid-mitnim-kontrolem.html
utylizaciya-vidpracovanoi-olyvy.html
utylizaciya-zamorozhenyh-produktiv.html
utylizaciya.html
vidhody.html
zbir.html
```

## 7. git diff --numstat HEAD^ HEAD
```
1	0	akt-utylizaciyi.html
1	0	dokumenty.html
91	0	faq-schema-fix-report.md
1	0	fotozvit-utylizaciyi.html
1	1	index.html
1	0	kudy-zdaty.html
1	0	pererobka-avtomobilnyh-shyn.html
1	0	pererobka-skla.html
1	0	pererobka.html
1	0	sortuvannya.html
1	0	utylizaciya-dokumentiv.html
1	0	utylizaciya-gazovanyh-napoyiv.html
1	0	utylizaciya-kabelyu-ta-drotiv.html
1	0	utylizaciya-konserviv.html
1	0	utylizaciya-li-ion-batarej.html
1	0	utylizaciya-myasnyh-produktiv.html
1	0	utylizaciya-nekondicijnoyi-sirovini.html
1	0	utylizaciya-odyagu-vzuttya.html
2	1	utylizaciya-plastyku-ta-polimeriv.html
2	1	utylizaciya-produktiv-harchuvannya-napoyiv.html
2	1	utylizaciya-promyslovyh-vidhodiv.html
1	0	utylizaciya-rybnyh-produktiv.html
1	0	utylizaciya-shyn.html
1	0	utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
1	0	utylizaciya-sonyachnih-panelij-vitryakiv.html
1	0	utylizaciya-tary-upakovki.html
1	0	utylizaciya-tovary-pid-mitnim-kontrolem.html
1	0	utylizaciya-vidpracovanoi-olyvy.html
1	0	utylizaciya-zamorozhenyh-produktiv.html
1	0	utylizaciya.html
1	0	vidhody.html
1	0	zbir.html
```

## faq-schema-fix-report.md
```markdown
# FAQ Schema Fix Report

## Summary
- index files changed: 31
- FAQPage JSON-LD added: 30
- FAQPage JSON-LD updated: 1
- noindex files changed: 0
- body text changed: 0
- title changed: 0
- H1 changed: 0
- canonical changed: 0
- meta description changed: 0
- public changed: 0
- dist changed: 0

## Changed Files
- akt-utylizaciyi.html
- dokumenty.html
- fotozvit-utylizaciyi.html
- index.html
- kudy-zdaty.html
- pererobka-avtomobilnyh-shyn.html
- pererobka-skla.html
- pererobka.html
- sortuvannya.html
- utylizaciya-dokumentiv.html
- utylizaciya-gazovanyh-napoyiv.html
- utylizaciya-kabelyu-ta-drotiv.html
- utylizaciya-konserviv.html
- utylizaciya-li-ion-batarej.html
- utylizaciya-myasnyh-produktiv.html
- utylizaciya-nekondicijnoyi-sirovini.html
- utylizaciya-odyagu-vzuttya.html
- utylizaciya-plastyku-ta-polimeriv.html
- utylizaciya-produktiv-harchuvannya-napoyiv.html
- utylizaciya-promyslovyh-vidhodiv.html
- utylizaciya-rybnyh-produktiv.html
- utylizaciya-shyn.html
- utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
- utylizaciya-sonyachnih-panelij-vitryakiv.html
- utylizaciya-tary-upakovki.html
- utylizaciya-tovary-pid-mitnim-kontrolem.html
- utylizaciya-vidpracovanoi-olyvy.html
- utylizaciya-zamorozhenyh-produktiv.html
- utylizaciya.html
- vidhody.html
- zbir.html
- faq-schema-fix-report.md

## Validation
- remaining index FAQ mismatch: 0
- JSON-LD parse errors: 0
- FAQ count mismatch: 0
- FAQ text mismatch: 0

## Git Status
```
M  akt-utylizaciyi.html
M  dokumenty.html
A  faq-schema-fix-report.md
M  fotozvit-utylizaciyi.html
M  index.html
M  kudy-zdaty.html
M  pererobka-avtomobilnyh-shyn.html
M  pererobka-skla.html
M  pererobka.html
M  sortuvannya.html
M  utylizaciya-dokumentiv.html
M  utylizaciya-gazovanyh-napoyiv.html
M  utylizaciya-kabelyu-ta-drotiv.html
M  utylizaciya-konserviv.html
M  utylizaciya-li-ion-batarej.html
M  utylizaciya-myasnyh-produktiv.html
M  utylizaciya-nekondicijnoyi-sirovini.html
M  utylizaciya-odyagu-vzuttya.html
M  utylizaciya-plastyku-ta-polimeriv.html
M  utylizaciya-produktiv-harchuvannya-napoyiv.html
M  utylizaciya-promyslovyh-vidhodiv.html
M  utylizaciya-rybnyh-produktiv.html
M  utylizaciya-shyn.html
M  utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
M  utylizaciya-sonyachnih-panelij-vitryakiv.html
M  utylizaciya-tary-upakovki.html
M  utylizaciya-tovary-pid-mitnim-kontrolem.html
M  utylizaciya-vidpracovanoi-olyvy.html
M  utylizaciya-zamorozhenyh-produktiv.html
M  utylizaciya.html
M  vidhody.html
M  zbir.html
?? faq-schema-audit.md
```
```
