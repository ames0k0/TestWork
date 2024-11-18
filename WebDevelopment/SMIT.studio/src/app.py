from typing_extensions import Annotated

from fastapi import FastAPI, Body, HTTPException, status

from src import utils
from src.core import config, schemas
from src.core.lifespan import lifespan


app = FastAPI(lifespan=lifespan)


@app.post(
    '/',
    response_model=schemas.InsuranceCalculationOut,
)
async def insurance_calculation(
    cargo_type: str,
    declared_value: int | float,
    insurance_rate: Annotated[schemas.InsuranceRateIn, Body()] = None,
) -> dict:
    """Расчёт стоимости страхования
    """
    if insurance_rate is None:
        if not config.INSURANCE_RATE_FILEPATH.exists():
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Отсутствует файл с тарифом. "
                       "Необходимо передать актуальный тариф!"
            )
        insurance_rate = await utils.load_insurance_rate_from_file()
    else:
        insurance_rate = await (
            utils.save_insurance_rate_to_file(insurance_rate)
        )

    return InsuranceCalculation(
        cargo_type=cargo_type,
        declared_value=declared_value
    ).calculate(
        insurance_rate=insurance_rate
    )


class InsuranceCalculation:
    """Расчёт стоимости страхования
    """
    def __init__(self, cargo_type: str, declared_value: int | float):
        self.cargo_type = cargo_type
        self.declared_value = declared_value

    def calculate(self, insurance_rate: dict) -> dict:
        """Поиск тарифа и расчёт
        """
        rate_date = None
        rate = None
        default_rate = None

        for date, values, in insurance_rate.items():
            rate_date = date
            for value in values:
                if value["cargo_type"].lower() == config.DEFAULT_CARGO_TYPE:
                    default_rate = value["rate"]
                    continue
                if value["cargo_type"] == self.cargo_type:
                    rate = value["rate"]
                    break

        if rate is None:
            rate = default_rate

        cost_of_insurance = self.declared_value * rate

        # NOTE: Округление до тысячных `.3f`
        return {
            "insurance_rate_date": rate_date,
            "cost_of_insurance": f"{cost_of_insurance:.3f}",
        }
