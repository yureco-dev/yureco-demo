# Post hub link fix wrong-topic audit

- total html files: 172
- total wrong-topic links: 113
- total generic hub placeholder links in main content: 770
- pererobka.html clean / Сторінки розділу: так
- kudy-zdaty.html clean / Сторінки розділу: ні

## Top source pages with wrong-topic links
- public/kudy-zdaty.html: 66
- public/utylizaciya-akumulyatoriv.html: 5
- public/utylizaciya-elektroniky.html: 5
- public/vidhody.html: 5
- public/sortuvannya.html: 4
- public/utylizaciya-napoyiv.html: 4
- public/utylizaciya-obladnannya.html: 4
- public/yak-peredaty-li-ion-batarei.html: 3
- public/utilizaciya-dlya-data-centriv.html: 2
- public/utylizaciya-importnyh-tovariv.html: 2
- public/akt-utylizaciyi.html: 1
- public/chy-potribno-pererobyty-chy-utylizuvaty.html: 1
- public/kontakty.html: 1
- public/likvidaciya-skladskykh-zalyshkiv.html: 1
- public/logistyka.html: 1
- public/pererobka.html: 1
- public/povernennya-tovariv-z-merezhi.html: 1
- public/spysannya-produkciyi.html: 1
- public/utilizaciya-brakovanoi-produkciyi.html: 1
- public/utylizaciya-konfidenciynykh-dokumentiv.html: 1

## Top source pages with generic hub placeholder links
- public/vidhody.html: 21
- public/utylizaciya-akumulyatoriv.html: 19
- public/utylizaciya-elektroniky.html: 19
- public/utylizaciya-obladnannya.html: 18
- public/yak-oformyty-spysannya-partiyi.html: 17
- public/yak-peredaty-li-ion-batarei.html: 17
- public/yak-peredaty-kosmetyku.html: 13
- public/yak-peredaty-skladski-zalyshky.html: 13
- public/utilizaciya-dlya-bankiv.html: 12
- public/utilizaciya-dlya-data-centriv.html: 10
- public/chy-potribno-pererobyty-chy-utylizuvaty.html: 9
- public/utylizaciya-importnyh-tovariv.html: 9
- public/sortuvannya.html: 8
- public/utilizaciya-dlya-importeriv.html: 8
- public/utilizaciya-dlya-riteylu.html: 8
- public/utilizaciya-dlya-skladiv.html: 8
- public/utilizaciya-dlya-vyrobnyctva.html: 8
- public/utylizaciya.html: 8
- public/utylizaciya-gazovanyh-napoyiv.html: 7
- public/utylizaciya-napoyiv.html: 7

## Generic hub counts by href
- /utylizaciya.html: 244
- /dokumenty.html: 214
- /logistyka.html: 138
- /sortuvannya.html: 76
- /pererobka.html: 60
- /zbir.html: 38

## Recommended next batch
- public/akt-utylizaciyi.html | Як визначити маршрут передачі | як визначити: переробка чи утилізація | /chy-potribno-pererobyty-chy-utylizuvaty.html -> /pererobka.html | REPLACE_HREF
- public/chy-potribno-pererobyty-chy-utylizuvaty.html | У чому різниця між переробкою та утилізацією | що таке переробка відходів | /utylizaciya.html -> /pererobka.html | REPLACE_HREF
- public/kontakty.html | Читайте також | Утилізація шин | /utylizaciya.html -> NEEDS_DECISION | NEEDS_DECISION
- public/kudy-zdaty.html | Сторінки розділу | Куди здати автомобільні шини | /utylizaciya-avtoshyn.html -> /kudy-zdaty.html | REPLACE_HREF
- public/kudy-zdaty.html | Сторінки розділу | Куди здати будівельні відходи | /utylizaciya-budivelnyh-vidhodiv.html -> /kudy-zdaty.html | REPLACE_HREF
- public/kudy-zdaty.html | Сторінки розділу | Куди здати деревину з будівництва | /utylizaciya-derevyny-z-budivnyctva.html -> /kudy-zdaty.html | REPLACE_HREF
- public/kudy-zdaty.html | Сторінки розділу | Куди здати конфіденційні документи | /utylizaciya-konfidenciynykh-dokumentiv.html -> /kudy-zdaty.html | REPLACE_HREF
- public/kudy-zdaty.html | Сторінки розділу | Куди здати енергетичні напої | /utylizaciya-energetychnyh-napoyiv.html -> /kudy-zdaty.html | REPLACE_HREF
- public/kudy-zdaty.html | Сторінки розділу | Куди здати фрукти та овочі | /utylizaciya-fruktiv-ta-ovochiv.html -> /kudy-zdaty.html | REPLACE_HREF
- public/kudy-zdaty.html | Сторінки розділу | Куди здати фрукти | /utylizaciya-fruktiv.html -> /kudy-zdaty.html | REPLACE_HREF

## Wrong-topic links
- source file: public/akt-utylizaciyi.html
  block/context: Як визначити маршрут передачі
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/chy-potribno-pererobyty-chy-utylizuvaty.html
  block/context: У чому різниця між переробкою та утилізацією
  anchor text: що таке переробка відходів
  current href: /utylizaciya.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kontakty.html
  block/context: Читайте також
  anchor text: Утилізація шин
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати автомобільні шини
  current href: /utylizaciya-avtoshyn.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати будівельні відходи
  current href: /utylizaciya-budivelnyh-vidhodiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати деревину з будівництва
  current href: /utylizaciya-derevyny-z-budivnyctva.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати конфіденційні документи
  current href: /utylizaciya-konfidenciynykh-dokumentiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати енергетичні напої
  current href: /utylizaciya-energetychnyh-napoyiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати фрукти та овочі
  current href: /utylizaciya-fruktiv-ta-ovochiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати фрукти
  current href: /utylizaciya-fruktiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати газовані напої
  current href: /utylizaciya-gazovanyh-napoyiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати гіпсокартон
  current href: /utylizaciya-gipsokartonu.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати харчові продукти
  current href: /utylizaciya-harchovyh-produktiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати кабель та дроти
  current href: /utylizaciya-kabelyu-ta-drotiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати кондитерські вироби
  current href: /utylizaciya-kondyterskyh-vyrobiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати консерви
  current href: /utylizaciya-konserviv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати косметику
  current href: /utylizaciya-kosmetyky.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати косметику з магазинів
  current href: /utylizaciya-kosmetyky-magazyniv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати косметику
  current href: /utylizaciya-kosmetyky.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати літій-іонні (Li-ion) батареї
  current href: /utylizaciya-li-ion-batarej.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати матеріали
  current href: /utylizaciya-materialiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати металеву стружку
  current href: /utylizaciya-metalevoyi-strushky.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: False
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати метал
  current href: /utylizaciya-metalu.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати молочні продукти
  current href: /utylizaciya-molochnyh-produktiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати м’ясні продукти
  current href: /utylizaciya-myasnyh-produktiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати напівфабрикати
  current href: /utylizaciya-napivfabrykatyv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати соки та напої
  current href: /utylizaciya-napoyiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати некондиційну сировину та продукцію
  current href: /utylizaciya-nekondicijnoyi-sirovini.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати некондиційну продукцію
  current href: /utylizaciya-nekondyciynoyi-produkciyi.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати обладнання
  current href: /utylizaciya-obladnannya.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати одяг та взуття
  current href: /utylizaciya-odyagu-vzuttya.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати офісні меблі та оргтехніку
  current href: /utylizaciya-ofisnih-mebliv-orgtehniki.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати овочі
  current href: /utylizaciya-ovochiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати папір та картон
  current href: /utylizaciya-paperu-ta-kartonu.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати парфумерію
  current href: /utylizaciya-parfumeriyi.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати партії продуктів
  current href: /utylizaciya-partiyi-produktiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати павербанки та ДБЖ
  current href: /utylizaciya-paverbankiv-dbj.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати пластик та полімери
  current href: /utylizaciya-plastyku-ta-polimeriv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати продукти харчування та напої
  current href: /utylizaciya-produktiv-harchuvannya-napoyiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати продукти на складі
  current href: /utylizaciya-produktiv-na-skladi.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати промислове обладнання та механізми
  current href: /utylizaciya-promyslovogo-obladnannya-mehanizmiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати промислові відходи
  current href: /utylizaciya-promyslovyh-vidhodiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати прострочену косметику
  current href: /utylizaciya-prostrochenoyi-kosmetyky.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати прострочені продукти
  current href: /utylizaciya-prostrochenyh-produktiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати пиво
  current href: /utylizaciya-pyva.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати рибні продукти
  current href: /utylizaciya-rybnyh-produktiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати шини
  current href: /utylizaciya-shyn.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати шини
  current href: /utylizaciya-shyn.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати шини: варіанти для бізнесу
  current href: /utylizaciya-shyn.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати скло
  current href: /utylizaciya-skla.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати складські залишки косметики
  current href: /utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати складські залишки
  current href: /utylizaciya-skladskyh-zalyshkiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати соки та напої
  current href: /utylizaciya-sokiv-ta-napoyiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати соки
  current href: /utylizaciya-sokiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати сонячні панелі та лопаті ВЕС
  current href: /utylizaciya-sonyachnih-panelij-vitryakiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати тару та упаковку
  current href: /utylizaciya-tary-upakovki.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати товари
  current href: /utylizaciya-tovariv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати товари під митним контролем
  current href: /utylizaciya-tovary-pid-mitnim-kontrolem.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати упаковку на підприємстві
  current href: /utylizaciya-upakovky-na-pidpryyemstvi.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати упаковку від косметики
  current href: /utylizaciya-upakovky-vid-kosmetyky.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати вантажні шини
  current href: /utylizaciya-shyn.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати відпрацьовану оливу
  current href: /utylizaciya-vidpracovanoi-olyvy.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати відпрацьовану моторну оливу
  current href: /utylizaciya-vidpracovanoi-olyvy.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати відпрацьовані оливи
  current href: /utylizaciya-vidpracovanyh-masel.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати воду (товарні залишки)
  current href: /utylizaciya-vody.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати виробничі відходи
  current href: /utylizaciya-vyrobnychyh-vidhodiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати ягоди
  current href: /utylizaciya-yagid.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: True
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати заморожені продукти
  current href: /utylizaciya-zamorozhenyh-produktiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/kudy-zdaty.html
  block/context: Сторінки розділу
  anchor text: Куди здати зіпсовані продукти
  current href: /utylizaciya-zipsovanyh-produktiv.html
  proposed href: /kudy-zdaty.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/likvidaciya-skladskykh-zalyshkiv.html
  block/context: Маршрут передачі продукції
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/logistyka.html
  block/context: Як визначити маршрут передачі
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/pererobka.html
  block/context: Як визначити маршрут передачі
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/povernennya-tovariv-z-merezhi.html
  block/context: Пов'язані матеріали
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/sortuvannya.html
  block/context: Сторінки розділу
  anchor text: Сортування будівельного відходи
  current href: /utylizaciya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/sortuvannya.html
  block/context: Сторінки розділу
  anchor text: Сортування пластику
  current href: /utylizaciya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/sortuvannya.html
  block/context: Сторінки розділу
  anchor text: Сортування промислових відходів
  current href: /utylizaciya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/sortuvannya.html
  block/context: Як визначити маршрут передачі
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/spysannya-produkciyi.html
  block/context: Пов'язані категорії утилізації
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/utilizaciya-brakovanoi-produkciyi.html
  block/context: Пов'язані категорії утилізації
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/utilizaciya-dlya-data-centriv.html
  block/context: Типові сценарії утилізації для галузі
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utilizaciya-dlya-data-centriv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Коротка відповідь
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/utylizaciya-elektroniky.html
  block/context: Коротка відповідь
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/utylizaciya-importnyh-tovariv.html
  block/context: Пов'язані сторінки
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/utylizaciya-importnyh-tovariv.html
  block/context: Пов'язані сторінки
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/utylizaciya-konfidenciynykh-dokumentiv.html
  block/context: Пов’язані матеріали
  anchor text: Знищення косметики
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-napoyiv.html
  block/context: Контекстні переходи за темою напоїв
  anchor text: утилізація скла
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-napoyiv.html
  block/context: Контекстні переходи за темою напоїв
  anchor text: утилізація пластику
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-napoyiv.html
  block/context: Дивіться також
  anchor text: Утилізація скляної тари
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-napoyiv.html
  block/context: Дивіться також
  anchor text: Утилізація пластикової тари
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: утилізація промислового обладнання
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: утилізація промислового обладнання
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/utylizaciya.html
  block/context: Як визначити маршрут поводження з продукцією
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/vidhody.html
  block/context: Сторінки розділу
  anchor text: Пластикові відходи
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/vidhody.html
  block/context: Сторінки розділу
  anchor text: Відходи демонтажу: сортування та утилізація
  current href: /utylizaciya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/vidhody.html
  block/context: Сторінки розділу
  anchor text: Відходи гуми: що відноситься і як утилізують
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/vidhody.html
  block/context: Пов’язані матеріали
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/vidhody.html
  block/context: Що означають основні терміни поводження з відходами
  anchor text: Що таке переробка відходів
  current href: /utylizaciya.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/vnutrishniy-akt-spysannya.html
  block/context: Як визначити маршрут передачі
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Які Li-ion батареї підлягають передачі
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Типові сценарії передачі
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Як відбувається процес утилізації
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/zbir.html
  block/context: Як визначити маршрут передачі
  anchor text: як визначити: переробка чи утилізація
  current href: /chy-potribno-pererobyty-chy-utylizuvaty.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: REPLACE_HREF

## Generic hub placeholder links
- source file: public/akt-pryimannya-peredachi.html
  block/context: main content
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/akt-pryimannya-peredachi.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/akt-pryimannya-peredachi.html
  block/context: Дивіться також
  anchor text: Логістика і вивезення партій
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/akt-pryimannya-peredachi.html
  block/context: Дивіться також
  anchor text: Хаб утилізації відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/akt-utylizaciyi.html
  block/context: main content
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/akt-utylizaciyi.html
  block/context: Дивіться також
  anchor text: Повний комплект документів
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/chy-potribno-pererobyty-chy-utylizuvaty.html
  block/context: У чому різниця між переробкою та утилізацією
  anchor text: що таке переробка відходів
  current href: /utylizaciya.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: KEEP_HUB
- source file: public/chy-potribno-pererobyty-chy-utylizuvaty.html
  block/context: У чому різниця між переробкою та утилізацією
  anchor text: що таке утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/chy-potribno-pererobyty-chy-utylizuvaty.html
  block/context: Як визначити правильний маршрут поводження з продукцією
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/chy-potribno-pererobyty-chy-utylizuvaty.html
  block/context: Коли застосовується переробка
  anchor text: як відбувається переробка відходів
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/chy-potribno-pererobyty-chy-utylizuvaty.html
  block/context: Коли застосовується утилізація
  anchor text: як відбувається утилізація продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/chy-potribno-pererobyty-chy-utylizuvaty.html
  block/context: Які документи оформлюються залежно від маршруту
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/chy-potribno-pererobyty-chy-utylizuvaty.html
  block/context: Як підготувати продукцію до передачі
  anchor text: сортування відходів
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/chy-potribno-pererobyty-chy-utylizuvaty.html
  block/context: Як підготувати продукцію до передачі
  anchor text: збір відходів
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/chy-potribno-pererobyty-chy-utylizuvaty.html
  block/context: Як підготувати продукцію до передачі
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/dokumenty-dlya-utylizaciyi-vidhodiv.html
  block/context: main content
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/dokumenty-dlya-utylizaciyi-vidhodiv.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/dokumenty-dlya-utylizaciyi-vidhodiv.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/dokumenty.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/dokumenty.html
  block/context: Дивіться також
  anchor text: Логістика і вивезення партій
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/dokumenty.html
  block/context: Дивіться також
  anchor text: Хаб утилізації відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/fotozvit-utylizaciyi.html
  block/context: main content
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/index.html
  block/context: Останні статті
  anchor text: Документи для утилізації відходів
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/kabelni-vidhody.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/kabelni-vidhody.html
  block/context: Дивіться також
  anchor text: Логістика і вивезення партій
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/kabelni-vidhody.html
  block/context: Дивіться також
  anchor text: Хаб утилізації відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/kontakty.html
  block/context: Читайте також
  anchor text: Огляд: Утилізація промислових відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/kontakty.html
  block/context: Читайте також
  anchor text: Утилізація шин
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/likvidaciya-skladskykh-zalyshkiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/likvidaciya-skladskykh-zalyshkiv.html
  block/context: Маршрут передачі продукції
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka/index.html
  block/context: main content
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka/index.html
  block/context: Матеріали про логістику відходів
  anchor text: пакет документів
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka/index.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka/index.html
  block/context: Дивіться також
  anchor text: Логістика і вивезення партій
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka/index.html
  block/context: Дивіться також
  anchor text: Хаб утилізації відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-budivelnyh-vidhodiv.html
  block/context: main content
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-budivelnyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-budivelnyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-budivelnyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-kabelyu.html
  block/context: main content
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-kabelyu.html
  block/context: Дивіться також
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-kabelyu.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-kabelyu.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-metalu.html
  block/context: main content
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-metalu.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-metalu.html
  block/context: Дивіться також
  anchor text: Логістика і вивезення партій
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-metalu.html
  block/context: Дивіться також
  anchor text: Хаб утилізації відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-paperu-ta-kartonu.html
  block/context: main content
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-paperu-ta-kartonu.html
  block/context: Дивіться також
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-paperu-ta-kartonu.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-paperu-ta-kartonu.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-plastyku.html
  block/context: main content
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-plastyku.html
  block/context: Дивіться також
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-plastyku.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-plastyku.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-promyslovyh-vidhodiv.html
  block/context: main content
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-promyslovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-promyslovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-promyslovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-shyn.html
  block/context: main content
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-shyn.html
  block/context: Дивіться також
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-shyn.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-shyn.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-skla.html
  block/context: main content
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-skla.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-skla.html
  block/context: Дивіться також
  anchor text: Логістика і вивезення партій
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka-skla.html
  block/context: Дивіться також
  anchor text: Хаб утилізації відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka.html
  block/context: Корисні матеріали довідника
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka.html
  block/context: Корисні матеріали довідника
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka.html
  block/context: Корисні матеріали довідника
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka.html
  block/context: Корисні матеріали довідника
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka.html
  block/context: Корисні матеріали довідника
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/logistyka.html
  block/context: Які документи супроводжують логістику передачі відходів
  anchor text: Документи передачі відходів
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/nebezpeka-vidpracovanogo-masla.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/nebezpeka-vidpracovanogo-masla.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/nebezpeka-vidpracovanogo-masla.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/oblik-promyslovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/oblik-promyslovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/oblik-promyslovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/optymizaciya-vidhodiv-na-vyrobnyctvi.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/optymizaciya-vidhodiv-na-vyrobnyctvi.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/optymizaciya-vidhodiv-na-vyrobnyctvi.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka/index.html
  block/context: Швидка орієнтація
  anchor text: документальному розділі
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-alyuminiyevogo-kabelyu.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-alyuminiyevogo-kabelyu.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-alyuminiyevogo-kabelyu.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-alyuminiyevogo-kabelyu.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-avtomobilnyh-shyn.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-avtomobilnyh-shyn.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-avtomobilnyh-shyn.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-avtomobilnyh-shyn.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-betonu.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-betonu.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-betonu.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-betonu.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-cegly.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-cegly.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-cegly.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-cegly.html
  block/context: Дивіться також
  anchor text: Логістика і вивезення партій
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-cegly.html
  block/context: Дивіться також
  anchor text: Хаб утилізації відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-gumovyh-vyrobiv.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-gumovyh-vyrobiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-gumovyh-vyrobiv.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-gumovyh-vyrobiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-izolyaciyi-kabelyu.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-izolyaciyi-kabelyu.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-izolyaciyi-kabelyu.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-izolyaciyi-kabelyu.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-kartonu.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-kartonu.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-kartonu.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-kartonu.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-makulatury.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-makulatury.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-makulatury.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-makulatury.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-metalu.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-metalu.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-metalu.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-metalu.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-midnogo-kabelyu.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-midnogo-kabelyu.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-midnogo-kabelyu.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-midnogo-kabelyu.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-pet.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-pet.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-pet.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-pet.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-plastykovoyi-upakovky.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-plastykovoyi-upakovky.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-plastykovoyi-upakovky.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-plastykovoyi-upakovky.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-polietylenu.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-polietylenu.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-polietylenu.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-polietylenu.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-polipropylenu.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-polipropylenu.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-polipropylenu.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-polipropylenu.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-polistyrolu.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-polistyrolu.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-polistyrolu.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-polistyrolu.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-shyn.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-shyn.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-shyn.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-shyn.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-skla.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-skla.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-skla.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-skla.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-vidpracovanyh-masel.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-vidpracovanyh-masel.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-vidpracovanyh-masel.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka-vidpracovanyh-masel.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka.html
  block/context: Корисні матеріали довідника
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka.html
  block/context: Корисні матеріали довідника
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka.html
  block/context: Корисні матеріали довідника
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka.html
  block/context: Корисні матеріали довідника
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pererobka.html
  block/context: Корисні матеріали довідника
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/plastyk-yak-vtorynna-syrovyna.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/plastyk-yak-vtorynna-syrovyna.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/plastyk-yak-vtorynna-syrovyna.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/plastykovi-vidhody.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/plastykovi-vidhody.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/plastykovi-vidhody.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/podribnennya-shyn-gumova-kryshka.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/podribnennya-shyn-gumova-kryshka.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/povernennya-tovariv-z-merezhi.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/povernennya-tovariv-z-merezhi.html
  block/context: Пов'язані матеріали
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/promyslovi-vidhody-na-pidpryyemstvi.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/promyslovi-vidhody-na-pidpryyemstvi.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/promyslovi-vidhody-na-pidpryyemstvi.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/promyslovi-vidhody.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/promyslovi-vidhody.html
  block/context: Дивіться також
  anchor text: Логістика і вивезення партій
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/promyslovi-vidhody.html
  block/context: Дивіться також
  anchor text: Хаб утилізації відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pryjom-kabelyu-na-utylizaciyu.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pryjom-kabelyu-na-utylizaciyu.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/pryjom-kabelyu-na-utylizaciyu.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/reestr-partiyi.html
  block/context: main content
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/scenarii-utilizaciyi.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/shcho-take-pererobka-vidhodiv.html
  block/context: main content
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/shcho-take-utylizaciya.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/shcho-take-znyshchennya-produkciyi.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/skilky-koshtuye-pererobka-kabelyu.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/skilky-koshtuye-pererobka-kabelyu.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/skilky-koshtuye-pererobka-kabelyu.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/skladuvannya-promyslovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/skladuvannya-promyslovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/skladuvannya-promyslovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya/index.html
  block/context: main content
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya/index.html
  block/context: Матеріали про сортування відходів
  anchor text: документів
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya/index.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya/index.html
  block/context: Дивіться також
  anchor text: Логістика і вивезення партій
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya/index.html
  block/context: Дивіться також
  anchor text: Хаб утилізації відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya-budivelnyh-vidhodiv.html
  block/context: main content
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya-budivelnyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya-budivelnyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya-plastyku.html
  block/context: main content
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya-plastyku.html
  block/context: Дивіться також
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya-plastyku.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya-promyslovyh-vidhodiv.html
  block/context: main content
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya-promyslovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya-promyslovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya.html
  block/context: Сторінки розділу
  anchor text: Сортування будівельного відходи
  current href: /utylizaciya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: NEEDS_DECISION
- source file: public/sortuvannya.html
  block/context: Сторінки розділу
  anchor text: Сортування пластику
  current href: /utylizaciya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: NEEDS_DECISION
- source file: public/sortuvannya.html
  block/context: Сторінки розділу
  anchor text: Сортування промислових відходів
  current href: /utylizaciya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: KEEP_HUB
- source file: public/sortuvannya.html
  block/context: Корисні матеріали довідника
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya.html
  block/context: Корисні матеріали довідника
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya.html
  block/context: Корисні матеріали довідника
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya.html
  block/context: Корисні матеріали довідника
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/sortuvannya.html
  block/context: Корисні матеріали довідника
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/spysannya-kosmetychnyh-tovariv.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/spysannya-kosmetychnyh-tovariv.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/spysannya-kosmetychnyh-tovariv.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/spysannya-produkciyi.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/spysannya-produkciyi.html
  block/context: Пов'язані категорії утилізації
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/spysannya-produktiv.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/spysannya-produktiv.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/spysannya-produktiv.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/transportuvannya-vidpracovanyh-masel.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/transportuvannya-vidpracovanyh-masel.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/transportuvannya-vidpracovanyh-masel.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/transportuvannya-vidpracovanyh-shyn.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/transportuvannya-vidpracovanyh-shyn.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/transportuvannya-vidpracovanyh-shyn.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-brakovanoi-produkciyi.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-brakovanoi-produkciyi.html
  block/context: Пов'язані категорії утилізації
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-bankiv.html
  block/context: Типові сценарії утилізації для банків
  anchor text: утилізація офісної техніки
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-bankiv.html
  block/context: Типові сценарії утилізації для банків
  anchor text: що таке знищення продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-bankiv.html
  block/context: Як підготувати продукцію до передачі
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-bankiv.html
  block/context: Як підготувати продукцію до передачі
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-bankiv.html
  block/context: Які документи оформлюються
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-bankiv.html
  block/context: Як відбувається процес утилізації
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-bankiv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-bankiv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-bankiv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: утилізація офісної техніки
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-bankiv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: що таке знищення продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-bankiv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-bankiv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-data-centriv.html
  block/context: Типові сценарії утилізації для галузі
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utilizaciya-dlya-data-centriv.html
  block/context: Як підготувати продукцію до передачі
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-data-centriv.html
  block/context: Як підготувати продукцію до передачі
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-data-centriv.html
  block/context: Які документи оформлюються
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-data-centriv.html
  block/context: Як відбувається процес утилізації
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-data-centriv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utilizaciya-dlya-data-centriv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-data-centriv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-data-centriv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-data-centriv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-importeriv.html
  block/context: Як підготувати продукцію до передачі
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-importeriv.html
  block/context: Як підготувати продукцію до передачі
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-importeriv.html
  block/context: Які документи оформлюються
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-importeriv.html
  block/context: Як відбувається процес утилізації
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-importeriv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-importeriv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-importeriv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-importeriv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-riteylu.html
  block/context: Як підготувати продукцію до передачі
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-riteylu.html
  block/context: Як підготувати продукцію до передачі
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-riteylu.html
  block/context: Які документи оформлюються
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-riteylu.html
  block/context: Як відбувається процес утилізації
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-riteylu.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-riteylu.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-riteylu.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-riteylu.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-skladiv.html
  block/context: Як підготувати продукцію до передачі
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-skladiv.html
  block/context: Як підготувати продукцію до передачі
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-skladiv.html
  block/context: Які документи оформлюються
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-skladiv.html
  block/context: Як відбувається процес утилізації
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-skladiv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-skladiv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-skladiv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-skladiv.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-vyrobnyctva.html
  block/context: Як підготувати продукцію до передачі
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-vyrobnyctva.html
  block/context: Як підготувати продукцію до передачі
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-vyrobnyctva.html
  block/context: Які документи оформлюються
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-vyrobnyctva.html
  block/context: Як відбувається процес утилізації
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-vyrobnyctva.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-vyrobnyctva.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-vyrobnyctva.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utilizaciya-dlya-vyrobnyctva.html
  block/context: Пов’язані маршрути передачі продукції
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya/index.html
  block/context: Пов'язані розділи
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Коротка відповідь
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Коротка відповідь
  anchor text: утилізація павербанків та ДБЖ
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: утилізація павербанків та ДБЖ
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: сортування відходів
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: збір відходів
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: утилізація павербанків та ДБЖ
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: сортування відходів
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: збір відходів
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-akumulyatoriv.html
  block/context: Пов'язані сторінки
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-avtoshyn.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-avtoshyn.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-avtoshyn.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-avtoshyn.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-budivelnyh-vidhodiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-budivelnyh-vidhodiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-budivelnyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-budivelnyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-derevyny-z-budivnyctva.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-derevyny-z-budivnyctva.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-derevyny-z-budivnyctva.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-derevyny-z-budivnyctva.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-dokumentiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-dokumentiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-dokumentiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-dokumentiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-elektroniky.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-elektroniky.html
  block/context: Коротка відповідь
  anchor text: утилізація офісної техніки
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-elektroniky.html
  block/context: Коротка відповідь
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: утилізація офісної техніки
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: сортування відходів
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: збір відходів
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: утилізація офісної техніки
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: сортування відходів
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: збір відходів
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-elektroniky.html
  block/context: Пов'язані сторінки
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-energetychnyh-napoyiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-energetychnyh-napoyiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-energetychnyh-napoyiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-energetychnyh-napoyiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-fruktiv-ta-ovochiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-fruktiv-ta-ovochiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-fruktiv-ta-ovochiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-fruktiv-ta-ovochiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-fruktiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-fruktiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-fruktiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-fruktiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-gazovanyh-napoyiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-gazovanyh-napoyiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-gazovanyh-napoyiv.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-gazovanyh-napoyiv.html
  block/context: Дивіться також
  anchor text: Логістика і вивезення партій
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-gazovanyh-napoyiv.html
  block/context: Дивіться також
  anchor text: Хаб утилізації відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-gazovanyh-napoyiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-gazovanyh-napoyiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-gipsokartonu.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-gipsokartonu.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-gipsokartonu.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-gipsokartonu.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-harchovyh-produktiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-harchovyh-produktiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-harchovyh-produktiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-harchovyh-produktiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-importnyh-tovariv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-importnyh-tovariv.html
  block/context: Коротка відповідь
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-importnyh-tovariv.html
  block/context: Коротка відповідь
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-importnyh-tovariv.html
  block/context: Пов'язані сторінки
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-importnyh-tovariv.html
  block/context: Пов'язані сторінки
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-importnyh-tovariv.html
  block/context: Пов'язані сторінки
  anchor text: утилізація товарів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-importnyh-tovariv.html
  block/context: Пов'язані сторінки
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-importnyh-tovariv.html
  block/context: Пов'язані сторінки
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-importnyh-tovariv.html
  block/context: Пов'язані сторінки
  anchor text: утилізація товарів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kabelyu-ta-drotiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kabelyu-ta-drotiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kabelyu-ta-drotiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kabelyu-ta-drotiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kondyterskyh-vyrobiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kondyterskyh-vyrobiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kondyterskyh-vyrobiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kondyterskyh-vyrobiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-konfidenciynykh-dokumentiv.html
  block/context: main content
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-konfidenciynykh-dokumentiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-konfidenciynykh-dokumentiv.html
  block/context: Пов’язані матеріали
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-konfidenciynykh-dokumentiv.html
  block/context: Пов’язані матеріали
  anchor text: Документи для утилізації відходів
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-konfidenciynykh-dokumentiv.html
  block/context: Пов’язані матеріали
  anchor text: Облік промислових відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-konfidenciynykh-dokumentiv.html
  block/context: Пов’язані матеріали
  anchor text: Знищення косметики
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-konserviv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-konserviv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-konserviv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-konserviv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kosmetyky-magazyniv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kosmetyky-magazyniv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kosmetyky-magazyniv.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kosmetyky-magazyniv.html
  block/context: Дивіться також
  anchor text: Логістика і вивезення партій
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kosmetyky-magazyniv.html
  block/context: Дивіться також
  anchor text: Хаб утилізації відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kosmetyky.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kosmetyky.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kosmetyky.html
  block/context: Які документи оформлюються під час передачі косметики на утилізацію
  anchor text: Документи передачі відходів
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-kosmetyky.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-li-ion-batarej.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-li-ion-batarej.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-li-ion-batarej.html
  block/context: Які документи оформлюються під час передачі Li-ion батарей
  anchor text: Документи передачі відходів
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-li-ion-batarej.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-li-ion-batarej.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-materialiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-materialiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-materialiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-materialiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-metalevoyi-strushky.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-metalevoyi-strushky.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-metalevoyi-strushky.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-metalevoyi-strushky.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-metalu.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-metalu.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-metalu.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-metalu.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-molochnyh-produktiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-molochnyh-produktiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-molochnyh-produktiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-molochnyh-produktiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-myasnyh-produktiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-myasnyh-produktiv.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-myasnyh-produktiv.html
  block/context: Дивіться також
  anchor text: Логістика і вивезення партій
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-myasnyh-produktiv.html
  block/context: Дивіться також
  anchor text: Хаб утилізації відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-napivfabrykatyv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-napivfabrykatyv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-napivfabrykatyv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-napivfabrykatyv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-napoyiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-napoyiv.html
  block/context: Контекстні переходи за темою напоїв
  anchor text: утилізація тари та упаковки
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-napoyiv.html
  block/context: Контекстні переходи за темою напоїв
  anchor text: утилізація скла
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-napoyiv.html
  block/context: Контекстні переходи за темою напоїв
  anchor text: утилізація пластику
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-napoyiv.html
  block/context: Дивіться також
  anchor text: Утилізація тари та упаковки
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-napoyiv.html
  block/context: Дивіться також
  anchor text: Утилізація скляної тари
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-napoyiv.html
  block/context: Дивіться також
  anchor text: Утилізація пластикової тари
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-nekondicijnoyi-sirovini.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-nekondicijnoyi-sirovini.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-nekondicijnoyi-sirovini.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-nekondicijnoyi-sirovini.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-nekondyciynoyi-produkciyi.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-nekondyciynoyi-produkciyi.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-nekondyciynoyi-produkciyi.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-nekondyciynoyi-produkciyi.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-obladnannya.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-obladnannya.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: утилізація промислового обладнання
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: утилізація офісної техніки та меблів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: сортування відходів
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: збір відходів
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: утилізація промислового обладнання
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: утилізація офісної техніки та меблів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: сортування відходів
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: збір відходів
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-obladnannya.html
  block/context: Дивіться також
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-odyagu-vzuttya.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-odyagu-vzuttya.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-odyagu-vzuttya.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-odyagu-vzuttya.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-ofisnih-mebliv-orgtehniki.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-ofisnih-mebliv-orgtehniki.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-ofisnih-mebliv-orgtehniki.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-ofisnih-mebliv-orgtehniki.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-ovochiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-ovochiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-ovochiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-ovochiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-paperu-ta-kartonu.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-paperu-ta-kartonu.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-paperu-ta-kartonu.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-paperu-ta-kartonu.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-parfumeriyi.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-parfumeriyi.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-parfumeriyi.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-parfumeriyi.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-partiyi-produktiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-partiyi-produktiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-partiyi-produktiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-partiyi-produktiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-paverbankiv-dbj.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-paverbankiv-dbj.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-paverbankiv-dbj.html
  block/context: У яких сценаріях підприємства передають павербанки та ДБЖ на утилізацію
  anchor text: Типові сценарії передачі продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-paverbankiv-dbj.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-paverbankiv-dbj.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-plastyku-ta-polimeriv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-plastyku-ta-polimeriv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-plastyku-ta-polimeriv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-plastyku-ta-polimeriv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-produktiv-harchuvannya-napoyiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-produktiv-harchuvannya-napoyiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-produktiv-harchuvannya-napoyiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-produktiv-harchuvannya-napoyiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-produktiv-na-skladi.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-produktiv-na-skladi.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-produktiv-na-skladi.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-produktiv-na-skladi.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-promyslovogo-obladnannya-mehanizmiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-promyslovogo-obladnannya-mehanizmiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-promyslovogo-obladnannya-mehanizmiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-promyslovogo-obladnannya-mehanizmiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-promyslovyh-vidhodiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-promyslovyh-vidhodiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-promyslovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-promyslovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-prostrochenoyi-kosmetyky.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-prostrochenoyi-kosmetyky.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-prostrochenoyi-kosmetyky.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-prostrochenoyi-kosmetyky.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-prostrochenyh-produktiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-prostrochenyh-produktiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-prostrochenyh-produktiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-prostrochenyh-produktiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-pyva.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-pyva.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-pyva.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-pyva.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-rybnyh-produktiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-rybnyh-produktiv.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-rybnyh-produktiv.html
  block/context: Дивіться також
  anchor text: Логістика і вивезення партій
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-rybnyh-produktiv.html
  block/context: Дивіться також
  anchor text: Хаб утилізації відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-shyn-pidpryyemstvamy.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-shyn-pidpryyemstvamy.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-shyn-pidpryyemstvamy.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-shyn-pidpryyemstvamy.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-shyn.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-shyn.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-shyn.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-shyn.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-skla.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-skla.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-skla.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-skla.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
  block/context: Дивіться також
  anchor text: Логістика і вивезення партій
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
  block/context: Дивіться також
  anchor text: Хаб утилізації відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-skladskyh-zalyshkiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-skladskyh-zalyshkiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-skladskyh-zalyshkiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-skladskyh-zalyshkiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-sokiv-ta-napoyiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-sokiv-ta-napoyiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-sokiv-ta-napoyiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-sokiv-ta-napoyiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-sokiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-sokiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-sokiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-sokiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-sonyachnih-panelij-vitryakiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-sonyachnih-panelij-vitryakiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-sonyachnih-panelij-vitryakiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-sonyachnih-panelij-vitryakiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-tary-upakovki.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-tary-upakovki.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-tary-upakovki.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-tary-upakovki.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-tovariv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-tovariv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-tovariv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-tovariv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-tovary-pid-mitnim-kontrolem.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-tovary-pid-mitnim-kontrolem.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-tovary-pid-mitnim-kontrolem.html
  block/context: Які сценарії виникають під час утилізації товарів під митним контролем
  anchor text: Типові сценарії передачі продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-tovary-pid-mitnim-kontrolem.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-tovary-pid-mitnim-kontrolem.html
  block/context: Дивіться також
  anchor text: Логістика і вивезення партій
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-tovary-pid-mitnim-kontrolem.html
  block/context: Дивіться також
  anchor text: Хаб утилізації відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-upakovky-na-pidpryyemstvi.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-upakovky-na-pidpryyemstvi.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-upakovky-na-pidpryyemstvi.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-upakovky-na-pidpryyemstvi.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-upakovky-vid-kosmetyky.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-upakovky-vid-kosmetyky.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-upakovky-vid-kosmetyky.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-upakovky-vid-kosmetyky.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vantazhnyh-shyn.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vantazhnyh-shyn.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vantazhnyh-shyn.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vantazhnyh-shyn.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vidpracovanoi-olyvy.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vidpracovanoi-olyvy.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vidpracovanoi-olyvy.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vidpracovanoi-olyvy.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vidpracovanyh-masel.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vidpracovanyh-masel.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vidpracovanyh-masel.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vidpracovanyh-masel.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vody.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vody.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vody.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vody.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vyrobnychyh-vidhodiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vyrobnychyh-vidhodiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vyrobnychyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-vyrobnychyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-yagid.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-yagid.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-yagid.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-yagid.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-zamorozhenyh-produktiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-zamorozhenyh-produktiv.html
  block/context: Коротка відповідь
  anchor text: документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-zamorozhenyh-produktiv.html
  block/context: Дивіться також
  anchor text: Документи для передачі та списання
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-zamorozhenyh-produktiv.html
  block/context: Дивіться також
  anchor text: Логістика і вивезення партій
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-zamorozhenyh-produktiv.html
  block/context: Дивіться також
  anchor text: Хаб утилізації відходів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-zamorozhenyh-produktiv.html
  block/context: Дивіться також
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-zamorozhenyh-produktiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya-zipsovanyh-produktiv.html
  block/context: main content
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya.html
  block/context: Корисні матеріали довідника
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya.html
  block/context: Корисні матеріали довідника
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya.html
  block/context: Корисні матеріали довідника
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya.html
  block/context: Корисні матеріали довідника
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya.html
  block/context: Корисні матеріали довідника
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya.html
  block/context: Що потрібно перевірити перед передачею партії на утилізацію
  anchor text: Типові сценарії передачі продукції на утилізацію
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya.html
  block/context: Що потрібно перевірити перед передачею партії на утилізацію
  anchor text: Документи для передачі відходів
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/utylizaciya.html
  block/context: Що означає процедура утилізації матеріалів
  anchor text: Що таке утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody-demontazhu.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody-demontazhu.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody-demontazhu.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody-gumy.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody-gumy.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody-gumy.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody-polimeriv.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody-polimeriv.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody-polimeriv.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody-vyrobnyctva.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody-vyrobnyctva.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody-vyrobnyctva.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Сторінки розділу
  anchor text: Пластикові відходи
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/vidhody.html
  block/context: Сторінки розділу
  anchor text: Промислові відходи на підприємстві: облік і правила
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Сторінки розділу
  anchor text: Відходи демонтажу: сортування та утилізація
  current href: /utylizaciya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Сторінки розділу
  anchor text: Відходи гуми: що відноситься і як утилізують
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/vidhody.html
  block/context: Сторінки розділу
  anchor text: Відходи полімерів
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Сторінки розділу
  anchor text: Відходи виробництва: класифікація та приклади
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Пов’язані матеріали
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Пов’язані матеріали
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Пов’язані матеріали
  anchor text: переробка відходів
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Пов’язані матеріали
  anchor text: сортування відходів
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Пов’язані матеріали
  anchor text: збір відходів
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Пов’язані матеріали
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Корисні матеріали довідника
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Корисні матеріали довідника
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Корисні матеріали довідника
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Корисні матеріали довідника
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Корисні матеріали довідника
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Корисні матеріали довідника
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Типові сценарії передачі продукції на утилізацію
  anchor text: Типові сценарії передачі продукції на утилізацію
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Що означають основні терміни поводження з відходами
  anchor text: Що таке промислові відходи
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidhody.html
  block/context: Що означають основні терміни поводження з відходами
  anchor text: Що таке переробка відходів
  current href: /utylizaciya.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: False
  recommendation: KEEP_HUB
- source file: public/vidy-kabelnyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidy-kabelnyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidy-kabelnyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidy-plastykovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidy-plastykovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vidy-plastykovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vnutrishniy-akt-spysannya.html
  block/context: main content
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vtorynna-syrovyna-z-budivelnyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vtorynna-syrovyna-z-budivelnyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vtorynna-syrovyna-z-budivelnyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vtorynna-syrovyna-z-vidhodiv.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vtorynna-syrovyna-z-vidhodiv.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vtorynna-syrovyna-z-vidhodiv.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vymogy-do-zberigannya-vidhodiv.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vymogy-do-zberigannya-vidhodiv.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vymogy-do-zberigannya-vidhodiv.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vyviz-budivelnyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vyviz-budivelnyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/vyviz-budivelnyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Які документи входять до пакета списання
  anchor text: внутрішній акт списання
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Які документи входять до пакета списання
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Як підготувати внутрішні документи
  anchor text: внутрішній акт списання
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Як оформлюється передача продукції
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Типові сценарії списання партій
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Як підтверджується утилізація продукції
  anchor text: внутрішній акт списання
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Як підтверджується утилізація продукції
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Корисні переходи
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Корисні переходи
  anchor text: сортування відходів
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Корисні переходи
  anchor text: збір відходів
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Корисні переходи
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Корисні переходи
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Корисні переходи
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Корисні переходи
  anchor text: сортування відходів
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Корисні переходи
  anchor text: збір відходів
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Корисні переходи
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-oformyty-spysannya-partiyi.html
  block/context: Корисні переходи
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-kosmetyku.html
  block/context: Які документи оформлюються
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-kosmetyku.html
  block/context: Типові сценарії передачі
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-kosmetyku.html
  block/context: Як відбувається утилізація косметики
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-kosmetyku.html
  block/context: Пов'язані матеріали та сценарії передачі
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-kosmetyku.html
  block/context: Пов'язані матеріали та сценарії передачі
  anchor text: сортування відходів
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-kosmetyku.html
  block/context: Пов'язані матеріали та сценарії передачі
  anchor text: збір відходів
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-kosmetyku.html
  block/context: Пов'язані матеріали та сценарії передачі
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-kosmetyku.html
  block/context: Пов'язані матеріали та сценарії передачі
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-kosmetyku.html
  block/context: Пов'язані матеріали та сценарії передачі
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-kosmetyku.html
  block/context: Пов'язані матеріали та сценарії передачі
  anchor text: сортування відходів
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-kosmetyku.html
  block/context: Пов'язані матеріали та сценарії передачі
  anchor text: збір відходів
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-kosmetyku.html
  block/context: Пов'язані матеріали та сценарії передачі
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-kosmetyku.html
  block/context: Пов'язані матеріали та сценарії передачі
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Які Li-ion батареї підлягають передачі
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Як підготувати батареї до транспортування
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Як підготувати батареї до транспортування
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Які документи оформлюються
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Типові сценарії передачі
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Як відбувається процес утилізації
  anchor text: утилізація Li-ion батарей
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: NEEDS_DECISION
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Як відбувається процес утилізації
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Як відбувається процес утилізації
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: сортування відходів
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: збір відходів
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: сортування відходів
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: збір відходів
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-li-ion-batarei.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-skladski-zalyshky.html
  block/context: Які документи оформлюються
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-skladski-zalyshky.html
  block/context: Типові сценарії ліквідації залишків
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-skladski-zalyshky.html
  block/context: Як відбувається процес передачі
  anchor text: документи утилізації
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-skladski-zalyshky.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-skladski-zalyshky.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: сортування відходів
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-skladski-zalyshky.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: збір відходів
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-skladski-zalyshky.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-skladski-zalyshky.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-skladski-zalyshky.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: сценарії утилізації
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-skladski-zalyshky.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: сортування відходів
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-skladski-zalyshky.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: збір відходів
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-skladski-zalyshky.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: логістика передачі відходів
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/yak-peredaty-skladski-zalyshky.html
  block/context: Пов'язані матеріали та процес передачі
  anchor text: процес утилізації продукції
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zberigannya-vidpracovanyh-masel.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zberigannya-vidpracovanyh-masel.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zberigannya-vidpracovanyh-masel.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-kabelyu.html
  block/context: main content
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-kabelyu.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-kabelyu.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-kartonu-na-pidpryyemstvi.html
  block/context: main content
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-kartonu-na-pidpryyemstvi.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-kartonu-na-pidpryyemstvi.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-metalu-na-pidpryyemstvi.html
  block/context: main content
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-metalu-na-pidpryyemstvi.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-metalu-na-pidpryyemstvi.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-plastyku-na-pidpryyemstvi.html
  block/context: main content
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-plastyku-na-pidpryyemstvi.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-plastyku-na-pidpryyemstvi.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-promyslovyh-vidhodiv.html
  block/context: main content
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-promyslovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-promyslovyh-vidhodiv.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-shyn-na-pidpryyemstvi.html
  block/context: main content
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-shyn-na-pidpryyemstvi.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-shyn-na-pidpryyemstvi.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-sklyanoyi-tary.html
  block/context: main content
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-sklyanoyi-tary.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-sklyanoyi-tary.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-vidpracovanoyi-olyvy.html
  block/context: main content
  anchor text: Збір
  current href: /zbir.html
  proposed href: /zbir.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-vidpracovanoyi-olyvy.html
  block/context: Дивіться також
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir-vidpracovanoyi-olyvy.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir.html
  block/context: Корисні матеріали довідника
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir.html
  block/context: Корисні матеріали довідника
  anchor text: Логістика
  current href: /logistyka.html
  proposed href: /logistyka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir.html
  block/context: Корисні матеріали довідника
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir.html
  block/context: Корисні матеріали довідника
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir.html
  block/context: Корисні матеріали довідника
  anchor text: Документи
  current href: /dokumenty.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/zbir.html
  block/context: Як визначають сценарій передачі матеріалів перед збором
  anchor text: Типові сценарії передачі продукції на утилізацію
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/znyshchennya-kosmetyky.html
  block/context: Дивіться також
  anchor text: Утилізація
  current href: /utylizaciya.html
  proposed href: 
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/znyshchennya-kosmetyky.html
  block/context: Дивіться також
  anchor text: Переробка
  current href: /pererobka.html
  proposed href: /pererobka.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
- source file: public/znyshchennya-kosmetyky.html
  block/context: Дивіться також
  anchor text: Сортування
  current href: /sortuvannya.html
  proposed href: /sortuvannya.html
  target exists: True
  target noindex: False
  target has sidebar: True
  topic match: True
  recommendation: KEEP_HUB
