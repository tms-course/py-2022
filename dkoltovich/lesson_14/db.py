import os
import pymysql.cursors


def _get_connector():
    connect_args = {
        'host': os.getenv('MYSQL_HOST'),
        'port': int(os.getenv('MYSQL_PORT')),
        'user': os.getenv('MYSQL_USER'),
        'password': os.getenv('MYSQL_PASSWORD'),
        'db': os.getenv('MYSQL_DATABASE'),
        'cursorclass': pymysql.cursors.DictCursor,
    }

    connection = pymysql.connect(**connect_args)
    try:
        yield connection
    finally:
        print('Closing connection')
        connection.close()


connector = _get_connector()

