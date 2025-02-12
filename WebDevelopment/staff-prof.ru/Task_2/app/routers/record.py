import asyncio
from typing import Annotated

from pydantic import HttpUrl, UUID4, PositiveInt, AfterValidator
from fastapi import APIRouter, Query, Form, status, UploadFile, File
from fastapi.responses import Response

from app import schemas
from app.config import settings
from app.dependencies import parse_record_id_and_user_id
from app.sqldb import crud


router = APIRouter()


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
async def upload_record(
    id: Annotated[PositiveInt, Form(description="Идентификатор пользователя")],
    token: Annotated[UUID4, Form(description="Токен доступа")],
    file: Annotated[
        UploadFile,
        File(description="Аудиозапись в формате .wav"),
        AfterValidator(schemas.supported_record_file_ext),
    ],
):
    user = crud.User.get(id=id, token=token)
    if not user:
        raise NotImplementedError()

    # XXX: Конвертирует...
    await asyncio.sleep(2)

    record = crud.Record.create(
        user_id=user.id,
        filename=file.filename,
        file=(await file.read()),
    )

    return settings.APP_RECORD_URL_TEMPLATE.format(
        HOST=settings.APP_HOST,
        PORT=settings.APP_PORT,
        RECORD_ID=record.id,
        USER_ID=user.id,
    )


@router.get("")
async def download_record(
    url: HttpUrl = Query(description="URL для скачивание записи"),
) -> Response:
    record_id, user_id = parse_record_id_and_user_id(url=url)
    record = crud.Record.get(
        record_id=record_id,
        user_id=user_id,
    )
    return Response(
        content=record.file,
        media_type="audio/x-wav",
    )
