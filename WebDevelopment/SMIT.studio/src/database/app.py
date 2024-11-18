from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

from src.core import config


Base = declarative_base()

engine = None
session = None


def initialize():
    global engine, session

    if engine is None:
        engine = create_engine(
            config.SQLALCHEMY_DATABASE_URL,
            connect_args={"check_same_thread": False},
        )

    if session is None:
        session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=engine)
        )


def get_engine():
    if engine is not None:
        return engine

    initialize()

    return engine


def get_session():
    if session is not None:
        return session

    initialize()

    return session