"""Создать приложение для регистрации на мероприятие используя фреймворк Flask. Под-
ключить базу данных используя SQLAlchemy, в которой будет храниться только список
всех участников. От участников нам необходимо знать имя, фамилию, телефон, да-
ту рождения и время регистрации. Каждый может получить список всех участников,
отменить свою регистрацию по номеру телефона, изменить данные."""

from flask import Flask, g, render_template, request, redirect, url_for
from db import Session
from models import Users
import datetime as dt


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
        print('ошибка чтения')
    return render_template('index.html', title="Главная", list=users)


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
            pass

        return redirect(url_for('index'))
    return render_template('register.html', title="Регистрация")


@app.route('/users/delete', methods=['GET', 'POST'])
def delete_user():
    session = get_db()
    
    
    if request.method == 'POST':
        
        try:
            user = Users.query.filter_by(phone=request.form['phone']).delete()
            session.commit()

        except:
            session.rollback()
            return {}, 403
    
        return redirect(url_for('index'))
    
    return render_template('delete.html', )
    


@app.route('/users/<int:id>/update', methods=['GET', 'POST'])
def update_user(id):
    session = get_db()
    try:
        user = Users.query.get(id)
    except:
        return {}, 403
    
    if request.method == 'POST':
        
        try:
            for field in request.form.keys():
                if field == 'birthday':
                    user.birthday = dt.datetime.strptime(request.form[field], '%Y-%m-%d')
                else:
                    setattr(user, field, request.form[field])
            session.commit()
            
        except:
            session.rollback()
            return {}, 403
        
        return redirect(url_for('index'))
   
    return render_template('update.html', title='Редактировать', user=user)
        



if __name__ =='__main__':
    app.run(debug=True)
