from typing import Annotated

from pydantic import HttpUrl
from fastapi import APIRouter, Query, Form

from app import schemas
from app.dependencies import parse_record_id_and_user_id


router = APIRouter()


@router.post("")
async def upload_record(
    data: Annotated[schemas.UploadRecordFormData, Form()],
):
    # TODO: convert
    # TODO: SAVE to db
    return data


@router.get("")
async def download_record(
    url: HttpUrl = Query(description="URL для скачивание записи"),
):
    record_id, user_id = parse_record_id_and_user_id(url=url)
    # TODO: stream downloaded record
    return {
        "record_id": record_id,
        "user_id": user_id,
    }
