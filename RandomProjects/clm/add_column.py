#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

import sqlite3
from os.path import exists
from itertools import count
from collections import defaultdict, deque
from random import choice, randint
from string import ascii_letters


"""
Tupic!!!
"""

class CreateYourOwnSity:
    """
    """
    __slots__ = (
        "model", "country", "city", "region",
        "town", "template", "connect", "cursor"
    )

    def __init__(
            self, model="map.db", country="hell",
            city="Semnh", region="henfild", town="shichan"
        ):
        self.city = city
        self.town = town
        self.model = model
        self.region = region
        self.country = country
        self.template = deque("country city region town".split())
        if not exists(self.model):
            self._first_run()
        self.connect = sqlite3.connect(model)
        self.cursor = self.connect.cursor()

    def _first_run(self):
        char = 30
        last = None
        with sqlite3.connect(self.model) as conn:
            cur = conn.cursor()
            for item, first in zip(self.template, (
                        self.country, self.city, self.region, self.town
                    )
                ):
                if not last:
                    cur.execute(
                        f"""CREATE TABLE IF NOT EXISTS {item} (
                        id INTEGER PRIMARY KEY,
                        name char ({char}))"""
                    )
                    cur.execute(
                        f"""INSERT INTO {item}(name)
                        VALUES (?)""", (first,)
                    )
                else:
                    cur.execute(
                        f"""CREATE TABLE IF NOT EXISTS {item} (
                        from_{last} char ({char}),
                        name char ({char}))"""
                    )
                    cur.execute(
                        f"""INSERT INTO {item}(from_{last}, name)
                        VALUES (?, ?)""", (1, first)
                    )
                last = item

    def _readable_data(self):
        self.cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table'""")
        print(self.cursor.fetchall())

    def user_interface(self):
        print("1: add info | 2: tree")
        return input('?: ')

    def _readable_choice(self, dct):
        """
        """
        for idx, value in dct.items():
            print(f"{idx}: {value}", end=" | ")
        return dct

    def _done_by_user(self):
        """
        """
        print(self.country)
        print(self.city)
        print(self.region)
        print(self.town)
        self._readable_data()

    def _gen_dct(self, temp):
        """
        """
        return defaultdict(str, zip(map(str, count()), temp))

    # def change_map_info(self):
    #     mdeb = self.template.popleft()
    #     self.cursor.execute(f"""SELECT * FROM {mdeb}""")

    #     gen = (
    #         [f"{idx}: {name:<20}" for _ in range(4) if idx]
    #         for (idx, name) in self.cursor.fetchal()
    #     )

    #     for each in gen:
    #         print("".join(each))

    def bar(self):
        return (
            tuple(
                zip(
                    count(),
                    ("".join([choice(ascii_letters) for _ in range(randint(6, 19))]),)
                )
            )
            for _ in range(4)
        )

    def add_info_to_map(self):
        """
        """
        pass
        # for _ in range(29):
            # temp = self.template().copy()
            # while temp:
            #     # mdeb = self._readable_choice(self._gen_dct())
            #     mdeb = temp.popleft()
            #     # mdeb = self.change_map_info()
            #     data = input(f'Type {mdeb.title():<8}: ')
            #     if data:
            #         exec(f"self.{mdeb} = '{data}'")

        # self._done_by_user()


cyos = CreateYourOwnSity()
# cyos.add_info_to_map()
print(type(cyos.foo()))
