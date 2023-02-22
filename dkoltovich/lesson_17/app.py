"""
1. Создать приложение для регистрации на мероприятие используя фреймворк Flask. 
Подключить базу данных используя SQLAlchemy, в которой будет храниться только 
список всех участников. От участников нам необходимо знать имя, фамилию, телефон, 
дату рождения и время регистрации. Каждый может получить список всех участников,
отменить свою регистрацию по номеру телефона, изменить данные.
"""


from flask import Flask, g, render_template, request, redirect, url_for

from db import Session
from models import Users
import datetime as dt

app = Flask(__name__)

def get_db() -> Session:
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
        return {}, 500

    return render_template("index.html", title="Список участников", list=users)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        session = get_db()
        try:
            u = Users(
                first_name=request.form['first_name'],
                second_name=request.form['second_name'],
                phone_number=request.form['phone_number'],
                birth_date=dt.date.fromisoformat(request.form['birth_date']),
                registration_time=dt.datetime.now()
                )      
            session.add(u)
            session.commit()
        except Exception as e:
            session.rollback()
            return {}, 403
        
        return redirect(url_for('index'))
    
    return render_template('register.html', title="Регистрация")


@app.route('/users/delete', methods=['POST', 'GET'])
def delete_user():
    if request.method == 'POST':
        session = get_db()
        try:
            user = Users.query.filter_by(phone_number=request.form['phone_number']).delete()
            session.commit()
        except:
            return {}, 403
    
        return redirect(url_for('index'))
    
    return render_template('delete_user.html', )


@app.route('/users/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    session = get_db()
    try:
        user = Users.query.filter_by(id=id).first()
    except:
        return {}, 403

    if request.method == 'POST':
        try:
            user.first_name = request.form['first_name']
            user.second_name = request.form['second_name']
            user.phone_number = request.form['phone_number']
            user.birth_date = dt.date.fromisoformat(request.form['birth_date'])
            session.commit()
        except:
            session.rollback()
            return {}, 403
        
        return redirect(url_for('index'))
    
    user = {
        'first_name': user.first_name,
        'second_name': user.second_name,
        'phone_number': user.phone_number,
        'birth_date': user.birth_date
    }
    return render_template('update.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
