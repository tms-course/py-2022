import datetime as dt
from sqlalchemy import Column, Integer, String, DateTime, Date
from db import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=True)
    last_name = Column(String(50), nullable=True)
    phone = Column(String(13), unique=True)
    birthday = Column(Date, nullable=True)
    created_at = Column(DateTime, default=dt.datetime.utcnow)