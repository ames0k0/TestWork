import datetime as dt
from typing import Sequence
from typing_extensions import Annotated

from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, Body, Query, HTTPException, status

from src.core import config, schemas, dependencies, lifespan
from src.database import crud
from src.logging.kafka import UserEventsLogger, TopicEnum


app = FastAPI(
    title="SMIT.studio",
    summary="REST API сервис по расчёту стоимости страхование "
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
    insurance_rate_date: dt.date = Query(description="Дата страхового тарифа"),
    insurance_rate: Annotated[
        schemas.InsuranceRateIn,
        Body(
            examples=config.INSURANCE_CALCULATION_EXAMPLES,
            description="Тариф для расчёта",
        )
    ] = None,
    db: Session = Depends(dependencies.sql_session),
) -> dict:
    """Расчёт стоимости страхования
    """
    if insurance_rate:
        UserEventsLogger.log_to_kafka(
            user_id=config.DEFAULT_USER_ID,
            event_topic=TopicEnum.TARIFF.value,
            event_message='Загружен тариф через API',
            event_timestamp=dt.datetime.now().timestamp(),
        )
        crud.Tariff.create(db, insurance_rate)

    tariff = crud.Tariff.get_by_date_and_cargo_type(
        db,
        insurance_rate_date=insurance_rate_date,
        cargo_type=cargo_type,
    )
    if not tariff:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Актуальный тариф не загружен!"
        )

    # NOTE: Округление до тысячных `.3f`
    cost_of_insurance = round(
        declared_value * tariff.rate,
        3,
    )

    # NOTE: Добавил тариф
    return {
        "cost_of_insurance": cost_of_insurance,
        "tariff": tariff,
    }


@app.get(
    '/tariff-get',
    tags=["Тариф"],
    name='Получение тарифов',
    response_model=Sequence[schemas.TariffOUT],
)
async def delete_tariff(
    tariff_date: dt.date | None = Query(None, description="Дата Тарифа"),
    db: Session = Depends(dependencies.sql_session),
) -> Sequence[schemas.TariffOUT]:
    """Получение тарифов по дате (опционально)
    """
    return crud.Tariff.get_by_date(db=db, tariff_date=tariff_date)


@app.delete(
    '/tariff-delete',
    tags=["Тариф"],
    name='Удаление тарифа',
)
async def delete_tariff(
    tariff_date: dt.date = Query(description="Дата Тарифа"),
    db: Session = Depends(dependencies.sql_session),
) -> str:
    """Удаление тарифа по дате
    """
    UserEventsLogger.log_to_kafka(
        user_id=config.DEFAULT_USER_ID,
        event_topic=TopicEnum.TARIFF.value,
        event_message=f"Запрос на удаление тарифа по дате: {tariff_date}",
        event_timestamp=dt.datetime.now().timestamp(),
    )
    crud.Tariff.delete_by_date(db=db, tariff_date=tariff_date)

    return 'OK'
