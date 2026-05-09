# JSON-LD Description Evidence

## 1. git status --short
```txt
?? meta-schema-audit.md
?? sitemap-add-evidence.md
```

## 2. git log --oneline -5
```txt
01e903a align json-ld descriptions with meta descriptions
fd601e1 add missing index urls to sitemap
3a5382e add duplicate and build structure audit reports
7e2f919 update fixed sitemap validation report
7dbff4b add independent sitemap validation checks
```

## 3. git show --name-only --oneline HEAD
```txt
01e903a align json-ld descriptions with meta descriptions
index.html
jsonld-description-fix-report.md
kabelni-vidhody.html
povernennya-tovariv-z-merezhi.html
spysannya-produkciyi.html
utylizaciya-dokumentiv.html
utylizaciya-li-ion-batarej.html
utylizaciya-nekondicijnoyi-sirovini.html
utylizaciya-odyagu-vzuttya.html
utylizaciya-ofisnih-mebliv-orgtehniki.html
utylizaciya-paverbankiv-dbj.html
utylizaciya-plastyku-ta-polimeriv.html
utylizaciya-produktiv-harchuvannya-napoyiv.html
utylizaciya-promyslovyh-vidhodiv.html
utylizaciya-prostrochenyh-produktiv.html
utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
utylizaciya-sonyachnih-panelij-vitryakiv.html
utylizaciya-tary-upakovki.html
utylizaciya-tovary-pid-mitnim-kontrolem.html
```

## 4. git show --stat --oneline HEAD
```txt
01e903a align json-ld descriptions with meta descriptions
 index.html                                      |  2 +-
 jsonld-description-fix-report.md                | 65 +++++++++++++++++++++++++
 kabelni-vidhody.html                            |  2 +-
 povernennya-tovariv-z-merezhi.html              |  2 +-
 spysannya-produkciyi.html                       |  2 +-
 utylizaciya-dokumentiv.html                     |  2 +-
 utylizaciya-li-ion-batarej.html                 |  2 +-
 utylizaciya-nekondicijnoyi-sirovini.html        |  2 +-
 utylizaciya-odyagu-vzuttya.html                 |  2 +-
 utylizaciya-ofisnih-mebliv-orgtehniki.html      |  2 +-
 utylizaciya-paverbankiv-dbj.html                |  2 +-
 utylizaciya-plastyku-ta-polimeriv.html          |  2 +-
 utylizaciya-produktiv-harchuvannya-napoyiv.html |  2 +-
 utylizaciya-promyslovyh-vidhodiv.html           |  2 +-
 utylizaciya-prostrochenyh-produktiv.html        |  2 +-
 utylizaciya-skladskyh-zalyshkiv-kosmetyky.html  |  2 +-
 utylizaciya-sonyachnih-panelij-vitryakiv.html   |  2 +-
 utylizaciya-tary-upakovki.html                  |  2 +-
 utylizaciya-tovary-pid-mitnim-kontrolem.html    |  2 +-
 19 files changed, 83 insertions(+), 18 deletions(-)
```

## 5. git diff HEAD^ HEAD -- "*.html"
```diff
diff --git a/index.html b/index.html
index c2718fd..20f6181 100644
--- a/index.html
+++ b/index.html
@@ -159,7 +159,7 @@
 <!-- Schema.org (WebSite) -->
 <!-- Schema.org (AboutPage) -->
 <!-- Schema.org (ItemList: structure of the guide) -->
-<link href="https://guide.youreco.com.ua/" hreflang="uk" rel="alternate"/><script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","headline":"Довідник YOURECO про поводження з відходами для підприємств","name":"Довідник YOURECO | як підприємствам організувати поводження з відходами — Довідник YOURECO","description":"Довідник YOURECO з промислових, небезпечних та комерційних відходів для підприємств України. Практичні інструкції підготовки відходів, типові ризики, документи та поширені сценарії утилізації.","url":"https://guide.youreco.com.ua","mainEntityOfPage":"https://guide.youreco.com.ua","inLanguage":"uk-UA"}</script>
+<link href="https://guide.youreco.com.ua/" hreflang="uk" rel="alternate"/><script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","headline":"Довідник YOURECO про поводження з відходами для підприємств","name":"Довідник YOURECO | як підприємствам організувати поводження з відходами — Довідник YOURECO","description":"Довідник YOURECO про відходи для підприємств України: утилізація, переробка, сортування, логістика, документи та типові ризики.","url":"https://guide.youreco.com.ua","mainEntityOfPage":"https://guide.youreco.com.ua","inLanguage":"uk-UA"}</script>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","url":"https://guide.youreco.com.ua","mainEntity":[{"@type":"Question","name":"Чим відрізняється переробка від утилізації та знешкодження?","acceptedAnswer":{"@type":"Answer","text":"Переробка повертає матеріали у вторинний обіг. Утилізація — ширше поняття, яке може включати переробку. Знешкодження застосовують, коли переробка неможлива або є небезпека."}},{"@type":"Question","name":"Чому важливо мати документи на утилізацію?","acceptedAnswer":{"@type":"Answer","text":"Документи підтверджують факт передачі відходів та коректне поводження з ними для внутрішнього обліку, контрагентів і перевірок."}},{"@type":"Question","name":"Що найчастіше “ламає” приймання відходів?","acceptedAnswer":{"@type":"Answer","text":"Змішування несумісних фракцій, відсутність маркування, протікання тари, наявність сторонніх домішок або небезпечних компонентів без попередження."}},{"@type":"Question","name":"Чи можна підготувати відходи заздалегідь, щоб зменшити вартість?","acceptedAnswer":{"@type":"Answer","text":"Так: сортування, зняття зайвого пакування, правильна тара й компактне складування майже завжди зменшують витрати на логістику та обробку."}},{"@type":"Question","name":"Де знайти практичні інструкції щодо конкретного виду відходів?","acceptedAnswer":{"@type":"Answer","text":"Оберіть розділ зліва. У кожному матеріалі є короткі правила підготовки, типові ризики та базовий комплект документів."}}],"inLanguage":"uk-UA"}</script>
 </head>
 <body>
diff --git a/kabelni-vidhody.html b/kabelni-vidhody.html
index 45d3894..4028851 100644
--- a/kabelni-vidhody.html
+++ b/kabelni-vidhody.html
@@ -203,7 +203,7 @@
 .breadcrumbs span{opacity:.8}</style>
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Кабельні відходи: класифікація та зберігання","name":"Кабельні відходи: класифікація та зберігання — Довідник YOURECO","description":"Кабельні відходи: класифікація та зберігання: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника…","url":"https://guide.youreco.com.ua/kabelni-vidhody.html","mainEntityOfPage":"https://guide.youreco.com.ua/kabelni-vidhody.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Кабельні відходи: класифікація та зберігання","name":"Кабельні відходи: класифікація та зберігання — Довідник YOURECO","description":"Кабельні відходи: класифікація, зберігання, підготовка до передачі, організація вивезення та документи для підприємств.","url":"https://guide.youreco.com.ua/kabelni-vidhody.html","mainEntityOfPage":"https://guide.youreco.com.ua/kabelni-vidhody.html","inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/povernennya-tovariv-z-merezhi.html b/povernennya-tovariv-z-merezhi.html
index 7820993..3ead23c 100644
--- a/povernennya-tovariv-z-merezhi.html
+++ b/povernennya-tovariv-z-merezhi.html
@@ -63,7 +63,7 @@
 .breadcrumbs span{opacity:.8}</style>
 
 <link href="/styles.css" rel="stylesheet"/>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Повернення товарів з мережі: коли партія переходить на утилізацію","name":"Повернення товарів з мережі: коли партія переходить на утилізацію — Довідник YOURECO","description":"Повернення товарів з мережі охоплює логістику зворотного руху продукції з магазинів, дистриб","url":"https://guide.youreco.com.ua/povernennya-tovariv-z-merezhi.html","mainEntityOfPage":"https://guide.youreco.com.ua/povernennya-tovariv-z-merezhi.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Повернення товарів з мережі: коли партія переходить на утилізацію","name":"Повернення товарів з мережі: коли партія переходить на утилізацію — Довідник YOURECO","description":"Повернення товарів з мережі охоплює логістику зворотного руху продукції з магазинів, дистриб'юторських точок або партнерських майданчиків до складу чи центру прийняття рішень.","url":"https://guide.youreco.com.ua/povernennya-tovariv-z-merezhi.html","mainEntityOfPage":"https://guide.youreco.com.ua/povernennya-tovariv-z-merezhi.html","inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/spysannya-produkciyi.html b/spysannya-produkciyi.html
index fbce50e..0dec7b7 100644
--- a/spysannya-produkciyi.html
+++ b/spysannya-produkciyi.html
@@ -63,7 +63,7 @@
 .breadcrumbs span{opacity:.8}</style>
 
 <link href="/styles.css" rel="stylesheet"/>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Списання продукції: як рішення переходить у процедуру утилізації","name":"Списання продукції: як рішення переходить у процедуру утилізації — Довідник YOURECO","description":"Списання продукції є внутрішнім рішенням підприємства про виведення товарів або матеріалів з обліку перед передачею на утилізацію, переробку або інше контрольоване поводження.","url":"https://guide.youreco.com.ua/spysannya-produkciyi.html","mainEntityOfPage":"https://guide.youreco.com.ua/spysannya-produkciyi.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Списання продукції: як рішення переходить у процедуру утилізації","name":"Списання продукції: як рішення переходить у процедуру утилізації — Довідник YOURECO","description":"Списання продукції: як підприємство виводить товари чи матеріали з обліку перед утилізацією, переробкою або передачею.","url":"https://guide.youreco.com.ua/spysannya-produkciyi.html","mainEntityOfPage":"https://guide.youreco.com.ua/spysannya-produkciyi.html","inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-dokumentiv.html b/utylizaciya-dokumentiv.html
index 4609171..e80383f 100644
--- a/utylizaciya-dokumentiv.html
+++ b/utylizaciya-dokumentiv.html
@@ -203,7 +203,7 @@
 .breadcrumbs span{opacity:.8}</style>
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як оформлюється утилізація конфіденційних документів","name":"Як оформлюється утилізація конфіденційних документів — Довідник YOURECO","description":"Безпечна утилізація конфіденційних документів: паперу, архівів, бухгалтерських та юридичних документів, носіїв даних. Гарантоване знищення та документи для звітності.","url":"https://guide.youreco.com.ua/utylizaciya-dokumentiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-dokumentiv.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як оформлюється утилізація конфіденційних документів","name":"Як оформлюється утилізація конфіденційних документів — Довідник YOURECO","description":"Утилізація конфіденційних документів: папір, архіви, бухгалтерські й юридичні документи, носії даних та підтвердження знищення.","url":"https://guide.youreco.com.ua/utylizaciya-dokumentiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-dokumentiv.html","inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-li-ion-batarej.html b/utylizaciya-li-ion-batarej.html
index 2d31886..1fce268 100644
--- a/utylizaciya-li-ion-batarej.html
+++ b/utylizaciya-li-ion-batarej.html
@@ -203,7 +203,7 @@
 .breadcrumbs span{opacity:.8}</style>
 <!-- Schema.org: TechArticle про Li-ion батареї -->
 <link href="/styles.css" rel="stylesheet"/>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як оформлюється утилізація літій-іонних батарей","name":"Як оформлюється утилізація літій-іонних батарей — Довідник YOURECO","description":"Правильна утилізація літій-іонних (Li-ion) батарей та акумуляторних модулів для підприємств. Основні ризики, етапи утилізації, документи та рекомендації з тимчасового зберігання.","url":"https://guide.youreco.com.ua/utylizaciya-li-ion-batarej.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-li-ion-batarej.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як оформлюється утилізація літій-іонних батарей","name":"Як оформлюється утилізація літій-іонних батарей — Довідник YOURECO","description":"Утилізація Li-ion батарей для підприємств: ризики, підготовка, тимчасове зберігання, етапи передачі та документи.","url":"https://guide.youreco.com.ua/utylizaciya-li-ion-batarej.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-li-ion-batarej.html","inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-nekondicijnoyi-sirovini.html b/utylizaciya-nekondicijnoyi-sirovini.html
index cdecd82..2117b50 100644
--- a/utylizaciya-nekondicijnoyi-sirovini.html
+++ b/utylizaciya-nekondicijnoyi-sirovini.html
@@ -203,7 +203,7 @@
 .breadcrumbs span{opacity:.8}</style>
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації некондиційної сировини та продукції","name":"Порядок утилізації некондиційної сировини та продукції — Довідник YOURECO","description":"Утилізація некондиційної сировини та продукції: прострочені партії, порушення умов зберігання, брак, рекламації. Від харчової сировини до косметичних компонентів та хімічних інгредієнтів.","url":"https://guide.youreco.com.ua/utylizaciya-nekondicijnoyi-sirovini.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-nekondicijnoyi-sirovini.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації некондиційної сировини та продукції","name":"Порядок утилізації некондиційної сировини та продукції — Довідник YOURECO","description":"Утилізація некондиційної сировини та продукції: прострочені партії, брак, порушення зберігання, рекламації й документи.","url":"https://guide.youreco.com.ua/utylizaciya-nekondicijnoyi-sirovini.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-nekondicijnoyi-sirovini.html","inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-odyagu-vzuttya.html b/utylizaciya-odyagu-vzuttya.html
index 7f9d729..01f3b2a 100644
--- a/utylizaciya-odyagu-vzuttya.html
+++ b/utylizaciya-odyagu-vzuttya.html
@@ -203,7 +203,7 @@
 .breadcrumbs span{opacity:.8}</style>
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Куди передають одяг та взуття на утилізацію","name":"Куди передають одяг та взуття на утилізацію — Довідник YOURECO","description":"Утилізація одягу та взуття для підприємств: списання, надлишки, брак, корпоративна форма, контрафакт. Практична підготовка до передачі, контроль повторного обігу, типові помилки та документи, що підтверджують знищення/утилізацію.","url":"https://guide.youreco.com.ua/utylizaciya-odyagu-vzuttya.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-odyagu-vzuttya.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Куди передають одяг та взуття на утилізацію","name":"Куди передають одяг та взуття на утилізацію — Довідник YOURECO","description":"Утилізація одягу та взуття для підприємств: списання, брак, надлишки, корпоративна форма, контроль повторного обігу й документи.","url":"https://guide.youreco.com.ua/utylizaciya-odyagu-vzuttya.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-odyagu-vzuttya.html","inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-ofisnih-mebliv-orgtehniki.html b/utylizaciya-ofisnih-mebliv-orgtehniki.html
index df149a9..f7e1389 100644
--- a/utylizaciya-ofisnih-mebliv-orgtehniki.html
+++ b/utylizaciya-ofisnih-mebliv-orgtehniki.html
@@ -203,7 +203,7 @@
 .breadcrumbs span{opacity:.8}</style>
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації офісних меблів та оргтехніки","name":"Порядок утилізації офісних меблів та оргтехніки — Довідник YOURECO","description":"Утилізація офісних меблів та оргтехніки для підприємств: WEEE та небезпечні компоненти, ризики витоку даних, підготовка до передачі, демонтаж, сортування, переробка та документи, що підтверджують утилізацію.","url":"https://guide.youreco.com.ua/utylizaciya-ofisnih-mebliv-orgtehniki.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-ofisnih-mebliv-orgtehniki.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації офісних меблів та оргтехніки","name":"Порядок утилізації офісних меблів та оргтехніки — Довідник YOURECO","description":"Утилізація офісних меблів та оргтехніки: WEEE, небезпечні компоненти, захист даних, демонтаж, сортування і документи.","url":"https://guide.youreco.com.ua/utylizaciya-ofisnih-mebliv-orgtehniki.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-ofisnih-mebliv-orgtehniki.html","inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-paverbankiv-dbj.html b/utylizaciya-paverbankiv-dbj.html
index 3d898ee..18b4e4f 100644
--- a/utylizaciya-paverbankiv-dbj.html
+++ b/utylizaciya-paverbankiv-dbj.html
@@ -205,7 +205,7 @@
 .breadcrumbs span{opacity:.8}</style>
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як оформлюється утилізація павербанків та ДБЖ","name":"Як оформлюється утилізація павербанків та ДБЖ — Довідник YOURECO","description":"Утилізація павербанків, ДБЖ (UPS) та акумуляторних блоків для підприємств: ризики Li-ion/LiPo, правила безпечного зберігання і передачі, підготовка, сортування, демонтаж, переробка та документи-підтвердження.","url":"https://guide.youreco.com.ua/utylizaciya-paverbankiv-dbj.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-paverbankiv-dbj.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як оформлюється утилізація павербанків та ДБЖ","name":"Як оформлюється утилізація павербанків та ДБЖ — Довідник YOURECO","description":"Утилізація павербанків, ДБЖ та акумуляторних блоків: ризики Li-ion/LiPo, зберігання, передача, сортування й документи.","url":"https://guide.youreco.com.ua/utylizaciya-paverbankiv-dbj.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-paverbankiv-dbj.html","inLanguage":"uk-UA"}</script>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","url":"https://guide.youreco.com.ua/utylizaciya-paverbankiv-dbj.html"}</script></head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-plastyku-ta-polimeriv.html b/utylizaciya-plastyku-ta-polimeriv.html
index 0f6fd13..31a193f 100644
--- a/utylizaciya-plastyku-ta-polimeriv.html
+++ b/utylizaciya-plastyku-ta-polimeriv.html
@@ -203,7 +203,7 @@
 .breadcrumbs span{opacity:.8}</style>
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації пластику та полімерів для підприємств","name":"Порядок утилізації пластику та полімерів для підприємств — Довідник YOURECO","description":"Утилізація пластику та полімерів: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника YOURECO.","url":"https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації пластику та полімерів для підприємств","name":"Порядок утилізації пластику та полімерів для підприємств — Довідник YOURECO","description":"Утилізація пластику та полімерів: що приймають, як організувати збір, вивезення та документи для підприємств.","url":"https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html","inLanguage":"uk-UA"}</script>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","url":"https://guide.youreco.com.ua/utylizaciya-plastyku-ta-polimeriv.html"}</script></head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-produktiv-harchuvannya-napoyiv.html b/utylizaciya-produktiv-harchuvannya-napoyiv.html
index d367573..3c72006 100644
--- a/utylizaciya-produktiv-harchuvannya-napoyiv.html
+++ b/utylizaciya-produktiv-harchuvannya-napoyiv.html
@@ -203,7 +203,7 @@
 .breadcrumbs span{opacity:.8}</style>
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації продуктів харчування та напоїв","name":"Порядок утилізації продуктів харчування та напоїв — Довідник YOURECO","description":"Утилізація продуктів харчування, напоїв та харчових жирів для підприємств: типові причини списання, класифікація потоків, підготовка, пакування, логістика, утилізація/переробка та документи-підтвердження.","url":"https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації продуктів харчування та напоїв","name":"Порядок утилізації продуктів харчування та напоїв — Довідник YOURECO","description":"Утилізація продуктів харчування, напоїв і жирів: причини списання, класифікація, підготовка, логістика та документи.","url":"https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html","inLanguage":"uk-UA"}</script>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","url":"https://guide.youreco.com.ua/utylizaciya-produktiv-harchuvannya-napoyiv.html"}</script></head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-promyslovyh-vidhodiv.html b/utylizaciya-promyslovyh-vidhodiv.html
index 34cbcae..49f356a 100644
--- a/utylizaciya-promyslovyh-vidhodiv.html
+++ b/utylizaciya-promyslovyh-vidhodiv.html
@@ -203,7 +203,7 @@
 .breadcrumbs span{opacity:.8}</style>
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації промислових відходів для підприємств","name":"Порядок утилізації промислових відходів для підприємств — Довідник YOURECO","description":"Утилізація промислових відходів: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника YOURECO.","url":"https://guide.youreco.com.ua/utylizaciya-promyslovyh-vidhodiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-promyslovyh-vidhodiv.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації промислових відходів для підприємств","name":"Порядок утилізації промислових відходів для підприємств — Довідник YOURECO","description":"Утилізація промислових відходів: що приймають, як організувати збір, вивезення та документи для підприємств.","url":"https://guide.youreco.com.ua/utylizaciya-promyslovyh-vidhodiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-promyslovyh-vidhodiv.html","inLanguage":"uk-UA"}</script>
 <script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","url":"https://guide.youreco.com.ua/utylizaciya-promyslovyh-vidhodiv.html"}</script></head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-prostrochenyh-produktiv.html b/utylizaciya-prostrochenyh-produktiv.html
index 812d0fb..2edb533 100644
--- a/utylizaciya-prostrochenyh-produktiv.html
+++ b/utylizaciya-prostrochenyh-produktiv.html
@@ -203,7 +203,7 @@
 .breadcrumbs span{opacity:.8}</style>
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Куди передають прострочені продукти на утилізацію","name":"Куди передають прострочені продукти на утилізацію — Довідник YOURECO","description":"Утилізація прострочених продуктів: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника YOURECO.","url":"https://guide.youreco.com.ua/utylizaciya-prostrochenyh-produktiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-prostrochenyh-produktiv.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Куди передають прострочені продукти на утилізацію","name":"Куди передають прострочені продукти на утилізацію — Довідник YOURECO","description":"Утилізація прострочених продуктів: що приймають, як організувати збір, вивезення та документи для підприємств.","url":"https://guide.youreco.com.ua/utylizaciya-prostrochenyh-produktiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-prostrochenyh-produktiv.html","inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html b/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
index 4682d56..d6c3179 100644
--- a/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
+++ b/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
@@ -199,7 +199,7 @@
 .breadcrumbs a{color:#9ad0ff;text-decoration:none}
 .breadcrumbs a:hover{text-decoration:underline}
 .breadcrumbs span{opacity:.8}</style>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації складських залишків косметики","name":"Порядок утилізації складських залишків косметики — Довідник YOURECO","description":"Довідка для підприємств про «утилізацію складських залишків косметики»: що включає, як підготувати партію, правила зберігання, логістика, документи та типові помилки.","url":"https://guide.youreco.com.ua/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації складських залишків косметики","name":"Порядок утилізації складських залишків косметики — Довідник YOURECO","description":"Утилізація складських залишків косметики: підготовка партії, правила зберігання, логістика, документи та типові помилки.","url":"https://guide.youreco.com.ua/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html","inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-sonyachnih-panelij-vitryakiv.html b/utylizaciya-sonyachnih-panelij-vitryakiv.html
index a97eba8..163e939 100644
--- a/utylizaciya-sonyachnih-panelij-vitryakiv.html
+++ b/utylizaciya-sonyachnih-panelij-vitryakiv.html
@@ -203,7 +203,7 @@
 .breadcrumbs span{opacity:.8}</style>
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як оформлюється утилізація сонячних панелей та лопатей ВЕС","name":"Як оформлюється утилізація сонячних панелей та лопатей ВЕС — Довідник YOURECO","description":"Довідка для підприємств про утилізацію сонячних панелей (СЕС) та лопатей вітроелектростанцій (ВЕС): що приймають, які компоненти потребують окремого поводження, етапи демонтажу/логістики/переробки, особливості композитів та документи-підтвердження утилізації.","url":"https://guide.youreco.com.ua/utylizaciya-sonyachnih-panelij-vitryakiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-sonyachnih-panelij-vitryakiv.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як оформлюється утилізація сонячних панелей та лопатей ВЕС","name":"Як оформлюється утилізація сонячних панелей та лопатей ВЕС — Довідник YOURECO","description":"Утилізація сонячних панелей і лопатей ВЕС: компоненти, демонтаж, логістика, переробка композитів та документи.","url":"https://guide.youreco.com.ua/utylizaciya-sonyachnih-panelij-vitryakiv.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-sonyachnih-panelij-vitryakiv.html","inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-tary-upakovki.html b/utylizaciya-tary-upakovki.html
index 6e7756b..6921af2 100644
--- a/utylizaciya-tary-upakovki.html
+++ b/utylizaciya-tary-upakovki.html
@@ -203,7 +203,7 @@
 .breadcrumbs span{opacity:.8}</style>
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як оформлюється утилізація тари та упаковки","name":"Як оформлюється утилізація тари та упаковки — Довідник YOURECO","description":"Довідка для підприємств про контрольовану утилізацію тари та упаковки: що приймають (етикетки, плівка, картон, контейнери, піддони, біг-беги), як запобігають повторному використанню брендованих елементів, як розділяють фракції та які документи видають після утилізації/переробки.","url":"https://guide.youreco.com.ua/utylizaciya-tary-upakovki.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-tary-upakovki.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Як оформлюється утилізація тари та упаковки","name":"Як оформлюється утилізація тари та упаковки — Довідник YOURECO","description":"Утилізація тари й упаковки: етикетки, плівка, картон, контейнери, піддони, біг-беги, розділення фракцій і документи.","url":"https://guide.youreco.com.ua/utylizaciya-tary-upakovki.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-tary-upakovki.html","inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
diff --git a/utylizaciya-tovary-pid-mitnim-kontrolem.html b/utylizaciya-tovary-pid-mitnim-kontrolem.html
index 9217f7c..905bbcd 100644
--- a/utylizaciya-tovary-pid-mitnim-kontrolem.html
+++ b/utylizaciya-tovary-pid-mitnim-kontrolem.html
@@ -203,7 +203,7 @@
 .breadcrumbs span{opacity:.8}</style>
 <!-- Schema.org: TechArticle -->
 <link href="/styles.css" rel="stylesheet"/>
-<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації товарів під митним контролем","name":"Порядок утилізації товарів під митним контролем — Довідник YOURECO","description":"Довідка для бізнесу про знищення та утилізацію товарів під митним контролем: що вважається таким товаром (контрафакт, брак, повернення, конфіскат), хто є учасниками процедури, типові сценарії, методи знищення та пакет документів, який підтверджує, що товар не потрапив у незаконний обіг.","url":"https://guide.youreco.com.ua/utylizaciya-tovary-pid-mitnim-kontrolem.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-tovary-pid-mitnim-kontrolem.html","inLanguage":"uk-UA"}</script>
+<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Порядок утилізації товарів під митним контролем","name":"Порядок утилізації товарів під митним контролем — Довідник YOURECO","description":"Утилізація товарів під митним контролем: контрафакт, брак, повернення, конфіскат, методи знищення та пакет документів.","url":"https://guide.youreco.com.ua/utylizaciya-tovary-pid-mitnim-kontrolem.html","mainEntityOfPage":"https://guide.youreco.com.ua/utylizaciya-tovary-pid-mitnim-kontrolem.html","inLanguage":"uk-UA"}</script>
 </head>
 <body>
 <div class="layout">
```

## 6. git diff --name-only HEAD^ HEAD
```txt
index.html
jsonld-description-fix-report.md
kabelni-vidhody.html
povernennya-tovariv-z-merezhi.html
spysannya-produkciyi.html
utylizaciya-dokumentiv.html
utylizaciya-li-ion-batarej.html
utylizaciya-nekondicijnoyi-sirovini.html
utylizaciya-odyagu-vzuttya.html
utylizaciya-ofisnih-mebliv-orgtehniki.html
utylizaciya-paverbankiv-dbj.html
utylizaciya-plastyku-ta-polimeriv.html
utylizaciya-produktiv-harchuvannya-napoyiv.html
utylizaciya-promyslovyh-vidhodiv.html
utylizaciya-prostrochenyh-produktiv.html
utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
utylizaciya-sonyachnih-panelij-vitryakiv.html
utylizaciya-tary-upakovki.html
utylizaciya-tovary-pid-mitnim-kontrolem.html
```

## 7. git diff --numstat HEAD^ HEAD
```txt
1	1	index.html
65	0	jsonld-description-fix-report.md
1	1	kabelni-vidhody.html
1	1	povernennya-tovariv-z-merezhi.html
1	1	spysannya-produkciyi.html
1	1	utylizaciya-dokumentiv.html
1	1	utylizaciya-li-ion-batarej.html
1	1	utylizaciya-nekondicijnoyi-sirovini.html
1	1	utylizaciya-odyagu-vzuttya.html
1	1	utylizaciya-ofisnih-mebliv-orgtehniki.html
1	1	utylizaciya-paverbankiv-dbj.html
1	1	utylizaciya-plastyku-ta-polimeriv.html
1	1	utylizaciya-produktiv-harchuvannya-napoyiv.html
1	1	utylizaciya-promyslovyh-vidhodiv.html
1	1	utylizaciya-prostrochenyh-produktiv.html
1	1	utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
1	1	utylizaciya-sonyachnih-panelij-vitryakiv.html
1	1	utylizaciya-tary-upakovki.html
1	1	utylizaciya-tovary-pid-mitnim-kontrolem.html
```

## jsonld-description-fix-report.md

# JSON-LD Description Fix Report

## Summary
- files changed: 19
- JSON-LD descriptions updated: 18
- HTML body changed: no
- title changed: no
- H1 changed: no
- canonical changed: no
- FAQ changed: no
- public changed: no
- dist changed: no

## Changed Files
- index.html
- kabelni-vidhody.html
- povernennya-tovariv-z-merezhi.html
- spysannya-produkciyi.html
- utylizaciya-dokumentiv.html
- utylizaciya-li-ion-batarej.html
- utylizaciya-nekondicijnoyi-sirovini.html
- utylizaciya-odyagu-vzuttya.html
- utylizaciya-ofisnih-mebliv-orgtehniki.html
- utylizaciya-paverbankiv-dbj.html
- utylizaciya-plastyku-ta-polimeriv.html
- utylizaciya-produktiv-harchuvannya-napoyiv.html
- utylizaciya-promyslovyh-vidhodiv.html
- utylizaciya-prostrochenyh-produktiv.html
- utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
- utylizaciya-sonyachnih-panelij-vitryakiv.html
- utylizaciya-tary-upakovki.html
- utylizaciya-tovary-pid-mitnim-kontrolem.html
- jsonld-description-fix-report.md

## Validation
- remaining index JSON-LD description mismatch: 2
- JSON-LD parse errors: 0
- JSON-LD url mismatch: 0
- H1/headline mismatch: 2
- noindex files changed: 0

## Git Status
```txt
 M index.html
 M kabelni-vidhody.html
 M povernennya-tovariv-z-merezhi.html
 M spysannya-produkciyi.html
 M utylizaciya-dokumentiv.html
 M utylizaciya-li-ion-batarej.html
 M utylizaciya-nekondicijnoyi-sirovini.html
 M utylizaciya-odyagu-vzuttya.html
 M utylizaciya-ofisnih-mebliv-orgtehniki.html
 M utylizaciya-paverbankiv-dbj.html
 M utylizaciya-plastyku-ta-polimeriv.html
 M utylizaciya-produktiv-harchuvannya-napoyiv.html
 M utylizaciya-promyslovyh-vidhodiv.html
 M utylizaciya-prostrochenyh-produktiv.html
 M utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
 M utylizaciya-sonyachnih-panelij-vitryakiv.html
 M utylizaciya-tary-upakovki.html
 M utylizaciya-tovary-pid-mitnim-kontrolem.html
?? jsonld-description-fix-report.md
?? meta-schema-audit.md
?? sitemap-add-evidence.md
```


## meta-schema-audit.md

# Meta Schema Audit

## Summary
- root HTML files scanned: 241
- index pages scanned: 62
- noindex pages scanned: 179
- missing H1: 0
- missing title: 0
- missing meta description: 0
- missing canonical: 0
- missing JSON-LD: 1
- JSON-LD parse errors: 0
- JSON-LD url mismatch: 0
- JSON-LD headline/name mismatch: 1
- JSON-LD description mismatch: 40
- FAQ mismatch: 61
- issues needing fix: 82

## High Priority Issues
- akt-utylizaciyi.html: FAQ mismatch
- dokumenty.html: FAQ mismatch
- fotozvit-utylizaciyi.html: FAQ mismatch
- index.html: JSON-LD description mismatch; FAQ mismatch
- kabelni-vidhody.html: JSON-LD description mismatch
- kudy-zdaty.html: FAQ mismatch
- pererobka-avtomobilnyh-shyn.html: FAQ mismatch
- pererobka-skla.html: FAQ mismatch
- pererobka.html: FAQ mismatch
- povernennya-tovariv-z-merezhi.html: JSON-LD description mismatch
- sortuvannya.html: FAQ mismatch
- spysannya-produkciyi.html: JSON-LD description mismatch
- utylizaciya-dokumentiv.html: JSON-LD description mismatch; FAQ mismatch
- utylizaciya-gazovanyh-napoyiv.html: FAQ mismatch
- utylizaciya-kabelyu-ta-drotiv.html: FAQ mismatch
- utylizaciya-konserviv.html: FAQ mismatch
- utylizaciya-li-ion-batarej.html: JSON-LD description mismatch; FAQ mismatch
- utylizaciya-myasnyh-produktiv.html: FAQ mismatch
- utylizaciya-nekondicijnoyi-sirovini.html: JSON-LD description mismatch; FAQ mismatch
- utylizaciya-odyagu-vzuttya.html: JSON-LD description mismatch; FAQ mismatch
- utylizaciya-ofisnih-mebliv-orgtehniki.html: JSON-LD description mismatch
- utylizaciya-paverbankiv-dbj.html: JSON-LD description mismatch
- utylizaciya-plastyku-ta-polimeriv.html: JSON-LD description mismatch; FAQ mismatch
- utylizaciya-produktiv-harchuvannya-napoyiv.html: JSON-LD description mismatch; FAQ mismatch
- utylizaciya-promyslovyh-vidhodiv.html: JSON-LD description mismatch; FAQ mismatch
- utylizaciya-prostrochenyh-produktiv.html: JSON-LD description mismatch
- utylizaciya-rybnyh-produktiv.html: FAQ mismatch
- utylizaciya-shyn.html: FAQ mismatch
- utylizaciya-skladskyh-zalyshkiv-kosmetyky.html: JSON-LD description mismatch; FAQ mismatch
- utylizaciya-sonyachnih-panelij-vitryakiv.html: JSON-LD description mismatch; FAQ mismatch
- utylizaciya-tary-upakovki.html: JSON-LD description mismatch; FAQ mismatch
- utylizaciya-tovary-pid-mitnim-kontrolem.html: JSON-LD description mismatch; FAQ mismatch
- utylizaciya-vidpracovanoi-olyvy.html: FAQ mismatch
- utylizaciya-zamorozhenyh-produktiv.html: FAQ mismatch
- utylizaciya.html: FAQ mismatch
- vidhody.html: FAQ mismatch
- zbir.html: FAQ mismatch

## JSON-LD URL Mismatches
- none

## H1 vs JSON-LD headline/name Mismatches
- file: sortuvannya-budivelnyh-vidhodiv.html
  H1: Сортування будівельних відходів
  JSON-LD headline/name: Сортування будівельного відходи / Сортування будівельного відходи — Довідник YOURECO

## Description Mismatches
- file: index.html
  meta description: Довідник YOURECO про відходи для підприємств України: утилізація, переробка, сортування, логістика, документи та типові ризики.
  JSON-LD description: Довідник YOURECO з промислових, небезпечних та комерційних відходів для підприємств України. Практичні інструкції підготовки відходів, типові ризики, документи та поширені сценарії утилізації.
- file: kabelni-vidhody.html
  meta description: Кабельні відходи: класифікація, зберігання, підготовка до передачі, організація вивезення та документи для підприємств.
  JSON-LD description: Кабельні відходи: класифікація та зберігання: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника…
- file: kudy-zdaty-gipsokartonu.html
  meta description: Службова сторінка перенаправлення для запиту щодо гіпсокартону: веде на канонічну сторінку утилізації, містить noindex і не входить до sitemap.
  JSON-LD description: Службова сторінка перенаправлення для гіпсокартону на канонічну URL утилізації.
- file: logistyka-promyslovyh-vidhodiv.html
  meta description: Логістика промислових відходів: як організувати збір, вивезення, маршрути передачі та документи для підприємства.
  JSON-LD description: Логістика промислових відходів: вивезення і маршрути: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка…
- file: optymizaciya-vidhodiv-na-vyrobnyctvi.html
  meta description: Оптимізація відходів на виробництві: підготовка партій, зберігання, логістика, документи та типові помилки підприємств.
  JSON-LD description: Довідка для підприємств про «оптимізація відходів на виробництві»: що включає, як підготувати партію, правила зберігання, логістика, документи та типові помилки.
- file: pererobka-izolyaciyi-kabelyu.html
  meta description: Переробка ізоляції кабелю: що належить до кабельних відходів, як зберігати, передавати, оформлювати документи й логістику.
  JSON-LD description: Гайд для бізнесу про «переробку ізоляції кабелю»: що відноситься до кабельних відходів, як зберігати та передавати, як оформити документи і організувати логістику.
- file: pererobka-plastykovoyi-upakovky.html
  meta description: Переробка пластикової упаковки: що приймають, як організувати збір, вивезення та які документи потрібні підприємствам.
  JSON-LD description: Переробка пластикової упаковки: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника YOURECO.
- file: pererobka-vidpracovanyh-masel.html
  meta description: Переробка і регенерація відпрацьованих олив: безпечне зберігання, збір, передача, логістика та документи для підприємств.
  JSON-LD description: Інструкція для підприємств про «переробку/регенерацію відпрацьованих олив»: безпечне зберігання, збір, передача на переробку/регенерацію, логістика та документи.
- file: povernennya-tovariv-z-merezhi.html
  meta description: Повернення товарів з мережі охоплює логістику зворотного руху продукції з магазинів, дистриб'юторських точок або партнерських майданчиків до складу чи центру прийняття рішень.
  JSON-LD description: Повернення товарів з мережі охоплює логістику зворотного руху продукції з магазинів, дистриб
- file: promyslovi-vidhody-na-pidpryyemstvi.html
  meta description: Промислові відходи на підприємстві: облік, правила зберігання, збір, вивезення та документи для передачі.
  JSON-LD description: Промислові відходи на підприємстві: облік і правила: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка…
- file: promyslovi-vidhody.html
  meta description: Промислові відходи: види, приклади, вимоги до збирання й зберігання, вивезення, утилізація, переробка та документи.
  JSON-LD description: Промислові відходи: що це, які бувають, приклади, вимоги до збирання та зберігання, як організувати вивезення, утилізацію або переробку. Документи для підприємств.
- file: shcho-take-promyslovi-vidhody.html
  meta description: Промислові відходи: що це за матеріали й залишки, де вони утворюються на підприємстві та як їх правильно визначати.
  JSON-LD description: Промислові відходи — це матеріали та залишки, що утворюються у виробництві, складських процесах, технічному обслуговуванні або допоміжних операціях підприємства.
- file: shcho-take-utylizaciya.html
  meta description: Утилізація: контрольована операція поводження з матеріалами або відходами, які потребують обробки, передачі чи знищення.
  JSON-LD description: Утилізація є контрольованою операцією поводження з матеріалами або відходами, які не можуть залишатися в господарському обороті без окремої обробки або передачі.
- file: shcho-take-znyshchennya-produkciyi.html
  meta description: Знищення продукції є процедурою, у межах якої товар або матеріал остаточно вилучається з обігу шляхом фізичного припинення його існування як придатного об'єкта.
  JSON-LD description: Знищення продукції є процедурою, у межах якої товар або матеріал остаточно вилучається з обігу шляхом фізичного припинення його існування як придатного об
- file: spysannya-produkciyi.html
  meta description: Списання продукції: як підприємство виводить товари чи матеріали з обліку перед утилізацією, переробкою або передачею.
  JSON-LD description: Списання продукції є внутрішнім рішенням підприємства про виведення товарів або матеріалів з обліку перед передачею на утилізацію, переробку або інше контрольоване поводження.
- file: spysannya-produktiv.html
  meta description: Списання продуктів: як оформити партію, організувати збір і вивезення та які документи потрібні підприємству.
  JSON-LD description: Списання продуктів: як правильно оформити: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника…
- file: utylizaciya-budivelnyh-vidhodiv.html
  meta description: Утилізація будівельних відходів: що приймають, як організувати збір, вивезення та документи для підприємств.
  JSON-LD description: Утилізація будівельних відходів: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника YOURECO.
- file: utylizaciya-dokumentiv.html
  meta description: Утилізація конфіденційних документів: папір, архіви, бухгалтерські й юридичні документи, носії даних та підтвердження знищення.
  JSON-LD description: Безпечна утилізація конфіденційних документів: паперу, архівів, бухгалтерських та юридичних документів, носіїв даних. Гарантоване знищення та документи для звітності.
- file: utylizaciya-li-ion-batarej.html
  meta description: Утилізація Li-ion батарей для підприємств: ризики, підготовка, тимчасове зберігання, етапи передачі та документи.
  JSON-LD description: Правильна утилізація літій-іонних (Li-ion) батарей та акумуляторних модулів для підприємств. Основні ризики, етапи утилізації, документи та рекомендації з тимчасового зберігання.
- file: utylizaciya-nekondicijnoyi-sirovini.html
  meta description: Утилізація некондиційної сировини та продукції: прострочені партії, брак, порушення зберігання, рекламації й документи.
  JSON-LD description: Утилізація некондиційної сировини та продукції: прострочені партії, порушення умов зберігання, брак, рекламації. Від харчової сировини до косметичних компонентів та хімічних інгредієнтів.
- file: utylizaciya-odyagu-vzuttya.html
  meta description: Утилізація одягу та взуття для підприємств: списання, брак, надлишки, корпоративна форма, контроль повторного обігу й документи.
  JSON-LD description: Утилізація одягу та взуття для підприємств: списання, надлишки, брак, корпоративна форма, контрафакт. Практична підготовка до передачі, контроль повторного обігу, типові помилки та документи, що підтверджують знищення/утилізацію.
- file: utylizaciya-ofisnih-mebliv-orgtehniki.html
  meta description: Утилізація офісних меблів та оргтехніки: WEEE, небезпечні компоненти, захист даних, демонтаж, сортування і документи.
  JSON-LD description: Утилізація офісних меблів та оргтехніки для підприємств: WEEE та небезпечні компоненти, ризики витоку даних, підготовка до передачі, демонтаж, сортування, переробка та документи, що підтверджують утилізацію.
- file: utylizaciya-paverbankiv-dbj.html
  meta description: Утилізація павербанків, ДБЖ та акумуляторних блоків: ризики Li-ion/LiPo, зберігання, передача, сортування й документи.
  JSON-LD description: Утилізація павербанків, ДБЖ (UPS) та акумуляторних блоків для підприємств: ризики Li-ion/LiPo, правила безпечного зберігання і передачі, підготовка, сортування, демонтаж, переробка та документи-підтвердження.
- file: utylizaciya-plastyku-ta-polimeriv.html
  meta description: Утилізація пластику та полімерів: що приймають, як організувати збір, вивезення та документи для підприємств.
  JSON-LD description: Утилізація пластику та полімерів: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника YOURECO.
- file: utylizaciya-produktiv-harchuvannya-napoyiv.html
  meta description: Утилізація продуктів харчування, напоїв і жирів: причини списання, класифікація, підготовка, логістика та документи.
  JSON-LD description: Утилізація продуктів харчування, напоїв та харчових жирів для підприємств: типові причини списання, класифікація потоків, підготовка, пакування, логістика, утилізація/переробка та документи-підтвердження.
- file: utylizaciya-promyslovogo-obladnannya-mehanizmiv.html
  meta description: Утилізація промислового обладнання: списання, демонтаж, сортування металу, електроніки й небезпечних компонентів, документи.
  JSON-LD description: Довідка для підприємств: як списувати та утилізувати промислове обладнання, верстати й механізми. Інвентаризація, демонтаж, сортування на метал/електроніку/небезпечні компоненти, логістика, переробка та документи.
- file: utylizaciya-promyslovyh-vidhodiv.html
  meta description: Утилізація промислових відходів: що приймають, як організувати збір, вивезення та документи для підприємств.
  JSON-LD description: Утилізація промислових відходів: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника YOURECO.
- file: utylizaciya-prostrochenoyi-kosmetyky.html
  meta description: Утилізація простроченої косметики: що приймають, як організувати збір, вивезення та документи для підприємств.
  JSON-LD description: Утилізація простроченої косметики: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника YOURECO.
- file: utylizaciya-prostrochenyh-produktiv.html
  meta description: Утилізація прострочених продуктів: що приймають, як організувати збір, вивезення та документи для підприємств.
  JSON-LD description: Утилізація прострочених продуктів: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника YOURECO.
- file: utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
  meta description: Утилізація складських залишків косметики: підготовка партії, правила зберігання, логістика, документи та типові помилки.
  JSON-LD description: Довідка для підприємств про «утилізацію складських залишків косметики»: що включає, як підготувати партію, правила зберігання, логістика, документи та типові помилки.
- file: utylizaciya-sonyachnih-panelij-vitryakiv.html
  meta description: Утилізація сонячних панелей і лопатей ВЕС: компоненти, демонтаж, логістика, переробка композитів та документи.
  JSON-LD description: Довідка для підприємств про утилізацію сонячних панелей (СЕС) та лопатей вітроелектростанцій (ВЕС): що приймають, які компоненти потребують окремого поводження, етапи демонтажу/логістики/переробки, особливості композитів та документи-підтвердження утилізації.
- file: utylizaciya-tary-upakovki.html
  meta description: Утилізація тари й упаковки: етикетки, плівка, картон, контейнери, піддони, біг-беги, розділення фракцій і документи.
  JSON-LD description: Довідка для підприємств про контрольовану утилізацію тари та упаковки: що приймають (етикетки, плівка, картон, контейнери, піддони, біг-беги), як запобігають повторному використанню брендованих елементів, як розділяють фракції та які документи видають після утилізації/переробки.
- file: utylizaciya-tovary-pid-mitnim-kontrolem.html
  meta description: Утилізація товарів під митним контролем: контрафакт, брак, повернення, конфіскат, методи знищення та пакет документів.
  JSON-LD description: Довідка для бізнесу про знищення та утилізацію товарів під митним контролем: що вважається таким товаром (контрафакт, брак, повернення, конфіскат), хто є учасниками процедури, типові сценарії, методи знищення та пакет документів, який підтверджує, що товар не потрапив у незаконний обіг.
- file: utylizaciya-upakovky-na-pidpryyemstvi.html
  meta description: Утилізація упаковки на підприємстві: підготовка партії, зберігання, логістика, документи та типові помилки.
  JSON-LD description: Довідка для підприємств про «утилізацію упаковки на підприємстві»: що включає, як підготувати партію, правила зберігання, логістика, документи та типові помилки.
- file: utylizaciya-vidpracovanyh-masel.html
  meta description: Утилізація відпрацьованих олив: що приймають, як організувати збір, вивезення та документи для підприємств.
  JSON-LD description: Утилізація відпрацьованих олив: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника YOURECO.
- file: vidhody-demontazhu.html
  meta description: Відходи демонтажу: сортування, утилізація, організація збору, вивезення та документи для підприємств.
  JSON-LD description: Відходи демонтажу: сортування та утилізація: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника…
- file: vidhody-gumy.html
  meta description: Відходи гуми: що відноситься до потоку, як їх утилізують, організовують збір, вивезення та документи.
  JSON-LD description: Відходи гуми: що відноситься і як утилізують: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка довідника…
- file: yak-vidbuvayetsya-utylizaciya-produkciyi.html
  meta description: Етапи утилізації продукції для підприємств: рішення, документи, підготовка партії, передача виконавцю та підтвердження.
  JSON-LD description: Практичний опис етапів утилізації продукції для підприємств: коли переходять до утилізації, які документи готують, як передають партію виконавцю та що отримують після завершення.
- file: zbir-promyslovyh-vidhodiv.html
  meta description: Збір промислових відходів: організація, вимоги, вивезення та документи для підприємств.
  JSON-LD description: Збір промислових відходів: організація та вимоги: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка…
- file: znyshchennya-kosmetyky.html
  meta description: Знищення косметики: коли потрібне, як організувати збір і вивезення та які документи потрібні підприємству.
  JSON-LD description: Знищення косметики: коли потрібне і які документи: що приймають, як організувати збір/вивезення та які документи потрібні для підприємств. Поради та перелінковка…

## FAQ Mismatches
- file: akt-utylizaciyi.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: dokumenty.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: fotozvit-utylizaciyi.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: index.html
  visible FAQ count: 8
  JSON-LD FAQ count: 5
  issue: count mismatch
- file: kudy-zdaty.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: logistyka-plastyku.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: nebezpeka-vidpracovanogo-masla.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: pererobka-avtomobilnyh-shyn.html
  visible FAQ count: 4
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: pererobka-izolyaciyi-kabelyu.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: pererobka-skla.html
  visible FAQ count: 4
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: pererobka-vidpracovanyh-masel.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: pererobka.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: reestr-partiyi.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: scenarii-utilizaciyi.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: shcho-take-pererobka-vidhodiv.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: shcho-take-promyslovi-vidhody.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: shcho-take-utylizaciya.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: shcho-take-znyshchennya-produkciyi.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: sortuvannya-budivelnyh-vidhodiv.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: sortuvannya-plastyku.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: sortuvannya.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: spysannya-produktiv.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: transportuvannya-vidpracovanyh-masel.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: transportuvannya-vidpracovanyh-shyn.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-avtoshyn.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-budivelnyh-vidhodiv.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-derevyny-z-budivnyctva.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-dokumentiv.html
  visible FAQ count: 4
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-energetychnyh-napoyiv.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-fruktiv-ta-ovochiv.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-gazovanyh-napoyiv.html
  visible FAQ count: 5
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-harchovyh-produktiv.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-kabelyu-ta-drotiv.html
  visible FAQ count: 4
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-konserviv.html
  visible FAQ count: 4
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-li-ion-batarej.html
  visible FAQ count: 4
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-myasnyh-produktiv.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-nekondicijnoyi-sirovini.html
  visible FAQ count: 4
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-odyagu-vzuttya.html
  visible FAQ count: 4
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-paperu-ta-kartonu.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-plastyku-ta-polimeriv.html
  visible FAQ count: 4
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-produktiv-harchuvannya-napoyiv.html
  visible FAQ count: 4
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-promyslovyh-vidhodiv.html
  visible FAQ count: 4
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-prostrochenoyi-kosmetyky.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-rybnyh-produktiv.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-shyn.html
  visible FAQ count: 4
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-sokiv-ta-napoyiv.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-sonyachnih-panelij-vitryakiv.html
  visible FAQ count: 4
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-tary-upakovki.html
  visible FAQ count: 4
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-tovary-pid-mitnim-kontrolem.html
  visible FAQ count: 4
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-upakovky-vid-kosmetyky.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-vantazhnyh-shyn.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-vidpracovanoi-olyvy.html
  visible FAQ count: 4
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-vody.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya-zamorozhenyh-produktiv.html
  visible FAQ count: 5
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: utylizaciya.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: vidhody.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: vidy-kabelnyh-vidhodiv.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: vnutrishniy-akt-spysannya.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: vymogy-do-zberigannya-vidhodiv.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch
- file: zbir.html
  visible FAQ count: 3
  JSON-LD FAQ count: 0
  issue: count mismatch

## Noindex Issues
- 404.html: missing JSON-LD
- kudy-zdaty-gipsokartonu.html: JSON-LD description mismatch
- logistyka-plastyku.html: FAQ mismatch
- logistyka-promyslovyh-vidhodiv.html: JSON-LD description mismatch
- nebezpeka-vidpracovanogo-masla.html: FAQ mismatch
- optymizaciya-vidhodiv-na-vyrobnyctvi.html: JSON-LD description mismatch
- pererobka-izolyaciyi-kabelyu.html: JSON-LD description mismatch; FAQ mismatch
- pererobka-plastykovoyi-upakovky.html: JSON-LD description mismatch
- pererobka-vidpracovanyh-masel.html: JSON-LD description mismatch; FAQ mismatch
- promyslovi-vidhody-na-pidpryyemstvi.html: JSON-LD description mismatch
- promyslovi-vidhody.html: JSON-LD description mismatch
- reestr-partiyi.html: FAQ mismatch
- scenarii-utilizaciyi.html: FAQ mismatch
- shcho-take-pererobka-vidhodiv.html: FAQ mismatch
- shcho-take-promyslovi-vidhody.html: JSON-LD description mismatch; FAQ mismatch
- shcho-take-utylizaciya.html: JSON-LD description mismatch; FAQ mismatch
- shcho-take-znyshchennya-produkciyi.html: JSON-LD description mismatch; FAQ mismatch
- sortuvannya-budivelnyh-vidhodiv.html: JSON-LD headline/name mismatch; FAQ mismatch
- sortuvannya-plastyku.html: FAQ mismatch
- spysannya-produktiv.html: JSON-LD description mismatch; FAQ mismatch
- transportuvannya-vidpracovanyh-masel.html: FAQ mismatch
- transportuvannya-vidpracovanyh-shyn.html: FAQ mismatch
- utylizaciya-avtoshyn.html: FAQ mismatch
- utylizaciya-budivelnyh-vidhodiv.html: JSON-LD description mismatch; FAQ mismatch
- utylizaciya-derevyny-z-budivnyctva.html: FAQ mismatch
- utylizaciya-energetychnyh-napoyiv.html: FAQ mismatch
- utylizaciya-fruktiv-ta-ovochiv.html: FAQ mismatch
- utylizaciya-harchovyh-produktiv.html: FAQ mismatch
- utylizaciya-paperu-ta-kartonu.html: FAQ mismatch
- utylizaciya-promyslovogo-obladnannya-mehanizmiv.html: JSON-LD description mismatch
- utylizaciya-prostrochenoyi-kosmetyky.html: JSON-LD description mismatch; FAQ mismatch
- utylizaciya-sokiv-ta-napoyiv.html: FAQ mismatch
- utylizaciya-upakovky-na-pidpryyemstvi.html: JSON-LD description mismatch
- utylizaciya-upakovky-vid-kosmetyky.html: FAQ mismatch
- utylizaciya-vantazhnyh-shyn.html: FAQ mismatch
- utylizaciya-vidpracovanyh-masel.html: JSON-LD description mismatch
- utylizaciya-vody.html: FAQ mismatch
- vidhody-demontazhu.html: JSON-LD description mismatch
- vidhody-gumy.html: JSON-LD description mismatch
- vidy-kabelnyh-vidhodiv.html: FAQ mismatch
- vnutrishniy-akt-spysannya.html: FAQ mismatch
- vymogy-do-zberigannya-vidhodiv.html: FAQ mismatch
- yak-vidbuvayetsya-utylizaciya-produkciyi.html: JSON-LD description mismatch
- zbir-promyslovyh-vidhodiv.html: JSON-LD description mismatch
- znyshchennya-kosmetyky.html: JSON-LD description mismatch

## Git Status
```txt
?? sitemap-add-evidence.md
```

