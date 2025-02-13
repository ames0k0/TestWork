import uvicorn
from fastapi import FastAPI

from app.config import settings
from app.dependencies import lifespan
from app.routers import routers


app = FastAPI(
    lifespan=lifespan,
    title="staff-prof.ru",
    summary="Музыкальный веб сервис",
    description="Пользователям доступно загрузки и отгрузки аудиозаписей",
)

for router in routers:
    app.include_router(router=router)


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host=settings.APP_HOST,
        port=settings.APP_PORT,
    )
