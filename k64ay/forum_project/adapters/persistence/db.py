from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from settings import DATABASE_URI

Base = declarative_base()
engine = create_async_engine(DATABASE_URI, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


