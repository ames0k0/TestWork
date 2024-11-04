# Generated by Django 5.1.2 on 2024-11-03 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CityWeather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degrees_celsius', models.SmallIntegerField(help_text='Температуру в городе в градусах Цельсия')),
                ('atmospheric_pressure', models.SmallIntegerField(help_text='Атмосферное давление (мм рт.ст.)')),
                ('wind_speed', models.SmallIntegerField(help_text='Скорость ветра (м/с)')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.city')),
            ],
        ),
    ]
