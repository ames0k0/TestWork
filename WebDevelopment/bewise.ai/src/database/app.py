from asyncio import current_task

from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)

from src.core.config import settings
from . import models


class Postgres:
    async_engine: AsyncEngine
    async_session_factory: async_sessionmaker

    @classmethod
    async def initialize(cls):
        async_engine = create_async_engine(settings.postgres.database_uri)
        async_session_factory = async_sessionmaker(
            async_engine,
            expire_on_commit=False,
        )
        async with async_engine.begin() as conn:
            await conn.run_sync(models.Base.metadata.create_all)

        cls.async_engine = async_engine
        cls.async_session_factory = async_session_factory

    @classmethod
    async def terminate(cls):
        await cls.async_engine.dispose()

    @classmethod
    async def get_async_scoped_session(cls):
        return async_scoped_session(
            session_factory=cls.async_session_factory,
            scopefunc=current_task,
        )
