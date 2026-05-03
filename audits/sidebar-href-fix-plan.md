# Sidebar Href Fix Plan

Diagnostics only. Source: `audits/full-sidebar-link-integrity-audit.json`. Scope: existing standard sidebar links only; no main content, no sidebar additions, no active-state changes.

## A. Summary
|Metric|Value|
|---|---|
|affected pages with standard sidebar|66|
|total sidebar WRONG_TOPIC /utylizaciya.html links|594|
|unique href replacements|9|

## B. Unique Replacements
|anchor text|current href|expected href|occurrences|
|---|---|---|---|
|♻️ Пластик та полімери|/utylizaciya.html|/utylizaciya-plastyku-ta-polimeriv.html|66|
|⭕ Шини|/utylizaciya.html|/utylizaciya-shyn.html|66|
|🏗️ Будівельні відходи|/utylizaciya.html|/utylizaciya-budivelnyh-vidhodiv.html|66|
|📄 Конфіденційні документи|/utylizaciya.html|/utylizaciya-konfidenciynykh-dokumentiv.html|66|
|📦 Тара та упаковка|/utylizaciya.html|/utylizaciya-tary-upakovki.html|66|
|🔋 Li-ion батареї|/utylizaciya.html|/utylizaciya-li-ion-batarej.html|66|
|🔌 Кабель та дроти|/utylizaciya.html|/utylizaciya-kabelyu-ta-drotiv.html|66|
|🖥️ Офісні меблі та оргтехніка|/utylizaciya.html|/utylizaciya-ofisnih-mebliv-orgtehniki.html|66|
|🛢️ Відпрацьована моторна олива|/utylizaciya.html|/utylizaciya-vidpracovanoi-olyvy.html|66|

## C. Affected Source Files
|source path|public path|title/H1|noindex|in sitemap|active item count|sidebar wrong-topic count|
|---|---|---|---|---|---|---|
|index.html|public/index.html|Довідник YOURECO про поводження з відходами для підприємств|no|yes|0|9|
|logistyka/index.html|public/logistyka/index.html|Матеріали про логістику відходів|no|yes|1|9|
|pererobka/index.html|public/pererobka/index.html|Матеріали про переробку відходів|no|yes|1|9|
|sortuvannya/index.html|public/sortuvannya/index.html|Матеріали про сортування відходів|no|yes|1|9|
|akt-pryimannya-peredachi.html|public/akt-pryimannya-peredachi.html|Акт приймання-передачі відходів: що це за документ і коли він потрібен|no|yes|0|9|
|akt-utylizaciyi.html|public/akt-utylizaciyi.html|Акт утилізації відходів: що підтверджує цей документ|no|yes|0|9|
|chy-potribno-pererobyty-chy-utylizuvaty.html|public/chy-potribno-pererobyty-chy-utylizuvaty.html|Чи потрібно переробити чи утилізувати продукцію|no|yes|0|9|
|dokumenty.html|public/dokumenty.html|Документи для утилізації відходів|no|yes|0|9|
|fotozvit-utylizaciyi.html|public/fotozvit-utylizaciyi.html|Фотозвіт утилізації: коли використовується і що підтверджує|no|yes|0|9|
|kabelni-vidhody.html|public/kabelni-vidhody.html|Кабельні відходи: класифікація та зберігання|no|yes|0|9|
|kudy-zdaty.html|public/kudy-zdaty.html|Куди здати|no|yes|0|9|
|likvidaciya-skladskykh-zalyshkiv.html|public/likvidaciya-skladskykh-zalyshkiv.html|Ліквідація складських залишків: як готують партію на передачу|no|yes|0|9|
|logistyka-metalu.html|public/logistyka-metalu.html|Логістика металу|no|yes|0|9|
|logistyka-skla.html|public/logistyka-skla.html|Логістика скла|no|yes|0|9|
|logistyka.html|public/logistyka.html|Логістика відходів для підприємств|no|yes|1|9|
|pererobka-cegly.html|public/pererobka-cegly.html|Як передають на переробку цеглу|no|yes|0|9|
|pererobka.html|public/pererobka.html|Порядок передання відходів на переробку|no|yes|0|9|
|povernennya-tovariv-z-merezhi.html|public/povernennya-tovariv-z-merezhi.html|Повернення товарів з мережі: коли партія переходить на утилізацію|no|yes|0|9|
|promyslovi-vidhody.html|public/promyslovi-vidhody.html|Промислові відходи|no|yes|0|9|
|sortuvannya.html|public/sortuvannya.html|Сортування відходів перед передачею|no|yes|1|9|
|spysannya-produkciyi.html|public/spysannya-produkciyi.html|Списання продукції: як рішення переходить у процедуру утилізації|no|yes|0|9|
|utilizaciya-brakovanoi-produkciyi.html|public/utilizaciya-brakovanoi-produkciyi.html|Утилізація бракованої продукції: як оформлюють партію браку|no|yes|0|9|
|utilizaciya-dlya-bankiv.html|public/utilizaciya-dlya-bankiv.html|Утилізація продукції та обладнання для банків|no|yes|0|9|
|utilizaciya-dlya-data-centriv.html|public/utilizaciya-dlya-data-centriv.html|Утилізація для дата-центрів|no|yes|0|9|
|utilizaciya-dlya-importeriv.html|public/utilizaciya-dlya-importeriv.html|Утилізація для імпортерів|no|yes|0|9|
|utilizaciya-dlya-riteylu.html|public/utilizaciya-dlya-riteylu.html|Утилізація для ритейлу|no|yes|0|9|
|utilizaciya-dlya-skladiv.html|public/utilizaciya-dlya-skladiv.html|Утилізація для складів|no|yes|0|9|
|utilizaciya-dlya-vyrobnyctva.html|public/utilizaciya-dlya-vyrobnyctva.html|Утилізація для виробництва|no|yes|0|9|
|utylizaciya-akumulyatoriv.html|public/utylizaciya-akumulyatoriv.html|Утилізація акумуляторів|no|yes|0|9|
|utylizaciya-elektroniky.html|public/utylizaciya-elektroniky.html|Утилізація електроніки|no|yes|0|9|
|utylizaciya-gazovanyh-napoyiv.html|public/utylizaciya-gazovanyh-napoyiv.html|Куди передають газовані напої на утилізацію|no|yes|0|9|
|utylizaciya-importnyh-tovariv.html|public/utylizaciya-importnyh-tovariv.html|Утилізація імпортних товарів|no|yes|0|9|
|utylizaciya-konfidenciynykh-dokumentiv.html|public/utylizaciya-konfidenciynykh-dokumentiv.html|Документи для утилізації конфіденційних документів|no|yes|0|9|
|utylizaciya-kosmetyky-magazyniv.html|public/utylizaciya-kosmetyky-magazyniv.html|Порядок утилізації косметики магазинів|no|yes|0|9|
|utylizaciya-kosmetyky.html|public/utylizaciya-kosmetyky.html|Порядок утилізації косметики для підприємств|no|yes|0|9|
|utylizaciya-myasnyh-produktiv.html|public/utylizaciya-myasnyh-produktiv.html|Куди передають м’ясні продукти на утилізацію|no|yes|0|9|
|utylizaciya-napoyiv.html|public/utylizaciya-napoyiv.html|Куди передають напої на утилізацію|no|yes|0|9|
|utylizaciya-obladnannya.html|public/utylizaciya-obladnannya.html|Порядок утилізації обладнання для підприємств|no|yes|0|9|
|utylizaciya-rybnyh-produktiv.html|public/utylizaciya-rybnyh-produktiv.html|Куди передають рибні продукти на утилізацію|no|yes|0|9|
|utylizaciya-skladskyh-zalyshkiv-kosmetyky.html|public/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html|Порядок утилізації складських залишків косметики|no|yes|0|9|
|utylizaciya-tovary-pid-mitnim-kontrolem.html|public/utylizaciya-tovary-pid-mitnim-kontrolem.html|Порядок утилізації товарів під митним контролем|no|yes|0|9|
|utylizaciya-zamorozhenyh-produktiv.html|public/utylizaciya-zamorozhenyh-produktiv.html|Куди передають заморожені продукти на утилізацію|no|yes|0|9|
|utylizaciya-zipsovanyh-produktiv.html|public/utylizaciya-zipsovanyh-produktiv.html|Куди передають зіпсовані продукти на утилізацію|no|yes|0|9|
|vidhody.html|public/vidhody.html|Види відходів і поводження з ними|no|yes|0|9|
|yak-oformyty-spysannya-partiyi.html|public/yak-oformyty-spysannya-partiyi.html|Як оформити списання партії продукції|no|yes|0|9|
|yak-peredaty-kosmetyku.html|public/yak-peredaty-kosmetyku.html|Як передати косметику на утилізацію|no|yes|0|9|
|yak-peredaty-li-ion-batarei.html|public/yak-peredaty-li-ion-batarei.html|Як передати Li-ion батареї на утилізацію|no|yes|0|9|
|yak-peredaty-skladski-zalyshky.html|public/yak-peredaty-skladski-zalyshky.html|Як передати складські залишки на утилізацію|no|yes|0|9|
|zbir.html|public/zbir.html|Збір відходів на підприємстві|no|yes|0|9|
|kontakty.html|public/kontakty.html|Контакти довідник YOURECO|yes|no|0|9|
|utylizaciya-budivelnyh-vidhodiv.html|public/utylizaciya-budivelnyh-vidhodiv.html|Порядок утилізації будівельних відходів для підприємств|yes|no|1|9|
|utylizaciya-kabelyu-ta-drotiv.html|public/utylizaciya-kabelyu-ta-drotiv.html|Як оформлюється утилізація кабелю та дротів|yes|no|1|9|
|utylizaciya-li-ion-batarej.html|public/utylizaciya-li-ion-batarej.html|Як оформлюється утилізація літій-іонних батарей|yes|no|1|9|
|utylizaciya-materialiv.html|public/utylizaciya-materialiv.html|Порядок утилізації матеріалів для підприємств|no|no|0|9|
|utylizaciya-nekondyciynoyi-produkciyi.html|public/utylizaciya-nekondyciynoyi-produkciyi.html|Порядок утилізації некондиційної продукції|yes|no|1|9|
|utylizaciya-odyagu-vzuttya.html|public/utylizaciya-odyagu-vzuttya.html|Куди передають одяг та взуття на утилізацію|yes|no|1|9|
|utylizaciya-ofisnih-mebliv-orgtehniki.html|public/utylizaciya-ofisnih-mebliv-orgtehniki.html|Порядок утилізації офісних меблів та оргтехніки|yes|no|1|9|
|utylizaciya-paverbankiv-dbj.html|public/utylizaciya-paverbankiv-dbj.html|Як оформлюється утилізація павербанків та ДБЖ|no|no|0|9|
|utylizaciya-plastyku-ta-polimeriv.html|public/utylizaciya-plastyku-ta-polimeriv.html|Порядок утилізації пластику та полімерів для підприємств|yes|no|1|9|
|utylizaciya-produktiv-harchuvannya-napoyiv.html|public/utylizaciya-produktiv-harchuvannya-napoyiv.html|Порядок утилізації продуктів харчування та напоїв|yes|no|1|9|
|utylizaciya-promyslovogo-obladnannya-mehanizmiv.html|public/utylizaciya-promyslovogo-obladnannya-mehanizmiv.html|Порядок утилізації промислового обладнання та механізмів|no|no|0|9|
|utylizaciya-shyn.html|public/utylizaciya-shyn.html|Як оформлюється утилізація шин|yes|no|1|9|
|utylizaciya-sonyachnih-panelij-vitryakiv.html|public/utylizaciya-sonyachnih-panelij-vitryakiv.html|Як оформлюється утилізація сонячних панелей та лопатей ВЕС|yes|no|1|9|
|utylizaciya-tary-upakovki.html|public/utylizaciya-tary-upakovki.html|Як оформлюється утилізація тари та упаковки|yes|no|1|9|
|utylizaciya-tovariv.html|public/utylizaciya-tovariv.html|Порядок утилізації товарів для підприємств|no|no|0|9|
|utylizaciya-vidpracovanoi-olyvy.html|public/utylizaciya-vidpracovanoi-olyvy.html|Утилізація відпрацьованої оливи для бізнесу|yes|no|1|9|

## D. Proposed Safe Batches
Batch order: `index.html`, then section `*/index.html` pages, then sitemap pages, then remaining affected files; each of the first three batches has at most 5 source files.

### Batch 1
- index.html
- logistyka/index.html
- pererobka/index.html
- sortuvannya/index.html
- akt-pryimannya-peredachi.html

### Batch 2
- akt-utylizaciyi.html
- chy-potribno-pererobyty-chy-utylizuvaty.html
- dokumenty.html
- fotozvit-utylizaciyi.html
- kabelni-vidhody.html

### Batch 3
- kudy-zdaty.html
- likvidaciya-skladskykh-zalyshkiv.html
- logistyka-metalu.html
- logistyka-skla.html
- logistyka.html

### Rest
- pererobka-cegly.html
- pererobka.html
- povernennya-tovariv-z-merezhi.html
- promyslovi-vidhody.html
- sortuvannya.html
- spysannya-produkciyi.html
- utilizaciya-brakovanoi-produkciyi.html
- utilizaciya-dlya-bankiv.html
- utilizaciya-dlya-data-centriv.html
- utilizaciya-dlya-importeriv.html
- utilizaciya-dlya-riteylu.html
- utilizaciya-dlya-skladiv.html
- utilizaciya-dlya-vyrobnyctva.html
- utylizaciya-akumulyatoriv.html
- utylizaciya-elektroniky.html
- utylizaciya-gazovanyh-napoyiv.html
- utylizaciya-importnyh-tovariv.html
- utylizaciya-konfidenciynykh-dokumentiv.html
- utylizaciya-kosmetyky-magazyniv.html
- utylizaciya-kosmetyky.html
- utylizaciya-myasnyh-produktiv.html
- utylizaciya-napoyiv.html
- utylizaciya-obladnannya.html
- utylizaciya-rybnyh-produktiv.html
- utylizaciya-skladskyh-zalyshkiv-kosmetyky.html
- utylizaciya-tovary-pid-mitnim-kontrolem.html
- utylizaciya-zamorozhenyh-produktiv.html
- utylizaciya-zipsovanyh-produktiv.html
- vidhody.html
- yak-oformyty-spysannya-partiyi.html
- yak-peredaty-kosmetyku.html
- yak-peredaty-li-ion-batarei.html
- yak-peredaty-skladski-zalyshky.html
- zbir.html
- kontakty.html
- utylizaciya-budivelnyh-vidhodiv.html
- utylizaciya-kabelyu-ta-drotiv.html
- utylizaciya-li-ion-batarej.html
- utylizaciya-materialiv.html
- utylizaciya-nekondyciynoyi-produkciyi.html
- utylizaciya-odyagu-vzuttya.html
- utylizaciya-ofisnih-mebliv-orgtehniki.html
- utylizaciya-paverbankiv-dbj.html
- utylizaciya-plastyku-ta-polimeriv.html
- utylizaciya-produktiv-harchuvannya-napoyiv.html
- utylizaciya-promyslovogo-obladnannya-mehanizmiv.html
- utylizaciya-shyn.html
- utylizaciya-sonyachnih-panelij-vitryakiv.html
- utylizaciya-tary-upakovki.html
- utylizaciya-tovariv.html
- utylizaciya-vidpracovanoi-olyvy.html
