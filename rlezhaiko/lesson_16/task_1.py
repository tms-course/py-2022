from flask import Flask, request

app = Flask(__name__)


@app.route('/users', methods=['GET', 'POST'])
def create_read_users():
    if request.method == 'GET':
        return '<p>Hello GET</p>'
    elif request.method == 'POST':
        return '<p>Hello POST</p>'


@app.route('/users/<id>', methods=['GET', 'POST'])
def update_delete_users(id):
    if request.method == 'GET':
        return '<p>Hello GET {id}</p>'
    elif request.method == 'POST':
        return '<p>Hello POST {id}</p>'