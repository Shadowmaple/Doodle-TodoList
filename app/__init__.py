from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("app")
db = SQLAlchemy(app)