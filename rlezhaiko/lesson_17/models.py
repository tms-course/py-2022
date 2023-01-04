import datetime as dt

from sqlalchemy import Column, Integer, String, DateTime, Date
# from sqlalchemy.orm import relationship

from db import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(13), unique=True)
    birthday = Column(Date, nullable=False)
    created_at = Column(DateTime, default=dt.datetime.utcnow)