from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends

from .endpoints.main import api_router
from .core.config import settings
from .core.dependencies import verify_jwt_token
from .sql import db


@asynccontextmanager
async def lifespan(_: FastAPI):
    db.Base.metadata.create_all(bind=db.engine)
    yield


app = FastAPI(
    openapi_tags=settings.PROJECT_TAGS_METADATA,
    title=settings.PROJECT_TITLE,
    description=settings.PROJECT_DESCRIPTION,
    lifespan=lifespan,
    dependencies=[Depends(verify_jwt_token)],
    swagger_ui_parameters={
        # "docExpansion": None,
    }
)

app.include_router(api_router)