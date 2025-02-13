from sqlalchemy import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.config import settings
from app.sqldb import models


class Postgres:
    engine: Engine
    session_factory: sessionmaker

    @classmethod
    def initialize(cls):
        cls.engine = create_engine(url=str(settings.PG_DSN))
        cls.session_factory = sessionmaker(
            bind=cls.engine,
            expire_on_commit=False,
        )
        models.Base.metadata.create_all(cls.engine)

    @classmethod
    def get_scoped_session(cls) -> scoped_session:
        return scoped_session(cls.session_factory)

    @classmethod
    def terminate(cls):
        cls.session_factory.close_all()
