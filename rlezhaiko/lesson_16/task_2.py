""" 
2. Создать приложение при помощи фреймворка fastAPI, добавить эндпоинты для CRUD
(Create-Read-Update-Delete) операций над пользователями. Не нужно подключаться к
базе данных, достаточно того, чтобы каждый эндпоинт возвращал то, что от него ожи-
дается.
"""
from fastapi import FastAPI
import uvicorn
from fastapi.responses import JSONResponse


simple_db = {1: {'username': 'JohnWick'},
             2: {'username': 'SandraBullok'},
             3: {'username': 'Morty123'}}

app = FastAPI()


@app.get("/users")
def read_users() -> dict:
    return simple_db


@app.post("/users")
def create_user(username: str) -> str:
    """ 
    :param username: username in string format 
    """
    keys = list(simple_db.keys())
    cursor = max(keys) + 1
    simple_db[cursor] = simple_db.get(cursor, {"username": username})
    print(simple_db[cursor])
    print(type(simple_db[cursor]))
    return JSONResponse(content=simple_db[cursor])


@app.delete("/users/{id}")
def delete_user(id: int) -> str:
    """ 
    :param id: id of user which need to delete 
    """
    try:
        simple_db.pop(id)
        return JSONResponse(content={"message": "Success", "errors": None})
    except KeyError:
        return JSONResponse(content={"message": "Failure", "errors": 'There is no user with given id'}, status_code=404)


@app.post("/users/{id}")
def update_user(id: int, new_username: str) -> str:
    """ 
    :param id: id of user which need to update
    :param new_username: username in string format 
    """
    try:
        simple_db[id]['username'] = new_username
        return JSONResponse(content={"message": "Success", "errors": None})
    except KeyError:
        return JSONResponse(content={"message": "Failure", "errors": 'There is no user with given id'}, status_code=404)


if __name__ == '__main__':
    uvicorn.run("task_2:app", host="127.0.0.1", port=5000, log_level="info")