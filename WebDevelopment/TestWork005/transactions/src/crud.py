import json

import sqlalchemy as sa
import sqlalchemy.orm as sao

from . import models, schemas, connections


class Postgres:
    """Transaction model CRUD functions
    """
    @staticmethod
    def create(
        *,
        data: schemas.TransactionsCreateIn,
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
    CACHE_NAME = "cache:{api_key}"
    DEFAULT_STATS = {
        "total_transactions": 0,
        "average_transaction_amount": 0,
        "top_transactions": [
        ]
    }

    @staticmethod
    def get(api_key: str) -> dict:
        """Returns the transactions statistics from the cache or empty schema
        """
        stats = connections.Redis.ins.get(
            name=Redis.CACHE_NAME.format(
                api_key=api_key,
            ),
        )
        if not stats:
            return Redis.DEFAULT_STATS

        return json.loads(stats)

    @staticmethod
    def set(api_key: str, stats: dict):
        """Setting the transactions statistics
        """
        connections.Redis.ins.set(
            name=Redis.CACHE_NAME.format(
                api_key=api_key,
            ),
            value=json.dumps(stats),
        )

    @staticmethod
    def delete(*, api_key: str):
        """Deletes the transactions statistics
        """
        connections.Redis.ins.delete(api_key)


class Celery:
    @staticmethod
    def update_transaction_statistics(*, api_key: str) -> str:
        """Creates a task `update_transaction_statistics`
        """
        return connections.Celery.ins.send_task(
            name="update_transaction_statistics",
            args=(
                api_key,
            )
        ).task_id
