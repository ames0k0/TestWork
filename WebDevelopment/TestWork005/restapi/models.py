from sqlalchemy.orm import Mapped
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class Transactions(Base):
    __tablename__ = "transactions"

    transaction_id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[str]
    amount: Mapped[float]
    currency: Mapped[str]
    timestamp: Mapped[str]

    api_key: Mapped[str]

    def __repr__(self) -> str:
        data = (
            f"id={self.transaction_id!r}",
            f"user_id={self.user_id}",
            f"amount={self.amount}",
            f"currency={self.currency}"
            f"timestamp={self.timestamp}",
        )
        return f"Transaction({', '.join(data)})"
