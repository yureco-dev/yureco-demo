## 1. git status --short
```text
 M lead-block-fix-report.md
?? lead-block-evidence.md
```

## 2. git log --oneline -10
```text
d14d091 add lead blocks after h1 on index pages
6dca447 build public after meta schema fixes
d99d4f2 add faq schema evidence reports
992570f add faqpage schema for visible faq blocks
1bace37 add meta schema audit evidence reports
0dc0e9f fix remaining meta schema mismatches
01e903a align json-ld descriptions with meta descriptions
fd601e1 add missing index urls to sitemap
3a5382e add duplicate and build structure audit reports
7e2f919 update fixed sitemap validation report
```

## 3. git diff --name-only
```text
lead-block-fix-report.md
```

## 4. git diff --numstat
```text
2	4	lead-block-fix-report.md
```

## 5. git diff -- "*.html"
```text
```

## 6. git reflog -10
```text
d14d091 HEAD@{0}: commit: add lead blocks after h1 on index pages
6dca447 HEAD@{1}: commit: build public after meta schema fixes
d99d4f2 HEAD@{2}: commit: add faq schema evidence reports
992570f HEAD@{3}: commit: add faqpage schema for visible faq blocks
1bace37 HEAD@{4}: commit: add meta schema audit evidence reports
0dc0e9f HEAD@{5}: commit: fix remaining meta schema mismatches
01e903a HEAD@{6}: commit: align json-ld descriptions with meta descriptions
fd601e1 HEAD@{7}: commit: add missing index urls to sitemap
3a5382e HEAD@{8}: commit: add duplicate and build structure audit reports
7e2f919 HEAD@{9}: commit: update fixed sitemap validation report
```

## 7. git stash list
```text
```

## 8. index.html H1 context
```text
  D:\Сайти\yureko-demo-restore-work\project-final-2\index.html:194:<li><a href="/utylizaciya-tary-upakovki.html">📦 Тара та упаковка</a></li>
  D:\Сайти\yureko-demo-restore-work\project-final-2\index.html:195:<li><a href="/utylizaciya-budivelnyh-vidhodiv.html">🏗️ Будівельні відходи</a></li>
  D:\Сайти\yureko-demo-restore-work\project-final-2\index.html:196:<li><a href="/utylizaciya-plastyku-ta-polimeriv.html">♻️ Пластик та полімери</a></li>
  D:\Сайти\yureko-demo-restore-work\project-final-2\index.html:197:<li><a href="/utylizaciya-kabelyu-ta-drotiv.html">🔌 Кабель та дроти</a></li><li><a href="/utylizaciya-vidpracovanoi-olyvy.html">🛢️ Відпрацьована моторна олива</a></li>
  D:\Сайти\yureko-demo-restore-work\project-final-2\index.html:198:</ul>
  D:\Сайти\yureko-demo-restore-work\project-final-2\index.html:199:</aside>
  D:\Сайти\yureko-demo-restore-work\project-final-2\index.html:200:<!-- MAIN -->
> D:\Сайти\yureko-demo-restore-work\project-final-2\index.html:201:<main class="main"><div class="cards"><div class="card" id="pillars"><h2>Основні розділи довідника</h2><p>Почніть з оглядових сторінок, щоб швидко знайти потрібну тему:</p><ul><li><a href="/utylizaciya-promyslovyh-vidhodiv.html">Утилізація промислових відходів</a></li><li><a href="/utylizaciya-budivelnyh-vidhodiv.html">Утилізація будівельних відходів</a></li><li><a href="/utylizaciya-plastyku-ta-polimeriv.html">Утилізація пластику та полімерів</a></li><li><a href="/utylizaciya-kabelyu-ta-drotiv.html">Утилізація кабелю та дротів</a></li><li><a href="/utylizaciya-shyn.html">Утилізація шин</a></li><li><a href="/utylizaciya-vidpracovanyh-masel.html">Утилізація відпрацьованих олив</a></li><li><a href="/">YOURECO довідник</a></li><li><a href="/utylizaciya-harchovyh-produktiv.html">Утилізація харчових продуктів</a></li><li><a href="/utylizaciya-kosmetyky.html">Утилізація косметики</a></li></ul></div><div class="card" id="latest"><h2>Останні статті</h2><p>Нові матеріали довідника (для швидкого старту та індексації):</p><ul><li><a href="/utylizaciya-vyrobnychyh-vidhodiv.html">Утилізація виробничих відходів</a></li><li><a href="/sortuvannya-promyslovyh-vidhodiv.html">Сортування промислових відходів</a></li><li><a href="/skladuvannya-promyslovyh-vidhodiv.html">Складування промислових відходів</a></li><li><a href="/oblik-promyslovyh-vidhodiv.html">Облік промислових відходів</a></li><li><a href="/dokumenty.html">Документи для утилізації відходів</a></li><li><a href="/utylizaciya-skladskyh-zalyshkiv.html">Утилізація складських залишків</a></li><li><a href="/utylizaciya-nekondyciynoyi-produkciyi.html">Утилізація некондиційної продукції</a></li><li><a href="/utylizaciya-upakovky-na-pidpryyemstvi.html">Утилізація упаковки на підприємстві</a></li><li><a href="/vtorynna-syrovyna-z-vidhodiv.html">Вторинна сировина з відходів</a></li><li><a href="/optymizaciya-vidhodiv-na-vyrobnyctvi.html">Оптимізація відходів на виробництві</a></li><li><a href="/vymogy-do-zberigannya-vidhodiv.html">Вимоги до зберігання відходів</a></li><li><a href="/utylizaciya-partiyi-produktiv.html">Утилізація партії продуктів</a></li></ul></div><div class="card"><nav aria-label="breadcrumb" class="breadcrumbs" id="breadcrumbs"><a href="/">YOURECO довідник</a></nav><h1>Довідник YOURECO про поводження з відходами для підприємств</h1>
  D:\Сайти\yureko-demo-restore-work\project-final-2\index.html:202:<p class="lead">Ця сторінка відкриває довідник YOURECO для підприємств, які мають організувати поводження з відходами без хаосу в документах і потоках. Вона допомагає швидко перейти до потрібного розділу: утилізації, переробки, збору, логістики, сортування або оформлення партій.</p><div class="intro-card">
  D:\Сайти\yureko-demo-restore-work\project-final-2\index.html:203:<p>
  D:\Сайти\yureko-demo-restore-work\project-final-2\index.html:204:<strong>Довідник YOURECO</strong> — довідник для підприємств України, який пояснює практичну логіку поводження з відходами:
  D:\Сайти\yureko-demo-restore-work\project-final-2\index.html:205:                що саме вважається відходами, які ризики виникають при неправильному зберіганні, як готувати відходи до передачі та
  D:\Сайти\yureko-demo-restore-work\project-final-2\index.html:206:                які документи зазвичай потрібні для підтвердження утилізації.
  D:\Сайти\yureko-demo-restore-work\project-final-2\index.html:207:            </p>
  D:\Сайти\yureko-demo-restore-work\project-final-2\index.html:208:<p>
```

