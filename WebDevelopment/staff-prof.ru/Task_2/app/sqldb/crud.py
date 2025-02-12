import sqlalchemy as sa
import sqlalchemy.orm as sao

from app.sqldb import models


class User:
    """User model curd"""

    @staticmethod
    def create(name: str, session: sao.Session) -> models.User:
        """Создание пользователя"""
        user = models.User(name=name)

        with session.begin():
            session.add(user)

        return user

    @staticmethod
    def get(id: int, token: str, session: sao.Session) -> models.User | None:
        """Получение записи"""
        return session.scalar(
            sa.select(models.User).where(
                models.User.id == id,
                models.User.token == token,
            )
        )


class Record:
    """Record model crud"""

    @staticmethod
    def create(
        user_id: int,
        filename: str,
        file: bytes,
        session: sao.Session,
    ) -> models.Record:
        """Сохранение записи"""
        record = models.Record(
            filename=filename,
            file=file,
            user_id=user_id,
        )
        session.add(record)
        session.commit()

        return record

    @staticmethod
    def get(
        record_id: str,
        user_id: int,
        session: sao.Session,
    ) -> models.Record | None:
        """Получение записи"""
        return session.scalar(
            sa.select(models.Record).where(
                models.Record.id == record_id,
                models.Record.user_id == user_id,
            )
        )
