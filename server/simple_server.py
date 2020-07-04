#!/usr/bin/env python3
from bottle import route, run
from bottle import template
#import app

from bottle import get, post, request # or route
from bottle import static_file

@route('/')
def server_static(filepath="index.html"):
    return static_file(filepath, root='./public/')

@post('/doform')
def process():

    name = request.forms.get('name')
    occupation = request.forms.get('occupation')
    return "Your name is {0} and you are a(n) {1}".format(name, occupation)

run(host='192.168.178.72', reloader=True, port=8080, debug=True)
