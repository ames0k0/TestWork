import sqlalchemy as sa
import sqlalchemy.orm as sao

from .config import settings
from .models import Base


class Sqlite:
    engine: sa.Engine
    session_factory: sao.sessionmaker

    @classmethod
    def initialize(cls):
        cls.engine = sa.create_engine(settings.sqlalchemy_database_uri)
        cls.session_factory = sao.sessionmaker(bind=cls.engine)
        # TODO: move to alembic
        Base.metadata.create_all(cls.engine)

    @classmethod
    def get_scoped_session(cls):
        return sao.scoped_session(
            session_factory=cls.session_factory
        )