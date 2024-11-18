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
        },
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_insurance_calculation_ignore_missing_insurance_rate():
    """Проверка на не необходимость получение тарифа через API

    в случае если файл с тарифом существует
    """
    with open(config.INSURANCE_RATE_FILEPATH, "w") as ftw:
        json.dump(
            {
                "2020-06-01": [
                    {
                        "cargo_type": "Glass",
                        "rate": 0.01
                    },
                    {
                        "cargo_type": "Other",
                        "rate": 0.10
                    }
                ]
            },
            ftw
        )

    response = client.post(
        '/',
        params={
            "cargo_type": "Glass",
            "declared_value": "33.45",
            "insurance_rate_date": "2020-06-01",
        },
    )
    assert response.status_code == status.HTTP_200_OK

    os.remove(config.INSURANCE_RATE_FILEPATH)


def test_insurance_calculation_require_default_cargo_type_for_insurance_rate():
    """Проверка на передачи дефолтных тарифов, полученный через API
    """
    assert not config.INSURANCE_RATE_FILEPATH.exists()

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


def test_insurance_calculation_save_insurance_rate_to_file():
    """Проверка на создание файла с тарифами, полученный через API
    """
    assert not config.INSURANCE_RATE_FILEPATH.exists()

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
                    "cargo_type": "Other",
                    "rate": "0.04"
                }
            ]
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert config.INSURANCE_RATE_FILEPATH.exists()

    os.remove(config.INSURANCE_RATE_FILEPATH)


def test_insurance_calculation_update_insurance_rate_file():
    """Проверка на обновление / пересоздание файла с тарифами,

    полученный через API
    """
    assert not config.INSURANCE_RATE_FILEPATH.exists()

    config.INSURANCE_RATE_FILEPATH.touch(exist_ok=True)
    file_st_size_before = config.INSURANCE_RATE_FILEPATH.stat().st_size

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
                    "cargo_type": "Other",
                    "rate": "0.04"
                }
            ]
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert config.INSURANCE_RATE_FILEPATH.exists()

    file_st_size_after = config.INSURANCE_RATE_FILEPATH.stat().st_size
    assert file_st_size_before != file_st_size_after

    os.remove(config.INSURANCE_RATE_FILEPATH)
