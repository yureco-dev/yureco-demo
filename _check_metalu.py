import pathlib, re
text = pathlib.Path('logistyka-metalu.html').read_text(encoding='utf-8')
pos = text.find('id="service-cta"')
segment = text[pos:pos+600]
m = re.search(r'<a[^>]+>([^<]+)</a>', segment)
if m:
    print(repr(m.group(1)))
else:
    print("No anchor found")
    print(repr(segment[:300]))
