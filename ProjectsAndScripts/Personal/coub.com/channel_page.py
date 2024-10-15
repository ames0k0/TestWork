#!/usr/bin/env python3
# coding:utf-8

from requests import get
from bs4 import BeautifulSoup as bs


def page(p):
    r = get(p).text
    soup = bs(r, 'lxml')
    for _id in soup.find_all("div", "-with-cover hero-cover"):
        return _id['channel-id']


print(page("https://coub.com/dwinofficial"))
