import os, pymysql

basedir = os.path.abspath(os.path.dirname(__file__))

DB_URL = os.environ.get('TODOLIST_DB_URL') or "mysql+pymysql://root:root@localhost:3306/todolist"


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'todo-list secret key'
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = True
