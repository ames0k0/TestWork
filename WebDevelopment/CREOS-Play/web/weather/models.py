from django.db import models


class City(models.Model):
    """Мод
    """
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()


class CityWeather(models.Model):
    """Jii
    """
    degrees_celsius = models.SmallIntegerField(
        help_text="Температуру в городе в градусах Цельсия"
    )
    atmospheric_pressure = models.SmallIntegerField(
        help_text="Атмосферное давление (мм рт.ст.)"
    )
    wind_speed = models.SmallIntegerField(
        help_text="Скорость ветра (м/с)"
    )
    # Settings
    created_at = models.DateTimeField(auto_now=True)
    # Relations
    city = models.ForeignKey(City, on_delete=models.CASCADE)