from fastapi import (
   APIRouter, Depends, status,
   HTTPException,
)

from sqlalchemy.orm import Session

from ...core.dependencies import get_db
from . import schemas, crud


router = APIRouter()


@router.post(
   "/create",
   response_model=schemas.TaskInDB,
   status_code=status.HTTP_201_CREATED,
   description="Создание задачи",
)
async def create_task(data: schemas.TaskCreateIn, db: Session = Depends(get_db)):
   # Add error handle ?
   return crud.create_task(db, data)


@router.get(
   "/list",
   response_model=list[schemas.TaskInDB],
   status_code=status.HTTP_200_OK,
   description="Предоставляет весь список задач",
)
async def task_list(db: Session = Depends(get_db)):
   return crud.get_all_tasks(db)


@router.get(
   "/{task_id}",
   response_model=schemas.TaskInDB,
   status_code=status.HTTP_200_OK,
   description="Данные по конкретной задаче",
)
async def get_task(
        task_id: int, db: Session = Depends(get_db)
) -> schemas.TaskInDB:
   task = crud.get_task(db, task_id)
   if task is not None:
      return task
   raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="Задача не найдена"
   )


@router.patch(
   "/{task_id}/update",
   response_model=schemas.TaskInDB,
   status_code=status.HTTP_201_CREATED,
   description="Обновление данные задачи",
)
async def update_task(
        task_id: int, data: schemas.TaskUpdateIn, db: Session = Depends(get_db)
) -> schemas.TaskInDB:
   task = crud.update_task(db, task_id, data)
   if task is not None:
      return task
   raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="Задача не найдена"
   )
