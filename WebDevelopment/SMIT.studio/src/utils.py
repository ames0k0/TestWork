import json

from src.core import config


async def get_current_rate(data: dict):
    """Возвращает актуальный тариф
    """
    # XXX: File shouldn't be empty
    if not data:
        raise RuntimeError("Файл с тарифом пусто!")

    oldest_date = sorted(data.keys())[-1]

    return {
        oldest_date: data[oldest_date]
    }


async def load_insurance_rate_from_file() -> dict:
    """Загрузка тарифа из файла и возвращает актуальный тариф
    """
    with open(config.INSURANCE_RATE_FILEPATH, "r") as ftr:
        data = json.load(ftr)

    return await get_current_rate(data)


async def save_insurance_rate_to_file(data: dict) -> dict:
    """Сохранение тарифа и возвращает актуальный тариф
    """
    with open(config.INSURANCE_RATE_FILEPATH, "w") as ftw:
        json.dump(data, ftw)

    return await get_current_rate(data)
