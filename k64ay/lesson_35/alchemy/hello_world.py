from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///:memory', echo=True)

with engine.connect() as conn:
    res = conn.execute(text('SELECT "hello world"')).scalar()
    print(res)
    
