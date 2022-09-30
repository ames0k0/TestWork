#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

"""
TODO:
    Активно, платно -> Активно, бесплатно
    Спокойно, бесплатно -> Спокойно, платно
    Активно, бесплатно -> Спокойно, бесплатно
    Спокойно, бесплатно -> Конец

and What i did ?:
    Spocoyno -> Besplatno
    Activno -> Platno
"""


start_message = "Добрый день! Я робот, \
который поможет вам найти развлечение для выходных!\
\n    Хотите провести время Активно или Спокойно?"

rule = {
    "start": {
        "output": start_message,
        "next": {
           "Активно": "Money",
           "Спокойно": "Money"
        }
    },
    "Money": {
        "output": "Вы готовы потратить на это деньги?",
        "next": {
            "Да": "Activeno",
            "Нет": "Spokoyno"
        }
    },
    "Spokoyno": {
        "output": "Вот несколько вариантов",
        "next": {
            "сходить на выставку; сходить в антикафе": "Da",
            "Посидеть в парке; посмотреть красивую архитектуру": "Da",
            "Не хочу": "Net"
        }
    },
    "Activeno": {
        "output": "Вот несколько вариантов",
        "next": {
            "Сыграйте с друзьями во фрисби в парке": "Da",
            "Прыгните с парашютом; сходите на квест": "Da",
            "Не хочу": "Net"
        }
    },
    "Da": {
        "output": "Рад был помочь!",
        "next": {
            "Вернуть на главную меню": "start"
        }
    },
    "Net": {
        "output": "Извините что мало вариантов!",
        "next": {
            "Передумать насчет денег?": "Money"
        }
    },
}

state = 'start'
choice = {}
bot_out = "\n:> {}\n"

while True:

    # privet (next)
    print(bot_out.format(f"{rule[state]['output']}"))

    # choice
    for i, n in enumerate(rule[state]['next']):
        choice[i] = rule[state]['next'][n]
        print(f'{i}) {n}')

    # in number
    try:
        user_input = input('?: ')
        user_input = int(user_input)
    except Exception:
        user_input = max(list(choice.keys()))

    # with index
    state = choice.get(user_input, state)
