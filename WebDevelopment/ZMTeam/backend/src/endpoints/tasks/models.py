from sqlalchemy import Column, DateTime, Integer, String, func

from ...sql.db import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    task_info = Column(String, nullable=False)
    datetime_to_do = Column(DateTime, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
