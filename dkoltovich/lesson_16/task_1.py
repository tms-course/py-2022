"""
1. Создать приложение при помощи фреймворка Flask, добавить эндпоинты для CRUD
(Create-Read-Update-Delete) операций над пользователями. Не нужно подключаться к
базе данных, достаточно того, чтобы каждый эндпоинт возвращал то, что от него ожи-
дается.
"""

from flask import Flask, request, abort


class UniqueUsernameError(Exception): ...
    
    
class InvalidId(Exception): ...


def is_username_unique(username: str) -> bool:
    """Checks if username is not already presented in db

    Args:
        username (str): username to be checked

    Raises:
        UniqueUsernameError: if username is not unique

    Returns:
        bool: True if username is unique
    """
    for user in users:
            if user['username'] == username: 
                raise UniqueUsernameError('Username is not unique')
    return True


users = [{'id': 1, 'username': 'John'},
         {'id': 2, 'username': 'Sarah'},
         {'id': 3, 'username': 'Martin'}
        ]


app = Flask(__name__)

@app.get('/users')
def show_users() -> list:
    return users

@app.post('/users')
def create_user() -> dict:
    """
    Args:
        username (str): username for user to be created. Defaults to Form().

    Returns:
        dict: created user's info
    """
    username = request.form['username']
    try:
        if is_username_unique(username):
            user = {'id': len(users) + 1, 'username': username}
            users.append(user)
            return user
    except UniqueUsernameError as e:
        abort(403,e.args)


@app.post('/users/<int:id>')
def update_user(id: int) -> dict:
    """
    Args:
        id (int): user's id
    Raises:
        InvalidId: if user's id is not present
        UniqueUsernameError: if new username is not unuqie
    Returns:
        dict: updated user's info
    """
    new_username = request.form['new_username']
    try:
        if is_username_unique(new_username):
            users[id - 1] = {'id': id, 'username': new_username}
            return users[id - 1]
    except UniqueUsernameError as e:
        abort(403,e.args)
    except IndexError:
        raise InvalidId('Invalid user id') from KeyError
    except InvalidId as e:
        abort(403,e.args)

    
@app.delete('/users/<int:id>')
def delete_user(id: int) -> dict:
    """
    Args:
        id (int): user's id

    Raises:
        InvalidId: if user's id is not present

    Returns:
        dict: deleted user's info
    """
    try:
        return users.pop(id - 1)
    except IndexError:
        raise InvalidId('Invalid user id') from IndexError
    except InvalidId as e:
        abort(403,e.args)
        
        
app.run(debug=True)