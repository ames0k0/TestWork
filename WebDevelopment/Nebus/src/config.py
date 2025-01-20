from pathlib import Path

from pydantic import (
    computed_field,
)
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    STATIC_DIRECTORY: Path = Path("../static").mkdir(exist_ok=True)
    DATABASE_FILEPATH: Path = STATIC_DIRECTORY / "db.sqlite3"

    @computed_field
    @property
    def sqlalchemy_database_uri(self) -> str:
        return "sqlite://" + self.DATABASE_FILEPATH.as_uri()


settings = Settings()
