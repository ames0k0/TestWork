#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from bs4 import BeautifulSoup as bs #----#
from requests import get #---------------#
from collections import Counter #--------#
from nltk.tokenize import TweetTokenizer #


def tree_most_popular(url: str):
    """
    :param: url -> website with text data

    :output:
        [('villains': 2), ('diamonds', 1), ('monsters', 1)]
    """

    text = ""
    for each in bs(get(url).text, 'lxml').find('div', 'lyrics').find_all('a'):
        text += f"{each.text}\n"

    token = TweetTokenizer()
    print(
        Counter(
            [gseven for gseven in token.tokenize(text) if len(gseven) > 7]
        ).most_common(3)
    )


if __name__ == "__main__":
    tree_most_popular("https://genius.com/Halsey-control-lyrics")
