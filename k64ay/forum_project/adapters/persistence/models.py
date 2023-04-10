from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from .db import Base


class Message(Base):
    __tablename__ = 'messages'

    id: int = Column(Integer, primary_key=True)
    author_id: int = Column(Integer, nullable=False, default=1)
    text: str = Column(String, nullable=False)
    created_at: datetime = Column(DateTime, 
                                  nullable=False, 
                                  default=datetime.utcnow)
