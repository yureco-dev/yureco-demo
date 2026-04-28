import re
from bs4 import BeautifulSoup
from pathlib import Path

def remove_noise_blocks(soup):
    for sel in ['header','nav','aside','footer','.breadcrumbs',"[class*='breadcrumb']","[id*='breadcrumb']",'.cta',"[class*='cta']","[id*='cta']"]:
        for node in soup.select(sel):
            node.decompose()

def wc(path):
    soup=BeautifulSoup(Path(path).read_text(encoding='utf-8'),'html.parser')
    remove_noise_blocks(soup)
    main=soup.select_one('main') or soup.body or soup
    text=main.get_text(' ',strip=True)
    words=re.findall(r"[A-Za-zА-Яа-яІіЇїЄєҐґ0-9'’`-]+", text)
    print(path, len(words), len(text))

wc('public/yak-oformyty-spysannya-partiyi.html')
wc('public/utylizaciya-myasnyh-produktiv.html')
wc('public/utylizaciya-rybnyh-produktiv.html')
