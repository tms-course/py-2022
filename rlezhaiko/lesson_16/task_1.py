"""
1. Создать приложение при помощи фреймворка Flask, добавить эндпоинты для CRUD
(Create-Read-Update-Delete) операций над пользователями. Не нужно подключаться к
базе данных, достаточно того, чтобы каждый эндпоинт возвращал то, что от него ожи-
дается.
"""
from flask import Flask, request

simple_db = {1: {'username': 'JohnWick'},
             2: {'username': 'SandraBullok'},
             3: {'username': 'Morty123'}}

app = Flask(__name__)


@app.route('/users', methods=['GET', 'POST'])
def create_read_users(username: str = None) -> dict:
    """ 
    :param username: username in integer format 
    """
    if request.method == 'GET':
        return simple_db
    elif request.method == 'POST':
        username = request.args['username']
        keys = list(simple_db.keys())
        cursor = max(keys) + 1
        simple_db[cursor] = simple_db.get(cursor, {"username": username})
        return simple_db[cursor]


@app.route('/users/<int:id>', methods=['DELETE', 'POST'])
def update_delete_users(id: int) -> str:
    """ 
    :param id: id of user which need to update or delete 
    """
    if request.method == 'DELETE':
        try:
            print(id)
            simple_db.pop(id)
        except KeyError:
            return {"message": "Failure", "errors": 'There is no user with given id'}
    elif request.method == 'POST':
        try:
            simple_db[id]['username'] = request.args['new_username']
        except KeyError:
            return {"message": "Failure", "errors": 'There is no user with given id'}

    return {"message": "Success", "errors": None}


if __name__ == '__main__':
    app.run(debug=True)