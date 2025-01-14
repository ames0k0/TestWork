import sqlalchemy as sa

from . import models


class Organization:
    @staticmethod
    def get_by_id(org_id: int, session: sa.Session):
        return session.scalar(
            sa.select(
                models.Organization
            ).where(
                models.Organization.id == org_id
            )
        )
