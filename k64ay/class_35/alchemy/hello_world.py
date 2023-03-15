from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///:memory:', echo=True)

with engine.connect() as conn:
    query = text('SELECT "hello, world!"')
    res = conn.execute(query).scalar()
    print(res)