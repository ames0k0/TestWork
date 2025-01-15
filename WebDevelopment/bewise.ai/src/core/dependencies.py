from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from src.database.app import Postgres


@asynccontextmanager
async def lifespan(app: FastAPI):
    add_pagination(app)

    await Postgres.initialize()
    yield
    await Postgres.terminate()