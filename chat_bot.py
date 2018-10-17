#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

"""
what i did ?:
    Spocoyno -> Besplatno
    Activno -> Platno


TODO:
    Активно, платно -> Активно, бесплатно
    Спокойно, бесплатно -> Спокойно, платно
    Активно, бесплатно -> Спокойно, бесплатно
    Спокойно, бесплатно -> Конец
"""


rule = {
    "start": {
        "output": "Dobriy den. Ya robot, which helps you to look up razvlechenie for freedays. \n\tDo you want Activeno or Spokoyno ?",
        "next": {
           "Activeno": "Money",
           "Spokoyno": "Money"
        }
    },
    "Money": {
        "output": "Are you ready to potratit dengi ?",
        "next": {
            "Da": "Activeno",
            "Net": "Spokoyno"
        }
    },
    "Spokoyno": {
        "output": "Vot neskolko Variantov",
        "next": {
            "сходить на выставку; сходить в антикафе": "Davayte",
            "Посидеть в парке; посмотреть красивую архитектуру": "Davayte",
            "Ne hochu": "Net"
        }
    },
    "Activeno": {
        "output": "Togda Poehali",
        "next": {
            "Сыграйте с друзьями во фрисби в парке": "Davayte",
            "Прыгните с парашютом; сходите на квест": "Davayte",
            "Ne hochu": "Net"
        }
    },
    "Davayte": {
        "output": "Rad bil pomoch!",
        "next": {
            "vernutcya na glavnuyu menyu?": "start"
        }
    },
    "Net": {
        "output": "nu nu Kotik",
        "next": {
            "kill yourself": "Da",
            "peredumat naschet deneg": "Money"
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
