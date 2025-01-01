from pydantic import BaseModel


__all__ = (
    'PostTransactionsIn',
    'PostTransactionsOut',
    'GetStatisticsOut',
)


class PostTransactionsIn(BaseModel):
    transaction_id: str
    user_id: int
    amount: float
    currency: str
    timestamp: str


class PostTransactionsOut(BaseModel):
    message: str
    task_id: str


class _TopTransactionsOut(BaseModel):
    transaction_id: str
    amount: int


class GetStatisticsOut(BaseModel):
    total_transactions: int
    average_transaction_amount: float
    top_transactions: list[_TopTransactionsOut]
