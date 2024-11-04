import datetime

import requests
from bs4 import BeautifulSoup

from ..models import City, CityWeather
from . import OpenStreetMap


YANDEX_WEATHER_URI = "https://yandex.ru/pogoda/ru-RU/details?lat={LATITUDE}&lon={LONGITUDE}&lang=ru&via=mf#3"
YANDEX_WEATHER_RENEW_EVERY_MIN = 30


def request_weather(city):
    session = requests.Session()
    response = session.get(
        YANDEX_WEATHER_URI.format(
            LATITUDE=city.latitude,
            LONGITUDE=city.longitude,
        )
    )
    response


def init_city_weather(city: City) -> tuple[str, CityWeather | None]:
    pass


def get_weather(city_name: str) -> tuple[str, CityWeather | None]:
    error = ""

    city = City.objects.filter(name=city_name).first()
    if not city:
        error, city, = OpenStreetMap.init_city(city_name)
    if error:
        return error, city

    city_weather = CityWeather.objects.filter(
        city=city
    ).order_by(
        CityWeather.created_at.desc()
    )
    if city_weather:
        expires_at = city_weather.created_at + \
                     datetime.timedelta(minutes=YANDEX_WEATHER_RENEW_EVERY_MIN)
        if expires_at > datetime.datetime.now():
            error, city_weather = init_city_weather(city)
    if error:
        return error, city

    return error, city_weather


get_weather("Фрязино")