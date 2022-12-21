from dotenv import load_dotenv
from db import connector

load_dotenv()

db = next(connector)

with db.cursor() as cursor:
    query = "INSERT INTO users (username, first_name, last_name) VALUES(%s,%s,%s)"

    cursor.execute(query, ('akarpovich', 'Aliaksandr', 'Karpovich'))
    db.commit()

    cursor.execute("SELECT * FROM users")
    result = cursor.fetchmany()
    print(result)
