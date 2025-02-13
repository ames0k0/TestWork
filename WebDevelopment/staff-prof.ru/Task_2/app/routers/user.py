import sqlalchemy.orm as sao
from fastapi import APIRouter, Query, Depends, status

from app import schemas, dependencies
from app.sqldb import crud


router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post(
    "/",
    response_model=schemas.CreatedUserData,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    name: str = Query(..., description="Имя пользователя"),
    session: sao.Session = Depends(dependency=dependencies.get_session),
):
    """Создание пользователя"""
    return crud.User.create(name=name, session=session)
