from typing import Generator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config import settings
from src.database import Base, engine


def create_static_dirs() -> None:
    settings.PROJECT_RESUME_FILES_DIR.mkdir(exist_ok=True)


@asynccontextmanager
async def lifespan(_: FastAPI) -> Generator[None, None, None]:
    Base.metadata.create_all(bind=engine)
    yield
