#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from os import mkdir, chdir #--------#
from bs4 import BeautifulSoup as bs ##
from os.path import exists #---------#
from requests import Session #-------#
from collections import deque #------#
from fake_useragent import UserAgent #


def get_proxy(url: str) -> dict:
    """ Parse proxy server and get ip and port
    """

    def lor(left, obj, equal, right):
        return left if obj == equal else right

    ua = UserAgent()
    typ = lor("yes", len(url.split(':')[0]), 5, "no")
    base = 'https://www.us-proxy.org'

    session = Session()
    session.headers.update({'User-Agent': ua.firefox})
    r = session.get(base).text

    soup = bs(r, 'lxml').find('tbody')
    tds = deque([i for i in soup.find_all('td')])

    def typo():
        while True:
            check = [tds.popleft() for _ in range(8)]
            for ch in check:
                if 'hx' in str(ch):
                    if ch.text == typ:
                        return f"{check[0].text}:{check[1].text}"

    proxy = {lor(f"http{typ[-1]}", len(typ), 3, "http"): typo()}
    del tds

    return proxy


def mkd(name):
    if not exists(name):
        mkdir(name)
    chdir(name)
