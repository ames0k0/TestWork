from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core import config
from src.logging.app import Kafka
from src.database.app import Base, SQL


def initialize_dependencies():
    SQL.initialize()
    Kafka.initialize()


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Создание директории для сохранения файла с тарифом
    config.STATIC_DIRECTORY.mkdir(exist_ok=True)

    initialize_dependencies()

    yield
