import pathlib, re
text = pathlib.Path('logistyka-metalu.html').read_text(encoding='utf-8')
pos = text.find('id="service-cta"')
# Find first <a> text within CTA block
m = re.search(r'(<a[^>]+>)([^<]+)(</a>)', text[pos:pos+1500])
if m:
    old_text = m.group(2)
    print('Found anchor text:', repr(old_text))
    # Replace in the full text
    abs_pos = pos + m.start(2)
    new_anchor = 'Замовити логістику металу'
    new_text = text[:abs_pos] + new_anchor + text[abs_pos + len(old_text):]
    pathlib.Path('logistyka-metalu.html').write_text(new_text, encoding='utf-8')
    print(f'FIXED: logistyka-metalu.html -> {new_anchor}')
else:
    print('No anchor found')
