import os

from pydantic import (
    BaseModel,
    computed_field,
)
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Postgres(BaseModel):
    SERVER: str
    PORT: int
    USER: str
    PASSWORD: str
    DB: str

    @computed_field
    @property
    def database_uri(self) -> str:
        return str(
            MultiHostUrl.build(
                scheme="postgresql+asyncpg",
                username=self.USER,
                password=self.PASSWORD,
                host=self.SERVER,
                port=self.PORT,
                path=self.DB,
            )
        )


class Settings(BaseSettings):
    if not os.environ.get("POSTGRES__SERVER"):
        model_config = SettingsConfigDict(
            env_file='deploy/secrets/.env-local',
            env_ignore_empty=True,
            extra="ignore",
            env_nested_delimiter="__",
        )

    FILTER_NAME_MIN_LENGTH: int = 1

    PAGINATION_PAGE_MIN: int = 1
    PAGINATION_SIZE_MIN: int = 1
    PAGINATION_SIZE_MAX: int = 100
    PAGINATION_SIZE_DEFAULT: int = 20

    postgres: Postgres


settings = Settings()
