from pydantic import BaseModel


__all__ = (
    'TransactionsCreateIn',
    'TaskStatsUpdateInfo',
    'StatisticsOut',
)


class TransactionsCreateIn(BaseModel):
    transaction_id: str
    user_id: int
    amount: float
    currency: str
    timestamp: str


class TaskStatsUpdateInfo(BaseModel):
    message: str
    task_id: str


class TopTransactionsOut(BaseModel):
    transaction_id: str
    amount: int


class StatisticsOut(BaseModel):
    total_transactions: int
    average_transaction_amount: float
    top_transactions: list[TopTransactionsOut]
