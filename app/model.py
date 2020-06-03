from . import app, db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, index=False)
    password = db.Column(db.String(255), unique=False, index=False)
    nick_name = db.Column(db.String(25), unique=False, index=False)

    def __repr__(self):
        return super().__repr__()


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, index=False)
    content = db.Column(db.String, unique=False, index=False)
    status = db.Column(db.Integer, unique=False, index=False)
    time = db.Column(db.String(25), unique=False, index=False)
    delete_time = db.Column(db.String(25), unique=False, index=False)
    user_id = db.Column(db.Integer, unique=True, index=True)

    def __repr__(self):
        return super().__repr__()
