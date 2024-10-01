import uvicorn

from src.main import app
from src.core.config import settings


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.PROJECT_HOST,
        port=settings.PROJECT_PORT,
    )