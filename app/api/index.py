from flask import redirect, url_for

from . import route


@index.index('/')
def index():
    # redirect(url_for('login'))
    return "hello"
