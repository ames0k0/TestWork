import uuid
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import UUID, LargeBinary
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    token: Mapped[str] = mapped_column(
        UUID,
        default=uuid.uuid4,
    )

    # Relations
    records: Mapped[List["Record"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"


class Record(Base):
    __tablename__ = "user_record"

    id: Mapped[str] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    filename: Mapped[str]
    file: Mapped[bytes] = mapped_column(LargeBinary)

    # Relations
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="records")

    def __repr__(self) -> str:
        return f"Record(id={self.id!r}, filename={self.filename!r})"
