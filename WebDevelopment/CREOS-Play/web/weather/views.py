from http.client import HTTPException

from django.http import JsonResponse
from django.shortcuts import render

from .services import YandexWeather


def weather(request):
  if request.method != "GET":
    raise HTTPException(f"Method \"{request.method}\" not supported!")

  city_name = request.GET.get("city")
  if not city_name:
    raise HTTPException("Missing `city` argument!")

  error, city_weather = YandexWeather.get_weather(city_name)
  if error:
    raise HTTPException(error)

  return JsonResponse(
    city_weather
  )


def requests():
  pass
