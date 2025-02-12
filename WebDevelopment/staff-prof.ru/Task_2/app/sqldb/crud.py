from app.sqldb import Postgres, models


class User:
    """User model curd"""

    @staticmethod
    def create(name: str) -> models.User:
        user = models.User(name=name)
        Session = Postgres.get_scoped_session()

        with Session().begin():
            Session.add(user)

        return user


class Record:
    pass
