import uuid
import contextlib
from typing import AnyStr, Generator
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
    Session = Postgres.get_scoped_session()
    with Session() as session:
        yield session


def parse_record_id_and_user_id(url: HttpUrl) -> tuple[str, int]:
    """Parsing the given `url` to downlaod a record

    Parameters
    ----------
    url : HttpUrl
        Give `url` to parse

    Returns
    -------
    tuple[int, int]
        record_id, user_id
    """

    def convert_to_type(
        data: list[AnyStr], type_: int | uuid.UUID
    ) -> int | uuid.UUID | None:
        for record_id in data:
            record_id = record_id.strip()
            if not record_id:
                continue
            with contextlib.suppress(ValueError):
                return type_(record_id)

    parsed_query: dict[AnyStr, list[AnyStr]] = parse_qs(url.query)

    record_ids: list[AnyStr] | None = parsed_query.get("id", [])
    user_ids: list[AnyStr] | None = parsed_query.get("user", [])

    record_id: uuid.UUID | None = convert_to_type(record_ids, uuid.UUID)
    user_id: int | None = convert_to_type(user_ids, int)

    if not all((record_id, user_id)):
        raise exceptions.RecordIDAndUserIDAreRequired()

    return str(record_id), user_id
