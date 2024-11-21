import os
import json

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from src.core import config
from src.app import app


client = TestClient(app)


def test_static_directory_creation():
    """Проверка создание директории для сохранения тарифа
    """
    assert config.STATIC_DIRECTORY.exists()


def test_insurance_calculation_require_missing_insurance_rate():
    """Проверка на необходимость получение тарифа через API

    в случае если нет файла с тарифом
    """
    response = client.post(
        '/',
        params={
            "cargo_type": "Glass",
            "declared_value": "33.45",
            "insurance_rate_date": "2020-06-01",
        },
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_insurance_calculation_require_default_cargo_type_for_insurance_rate():
    """Проверка на передачи дефолтных тарифов, полученный через API
    """
    response = client.post(
        '/',
        params={
            "cargo_type": "Glass",
            "declared_value": "33.45",
            "insurance_rate_date": "2020-06-01",
        },
        json={
            "2020-06-01": [
                {
                    "cargo_type": "Glass",
                    "rate": "0.04"
                }
            ]
        },
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_insurance_calculation_ok():
    """Проверка на сохранение тарифов, полученный через API
    """
    response = client.post(
        '/',
        params={
            "cargo_type": "Glass",
            "declared_value": "33.45",
            "insurance_rate_date": "2020-06-01",
        },
        json={
            "2020-06-01": [
                {
                    "cargo_type": "Glass",
                    "rate": "0.04"
                },
                {
                    "cargo_type": "Other",
                    "rate": "0.04"
                }
            ]
        },
    )
    assert response.status_code == status.HTTP_200_OK


def test_insurance_calculation_ignore_missing_insurance_rate():
    """Проверка на не необходимость получение тарифа через API

    в случае если тариф уже загружен
    """
    response = client.post(
        '/',
        params={
            "cargo_type": "Glass",
            "declared_value": "33.45",
            "insurance_rate_date": "2020-06-01",
        },
    )
    assert response.status_code == status.HTTP_200_OK
