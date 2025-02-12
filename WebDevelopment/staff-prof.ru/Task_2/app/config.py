from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PG_DSN: PostgresDsn


settings = Settings()
