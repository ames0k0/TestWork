from pydantic import PostgresDsn, Field
from pydantic_settings import BaseSettings


# XXX: https://mimetype.io/audio/wav
SUPPORTED_RECORD_UPLOAD_FILE_TYPES: set[str] = {
    "audio/vnd.wav",
    "audio/vnd.wave",
    "audio/wave",
    "audio/x-pn-wav",
    "audio/x-wav",
}
# XXX: https://mimetype.io/audio/mp3
SUPPORTED_RECORD_RESPONSE_FILE_TYPE: str = "audio/mpeg"
SUPPORTED_RECORD_EXPORT_FILE_FORMAT = "mp3"


class Settings(BaseSettings):
    APP_HOST: str = "localhost"
    APP_PORT: int = 8000
    APP_RECORD_URL_TEMPLATE: str = (
        "http://{HOST}:{PORT}/record?id={RECORD_ID}&user={USER_ID}"
    )
    PG_DSN: PostgresDsn = Field(default=...)


settings = Settings()
