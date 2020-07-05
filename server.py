#!/usr/bin/env python3
from bottle import route, run
from bottle import template
import app

from bottle import get, post, request # or route
from bottle import static_file

@route('/')
def server_static(filepath="index.html"):
    return static_file(filepath, root='./')

@post('/doform')
def process():

    alcnumber = request.forms.get('drinks')
    id_mischv = request.forms.get('mischverhaeltnis')
    drinknumber = request.forms.get('AlkoholAuswahl_1')
<<<<<<< HEAD
#    app.enter()
    dir(app)
=======
    #app.enter()
    x = dir(app)
    return "die Module: {0}".format(x)

>>>>>>> e5dbfdb3c789930f352c3954daccba2d121edde3
    return "Your name is {0} and you are a(n) {1} {2}".format(alcnumber, id_mischv, drinknumber)

run(host='192.168.178.72', reloader=True, port=8080, debug=True)
