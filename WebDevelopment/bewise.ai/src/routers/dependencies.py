from typing import Annotated

from pydantic import constr
from fastapi import Query

from src.core.config import settings


def filter_params(
    user_name: Annotated[
        constr(
            strip_whitespace=True,
            min_length=settings.FILTER_NAME_MIN_LENGTH,
        ) | None,
        Query(description="Имя пользователя"),
    ] = None,
) -> dict:
    """Параметры фильтрации
    """
    return {
        "user_name": user_name,
    }