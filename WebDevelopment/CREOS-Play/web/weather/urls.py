from django.urls import path

from . import views

urlpatterns = [
  path('weather', views.weather, name='weather-weather'),
  path('requests', views.requests, name='weather-requests'),
]