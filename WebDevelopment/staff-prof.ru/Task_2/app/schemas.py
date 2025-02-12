import os
from typing import Annotated

from pydantic import (
    BaseModel,
    Field,
    BeforeValidator,
)
from fastapi import UploadFile

from app.config import SUPPORTED_RECORD_FILE_TYPES


class CreatedUserData(BaseModel):
    """Данные созданного пользователя"""

    id: int = Field(..., description="Идентификатор пользователя")
    token: Annotated[str, BeforeValidator(lambda x: str(x))] = Field(
        ..., description="Токен доступа"
    )


def supported_record_file_ext(v: UploadFile):
    # NOTE: not used `v.content_type` which is `` for me
    if v.content_type not in SUPPORTED_RECORD_FILE_TYPES:
        raise ValueError(f"File type: `{v.content_type}` is not supported!")

    return v
