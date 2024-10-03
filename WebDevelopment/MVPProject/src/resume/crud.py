import os.path
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

from . import models, enums, schemas


def create_resume(
        db: Session, username: str, filepath: Path
) -> models.Resume:
    """ Returns created Resume
    """
    resume = models.Resume(
        username=username,
        filepath=filepath.absolute().as_posix(),
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return resume


def get_by_id(
        db: Session, resume_id: int
) -> models.Resume | None:
    """ Returns Resume or None
    """
    return db.query(
        models.Resume
    ).filter(
        models.Resume.id == resume_id
    ).first()


def increment_vote(
        db: Session, resume_id: int
) -> models.Resume:
    """ Returns a Resume, increments `vote_count`

    raises an Exception for a missing Resume
    """
    resume = get_by_id(db, resume_id)

    if resume is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Resume(id={resume_id}) not found!"
        )

    resume.vote_count += 1
    db.commit()
    db.refresh(resume)

    return resume


def delete(db: Session, resume_id: int) -> None:
    """ Deletes a Resume with the attached file

    raises an Exception for a missing Resume
    """
    resume = get_by_id(db, resume_id)

    if resume is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Resume(id={resume_id}) not found!"
        )

    if os.path.exists(resume.filepath):
        os.remove(resume.filepath)

    db.delete(resume)
    db.commit()


def get_all_paginated(
        db: Session, order_by: enums.PaginationOrder
) -> Page[schemas.ListOut]:
    """ Returns Paginated query result
    """
    q = select(models.Resume)

    if order_by == enums.PaginationOrder.CREATED_AT:
        q = q.order_by(models.Resume.created_at.desc())
    if order_by == enums.PaginationOrder.VOTE_COUNT:
        q = q.order_by(models.Resume.vote_count.desc())

    return paginate(
        db, q
    )
