import datetime as dt
from typing import TypeVar

from pydantic import BaseModel, Field
from fastapi import Query
from fastapi_pagination import Page
from fastapi_pagination.customization import CustomizedPage, UseParamsFields

from src.core.config import settings


class PostApplicationIn(BaseModel):
    user_name: str = Field(description="Имя пользователя")
    description: str = Field(description="Описание заявки")


class ApplicationInDB(BaseModel):
    id: int = Field(description="Айди заявки")
    user_name: str = Field(description="Имя пользователя")
    description: str = Field(description="Описание заявки")
    created_at: dt.datetime = Field(description="Дата и время создания")


T = TypeVar("T")


PaginationPage = CustomizedPage[
    Page[T],
    UseParamsFields(
        size=Query(
            settings.PAGINATION_SIZE_DEFAULT,
            ge=settings.PAGINATION_SIZE_MIN,
            le=settings.PAGINATION_SIZE_MAX,
            description="Размер страницы",
        ),
        page=Query(
            settings.PAGINATION_PAGE_MIN,
            description="Страница пагинации",
        ),
    ),
]