#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳

from json import dump, load #
from requests import get #--#


"""
TODO:
Необходимо написать PHP or Python скрипт,
    который будет получать цену last USD и сохранять её в файл
"""


def table_print(cur, value):
    print(f"""
    +---------------+----------+
    |   Currency    |   Last   |
    +---------------+----------+
    |{cur:^15}|{value:^10}|
    +--------------------------+
    """)


def get_last(url: str, bit: str="USD", out: str="bitcoin.json"): 
    """
    :param: url -> website with data
    :param: bit -> currency name
    :param: out -> file name for dumping data
    """

    ticket = get(url, "USD").json()
    last_c = ticket[bit]['last']
    table_print(bit, last_c)

    with open(out, 'w') as file:
        dump({bit: last_c}, file)


if __name__ == "__main__":
    get_last('https://blockchain.info/ticker')
