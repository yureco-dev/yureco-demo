import os

files = [
    'utylizaciya-ovochiv.html',
    'utylizaciya-paperu-ta-kartonu.html',
    'utylizaciya-parfumeriyi.html',
    'utylizaciya-paverbankiv-dbj.html',
    'utylizaciya-plastyku-ta-polimeriv.html',
    'utylizaciya-produktiv-harchuvannya-napoyiv.html',
    'utylizaciya-promyslovogo-obladnannya-mehanizmiv.html',
    'utylizaciya-promyslovyh-vidhodiv.html',
    'utylizaciya-prostrochenoyi-kosmetyky.html',
    'utylizaciya-pyva.html',
]

for f in files:
    url = 'https://guide.youreco.com.ua/' + f
    with open(f, encoding='utf-8') as fh:
        content = fh.read()
    # Revert incorrect mainEntityOfPage fix (added in first attempt)
    old1 = '"mainEntityOfPage":{"@type":"WebPage","@id":"' + url + '","url":"' + url + '"}'
    new1 = '"mainEntityOfPage":{"@type":"WebPage","@id":"' + url + '"}'
    content = content.replace(old1, new1)
    # Add separate WebPage JSON-LD block before </head> (matches batch_001..007 pattern)
    wp_block = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","url":"' + url + '"}</script>'
    if wp_block not in content:
        content = content.replace('</head>', wp_block + '</head>', 1)
    with open(f, 'w', encoding='utf-8', newline='') as fh:
        fh.write(content)
    print('DONE:', f)
