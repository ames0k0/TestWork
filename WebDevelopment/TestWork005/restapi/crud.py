import json
from typing import Sequence

import sqlalchemy as sa
import sqlalchemy.orm as sao

from . import models, schemas, connections


class Postgres:
    """Transaction model CRUD functions
    """
    @staticmethod
    def create(
        *,
        data: schemas.PostTransactionsIn,
        api_key: str,
        session: sao.Session,
    ) -> None:
        """Saves the transaction, ignores if exists
        """
        if session.scalar(
            sa.select(
                models.Transactions,
            ).where(
                models.Transactions.transaction_id == data.transaction_id,
            )
        ):
            return None

        session.add(
            models.Transactions(
                api_key=api_key,
                **data.model_dump()
            )
        )
        session.commit()

    @staticmethod
    def get_all(
        *,
        api_key: str,
        session: sao.Session,
    ) -> Sequence[models.Transactions]:
        """Returns all transactions for the given `api_key`
        """
        return session.scalars(
            sa.select(
                models.Transactions,
            ).where(
                models.Transactions.api_key == api_key,
            )
        ).all()

    @staticmethod
    def delete(
        *,
        api_key: str,
        session: sao.Session,
    ) -> None:
        """Deletes all transactions with the given `api_key`
        """
        session.execute(
            sa.delete(
                models.Transactions
            ).where(
                models.Transactions.api_key == api_key,
            )
        )
        session.commit()


class Redis:
    CACHE_NAME = "transactions_analysis:{api_key}"
    DEFAULT_TRANSACTIONS_ANALYSIS = {
        "total_transactions": 0,
        "average_transaction_amount": 0,
        "top_transactions": [
        ]
    }

    @staticmethod
    def get(api_key: str) -> dict:
        """Returns the transactions analysis from the cache or default
        """
        transactions_analysis = connections.Redis.ins.get(
            name=Redis.CACHE_NAME.format(
                api_key=api_key,
            ),
        )
        if not transactions_analysis:
            return Redis.DEFAULT_TRANSACTIONS_ANALYSIS

        return json.loads(transactions_analysis)

    @staticmethod
    def set(*, api_key: str, transactions_analysis: dict):
        """Caching the transactions analysis
        """
        connections.Redis.ins.set(
            name=Redis.CACHE_NAME.format(
                api_key=api_key,
            ),
            value=json.dumps(transactions_analysis),
        )

    @staticmethod
    def delete(*, api_key: str):
        """Deletes the transactions analysis
        """
        connections.Redis.ins.delete(
            Redis.CACHE_NAME.format(
                api_key=api_key,
            ),
        )


class Celery:
    @staticmethod
    def update_transactions_analysis(*, api_key: str) -> str:
        """Creates a task `update_transactions_analysis`
        """
        return connections.Celery.ins.send_task(
            name="update_transactions_analysis",
            kwargs={
                "api_key": api_key,
            }
        ).task_id
