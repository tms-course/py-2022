from sqlalchemy import create_engine, select, \
    Table, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(engine)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    username: str = Column(String(64), unique=True, index=True)
    full_name: str = Column(String(256))
    password_hash: str = Column(String(256))

    def __repr__(self) -> str:
        return f'User({self.id}, {self.username})'
    
with engine.begin() as conn:
    Base.metadata.create_all(bind=conn)

with Session() as session:
    john = User(username='john',
                full_name='John Wick',
                password_hash='oiwjeofijwoeifj')
    sandra = User(username='Sandra',
                  full_name='Sandra Bullock',
                  password_hash='oijo32ij3r223')
    session.add_all([john, sandra])
    session.commit()

    query = select(User)
    res = session.execute(query).all()

    print(res)