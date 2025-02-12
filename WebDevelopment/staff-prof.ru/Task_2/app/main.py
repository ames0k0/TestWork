from fastapi import FastAPI

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
