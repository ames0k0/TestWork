from datetime import datetime

from pydantic import BaseModel, Field


class TaskCreateIn(BaseModel):
    task_info: str = Field(description="Информация о задаче")
    datetime_to_do: datetime = Field(
        description="Предполагаемая дата выполнения задачи"
    )


class TaskUpdateIn(BaseModel):
    task_info: str | None = Field(None, description="Информация о задаче")
    datetime_to_do: datetime = Field(
        description="Предполагаемая дата выполнения задачи"
    )


class TaskInDB(BaseModel):
    id: int = Field(description="ID Задачи")
    task_info: str = Field(description="Информация о задаче")
    datetime_to_do: datetime = Field(
        description="Предполагаемая дата выполнения задачи"
    )
    created_at: datetime = Field(description="Дата создания задачи")
    updated_at: datetime | None = Field(description="Дата обновления задачи")
