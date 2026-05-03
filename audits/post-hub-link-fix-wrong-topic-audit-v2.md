# Post hub link fix wrong-topic audit v2

- build command: `python scripts/build_public.py`
- total html files: 172
- total real wrong-topic links: 63
- total generic hub placeholder links in main content: 556
- pererobka.html clean: так
- kudy-zdaty.html clean: так
- disallowed changes during audit: no
- Cyrillic: not corrupted

## Generic hub placeholder counts by href
- /utylizaciya.html: 244
- /logistyka.html: 138
- /sortuvannya.html: 76
- /pererobka.html: 60
- /zbir.html: 38

## Top source pages with remaining real wrong-topic links
- public/utylizaciya-akumulyatoriv.html: 6
- public/utylizaciya-elektroniky.html: 6
- public/utylizaciya-napoyiv.html: 6
- public/vidhody.html: 6
- public/utylizaciya-obladnannya.html: 4
- public/sortuvannya.html: 3
- public/yak-peredaty-li-ion-batarei.html: 3
- public/chy-potribno-pererobyty-chy-utylizuvaty.html: 2
- public/kontakty.html: 2
- public/utilizaciya-dlya-bankiv.html: 2
- public/utilizaciya-dlya-data-centriv.html: 2
- public/utylizaciya-importnyh-tovariv.html: 2
- public/akt-pryimannya-peredachi.html: 1
- public/dokumenty.html: 1
- public/kabelni-vidhody.html: 1
- public/logistyka/index.html: 1
- public/logistyka-metalu.html: 1
- public/logistyka-skla.html: 1
- public/pererobka-cegly.html: 1
- public/promyslovi-vidhody.html: 1
- public/sortuvannya/index.html: 1
- public/utylizaciya-gazovanyh-napoyiv.html: 1
- public/utylizaciya-konfidenciynykh-dokumentiv.html: 1
- public/utylizaciya-kosmetyky-magazyniv.html: 1
- public/utylizaciya-myasnyh-produktiv.html: 1
- public/utylizaciya-rybnyh-produktiv.html: 1
- public/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html: 1
- public/utylizaciya-tovary-pid-mitnim-kontrolem.html: 1
- public/utylizaciya-zamorozhenyh-produktiv.html: 1
- public/utylizaciya.html: 1
- public/zbir.html: 1

## Remaining real wrong-topic links
| source file | block/context | anchor text | current href | proposed href | reason | recommendation |
|---|---|---|---|---|---|---|
|public/akt-pryimannya-peredachi.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/chy-potribno-pererobyty-chy-utylizuvaty.html|Коли застосовується переробка|як відбувається переробка відходів|/pererobka.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/chy-potribno-pererobyty-chy-utylizuvaty.html|Коли застосовується утилізація|як відбувається утилізація продукції|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/dokumenty.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/kabelni-vidhody.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/kontakty.html|Читайте також|Огляд: Утилізація промислових відходів|/utylizaciya.html|/utylizaciya-promyslovyh-vidhodiv.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/kontakty.html|Читайте також|Утилізація шин|/utylizaciya.html|/utylizaciya-vantazhnyh-shyn.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/logistyka/index.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/logistyka-metalu.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/logistyka-skla.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/pererobka-cegly.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/promyslovi-vidhody.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/sortuvannya/index.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/sortuvannya.html|Сторінки розділу|Сортування будівельного відходи|/utylizaciya.html|/sortuvannya-budivelnyh-vidhodiv.html|anchor about sorting points to non-sorting target|REPLACE_HREF|
|public/sortuvannya.html|Сторінки розділу|Сортування пластику|/utylizaciya.html|/sortuvannya-plastyku.html|anchor about sorting points to non-sorting target|REPLACE_HREF|
|public/sortuvannya.html|Сторінки розділу|Сортування промислових відходів|/utylizaciya.html|/sortuvannya-promyslovyh-vidhodiv.html|anchor about sorting points to non-sorting target|REPLACE_HREF|
|public/utilizaciya-dlya-bankiv.html|Типові сценарії утилізації для банків|утилізація офісної техніки|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utilizaciya-dlya-bankiv.html|Пов’язані маршрути передачі продукції|утилізація офісної техніки|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utilizaciya-dlya-data-centriv.html|Типові сценарії утилізації для галузі|утилізація Li-ion батарей|/utylizaciya.html|/utylizaciya-li-ion-batarej.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utilizaciya-dlya-data-centriv.html|Пов’язані маршрути передачі продукції|утилізація Li-ion батарей|/utylizaciya.html|/utylizaciya-li-ion-batarej.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-akumulyatoriv.html|Коротка відповідь|утилізація Li-ion батарей|/utylizaciya.html|/utylizaciya-li-ion-batarej.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-akumulyatoriv.html|Коротка відповідь|утилізація павербанків та ДБЖ|/utylizaciya.html|/utylizaciya-paverbankiv-dbj.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-akumulyatoriv.html|Пов'язані сторінки|утилізація Li-ion батарей|/utylizaciya.html|/utylizaciya-li-ion-batarej.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-akumulyatoriv.html|Пов'язані сторінки|утилізація павербанків та ДБЖ|/utylizaciya.html|/utylizaciya-paverbankiv-dbj.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-akumulyatoriv.html|Пов'язані сторінки|утилізація Li-ion батарей|/utylizaciya.html|/utylizaciya-li-ion-batarej.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-akumulyatoriv.html|Пов'язані сторінки|утилізація павербанків та ДБЖ|/utylizaciya.html|/utylizaciya-paverbankiv-dbj.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-elektroniky.html|Коротка відповідь|утилізація офісної техніки|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-elektroniky.html|Коротка відповідь|утилізація Li-ion батарей|/utylizaciya.html|/utylizaciya-li-ion-batarej.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-elektroniky.html|Пов'язані сторінки|утилізація офісної техніки|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-elektroniky.html|Пов'язані сторінки|утилізація Li-ion батарей|/utylizaciya.html|/utylizaciya-li-ion-batarej.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-elektroniky.html|Пов'язані сторінки|утилізація офісної техніки|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-elektroniky.html|Пов'язані сторінки|утилізація Li-ion батарей|/utylizaciya.html|/utylizaciya-li-ion-batarej.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-gazovanyh-napoyiv.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-importnyh-tovariv.html|Пов'язані сторінки|утилізація товарів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-importnyh-tovariv.html|Пов'язані сторінки|утилізація товарів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-konfidenciynykh-dokumentiv.html|Пов’язані матеріали|Знищення косметики|/utylizaciya.html|/utylizaciya-upakovky-vid-kosmetyky.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-kosmetyky-magazyniv.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-myasnyh-produktiv.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-napoyiv.html|Контекстні переходи за темою напоїв|утилізація тари та упаковки|/utylizaciya.html|/utylizaciya-tary-upakovki.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-napoyiv.html|Контекстні переходи за темою напоїв|утилізація скла|/utylizaciya.html|/utylizaciya-skla.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-napoyiv.html|Контекстні переходи за темою напоїв|утилізація пластику|/utylizaciya.html|/utylizaciya-plastyku-ta-polimeriv.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-napoyiv.html|Дивіться також|Утилізація тари та упаковки|/utylizaciya.html|/utylizaciya-tary-upakovki.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-napoyiv.html|Дивіться також|Утилізація скляної тари|/utylizaciya.html|/utylizaciya-tary-upakovki.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-napoyiv.html|Дивіться також|Утилізація пластикової тари|/utylizaciya.html|/utylizaciya-tary-upakovki.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-obladnannya.html|Дивіться також|утилізація промислового обладнання|/utylizaciya.html|/utylizaciya-promyslovogo-obladnannya-mehanizmiv.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-obladnannya.html|Дивіться також|утилізація офісної техніки та меблів|/utylizaciya.html|/utylizaciya-ofisnih-mebliv-orgtehniki.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-obladnannya.html|Дивіться також|утилізація промислового обладнання|/utylizaciya.html|/utylizaciya-promyslovogo-obladnannya-mehanizmiv.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-obladnannya.html|Дивіться також|утилізація офісної техніки та меблів|/utylizaciya.html|/utylizaciya-ofisnih-mebliv-orgtehniki.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-rybnyh-produktiv.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-skladskyh-zalyshkiv-kosmetyky.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-tovary-pid-mitnim-kontrolem.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya-zamorozhenyh-produktiv.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/utylizaciya.html|Що потрібно перевірити перед передачею партії на утилізацію|Типові сценарії передачі продукції на утилізацію|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/vidhody.html|Сторінки розділу|Промислові відходи на підприємстві: облік і правила|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/vidhody.html|Сторінки розділу|Відходи демонтажу: сортування та утилізація|/utylizaciya.html|NEEDS_DECISION|anchor about sorting points to non-sorting target|REPLACE_HREF|
|public/vidhody.html|Сторінки розділу|Відходи гуми: що відноситься і як утилізують|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/vidhody.html|Сторінки розділу|Відходи полімерів|/utylizaciya.html|/utylizaciya-plastyku-ta-polimeriv.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/vidhody.html|Типові сценарії передачі продукції на утилізацію|Типові сценарії передачі продукції на утилізацію|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/vidhody.html|Що означають основні терміни поводження з відходами|Що таке промислові відходи|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/yak-peredaty-li-ion-batarei.html|Які Li-ion батареї підлягають передачі|утилізація Li-ion батарей|/utylizaciya.html|/utylizaciya-li-ion-batarej.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/yak-peredaty-li-ion-batarei.html|Типові сценарії передачі|утилізація Li-ion батарей|/utylizaciya.html|/utylizaciya-li-ion-batarej.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/yak-peredaty-li-ion-batarei.html|Як відбувається процес утилізації|утилізація Li-ion батарей|/utylizaciya.html|/utylizaciya-li-ion-batarej.html|specific anchor points to generic hub placeholder|REPLACE_HREF|
|public/zbir.html|Як визначають сценарій передачі матеріалів перед збором|Типові сценарії передачі продукції на утилізацію|/utylizaciya.html|NEEDS_DECISION|specific anchor points to generic hub placeholder|REPLACE_HREF|

## Recommended next batch
| source file | block/context | anchor text | current href | proposed href | recommendation |
|---|---|---|---|---|---|
|public/akt-pryimannya-peredachi.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|REPLACE_HREF|
|public/chy-potribno-pererobyty-chy-utylizuvaty.html|Коли застосовується переробка|як відбувається переробка відходів|/pererobka.html|NEEDS_DECISION|REPLACE_HREF|
|public/chy-potribno-pererobyty-chy-utylizuvaty.html|Коли застосовується утилізація|як відбувається утилізація продукції|/utylizaciya.html|NEEDS_DECISION|REPLACE_HREF|
|public/dokumenty.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|REPLACE_HREF|
|public/kabelni-vidhody.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|REPLACE_HREF|
|public/kontakty.html|Читайте також|Огляд: Утилізація промислових відходів|/utylizaciya.html|/utylizaciya-promyslovyh-vidhodiv.html|REPLACE_HREF|
|public/kontakty.html|Читайте також|Утилізація шин|/utylizaciya.html|/utylizaciya-vantazhnyh-shyn.html|REPLACE_HREF|
|public/logistyka/index.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|REPLACE_HREF|
|public/logistyka-metalu.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|REPLACE_HREF|
|public/logistyka-skla.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|REPLACE_HREF|
|public/pererobka-cegly.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|REPLACE_HREF|
|public/promyslovi-vidhody.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|REPLACE_HREF|
|public/sortuvannya/index.html|Дивіться також|Хаб утилізації відходів|/utylizaciya.html|NEEDS_DECISION|REPLACE_HREF|
|public/sortuvannya.html|Сторінки розділу|Сортування будівельного відходи|/utylizaciya.html|/sortuvannya-budivelnyh-vidhodiv.html|REPLACE_HREF|
|public/sortuvannya.html|Сторінки розділу|Сортування пластику|/utylizaciya.html|/sortuvannya-plastyku.html|REPLACE_HREF|
|public/sortuvannya.html|Сторінки розділу|Сортування промислових відходів|/utylizaciya.html|/sortuvannya-promyslovyh-vidhodiv.html|REPLACE_HREF|
|public/utilizaciya-dlya-bankiv.html|Типові сценарії утилізації для банків|утилізація офісної техніки|/utylizaciya.html|NEEDS_DECISION|REPLACE_HREF|
|public/utilizaciya-dlya-bankiv.html|Пов’язані маршрути передачі продукції|утилізація офісної техніки|/utylizaciya.html|NEEDS_DECISION|REPLACE_HREF|
|public/utilizaciya-dlya-data-centriv.html|Типові сценарії утилізації для галузі|утилізація Li-ion батарей|/utylizaciya.html|/utylizaciya-li-ion-batarej.html|REPLACE_HREF|
|public/utilizaciya-dlya-data-centriv.html|Пов’язані маршрути передачі продукції|утилізація Li-ion батарей|/utylizaciya.html|/utylizaciya-li-ion-batarej.html|REPLACE_HREF|

## Sidebar wrong-topic links observed but excluded from main total
- count: 278
