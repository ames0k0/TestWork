from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends

from src.database import crud
from src.database.app import Postgres
from src.datastream.publication import Kafka

from . import schemas, dependencies


router = APIRouter()


@router.post(
    "/",
    summary="Создания новой заявки",
    response_model=schemas.ApplicationInDB,
)
async def post(
    application: schemas.PostApplicationIn,
    async_session: Annotated[
        AsyncSession,
        Depends(dependency=Postgres.get_async_scoped_session),
    ],
):
    """Создания новой заявки, возвращает модель
    """
    obj = await crud.Application.create(
        application=application,
        async_session=async_session,
    )
    await Kafka.publish_new_application(obj=obj)
    return obj


@router.get(
    "/",
    summary="Получения списка заявок",
    response_model=schemas.PaginationPage[schemas.ApplicationInDB],
)
async def get(
    filter_params: Annotated[
        dict, Depends(dependency=dependencies.filter_params)
    ],
    async_session: Annotated[
        AsyncSession,
        Depends(dependency=Postgres.get_async_scoped_session),
    ],
):
    """Получения списка заявок
    """
    return await crud.Application.get_all_paginated(
        filter_params=filter_params,
        async_session=async_session,
    )