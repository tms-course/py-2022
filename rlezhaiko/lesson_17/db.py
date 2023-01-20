import os
from flask import g
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

basedir = os.path.abspath(os.path.dirname(__file__))     

"""
sqlite://file_name.sqlite
postgresql://user:password@host:port/dbname
mysql://user:password@host:port/dbname
oracle://user:password@host:port/dbname
"""
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'storage.db')}?check_same_thread=False"

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Session = scoped_session(
    sessionmaker(autocommit=False,
                 autoflush=False,
                 bind=engine))
Base = declarative_base()
Base.query = Session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)