#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from bs4 import BeautifulSoup as bs #----#
from requests import get #---------------#
from collections import Counter #--------#
from nltk.tokenize import TweetTokenizer #
token = TweetTokenizer()


def get_text(url):
    mktext = ""
    soup = bs(get(url).text, 'lxml')
    lyrics = soup.find('div', 'lyrics')
    for i in lyrics.find_all('a'):
        mktext += f"{i.text}\n"
    return mktext


def tree_most_popular(text):
    """
    [('villains': 2), ('diamonds', 1), ('monsters', 1)]
    """
    texts = [gseven for gseven in token.tokenize(text) if len(gseven) > 7]
    cnt = Counter(texts).most_common(3)
    print(cnt)


if __name__ == "__main__":
    text = get_text("https://genius.com/Halsey-control-lyrics")
    tree_most_popular(text)
