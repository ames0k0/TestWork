from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database.app import Postgres
from src.datastream.app import Kafka


@asynccontextmanager
async def lifespan(app: FastAPI):
    await Postgres.initialize()
    await Kafka.initialize()
    yield
    await Kafka.terminate()
    await Postgres.terminate()