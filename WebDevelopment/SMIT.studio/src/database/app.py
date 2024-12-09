from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

from src.core import config


__all__ = (
    'Base',
    'SQL',
)


Base = declarative_base()


class SQL:
    engine = None
    session = None

    @classmethod
    def initialize(cls):
        cls.engine = create_engine(
            config.SQLALCHEMY_DATABASE_URL,
            connect_args={"check_same_thread": False},
        )
        cls.session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=cls.engine)
        )

        # Создание таблиц в базе
        Base.metadata.create_all(bind=cls.engine)
