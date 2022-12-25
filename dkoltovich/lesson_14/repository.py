from dotenv import load_dotenv
from db import connector


load_dotenv()
db = next(connector)


class Table:
    @staticmethod
    def login(username: str, first_name: str, last_name: str):
        with db.cursor() as cursor:
            query = "INSERT INTO users (username, first_name, last_name) VALUES(%s,%s,%s)"
            cursor.execute(query, (username, first_name, last_name))
            db.commit()

    @staticmethod
    def edit_user(username: str, field_to_change: str, new_value: str):
        with db.cursor() as cursor:
            query = "UPDATE users SET {}={} WHERE username='{}'"\
                .format(field_to_change, new_value, username)
            print(query)
            cursor.execute(query)
            cursor.commit()

    @staticmethod
    def delete_user(username: str):
        with db.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE username='{}'".format(username))
            cursor.commit()

