import os
import asyncio
from typing import Annotated

import sqlalchemy.orm as sao
from pydantic import UUID4, PositiveInt, AfterValidator
from fastapi import APIRouter, Query, Form, status, UploadFile, File, Depends
from fastapi.responses import Response

from app import schemas, dependencies, exceptions, config
from app.core import utils
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
    user = crud.User.get(
        id=id,
        token=str(token),
        session=session,
    )
    if not user:
        raise exceptions.UserIDOrTokenIsInvalid()

    loop = asyncio.get_running_loop()
    converted_file = await loop.run_in_executor(
        None,
        utils.convert_wav_to_mp3,
        await file.read(),
    )

    filename = file.filename
    if filename is None:
        # NOTE: Название файла, если она не задана
        filename = f"{user.id}.{config.SUPPORTED_RECORD_EXPORT_FILE_FORMAT}"
    else:
        filename, _ = os.path.splitext(file.filename)
        filename = f"{filename}.{config.SUPPORTED_RECORD_EXPORT_FILE_FORMAT}"

    record = crud.Record.create(
        user_id=user.id,
        filename=filename,
        file=converted_file,
        session=session,
    )

    return config.settings.APP_RECORD_URL_TEMPLATE.format(
        HOST=config.settings.APP_HOST,
        PORT=config.settings.APP_PORT,
        RECORD_ID=record.id,
        USER_ID=user.id,
    )


@router.get("")
async def download_record(
    id: Annotated[UUID4, Query(description="Идентификатор аудиозаписи")],
    user: Annotated[int, Query(description="Идентификатор пользователя")],
    session: sao.Session = Depends(dependency=dependencies.get_session),
) -> Response:
    """Скачивание аудизаписей по URL"""
    record = crud.Record.get(
        record_id=str(id),
        user_id=user,
        session=session,
    )
    if not record:
        raise exceptions.RecordIDOrUserIDIsInvalid()

    return Response(
        content=record.file,
        media_type=config.SUPPORTED_RECORD_RESPONSE_FILE_TYPE,
        headers={
            "Content-Disposition": f'attachment; filename="{record.filename}"',
        },
    )
