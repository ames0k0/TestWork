import uuid
import contextlib
from typing import Generator
from urllib.parse import parse_qs

import sqlalchemy.orm as sao
from pydantic import HttpUrl
from fastapi import FastAPI

from app import exceptions
from app.sqldb import Postgres


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    """`startup` and `shutdown` logic"""
    Postgres.initialize()
    yield
    Postgres.terminate()


def get_session() -> Generator[sao.Session, None, None]:
    scoped_session = Postgres.get_scoped_session()
    with scoped_session() as session:
        yield session


def parse_record_id_and_user_id(url: HttpUrl) -> tuple[str, int]:
    """Parsing the given `url` to download a record

    Parameters
    ----------
    url : HttpUrl
        Give `url` to parse

    Returns
    -------
    tuple[int, int]
        record_id, user_id
    """
    parsed_query: dict[str, list[str]] = parse_qs(url.query)

    record_ids: list[str] = parsed_query.get("id", [])
    user_ids: list[str] = parsed_query.get("user", [])

    if not all((record_ids, user_ids)):
        raise exceptions.RecordIDAndUserIDAreRequired()

    record_id: str | None = None
    with contextlib.suppress(ValueError):
        record_id = str(uuid.UUID(record_ids[0]))

    user_id: int | None = None
    with contextlib.suppress(ValueError):
        user_id = int(user_ids[0])

    if (record_id is None) or (user_id is None):
        raise exceptions.RecordIDAndUserIDAreRequired()

    return record_id, user_id
