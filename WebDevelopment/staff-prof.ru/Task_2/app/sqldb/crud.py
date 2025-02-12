import sqlalchemy as sa

from app.sqldb import Postgres, models


class User:
    """User model curd"""

    @staticmethod
    def create(name: str) -> models.User:
        """Создание пользователя"""
        user = models.User(name=name)
        Session = Postgres.get_scoped_session()

        with Session().begin():
            Session.add(user)

        return user

    @staticmethod
    def get(id: int, token: str) -> models.User | None:
        """Получение записи"""
        Session = Postgres.get_scoped_session()
        with Session() as session:
            return session.scalar(
                sa.select(models.User).where(
                    models.User.id == id,
                    models.User.token == token,
                )
            )


class Record:
    """Record model crud"""

    @staticmethod
    def create(user_id: int, filename: str, file: bytes) -> models.Record:
        """Сохранение записи"""
        record = models.Record(
            filename=filename,
            file=file,
            user_id=user_id,
        )
        Session = Postgres.get_scoped_session()

        with Session().begin():
            Session.add(record)

        return record

    @staticmethod
    def get(record_id: str, user_id: int) -> models.Record | None:
        """Получение записи"""
        Session = Postgres.get_scoped_session()
        with Session() as session:
            return session.scalar(
                sa.select(models.Record).where(
                    models.Record.id == record_id,
                    models.Record.user_id == user_id,
                )
            )
