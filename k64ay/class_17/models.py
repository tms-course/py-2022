import datetime as dt

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True)
    password_hash = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=dt.datetime.utcnow)

    profile = relationship('Profiles', backref='users', uselist=False)

    def __repr__(self) -> str:
        return f"<users {self.id}>"


class Profiles(Base):
    __tablename__ = 'profiles'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    old = Column(Integer)
    city = Column(String(100))

    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self) -> str:
        return f"<profiles {self.id}>"
