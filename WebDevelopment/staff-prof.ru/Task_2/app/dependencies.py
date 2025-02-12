import contextlib
from typing import AnyStr
from urllib.parse import parse_qs

from pydantic import HttpUrl
from fastapi import FastAPI

from app.sqldb import Postgres
from app.exceptions import RecordIDAndUserIDAreRequired


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    """`startup` and `shutdown` logic"""
    Postgres.initialize()
    yield
    Postgres.terminate()


def parse_record_id_and_user_id(url: HttpUrl) -> tuple[int, int]:
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

    def str_to_int(data: list[AnyStr]) -> int | None:
        for record_id in data:
            record_id = record_id.strip()
            if not record_id:
                continue
            with contextlib.suppress(ValueError):
                return int(record_id)

    parsed_query: dict[AnyStr, list[AnyStr]] = parse_qs(url.query)
    record_ids: list[AnyStr] | None = parsed_query.get("id", [])
    user_ids: list[AnyStr] | None = parsed_query.get("user", [])

    record_id: int | None = str_to_int(record_ids)
    user_id: int | None = str_to_int(user_ids)

    if not all((record_id, user_id)):
        raise RecordIDAndUserIDAreRequired()

    return record_id, user_id
