import os
import bcrypt
import datetime as dt

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

app = Flask(__name__)

"""
sqlite://file_name.sqlite
postgresql://user:password@host:port/dbname
mysql://user:password@host:port/dbname
oracle://user:password@host:port/dbname
"""
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'storage.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)

    profile = db.relationship('Profiles', backref='users', uselist=False)

    def __repr__(self) -> str:
        return f"<users {self.id}>"


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    old = db.Column(db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self) -> str:
        return f"<profiles {self.id}>"


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
        try:
            salt = bcrypt.gensalt()
            hash = bcrypt.hashpw(request.form['password'].encode(), salt)
            u = Users(email=request.form['email'], password_hash=hash.decode())
            db.session.add(u)
            db.session.flush()

            p = Profiles(name=request.form['name'], old=request.form['old'],
                         city=request.form['city'], user_id=u.id)
            db.session.add(p)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print('Ошибка добавления данных')
            pass
    return render_template('register.html', title="Регистрация")

if __name__ == '__main__':
    app.run(debug=True)
