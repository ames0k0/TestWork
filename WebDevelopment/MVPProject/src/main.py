from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_pagination import LimitOffsetPage, Page, add_pagination

from src.config import settings
from src.lifespan import lifespan
from src.resume.router import resume


def get_app() -> FastAPI:
    """ Creates and Returns the FastAPI application
    """
    app = FastAPI(
        lifespan=lifespan,
        title=settings.PROJECT_TITLE,
        description=settings.PROJECT_DESCRIPTION,
    )

    app.mount(
        path="/" + settings.PROJECT_STATICFILES_DIR.name,
        app=StaticFiles(
            directory=settings.PROJECT_STATICFILES_DIR.name
        ),
    )

    app.include_router(resume, tags=["resume"])

    add_pagination(app)

    return app