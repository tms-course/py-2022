from sqlalchemy import create_engine, select, \
    Table, Column, Integer, String,  MetaData
    
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///:memory', echo=True)
Session = sessionmaker(engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id: int = Column(Integer, primary_key=True)
    username: str = Column(String(64), unique=True,index=True)
    full_name: str = Column(String(64))
    password_hash: str = Column(String(256))
    
    def __repr__(self) -> str:
        return f'User({self.id}, {self.username})'
    
with engine.begin() as conn:
    Base.metadata.create_all(bind=conn)
    
with Session() as session:
    john = User(
        username='John',
        full_name='John Wick',
        password_hash='4r3wcefqewf'
    )
    sandra = User(
        username='Sandra',
        full_name='SANDRA Bullock',
        password_hash='ernwofiuneo43'
    )
    session.add_all([john, sandra])
    session.commit()
    
    query = select(User)
    #query = select(User).where(username='John')
    res = session.execute(query).all()
    
    print(res)