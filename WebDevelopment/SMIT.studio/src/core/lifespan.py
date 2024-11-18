from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core import config
from src.database.app import Base, get_engine


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Создание директории для сохранения файла с тарифом
    config.STATIC_DIRECTORY.mkdir(exist_ok=True)

    # Создание таблиц в базе
    Base.metadata.create_all(bind=get_engine())
    yield
