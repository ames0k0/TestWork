import celery
import redis
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from .config import settings
from .models import Base


class Celery:
    ins: celery.Celery

    @classmethod
    def initialize(cls):
        cls.ins = celery.Celery(
            broker=settings.celery_broker_url,
        )
        cls.ins.conf.broker_connection_retry_on_startup = True


class Postgres:
    engine: Engine
    session_factory: sessionmaker

    @classmethod
    def initialize(cls):
        cls.engine = create_engine(str(
            settings.sqlalchemy_database_uri
        ))
        cls.session_factory = sessionmaker(
            cls.engine,
            expire_on_commit=False,
        )
        Base.metadata.create_all(cls.engine)

    @classmethod
    def get_scoped_session(cls):
        return scoped_session(
            session_factory=cls.session_factory
        )


class Redis:
    ins: redis.Redis

    @classmethod
    def initialize(cls):
        cls.ins = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
        )
