import datetime as dt

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.database.app import Base


class InsuranceCalculationRequest(Base):
    """Таблица истории запросов и ответов
    """
    __tablename__ = "insurance_calculation_request"

    id: Mapped[int] = mapped_column(primary_key=True)

    cargo_type: Mapped[str]
    declared_value: Mapped[float]
    cost_of_insurance: Mapped[float]

    insurance_rate_date: Mapped[str]
    insurance_rate: Mapped[float]

    request_dt: Mapped[dt.datetime]
    response_dt: Mapped[dt.datetime]
