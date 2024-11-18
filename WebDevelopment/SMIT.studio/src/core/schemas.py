import datetime as dt

from typing_extensions import Annotated
from pydantic import BaseModel
from pydantic.functional_validators import AfterValidator
from pydantic.functional_validators import model_validator

from . import config


class InsuranceRate(BaseModel):
    """Схема страхового тарифа
    """
    cargo_type: str
    rate: float

    @model_validator(mode='after')
    def dumping_the_model(self):
        return self.model_dump()


def check_date_format(v: dict) -> dict:
    """Проверка на формат дат для тарифов
    """
    for key in v.keys():
        try:
            dt.datetime.strptime(
                key,
                config.INSURANCE_RATE_DATE_FORMAT,
            )
        except ValueError:
            raise ValueError("Необходимо передать тариф с актуальной датой")

    return v


def check_missing_default_cargo_type(v: dict) -> dict:
    """Проверка на передачи дефолтных тарифов
    """
    for values in v.values():
        for value in values:
            if value["cargo_type"].lower() == config.DEFAULT_CARGO_TYPE:
                break
        else:
            raise ValueError(
                "Необходимо передать дефолтный тариф `cargo_type: Other`"
            )

    return v


def check_insurance_rate_file(v: None) -> None:
    if config.INSURANCE_RATE_FILEPATH.exists():
        return

    raise FileNotFoundError(
        "Отсутствует файл с тарифом. Необходимо передать актуальный тариф!"
    )


# NOTE: `str` - Избегаю конвертации `dt.date` обратно в строку ("2020-06-01")
InsuranceRateIn = Annotated[
    dict[str, list[InsuranceRate]],
    AfterValidator(check_date_format),
    AfterValidator(check_missing_default_cargo_type),
]

InsuranceRateFromFile = Annotated[
    None,
    AfterValidator(check_insurance_rate_file),
]


class InsuranceCalculationOut(BaseModel):
    insurance_rate_date: str
    cost_of_insurance: float


class InsuranceCalculationRequestIN:
    __slots__ = (
        'cargo_type',
        'declared_value',
        'cost_of_insurance',
        'insurance_rate_date',
        'insurance_rate',
        'request_dt',
        'response_dt',
    )


class InsuranceCalculationRequestOUT(BaseModel):
    id: int

    cargo_type: str
    declared_value: float
    cost_of_insurance: float

    insurance_rate_date: str
    insurance_rate: float

    request_dt: dt.datetime
    response_dt: dt.datetime
