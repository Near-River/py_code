#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template

# Flask: web framework
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'admin':
        return '<h3>Hello, Admin!</h3>'
    data = dict(message='Username or password is incorrect.', username=username)
    return render_template('login.html', **data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888)
