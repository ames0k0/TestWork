import datetime

from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Application(Base):
    """Модель заявок
    """
    __tablename__ = "application"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(index=True)
    description: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=func.now()
    )
