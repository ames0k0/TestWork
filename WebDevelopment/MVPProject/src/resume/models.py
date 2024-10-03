from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from src.database import Base


class Resume(Base):
    __tablename__ = "resume"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    vote_count = Column(Integer, nullable=False, server_default="0")

    # Settings
    created_at = Column(DateTime(timezone=True), server_default=func.now())
