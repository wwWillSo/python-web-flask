#!/usr/bin/env python
# encoding: utf-8

"""
@author: WillSo
@license: Apache Licence 
@software: PyCharm
@file: TestDemo.py
@time: 2017\10\16 0016 9:54
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world () :
    # i = 1/0
    return "hello world"

@app.route('/web/<username>')
def say_hello (username) :
    return "hello, %s" % username

if __name__ == '__main__':
    app.run(debug = True)