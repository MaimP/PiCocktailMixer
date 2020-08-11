from bottle import get, run, template
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket

@get('/')
def index():
    return template('index')

@get('/websocket', apply=[websocket])
def echo(ws):
    while True:
        msg = ws.receive()
        if msg is not None:
            ws.send(msg)
        else: break

run(host='192.168.178.72', port=8080, server=GeventWebSocketServer)
