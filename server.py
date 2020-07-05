#!/usr/bin/env python3
from bottle import route, run
from bottle import template
import mx
import getData

from bottle import get, post, request # or route
from bottle import static_file

@route('/')
def server_static(filepath="index.html"):
    return static_file(filepath, root='./')

@post('/doform')
def process():
    import mx
    #xx

#    alcnumber = request.forms.get('drinks')
#    id_mischv = request.forms.get('mischverhaeltnis')
#    drinknumber = request.forms.get('AlkoholAuswahl_1')
    #mx.enter()
    mx.enter(request.forms.get('AlkoholAuswahl_1'), request.forms.get('drinks'))
    x = dir(mx)
    y = dir(getData)
    return "die Module mx: {0}, die Module getData: {1}".format(x, y)


    return "Your name is {0} and you are a(n) {1} {2}".format(alcnumber, id_mischv, drinknumber)

run(host='192.168.178.72', reloader=True, port=8080, debug=True)
