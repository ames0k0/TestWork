import asyncio
from typing import Annotated

import sqlalchemy.orm as sao
from pydantic import HttpUrl, UUID4, PositiveInt, AfterValidator
from fastapi import APIRouter, Query, Form, status, UploadFile, File, Depends
from fastapi.responses import Response

from app import schemas, dependencies, exceptions
from app.config import settings, SUPPORTED_RECORD_RESPONSE_FILE_TYPE
from app.dependencies import parse_record_id_and_user_id
from app.sqldb import crud


router = APIRouter(
    prefix="/record",
    tags=["record"],
)


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
    session: sao.Session = Depends(dependency=dependencies.get_session),
) -> str:
    """Загрузка аудиозаписи"""
    user = crud.User.get(id=id, token=token, session=session)
    if not user:
        raise exceptions.UserIDOrTokenIsInvalid()

    # XXX: Конвертирует...
    await asyncio.sleep(2)

    record = crud.Record.create(
        user_id=user.id,
        filename=file.filename,
        file=(await file.read()),
        session=session,
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
    session: sao.Session = Depends(dependency=dependencies.get_session),
) -> Response:
    """Скачивание аудизаписей по URL"""
    record_id, user_id = parse_record_id_and_user_id(url=url)
    record = crud.Record.get(
        record_id=record_id,
        user_id=user_id,
        session=session,
    )
    if not record:
        raise exceptions.RecordIDOrUserIDIsInvalid()

    return Response(
        content=record.file,
        media_type=SUPPORTED_RECORD_RESPONSE_FILE_TYPE,
    )
