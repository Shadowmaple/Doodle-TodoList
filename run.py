#!/usr/bin/python3

from app import app

if __name__ == '__main__':
    app.run("127.0.0.1", 3300, debug=True)
