import uvicorn

from src.config import settings
from src.main import get_app
from src.lifespan import create_static_dirs


def start_up():
    create_static_dirs()


if __name__ == "__main__":
    start_up()

    uvicorn.run(
        get_app(),
        host=settings.PROJECT_HOST,
        port=settings.PROJECT_PORT,
    )
