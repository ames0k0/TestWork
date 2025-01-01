from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Header, Depends
from sqlalchemy.orm import Session

from . import schemas, models, connections, crud


@asynccontextmanager
async def lifespan(app: FastAPI):
    connections.Postgres.initialize()
    connections.Redis.initialize()
    connections.Celery.initialize()
    yield


app = FastAPI(
    title="TestWork005",
    summary="Микросервис анализа финансовых транзакций",
    lifespan=lifespan,
)


@app.post(
    '/transactions',
    summary='Загрузка транзакции',
    response_model=schemas.TaskStatsUpdateInfo,
)
async def post_transactions(
    data: schemas.TransactionsCreateIn,
    api_key: Annotated[str, Header(alias="ApiKey")],
    session: Annotated[
        Session,
        Depends(connections.Postgres.get_scoped_session)
    ],
) -> dict:
    crud.Postgres.create(
        data=data,
        api_key=api_key,
        session=session,
    )
    task_id = crud.Celery.update_transaction_statistics(
        api_key=api_key,
    )
    return {
        "message": "Transaction received",
        "task_id": task_id,
    }


@app.delete(
    '/transactions',
    summary='Удаление всех транзакций',
)
async def delete_transactions(
    api_key: Annotated[str, Header(alias="ApiKey")],
    session: Annotated[
        Session,
        Depends(connections.Postgres.get_scoped_session)
    ],
) -> str:
    """Deletes the transactions from the database and the cached analysis
    """
    crud.Postgres.delete(api_key=api_key, session=session)
    crud.Redis.delete(api_key=api_key)
    return 'OK'


@app.get(
    '/statistics',
    summary='Получение статистики по транзакциям',
)
async def get_statistics(
    api_key: Annotated[str, Header(alias="ApiKey")],
) -> dict:
    """Returns the transaction analysis from the cache
    """
    return crud.Redis.get(api_key)
