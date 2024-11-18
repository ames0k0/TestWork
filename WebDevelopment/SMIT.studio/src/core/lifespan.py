from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core import config


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Создание директории для сохранения файла с тарифом
    config.STATIC_DIRECTORY.mkdir(exist_ok=True)
    yield
