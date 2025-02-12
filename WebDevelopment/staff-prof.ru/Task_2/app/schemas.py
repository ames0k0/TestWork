from typing import Annotated

from pydantic import BaseModel, Field, BeforeValidator, UUID4
from fastapi import Query, UploadFile


class CreatedUserData(BaseModel):
    """Данные созданного пользователя"""

    id: int = Field(..., description="Идентификатор пользователя")
    token: Annotated[str, BeforeValidator(lambda x: str(x))] = Field(
        ..., description="Токен доступа"
    )


class UploadRecordFormData(BaseModel):
    """Входные данные для добавление аудиозаписи"""

    id: int = Query(description="Идентификатор пользователя")
    token: UUID4 = Query(description="Токен доступа")
    file: UploadFile

    model_config = {"extra": "forbid"}
