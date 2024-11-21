import datetime as dt
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, DateTime, func

from src.database.app import Base


class Tariff(Base):
    """Таблица тарифов
    """
    __tablename__ = "tariff"

    id: Mapped[int] = mapped_column(primary_key=True)

    date: Mapped[str]
    cargo_type: Mapped[str]
    rate: Mapped[float]

    # Settings
    created_at: Mapped[dt.datetime] = Column(
        DateTime, server_default=func.now(),
    )

