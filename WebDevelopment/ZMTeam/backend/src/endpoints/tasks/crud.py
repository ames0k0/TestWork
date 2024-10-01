from datetime import datetime

from sqlalchemy.orm import Session

from . import models, schemas


def get_task(db: Session, task_id: int):
    return db.query(
        models.Tasks
    ).filter(
        models.Tasks.id == task_id,
    ).first()


def get_all_tasks(db: Session):
    return db.query(
        models.Tasks
    ).order_by(
        models.Tasks.id.desc()
    ).all()


def create_task(db: Session, data: schemas.TaskCreateIn):
    task = models.Tasks(
        task_info=data.task_info,
        datetime_to_do=data.datetime_to_do,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def update_task(db: Session, task_id: int, data: schemas.TaskUpdateIn):
    task = get_task(db, task_id)
    if task is None:
        return task

    # XXX: 4.3 "и/или"
    if data.task_info:
        task.task_info = data.task_info
    task.datetime_to_do = data.datetime_to_do
    task.update_dt = datetime.now()

    db.commit()
    db.refresh(task)

    return task
