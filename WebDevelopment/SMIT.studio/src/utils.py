import json

from src.core import config


async def get_current_rate(
    insurance_rate: dict, insurance_rate_date: str,
) -> tuple[str, dict | None]:
    """Возвращает актуальный тариф
    """
    if not insurance_rate:
        return "Файл с тарифом пусто!", None

    values = insurance_rate.get(insurance_rate_date)
    if values is None:
        return "Актуальный тариф не загружен!", None

    return "", {
        insurance_rate_date: values
    }


async def load_insurance_rate_from_file() -> dict:
    """Загрузка тарифа из файла и возвращает актуальный тариф
    """
    with open(config.INSURANCE_RATE_FILEPATH, "r") as ftr:
        return json.load(ftr)


async def save_insurance_rate_to_file(data: dict) -> None:
    """Сохранение тарифа и возвращает актуальный тариф
    """
    with open(config.INSURANCE_RATE_FILEPATH, "w") as ftw:
        json.dump(data, ftw)
