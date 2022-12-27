from fastapi import FastAPI
import uvicorn

simple_db = {1: {'username': 'JohnWick'},
             2: {'username': 'SandraBullok'},
             3: {'username': 'Morty123'}}
cursor = 4

app = FastAPI()


@app.get("/users")
def read_users():
    return simple_db


@app.post("/users")
def create_user(username: str):
    return 'User successfully created'


@app.delete("/users/{id}")
def delete_user(id: int):
    if id in simple_db:
        simple_db.pop(id)
        return 'User successfully deleted'
    else:
        return 'There is no user with given id'


@app.post("/users/{id}")
def update_user(id: int, new_username: str):
    return simple_db


if __name__ == '__main__':
    uvicorn.run("task_2:app", host="127.0.0.1", port=5000, log_level="info")