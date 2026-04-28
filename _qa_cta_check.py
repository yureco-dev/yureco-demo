import re, pathlib

files = {
    'index.html': None,
    'kabelni-vidhody.html': None,
    'kontakty.html': None,
    'logistyka/index.html': None,
    'logistyka-metalu.html': None,
}

stop = frozenset([
    'замовити','зробити','дізнатись','отримати','більше','послугу','послуги',
    'підприємство','підприємств','підприємствам','підприємства','довідник',
    'youreco','організувати','поводження','організація','відкрити',
])

def content_words(t):
    words = re.findall(r'[а-яіїєґa-z]{4,}', t.lower())
    return {w for w in words if w not in stop}

print('=== CHECK 1: CTA anchor vs H1 alignment ===')
for f in files:
    text = pathlib.Path(f).read_text(encoding='utf-8')
    h1_m = re.search(r'<h1[^>]*>([^<]+)', text)
    h1 = h1_m.group(1).strip() if h1_m else 'NOT FOUND'
    cta_pos = text.find('id="service-cta"')
    anc_m = re.search(r'<a[^>]+>([^<]+)</a>', text[cta_pos:cta_pos+1500]) if cta_pos != -1 else None
    anchor = anc_m.group(1) if anc_m else 'NOT FOUND'
    href_m = re.search(r'<a\s+href="([^"]+)"', text[cta_pos:cta_pos+1500]) if cta_pos != -1 else None
    href = href_m.group(1) if href_m else 'NOT FOUND'
    h1_words = content_words(h1)
    anc_words = content_words(anchor)
    overlap = h1_words & anc_words
    status = 'PASS' if overlap else 'FAIL'
    print(f'[{status}] {f}')
    print(f'  H1:     {h1}')
    print(f'  anchor: {anchor}')
    print(f'  href:   {href}')
    print(f'  shared: {overlap}')
