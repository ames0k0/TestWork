from typing import Annotated

from pydantic import BaseModel, HttpUrl
from fastapi import APIRouter, Query, UploadFile, Form


router = APIRouter()


class UploadRecordFormData(BaseModel):
    """Входные данные для добавление аудиозаписи"""

    id: int = Query(description="Идентификатор пользователя")
    token: str = Query(description="Токен доступа")
    file: UploadFile

    model_config = {"extra": "forbid"}


@router.post("")
async def upload_record(
    data: Annotated[UploadRecordFormData, Form()],
):
    # TODO: convert
    # TODO: SAVE to db
    return data


@router.get("")
async def download_record(
    url: HttpUrl = Query(description="URL для скачивание записи"),
):
    # TODO: stream downloaded record
    return url
