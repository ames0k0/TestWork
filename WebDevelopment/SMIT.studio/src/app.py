import datetime as dt
from typing_extensions import Annotated

from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, Body, Query, HTTPException, status

from src import utils
from src.core import config, schemas, dependencies, lifespan
from src.database import crud


app = FastAPI(
    title="SMIT.studio",
    summary=
    "REST API сервис по расчёту стоимости страхование "
    "в зависимости от типа груза и объявленной стоимости (ОС)",
    lifespan=lifespan.lifespan,

)


@app.post(
    '/',
    tags=["Стоимость страхования"],
    name='Расчёт стоимости страхования',
    response_model=schemas.InsuranceCalculationOut,
)
async def insurance_calculation(
    cargo_type: str = Query(description="Тип груза"),
    declared_value: int | float = Query(description="Объявленный стоимость"),
    insurance_rate_date: dt.date = Query(description="Дата груза"),
    insurance_rate: Annotated[
        schemas.InsuranceRateIn,
        Body(
            examples=config.INSURANCE_CALCULATION_EXAMPLES,
            description="Тариф для расчёта",
        )
    ] = None,
    db: Session = Depends(dependencies.get_session),
) -> dict:
    """Расчёт стоимости страхования
    """
    icr = schemas.InsuranceCalculationRequestIN()

    insurance_rate_date = insurance_rate_date.strftime(
        config.INSURANCE_RATE_DATE_FORMAT
    )

    icr.request_dt = dt.datetime.now()
    icr.cargo_type = cargo_type
    icr.declared_value = declared_value
    icr.insurance_rate_date = insurance_rate_date

    if insurance_rate is None:
        if not config.INSURANCE_RATE_FILEPATH.exists():
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Отсутствует файл с тарифом. "
                       "Необходимо передать актуальный тариф!"
            )
        insurance_rate = await utils.load_insurance_rate_from_file()
    else:
        await utils.save_insurance_rate_to_file(insurance_rate)

    error_msg, insurance_rate = await utils.get_current_rate(
        insurance_rate, insurance_rate_date
    )
    if error_msg:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=error_msg
        )

    result = InsuranceCalculation(
        icr=icr,
        cargo_type=cargo_type,
        declared_value=declared_value
    ).calculate(
        insurance_rate=insurance_rate
    )

    icr.response_dt = dt.datetime.now()

    crud.InsuranceCalculationRequest.add(db=db, data=icr)

    return result


class InsuranceCalculation:
    """Расчёт стоимости страхования
    """
    def __init__(
        self,
        icr: schemas.InsuranceCalculationRequestIN,
        cargo_type: str, declared_value: int | float,
    ):
        self.icr = icr
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

        # NOTE: Округление до тысячных `.3f`
        cost_of_insurance = round(self.declared_value * rate, 3)

        self.icr.cost_of_insurance = cost_of_insurance
        self.icr.insurance_rate_date = rate_date
        self.icr.insurance_rate = rate

        return {
            "insurance_rate_date": rate_date,
            "cost_of_insurance": cost_of_insurance,
        }


@app.get(
    '/requests',
    tags=["Стоимость страхования"],
    name='Запросы по расчёту стоимости страхования',
    response_model=list[schemas.InsuranceCalculationRequestOUT],
)
async def insurance_calculation_requests(
    limit: int,
    db: Session = Depends(dependencies.get_session),
) -> list:
    """Запросы по расчёту стоимости страхования
    """
    return crud.InsuranceCalculationRequest.load_least_n(db=db, limit=limit)
