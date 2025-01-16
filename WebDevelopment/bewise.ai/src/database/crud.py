import sqlalchemy as sa

from fastapi_pagination import paginate
from fastapi_pagination.ext.sqlalchemy import paginate

from . import models


class Application:
    @staticmethod
    async def create(application, async_session) -> models.Application:
        obj = models.Application(
            **application.model_dump()
        )
        async_session.add(obj)
        await async_session.commit()
        return obj

    @staticmethod
    async def get_all_paginated(
        filter_params, async_session
    ):
        q = sa.select(models.Application)

        user_name = filter_params.get("user_name")
        if user_name is not None:
            # XXX: no context, used `eq`
            q = q.where(models.Application.user_name == user_name)

        q = q.order_by(models.Application.id.desc())

        return await paginate(async_session, q)
