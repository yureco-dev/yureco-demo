# Dead-End / Misleading Internal Links Audit

## Scope
- source HTML checked: 246
- public HTML checked: 246
- build run: no
- files changed: this report only
- excluded: `dist/`, `node_modules/`, `.git/`, service caches; `public/` excluded from source pass
- git branch: `main`
- last commits checked: `dae5146`, `72355ad`, `eb5df6f`

## Summary
- fake href found: 0
- broken local links: 0
- missing assets: 0
- misleading internal links: 90 in source, 90 mirrored in public
- duplicate target groups: 6 in source, 6 mirrored in public
- links to noindex pages: 1196 in source, 1196 mirrored in public
- noindex warnings: 911 in source, 911 mirrored in public
- noindex info: 285 in source, 285 mirrored in public
- critical issues: 0
- warnings: 1007 in source, 1007 mirrored in public

## Fake Hrefs
No `href=""`, `href="#"`, `href="#!"`, `javascript:void(0)`, or `href="javascript:*"` instances found in source or public HTML.

## Broken Local Links
No broken local `.html` links found in source or public HTML. Same-page fragment links were checked against existing `id` values.

## Missing Assets
No missing local `img/src`, `script/src`, `iframe/src`, `source/src`, or stylesheet/icon `link/href` assets found in source or public HTML. No links to missing `public/source` deployment-only paths were detected.

## Misleading Internal Links
The main pattern is a concrete anchor pointing to a broad hub even though a more specific HTML page exists. Public has the same mirrored findings.

| source page | anchor text | current href | suggested href | reason | target exists | severity |
|---|---|---|---|---|---|---|
| `akt-pryimannya-peredachi.html` | Документи для передачі та списання | `/dokumenty.html` | `/utylizaciya-dokumentiv.html` | document-specific anchor points to general documents hub | yes | warning |
| `akt-utylizaciyi.html` | Повний комплект документів | `/dokumenty.html` | `/utylizaciya-dokumentiv.html` | document-specific anchor points to general documents hub | yes | warning |
| `articles/index.html` | Документи для передачі та списання | `/dokumenty.html` | `/utylizaciya-dokumentiv.html` | document-specific anchor points to general documents hub | yes | warning |
| `chy-potribno-pererobyty-chy-utylizuvaty.html` | документи утилізації | `/dokumenty.html` | `/utylizaciya-dokumentiv.html` | document-specific anchor points to general documents hub | yes | warning |
| `dokumenty.html` | Документи для передачі та списання | `/dokumenty.html` | `/utylizaciya-dokumentiv.html` | self/general hub link where concrete document page exists | yes | warning |
| `index.html` | Документи для утилізації відходів | `/dokumenty.html` | `/utylizaciya-dokumentiv.html` | document-specific anchor points to general documents hub | yes | warning |
| `kudy-zdaty-gipsokartonu.html` | Куди передають гіпсокартон на утилізацію | `/utylizaciya.html` | `/utylizaciya-paperu-ta-kartonu.html` | specific material anchor points to utilization hub | yes | warning |
| `kudy-zdaty-ofisnih-mebliv-orgtehniki.html` | Порядок утилізації офісних меблів та оргтехніки | `/utylizaciya.html` | `/utylizaciya-ofisnih-mebliv-orgtehniki.html` | specific service anchor points to utilization hub | yes | warning |
| `kudy-zdaty-paperu-ta-kartonu.html` | Як оформлюється утилізація паперу та картону | `/utylizaciya.html` | `/utylizaciya-paperu-ta-kartonu.html` | specific material anchor points to utilization hub | yes | warning |
| `kudy-zdaty-promyslovogo-obladnannya-mehanizmiv.html` | Порядок утилізації промислового обладнання та механізмів | `/utylizaciya.html` | `/utylizaciya-promyslovogo-obladnannya-mehanizmiv.html` | specific equipment anchor points to utilization hub | yes | warning |
| `kudy-zdaty-promyslovyh-vidhodiv.html` | Порядок утилізації промислових відходів для підприємств | `/utylizaciya.html` | `/utylizaciya-promyslovyh-vidhodiv.html` | specific waste anchor points to utilization hub | yes | warning |
| `kudy-zdaty-shin.html` | Як оформлюється утилізація шин | `/utylizaciya.html` | `/utylizaciya-shyn.html` | tire-specific anchor points to utilization hub | yes | warning |
| `kudy-zdaty-shyn-pidpryyemstvamy.html` | Документи для утилізації шин підприємствами | `/utylizaciya.html` | `/utylizaciya-shyn-pidpryyemstvamy.html` | tire-specific anchor points to utilization hub | yes | warning |
| `kudy-zdaty-tary-upakovki.html` | Як оформлюється утилізація тари та упаковки | `/utylizaciya.html` | `/utylizaciya-tary-upakovki.html` | packaging-specific anchor points to utilization hub | yes | warning |
| `kudy-zdaty-vidpracovane-maslo.html` | Відпрацьована моторна олива | `/utylizaciya.html` | `/utylizaciya-vidpracovanyh-masel.html` | oil-specific anchor points to utilization hub | yes | warning |
| `kudy-zdaty-vidpracovanoi-olyvy.html` | Відпрацьована моторна олива | `/utylizaciya.html` | `/utylizaciya-vidpracovanyh-masel.html` | oil-specific anchor points to utilization hub | yes | warning |
| `shyny.html` | Як оформлюється утилізація шин | `/utylizaciya.html` | `/utylizaciya-shyn.html` | tire-specific anchor points to utilization hub | yes | warning |

Additional repeated warning pattern: many pages use anchors like `документи утилізації`, `Документи передачі відходів`, or `Документи для передачі та списання` with `/dokumenty.html`. The concrete target `/utylizaciya-dokumentiv.html` exists in both source and public.

## Duplicate Target Groups

| source page | shared href | anchor texts | assessment |
|---|---|---|---|
| `kudy-zdaty.html` | `/utylizaciya-shyn.html` | `куди здати вантажні шини`; `куди здати шини`; `куди здати шини: варіанти для бізнесу`; `⭕ шини` | review: several tire-specific anchors share one valid tire target; not broken, but check whether more specific pages should be used |
| `kudy-zdaty.html` | `/utylizaciya-vidpracovanoi-olyvy.html` | `куди здати відпрацьовану моторну оливу`; `куди здати відпрацьовану оливу`; `🛢️ відпрацьована моторна олива` | review: related anchors share one oil target |
| `utylizaciya-importnyh-tovariv.html` | `/utylizaciya-tovary-pid-mitnim-kontrolem.html` | `утилізацію товарів під митним контролем`; `утилізація товарів під митним контролем`; `📦 товари під митним контролем` | acceptable/review: same topic phrased differently |
| `utylizaciya-napoyiv.html` | `/utylizaciya-tary-upakovki.html` | `утилізація пластикової тари`; `утилізація скляної тари`; `утилізація тари та упаковки`; `📦 тара та упаковка` | warning: plastic and glass packaging anchors may deserve separate targets if such pages exist |
| `utylizaciya/index.html` | `/utylizaciya-konfidenciynykh-dokumentiv.html` | `документи для утилізації конфіденційних документів`; `як оформлюється утилізація конфіденційних документів`; `📄 конфіденційні документи` | acceptable/review: same concrete topic |
| `vidhody.html` | `/promyslovi-vidhody.html` | `промислові відходи`; `що таке промислові відходи`; `📋 промислові відходи` | acceptable/review: same concrete topic, but target is noindex |

## Links To Noindex Pages
Large repeated pattern: navigational/category blocks point to content-looking pages that carry `noindex, follow`. This is not a 404, but it is a dead-end risk for users and SEO because the anchor looks like a normal content page.

| source page | anchor text | href | target robots | assessment |
|---|---|---|---|---|
| `akt-pryimannya-peredachi.html` | 🧰 Обладнання | `/utylizaciya-obladnannya.html` | `noindex, follow` | warning: content-looking target is noindex |
| `akt-pryimannya-peredachi.html` | 📋 Промислові відходи | `/promyslovi-vidhody.html` | `noindex, follow` | warning: content-looking target is noindex |
| `akt-pryimannya-peredachi.html` | 🏭 Промислове обладнання та механізми | `/utylizaciya-promyslovogo-obladnannya-mehanizmiv.html` | `noindex, follow` | warning: content-looking target is noindex |
| `akt-pryimannya-peredachi.html` | 📄 Конфіденційні документи | `/utylizaciya-konfidenciynykh-dokumentiv.html` | `noindex, follow` | warning: content-looking target is noindex |
| `akt-pryimannya-peredachi.html` | 🏗️ Будівельні відходи | `/utylizaciya-budivelnyh-vidhodiv.html` | `noindex, follow` | warning: content-looking target is noindex |
| `chy-potribno-pererobyty-chy-utylizuvaty.html` | що таке переробка відходів | `/shcho-take-pererobka-vidhodiv.html` | `noindex, follow` | warning: article-like target is noindex |
| `chy-potribno-pererobyty-chy-utylizuvaty.html` | як відбувається утилізація продукції | `/yak-vidbuvayetsya-utylizaciya-produkciyi.html` | `noindex, follow` | warning: article-like target is noindex |
| `zbir.html` | Збір кабелю | `/zbir-kabelyu.html` | `noindex, follow` | warning: content-looking target is noindex |
| `zbir.html` | Збір картону на підприємстві | `/zbir-kartonu-na-pidpryyemstvi.html` | `noindex, follow` | warning: content-looking target is noindex |
| `zbir.html` | Збір відпрацьованої оливи | `/zbir-vidpracovanoyi-olyvy.html` | `noindex, follow` | warning: content-looking target is noindex |

Info-only pattern: broad service/category labels such as `Товари`, `Матеріали`, and `Контакти` also point to `noindex, follow` pages. These are less misleading than concrete article/service anchors, but should still be intentional.

## Special Pages Checked

| page | source exists | public exists | source robots | public robots | assessment |
|---|---:|---:|---|---|---|
| `utylizaciya-obladnannya.html` | yes | yes | `noindex, follow` | `noindex, follow` | warning: many normal anchors point here |
| `utylizaciya-vidpracovanyh-masel.html` | yes | yes | `noindex, follow` | `noindex, follow` | warning: recommended as specific oil target, but currently noindex |

## Priority Fix List

| page | anchor text | current href | recommended href |
|---|---|---|---|
| `kudy-zdaty-vidpracovane-maslo.html` | Відпрацьована моторна олива | `/utylizaciya.html` | `/utylizaciya-vidpracovanyh-masel.html` after deciding whether this target should remain `noindex` |
| `kudy-zdaty-vidpracovanoi-olyvy.html` | Відпрацьована моторна олива | `/utylizaciya.html` | `/utylizaciya-vidpracovanyh-masel.html` after deciding whether this target should remain `noindex` |
| `kudy-zdaty-promyslovogo-obladnannya-mehanizmiv.html` | Порядок утилізації промислового обладнання та механізмів | `/utylizaciya.html` | `/utylizaciya-promyslovogo-obladnannya-mehanizmiv.html` after deciding whether this target should remain `noindex` |
| `kudy-zdaty-ofisnih-mebliv-orgtehniki.html` | Порядок утилізації офісних меблів та оргтехніки | `/utylizaciya.html` | `/utylizaciya-ofisnih-mebliv-orgtehniki.html` |
| `kudy-zdaty-tary-upakovki.html` | Як оформлюється утилізація тари та упаковки | `/utylizaciya.html` | `/utylizaciya-tary-upakovki.html` |
| `kudy-zdaty-shin.html` | Як оформлюється утилізація шин | `/utylizaciya.html` | `/utylizaciya-shyn.html` |
| `shyny.html` | Як оформлюється утилізація шин | `/utylizaciya.html` | `/utylizaciya-shyn.html` |
| `index.html` | Документи для утилізації відходів | `/dokumenty.html` | `/utylizaciya-dokumentiv.html` |
| `akt-pryimannya-peredachi.html` | Документи для передачі та списання | `/dokumenty.html` | `/utylizaciya-dokumentiv.html` |
| `akt-utylizaciyi.html` | Повний комплект документів | `/dokumenty.html` | `/utylizaciya-dokumentiv.html` |
| `zbir.html` | Збір кабелю | `/zbir-kabelyu.html` | keep only if target intentionally remains `noindex`; otherwise remove `noindex` or link to an indexable equivalent |
| `zbir.html` | Збір картону на підприємстві | `/zbir-kartonu-na-pidpryyemstvi.html` | keep only if target intentionally remains `noindex`; otherwise remove `noindex` or link to an indexable equivalent |

## Guardrails
- HTML changed: no
- CSS changed: no
- JS changed: no
- sitemap/robots changed: no
- public changed: no
- build run: no
- commit done: no
- push done: no
- Cyrillic/UTF-8 issues: none observed while reading HTML with UTF-8/UTF-8 BOM fallback
