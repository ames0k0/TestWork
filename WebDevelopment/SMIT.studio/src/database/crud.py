import datetime as dt
from typing import Sequence

import sqlalchemy as sa
from sqlalchemy.orm import Session

from src.core import config, schemas
from . import models


class Tariff:

    @staticmethod
    def create(db: Session, insurance_rate: schemas.InsuranceRateIn) -> None:
        """Сохранение тарифов

        Удаляет существующих в базе по `дате`
            - ожидается, что поступил новый тариф, а не дополнение
        """
        dates_to_delete = []
        data_to_create = []

        for ir_date, ir_data, in insurance_rate.items():
            dates_to_delete.append(ir_date)

            for ird in ir_data:
                data_to_create.append(
                    models.Tariff(
                        date=ir_date,
                        # XXX: Force titled, to match `Other`
                        cargo_type=ird.cargo_type.title(),
                        rate=ird.rate,
                    )
                )

        db.execute(
            sa.delete(
                models.Tariff
            ).where(
                models.Tariff.date.in_(dates_to_delete)
            )
        )

        db.add_all(data_to_create)
        db.commit()

    @staticmethod
    def delete_by_date(db: Session, tariff_date: dt.date) -> None:
        """Удаление тарифа по дате
        """
        db.execute(
            sa.delete(
                models.Tariff
            ).where(
                models.Tariff.date == str(tariff_date),
            )
        )
        db.commit()

    @staticmethod
    def get_by_date(
        db: Session,
        tariff_date: dt.date | None
    ) -> Sequence[models.Tariff]:
        """Получение тарифов по дате (опционально)
        """
        q = sa.select(models.Tariff)
        if tariff_date:
            q = q.where(
                models.Tariff.date == str(tariff_date),
            )
        return db.scalars(q).all()

    @staticmethod
    def get_by_date_and_cargo_type(
        db: Session,
        insurance_rate_date: dt.date,
        cargo_type: str,
    ) -> models.Tariff | None:
        """Загрузка тарифа с базы по дате и типу груза
        """
        by_input_cargo_type = db.scalars(
            sa.select(
                models.Tariff
            ).where(
                models.Tariff.date == str(insurance_rate_date),
                models.Tariff.cargo_type == cargo_type.title(),
            )
        ).first()

        if by_input_cargo_type:
            return by_input_cargo_type

        # XXX: `or_` isn't useful
        return db.scalars(
            sa.select(
                models.Tariff
            ).where(
                models.Tariff.date == insurance_rate_date,
                models.Tariff.cargo_type == config.DEFAULT_CARGO_TYPE,
            )
        ).first()
