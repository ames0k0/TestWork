#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

import urllib.request #--------------#
from os import remove #--------------#
from bs4 import BeautifulSoup as bs ##
from time import sleep, time #-------#
from os.path import getmtime, exists #
from requests import get #-----------#
from datetime import datetime #------#
from subprocess import call #--------#


"""
https://stackoverflow.com/questions/10450776/python-always-returning-network-is-unreachable-because-of-old-ipv6-configuration

ИЗ-ЗИ БЛОКИРОВКИ ТАКИЕ ОШИБКИ ВЫХОДЯТ
ПОПРОБОВАЛ ЧЕРЕЗ ПРОКСИ, НО ХЗ
"""

key   = "secret key"    # for weather
token = "secret token"  # for telegram


def w(city):
    r = get("http://api.openweathermap.org/data/2.5/weather?appid={}&q={}".format(key, city))
    data = r.json()
    if int(data['cod']) == 200:
        _id = data['id']
        _temp = data['main']['temp']
        _temp_min = data['main']['temp_min']
        _temp_max = data['main']['temp_max']
        _clouds = data['clouds']['all']
        _country = data['sys']['country']
        _weather = data['weather'][0]['main']
        _wind_speed = data['wind']['speed']
        _desc = data['weather'][0]['description']
        _name = data['name']
        _tem = int(_temp) - 273.15
        _tem_min = int(_temp_min) - 273.15
        _tem_max = int(_temp_max) - 273.15
        _msg = "{}::{}::{}\n~> weather:-------: {}\n~> desc:------------: {}"
        _msg += "\n~> wind:------------: {}m/s\n~> clouds:---------: {}%"
        _msg += "\n~> temp:-----------: {:.2f}°C\n\n~> min_temp:----: {:.2f}°C"
        _msg += "\n~> max_temp:----: {:.2f}°C".format(
            _id, _name, _country, _weather, _desc,
            _wind_speed, _clouds, _tem, _tem_min, _tem_max
            )
        return _msg
    else:
        return "Uncorrect Name or Can't find Country", 'nah'


class TBot():

    def __init__(self):
        self._days = ['月曜日','火曜日','水曜日','木曜日','金曜日','土曜日','日曜日']
        self._time = int(datetime.now().strftime('%H'))
        self._day = self._days[datetime.weekday(datetime.now())]
        self._k = datetime.today().strftime("{}%Y年%m月%d日/%H:%M:%S".format(self._day))
        self._last_update = None
        self._chat_message = None
        self._chat_id = None
        self._user = None
        self._message_id = None
        self._url = "https://api.telegram.org/bot" + token + '/'

    def get_soup(self, url):
        r = urllib.request.urlopen(urllib.request.Request(
            url, headers={
                'User-Agent': 'Mozilla'
            }))
        return bs(r, 'lxml')

    def get_proxy(self):
        soup = self.get_soup('https://www.us-proxy.org')
        tds = soup.find_all('td')
        return [tds[i].text for i in [0, 1, 5]]

    def with_proxy(self, url):
        host, port, ss = self.get_proxy()
        if ss == "yes":
            PROXY = {'https': f"{host}:{port}"}
        else:
            PROXY = {'http': f'{host}:{port}'}
        proxy_support = urllib.request.ProxyHandler(PROXY)
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
        return urllib.request.urlopen(url)

    def get_updates(self):
        try:
            # r = self.with_proxy(self._url + 'getupdates')
            r = get(self._url + 'getupdates')
            data = r.json()['result'][-1]
            self._user = data['message']['from']['first_name']
            message_id = data['message']['message_id']
            self._chat_message = data['message']['text']
            self._chat_id = data['message']['chat']['id']
            return message_id
        except IndexError:
            # (IndexError, KeyError) | ЕСЛИ БОТУ ЕЩЕ НЕ НЕАПИСАЛИ
            return False

    def get_message(self):
        data = self.get_updates()
        if data:
            if data != self._message_id:
                self._message_id = data
                return True
            else:
                return None
        else:
            return None

    def send_message(self, text):
        url = self._url
        get(url + 'sendmessage?chat_id={}&text={}'.format(self._chat_id, text))

    def _ohayo_user(self):
        _msg = "{}, {}\n::{}"
        if self._time < 12:
            self.send_message(_msg.format('おはようございます', self._user, self._k))
        elif self._time >= 12 and self._time <= 22:
            self.send_message(_msg.format('こんにちは', self._user, self._k))

    def _weather_info(self, country):
        if len(country) > 5:
            _rmw = country.replace('/w', '').strip()
            data = w(_rmw)
            self.send_message(data)
        else:
            self._weather_info('Tokyo')

    def _help(self):
        _all = """/w Country name\n/w Tokyo"""
        return _all

    def main(self, debug):
        while True:
            answer = self.get_message()
            if answer != None:
                if debug:
                    print("debug: ", answer)
                text = self._chat_message
                hi = ['hello','hi','nihao','hola', 'ohayo', 'yo', 'hellp']
                _lo = text.lower()
                if _lo in hi:
                    self._ohayo_user()
                elif _lo == '/help':
                    self.send_message(self._help())
                elif _lo.startswith('/w'):
                    self._weather_info(_lo)
                elif text == '/stop':
                    break
                else:
                    pass
            else:
                continue


if __name__=='__main__':
    nya = TBot()
    nya.main(True)
