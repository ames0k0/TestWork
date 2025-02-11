from fastapi import FastAPI

from app.dependencies import lifespan
from app.routers import user, record


app = FastAPI(lifespan=lifespan)


app.include_router(
    user.router,
    prefix="/user",
    tags=["user"],
)
app.include_router(
    record.router,
    prefix="/record",
    tags=["record"],
)
