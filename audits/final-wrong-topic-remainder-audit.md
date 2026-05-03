# Final Wrong-Topic Remainder Audit

- статус: НЕ ДОБРЕ
- build: PUBLIC_BUILD_OK files=179 html=172
- total real wrong-topic links: 14
- total generic hub placeholder links у main content: 510
- clean confirmed для перелічених файлів: так
- недозволені зміни під час аудиту: ні
- Кирилиця: не зіпсована

## Clean Confirmed
- public/pererobka.html: так
- public/kudy-zdaty.html: так
- public/sortuvannya.html: так
- public/utylizaciya-akumulyatoriv.html: так
- public/yak-peredaty-li-ion-batarei.html: так
- public/utylizaciya-elektroniky.html: так
- public/vidhody.html: так
- public/utylizaciya-napoyiv.html: так
- public/utylizaciya-obladnannya.html: так
- public/kontakty.html: так
- public/utylizaciya-konfidenciynykh-dokumentiv.html: так

## Top Source Pages
- public/utilizaciya-dlya-bankiv.html: 4
- public/chy-potribno-pererobyty-chy-utylizuvaty.html: 3
- public/yak-oformyty-spysannya-partiyi.html: 3
- public/utilizaciya-dlya-data-centriv.html: 2
- public/utylizaciya-importnyh-tovariv.html: 2

## Remaining Real Wrong-Topic Links
| source file | block/context | anchor text | current href | proposed href | reason | recommendation |
|---|---|---|---|---|---|---|
| public/chy-potribno-pererobyty-chy-utylizuvaty.html | Чи потрібно переробити чи утилізувати продукцію | що таке переробка відходів | /utylizaciya.html | /shcho-take-pererobka-vidhodiv.html | anchor about pererobka points to utylizaciya hub | REPLACE_HREF |
| public/chy-potribno-pererobyty-chy-utylizuvaty.html | Чи потрібно переробити чи утилізувати продукцію | як відбувається переробка відходів | /pererobka.html | NEEDS_DECISION | specific anchor points to generic hub placeholder; no exact safe target selected | NEEDS_DECISION |
| public/chy-potribno-pererobyty-chy-utylizuvaty.html | Чи потрібно переробити чи утилізувати продукцію | як відбувається утилізація продукції | /utylizaciya.html | NEEDS_DECISION | specific anchor points to generic hub placeholder; no exact safe target selected | NEEDS_DECISION |
| public/utilizaciya-dlya-bankiv.html | Утилізація продукції та обладнання для банків | утилізація офісної техніки | /utylizaciya.html | /utylizaciya-ofisnih-mebliv-orgtehniki.html | specific anchor points to generic hub placeholder | REPLACE_HREF |
| public/utilizaciya-dlya-bankiv.html | Утилізація продукції та обладнання для банків | утилізація офісної техніки | /utylizaciya.html | /utylizaciya-ofisnih-mebliv-orgtehniki.html | specific anchor points to generic hub placeholder | REPLACE_HREF |
| public/utilizaciya-dlya-bankiv.html | Утилізація продукції та обладнання для банків | що таке знищення продукції | /utylizaciya.html | /shcho-take-znyshchennya-produkciyi.html | specific anchor points to generic hub placeholder | REPLACE_HREF |
| public/utilizaciya-dlya-bankiv.html | Утилізація продукції та обладнання для банків | що таке знищення продукції | /utylizaciya.html | /shcho-take-znyshchennya-produkciyi.html | specific anchor points to generic hub placeholder | REPLACE_HREF |
| public/utilizaciya-dlya-data-centriv.html | Утилізація для дата-центрів | утилізація Li-ion батарей | /utylizaciya.html | /utylizaciya-li-ion-batarej.html | specific anchor points to generic hub placeholder | REPLACE_HREF |
| public/utilizaciya-dlya-data-centriv.html | Утилізація для дата-центрів | утилізація Li-ion батарей | /utylizaciya.html | /utylizaciya-li-ion-batarej.html | specific anchor points to generic hub placeholder | REPLACE_HREF |
| public/utylizaciya-importnyh-tovariv.html | Утилізація імпортних товарів | утилізація товарів | /utylizaciya.html | /utylizaciya-tovariv.html | specific anchor points to generic hub placeholder | REPLACE_HREF |
| public/utylizaciya-importnyh-tovariv.html | Утилізація імпортних товарів | утилізація товарів | /utylizaciya.html | /utylizaciya-tovariv.html | specific anchor points to generic hub placeholder | REPLACE_HREF |
| public/yak-oformyty-spysannya-partiyi.html | Як оформити списання партії продукції | внутрішній акт списання | /utylizaciya.html | /vnutrishniy-akt-spysannya.html | specific anchor points to generic hub placeholder | REPLACE_HREF |
| public/yak-oformyty-spysannya-partiyi.html | Як оформити списання партії продукції | внутрішній акт списання | /utylizaciya.html | /vnutrishniy-akt-spysannya.html | specific anchor points to generic hub placeholder | REPLACE_HREF |
| public/yak-oformyty-spysannya-partiyi.html | Як оформити списання партії продукції | внутрішній акт списання | /utylizaciya.html | /vnutrishniy-akt-spysannya.html | specific anchor points to generic hub placeholder | REPLACE_HREF |

## NEEDS_DECISION Items
| source file | block/context | anchor text | current href | reason |
|---|---|---|---|---|
| public/chy-potribno-pererobyty-chy-utylizuvaty.html | Чи потрібно переробити чи утилізувати продукцію | як відбувається переробка відходів | /pererobka.html | specific anchor points to generic hub placeholder; no exact safe target selected |
| public/chy-potribno-pererobyty-chy-utylizuvaty.html | Чи потрібно переробити чи утилізувати продукцію | як відбувається утилізація продукції | /utylizaciya.html | specific anchor points to generic hub placeholder; no exact safe target selected |

## Recommended Next Batch
Batch: chy-potribno-pererobyty-chy-utylizuvaty.html, utilizaciya-dlya-bankiv.html, utilizaciya-dlya-data-centriv.html, utylizaciya-importnyh-tovariv.html, yak-oformyty-spysannya-partiyi.html.
