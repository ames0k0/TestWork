import datetime as dt

from typing_extensions import Annotated
from pydantic import BaseModel
from pydantic.functional_validators import AfterValidator

from . import config


class InsuranceRate(BaseModel):
    """Схема страхового тарифа
    """
    cargo_type: str
    rate: float


def check_date_format(v: dict) -> dict:
    """Проверка на формат дат для тарифов
    """
    dates = set()

    for key in v.keys():
        try:
            date = dt.datetime.strptime(
                key,
                config.INSURANCE_RATE_DATE_FORMAT,
            )
            if date in dates:
                raise ValueError(f"Дублирован даты тарифа: {key}")

            dates.add(date)
        except ValueError:
            raise ValueError("Необходимо передать тариф с актуальной датой")

    return v


def check_missing_default_cargo_type(v: dict) -> dict:
    """Проверка на передачи дефолтных тарифов
    """
    for values in v.values():
        for value in values:
            if value.cargo_type.title() == config.DEFAULT_CARGO_TYPE:
                break
        else:
            raise ValueError(
                "Необходимо передать дефолтный тариф `cargo_type: Other`"
            )

    return v


# NOTE: `str` - Избегаю конвертации `dt.date` обратно в строку ("2020-06-01")
InsuranceRateIn = Annotated[
    dict[str, list[InsuranceRate]],
    AfterValidator(check_date_format),
    AfterValidator(check_missing_default_cargo_type),
]


class TariffOUT(BaseModel):
    date: str
    cargo_type: str
    rate: float


class InsuranceCalculationOut(BaseModel):
    cost_of_insurance: float
    tariff: TariffOUT
