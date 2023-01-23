import datetime as dt

from sqlalchemy import Column, Integer, String, Date, DATETIME
from sqlalchemy.orm import relationship

from db import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), unique=False)
    second_name = Column(String(50), unique=False)
    phone_number = Column(String(500), nullable=False)
    birth_date = Column(Date, nullable=True)
    registration_time = Column(DATETIME, nullable=False)

    def __repr__(self) -> str:
        return f"<users {self.id}>"
