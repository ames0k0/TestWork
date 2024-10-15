#!/usr/bin/python3
# coding=utf-8

import os
from requests import get

def w(city):
    key = os.environ['OPENWEATHERMAP_KEY']
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
        _msg = """{}::{}::{}\n~> weather:-------: {}\n~> desc:------------: {}\n~> wind:------------: {}m/s\n~> clouds:---------: {}%\n~> temp:-----------: {:.2f}°C\n\n~> min_temp:----: {:.2f}°C\n~> max_temp:----: {:.2f}°C""".format(_id, _name, _country, _weather, _desc, _wind_speed, _clouds, _tem, _tem_min, _tem_max)
        return _msg, _weather
    else:
        return "Uncorrect Name or Can't find Country", 'nah'
