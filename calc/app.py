from flask import Flask, request
app = Flask(__name__)

from pathlib import Path
from operations import *
import operations

@app.route('/add')
def show_add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"{add(a,b)}"

@app.route('/sub')
def show_sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"{sub(a,b)}"

@app.route('/mult')
def show_mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"{mult(a,b)}"

@app.route('/div')
def show_div():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"{div(a,b)}"

operators = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div,
}

@app.route('/math/<func>')
def show_math(func):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"{operators[func](a,b)}"