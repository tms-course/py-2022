from flask import Flask, g, render_template, request
from werkzeug.security import generate_password_hash

from db import Session
from models import Users, Profiles

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
            hash = generate_password_hash(request.form['password'])
            u = Users(email=request.form['email'], password_hash=hash)
            session.add(u)
            session.flush()

            p = Profiles(name=request.form['name'], old=request.form['old'],
                         city=request.form['city'], user_id=u.id)
            session.add(p)
            session.commit()
        except Exception as e:
            session.rollback()
            print('Ошибка добавления данных')
            pass
    return render_template('register.html', title="Регистрация")


if __name__ == '__main__':
    app.run(debug=True)
