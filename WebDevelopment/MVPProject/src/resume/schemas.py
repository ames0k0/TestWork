from datetime import datetime

from pydantic import BaseModel, Field


class ResumeInDB(BaseModel):
    id: int = Field(description="ID Резюме")
    username: str = Field(description="Наименование")
    filepath: str = Field(description="Путь к файлу")
    vote_count: int = Field(description="Рейтинг")
    created_at: datetime = Field(description="Время создание")


class ListOut(BaseModel):
    username: str = Field(description="Наименование")
    filepath: str = Field(description="Путь к файлу")
    vote_count: int = Field(description="Рейтинг")
