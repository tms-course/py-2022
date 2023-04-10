from sqlalchemy import create_engine, text
engine = create_engine('sqlite:///:memory:', echo=True)

with engine.connect() as session:
    res = session.execute(text('select "Hello, world!"')).scalar()
    print(res)