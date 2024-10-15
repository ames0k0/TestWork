#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from pickle import dump
from requests import get
from bs4 import BeautifulSoup as bs


r = get("https://lifehacker.ru/special/etiquette/").text
soup = bs(r, 'lxml')

kek = {}
for c, i in enumerate(soup.find_all('span')):
    try:
        kk = i.text.strip()
        if len(kk) > 20:
            kek[c] = kk
    except Exception as e:
        raise e

with open('etiquette.pickle', 'wb') as f:
    dump(kek, f)
