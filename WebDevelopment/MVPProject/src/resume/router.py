from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, UploadFile, File, status
from fastapi_pagination import Page

from ..dependencies import get_db
from . import schemas, crud, enums, utils


resume = APIRouter()


@resume.post(
    path="/upload/",
    response_model=schemas.ResumeInDB,
    status_code=status.HTTP_201_CREATED,
    description="Принимает файл и имя претендента, сохраняет их",
)
async def upload(
        username: str,
        file: UploadFile = File(description="Файл"),
        db: Session = Depends(get_db)
) -> schemas.ResumeInDB:
    """ Returns the created Resume
    """
    filepath = await utils.save_resume_file(file)
    return crud.create_resume(
        db,
        username=username,
        filepath=filepath,
    )


@resume.post(
    path="/vote/",
    response_model=schemas.ResumeInDB,
    status_code=status.HTTP_200_OK,
    description="Увеличивает голоса к резюме",
)
async def vote(
        resume_id: int, db: Session = Depends(get_db)
) -> schemas.ResumeInDB:
    """ Returns the updated Resume
    """
    return crud.increment_vote(db, resume_id)


@resume.delete(
    path="/delete/{resume_id}/",
    response_model=str,
    status_code=status.HTTP_200_OK,
    description="Удаляет резюме из базы и удаляет файл",
)
async def delete(
        resume_id: int, db: Session = Depends(get_db)
) -> str:
    """ Deletes the Resume by id

    Returns OK
    """
    crud.delete(db, resume_id)
    return "OK"


@resume.get(
    path="/list/",
    response_model=Page[schemas.ListOut],
    status_code=status.HTTP_200_OK,
    description="Выводит пагинированный список резюме",
)
async def get_all_paginated(
        db: Session = Depends(get_db),
        order_by: enums.PaginationOrder = enums.PaginationOrder.CREATED_AT,
) -> Page[schemas.ListOut]:
    """ Returns paginated Resume
    """
    return crud.get_all_paginated(db, order_by)
