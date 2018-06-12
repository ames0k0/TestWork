#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳

# to save data
from json import dump, load #
# get data from web app
from requests import get #--#


"""
Тока Python3, Сорянте, Совсем Ноль в PHP
Спасибо за тестовое задание!

Решил не пойти на Веб: but can write something in Django and Flask to myself...


TODO:: Необходимо написать PHP и Python скрипт, \
        который будет получать цену last USD и сохранять её в файл
"""


def get_last(ticket, bitc): 
    """
    ticket:: dict odj
    bitc  :: key, to get value from 'ticket'
    """
    print('valyuta: {0} >> last: {1}'.format(bitc, ticket.get(bitc)['last']))
    # Если все ОК, то сохраним в файл
    # Если ticket в json формате то сохраню это в .json format
    with open('bitcoin.json', 'w') as file:
        val = {bitc: ticket[bitc]['last']}
        dump(val, file)


if __name__ == "__main__":
    # Получит валюту в .json format чтобы "last" обращаться через Клю "USD"
    get_ticket = get('https://blockchain.info/ticker').json()
    # Вызвать (Исполнить) Функцию передовая ему Аргументы
    get_last(get_ticket, "USD")
