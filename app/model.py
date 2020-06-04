from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

from . import db, login


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    password = db.Column(db.String(255))
    nick_name = db.Column(db.String(25))

    # def __repr__(self):
    #     return super().__repr__()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class List(db.Model):
    __tablename__ = 'list'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.Text)
    status = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, index=True)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
