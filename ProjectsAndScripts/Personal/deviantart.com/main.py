#!/usr/bin/python3
# coding=utf-8

from requests import get
from bs4 import BeautifulSoup as bs


def show():
    r = get('https://yamio.deviantart.com/gallery/').text
    soup = bs(r, 'lxml')
    for i in soup.find_all('img'):
        da = i.get('src')
        if "https://yamio.deviantart.com/art/Halloween-Annies-2017-Batch-2-712550582" in da:
            print(da)


if __name__=='__main__':
    show()
