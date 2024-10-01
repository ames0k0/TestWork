from typing import Annotated

from fastapi import HTTPException, Header

from ..sql.db import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def verify_jwt_token(
        x_jwt_token: Annotated[str, Header()] = "fake-super-secret-token"
):
    if x_jwt_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-JWT-Token header invalid")
