from pathlib import Path

from pydantic import (
    PostgresDsn,
    computed_field,
)
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./secret/.env-backend",
        env_ignore_empty=True,
        extra="ignore",
    )
    PROJECT_HOST: str
    PROJECT_PORT: int
    PROJECT_TITLE: str
    PROJECT_DESCRIPTION: str
    PROJECT_STATICFILES_DIR: Path = Path("static")
    PROJECT_RESUME_FILES_DIR: Path = PROJECT_STATICFILES_DIR / "resume"
    PROJECT_TAGS_METADATA: list[dict] = [
        {
            "name": "resume",
            "description": "Резюме",
        },
    ]

    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg2",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )


settings = Settings()