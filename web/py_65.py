#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request


# Flask: web framework
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home Page</h1>'


@app.route('/login', methods=['GET'])
def login_form():
    return '''<form action="/login" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/login', methods=['POST'])
def login():
    # Access form parameters from request：
    if request.form['username']=='admin' and request.form['password']=='admin':
        return '<h3>Hello, Admin!</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888)
