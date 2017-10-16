#!/usr/bin/env python
# encoding: utf-8

"""
@author: WillSo
@license: Apache Licence 
@software: PyCharm
@file: flaskr.py
@time: 2017\10\16 0016 11:05
"""

# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from com.szw.web.bean import Bean
from com.szw.web.dao import DAOFactory

DAOFactory = DAOFactory.DAOFactory
User = Bean.User

app = Flask(__name__)

@app.route('/')
def show_users():
    value = DAOFactory.getDAOImpl(User.__name__).queryAll()
    users = list(map(lambda iter : User(iter[0], iter[1]), value))
    return render_template('show_entries.html', users=users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    # value = DAOFactory.getDAOImpl(User.__name__).queryAll()
    # print(value)
    app.run(debug=True)