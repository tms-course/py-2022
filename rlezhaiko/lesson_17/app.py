from flask import Flask, g, render_template, request
import datetime as dt
from models import Users
from db import Session
from datetime import date

app = Flask(__name__)

def get_db() -> Session:
    print('Getting db instance')
    if not hasattr(g, 'db'):
        g.db = Session()
    
    return g.db


@app.teardown_appcontext
def shutdown(error):
    print('Shutdown app', error)
    if hasattr(g, 'db'):
        g.db.close()


@app.route('/')
def index():
    users = []
    try:
        users = Users.query.all()
    except:
        print('Ошибка чтения')

    return render_template("index.html", title="Главная", list=users)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session = get_db()
        try:
            birthday_tmp = dt.datetime.strptime(request.form['birthday'], '%Y-%m-%d')
            u = Users(first_name=request.form['first_name'],
                      last_name=request.form['last_name'],
                      phone=request.form['phone'],
                      birthday=birthday_tmp)
            session.add(u)
            session.commit()
        except Exception as e:
            session.rollback()
            print('Ошибка добавления данных')
    return render_template('register.html', title="Регистрация")


@app.delete('/users/<int:id>')
def delete_user(id):
    session = get_db()
    try:
        Users.query.filter_by(id=id).delete()
        session.commit()
    except:
        session.rollback()
        return {}, 403

    return {}, 200


@app.route('/users/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    if request.method == 'POST':
        session = get_db()
        try:
            birthday_tmp = dt.datetime.strptime(request.form['birthday'], '%Y-%m-%d')
            user = Users.query.filter_by(id=id)
            data = dict(first_name =request.form['first_name'],
                        last_name=request.form['last_name'],
                        phone=request.form['phone'],
                        birthday=birthday_tmp)
            user.update(data)
            session.commit()
            return index()
        except Exception as e:
            session.rollback()
            print('Ошибка обновления данных')
            return {}, 403
    if request.method == 'GET':
        return render_template('update.html', title="Обновление данных", u=request.args)


if __name__ == '__main__':
    app.run(debug=True)