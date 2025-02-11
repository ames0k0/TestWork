from fastapi import APIRouter, Query


router = APIRouter()


@router.post("/")
async def create_user(
    username: str = Query(..., description="Имя пользователя"),
):
    # TODO: add user to db
    return [{"username": "Rick"}, {"username": "Morty"}]
