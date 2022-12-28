import os
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

engine = create_engine(f"sqlite:///{os.path.join(basedir, 'storage.db')}", echo=True)
Session = scoped_session(
    sessionmaker(autocommit=False,
                 autoflush=False,
                 bind=engine))
Base = declarative_base()
Base.query = Session.query_property()

session = Session()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)
