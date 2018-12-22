#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-天底 ガジ'

import re
import socket
from bs4 import BeautifulSoup as bs
from collections import deque


"""
Congrats! Now you know about socket, deque, re and bs4
Happy coding!!!

Code was written with Pep8 code style, and PyLint syntax :)
"""


def solution():
    """
    information about code style

    {{ block code }}
        N. Номер задание
        # Сайты с информациями которых использовал чтобы решать задачу

        Сам код
    {{ endblock }}
    """
    BARER = f"{'-' * 55}\n"

    # 1. No error handler is here
    # Code was written only for var t with 12 elements

    t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    t = deque(t)
    print('\n1. 3p4e: ', [[t.popleft() for _ in range(4)] for _ in range(3)])

    print(BARER)
    # 3. Plz read sources to better understand what's going on in here
    # source to read
    # https://realpython.com/python-sockets/
    # https://www.w3.org/Protocols/rfc2616/rfc2616.html
    # https://stackoverflow.com/questions/32428454/python-sock-recv-not-getting-all-data-from-page

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('iict.kz', 80))
        s.send(b'GET / HTTP/1.1\nHost: iict.kz\r\n\r\n')
        responce = ''.encode()

        while True:
            data = s.recv(1024)

            if not len(data):
                break

            responce += data

        # responce = responce.decode().replace('Институт', 'Корпорация')
        responce = responce.decode().replace('Институт', 'Корпорация')

        with open('iict.html', 'w') as f:
            f.write(responce)

        print('3. source was written to file <iict.html> with success')

    print(BARER)
    # 2. Same thing
    # source to read, and use
    # https://www.gps-coordinates.net/
    # https://support.google.com/maps/answer/18539?co=GENIE.Platform%3DDesktop&hl=en
    # <a href="??">050010, Қазақстан Республикасы Алматы қ. Пушкин к., 125</a>

    for url in bs(responce, 'lxml').find_all('a'):
        url = url.get('href')
        if url and url.startswith('https://2gis.kz'):
            lat_lon = re.compile(r'\d+\.\d+')
            print("2. latitude_longitude:", re.findall(lat_lon, url))
            break

    print(BARER, end='')


if __name__ == "__main__":
    solution()
