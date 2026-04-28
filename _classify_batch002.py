import re, pathlib, sys

root = pathlib.Path(r"d:\Сайти\yureco-demo")
files = [
    "logistyka-paperu-ta-kartonu.html",
    "logistyka-plastyku.html",
    "logistyka-shyn.html",
    "logistyka-skla.html",
    "nebezpeka-vidpracovanogo-masla.html",
    "pererobka-alyuminiyevogo-kabelyu.html",
    "pererobka-avtomobilnyh-shyn.html",
    "pererobka-cegly.html",
    "pererobka-gumovyh-vyrobiv.html",
    "pererobka-izolyaciyi-kabelyu.html",
]

stop = frozenset([
    'замовити','зробити','дізнатись','отримати','більше','послугу','послуги',
    'підприємство','підприємств','підприємствам','підприємства','довідник',
    'youreco','організувати','поводження','організація','відкрити','дивитись',
    'потрібна','послуга','умовами','вивозом','документальним','супроводом',
    'релевантну','комерційну','сторінку','зв\'язатись','замовити'
])

def content_words(t):
    words = re.findall(r'[а-яіїєґa-z]{4,}', t.lower())
    return {w for w in words if w not in stop}

results = []
for fname in files:
    path = root / fname
    text = path.read_text(encoding='utf-8')
    # Check for CTA block
    cta_pos = -1
    for pattern in [r'id=["\']service-cta["\']', r'id=["\'][^"\']*cta[^"\']*["\']', r'class=["\'][^"\']*cta[^"\']*["\']']:
        m = re.search(pattern, text)
        if m:
            cta_pos = m.start()
            break
    
    if cta_pos == -1:
        results.append((fname, 'no-cta-block'))
        continue
    
    # Get H1
    h1_m = re.search(r'<h1[^>]*>([^<]+)', text)
    h1 = h1_m.group(1).strip() if h1_m else ''
    
    # Get first anchor text in CTA block
    anc_m = re.search(r'<a[^>]+>([^<]+)</a>', text[cta_pos:cta_pos+1500])
    anchor = anc_m.group(1).strip() if anc_m else ''
    
    if not anchor:
        results.append((fname, 'no-cta-block'))
        continue
    
    h1_words = content_words(h1)
    anc_words = content_words(anchor)
    overlap = h1_words & anc_words
    
    if overlap:
        error_type = 'PASS (no mismatch)'
    else:
        error_type = 'topic-mismatch'
    
    results.append((fname, error_type))
    print(f"{fname}: H1=[{h1}] anchor=[{anchor}] overlap={overlap} -> {error_type}")

print("\n=== SUMMARY ===")
for fname, etype in results:
    print(f"{fname} | {etype}")
