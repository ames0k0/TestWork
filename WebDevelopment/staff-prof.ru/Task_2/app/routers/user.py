from fastapi import APIRouter, Query, status

from app import schemas
from app.sqldb import crud


router = APIRouter()


@router.post(
    "/",
    response_model=schemas.CreatedUserData,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    name: str = Query(..., description="Имя пользователя"),
) -> dict:
    return crud.User.create(name=name)
