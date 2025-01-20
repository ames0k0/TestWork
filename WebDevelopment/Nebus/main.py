from contextlib import asynccontextmanager

from fastapi import FastAPI

from src import connections
from src.app import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    connections.Sqlite.initialize()
    yield


app = FastAPI(
    title="Nebus",
    summary="Справочника Организаций, Зданий, Деятельности",
    lifespan=lifespan,
)

app.include_router(
    router=router,
    prefix='/organization',
    tags=['Организация'],
)
