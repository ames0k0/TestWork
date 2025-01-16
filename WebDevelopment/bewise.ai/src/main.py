from fastapi import FastAPI
from fastapi_pagination import add_pagination

from src.core import dependencies
from src.routers import application


app = FastAPI(
    title="bewise.ai",
    summary="Сервис для обработки заявок пользователей",
    lifespan=dependencies.lifespan,
)
app.include_router(
    router=application.router,
    prefix='/applications',
    tags=['Заявки'],
)

add_pagination(app)
