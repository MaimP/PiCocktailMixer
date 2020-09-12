#!/usr/bin/env python3
#-*- coding:utf-8 -*-#
from bottle import route, run, static_file, get, post, request, template, Bottle, abort

import ultraschallsensor
import pump
import RPi.GPIO as GPIO
import time
import app
import json
import hanging_threads
import threading
global ap

global zustand
global hoehe
global entfernung
global progress

global mischv
mischv = []

#!/usr/bin/python

from bottle import get, run, template
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket

drink_1 = None
drink_2 = None
drink_3 = None
drink_4 = None
drink_5 = None
drink_6 = None

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def server_static(filepath="mdb.html"):
    return static_file(filepath, root='./')

result_available = threading.Event() #fuer Thread


@post('/doform')
def process():
    global order
    print("**11")
    order = json.load(request.body)
    print(order)
    order()
#    print(order)
#@post('/readycocktail')


def order():
    global order_list
    order_list = []
    global drink_list
    drink_list = []
    #für warteschelife, zeigt an an welcher position deine Bestellung ist
    ordernumber_raw = 0
    global ordernumber
    #für ordernumber, um im Array postion zu finden, wo als naechstes fortgefahren werden soll
    x = 0
    if len(order_list) > 0:
        x = (order_list[0] * 2) + 1 #order_list[0] * 2, weil noc hmoischverhaeltnis reingeschrieben werden muss
        ordernumber_raw = ordernumber_raw + 1
        while True:
            if x < len(order_list):
                x = x + order_list[x] + 1
                ordernumber_raw = ordernumber_raw + 1
            else:
                ordernumber = math.ceil(ordernumber_raw)
                print("Deine Bestellung ist an Position: {}".format(ordernumber))
                break
    else:
        print("Dein Bestellung ist an erster Position")


    #Variabel für Anzahl der getraenke pro Bestelleung
    number = 0

    if order.getraenke[0] != 6:
        drink1 = int(order.getraenke[0])
        drink_list.append(drink1)
        value = int(order.verhaeltnis[0])
        drink_list.append(value)
        number = number + 1
        print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}, mischverhaeltnis: {}".format(drink1, number, mischv[1]))
        if order.getraenke[1] != 6:
            drink2 = int(order.getraenke[1])
            drink_list.append(drink2)
            value = int(order.verhaeltnis[1])
            drink_list.append(value)
            number = number + 1
            print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}, mischverhaeltnis: {}".format(drink2, number, mischv[2]))
            if order.getraenke[2] != 6:
                drink3 = int(order.getraenke[2])
                drink_list.append(drink3)
                value = int(order.verhaeltnis[2])
                drink_list.append(value)
                number = number + 1
                print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}, mischverhaeltnis: {}".format(drink3, number, mischv[3]))
                if order.getraenke[3] != 6:
                    drink4 = int(order.getraenke[3])
                    drink_list.append(drink4)
                    value = int(order.verhaeltnis[3])
                    drink_list.append(value)
                    number = number + 1
                    if order.getraenke[4] != 6:
                        drink5 = int(order.getraenke[4])
                        drink_list.append(drink5)
                        value = int(order.verhaeltnis[4])
                        drink_list.append(value)
                        number = number + 1
                        if order.getraenke[5] != 6:
                            drink6 = int(order.getraenke[5])
                            drink_list.append(drink6)
                            value = int(order.verhaeltnis[5])
                            drink_list.append(value)
                            number = number + 1
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass


    #im Format: Anzahl der Getraenke pro Bestellung, getraenk1, Mischv. 1, getraenk2, ...
    #schreibt bestellung in Array
    order_list.append(number)
    z = order_list[0] * 2
    print("index 0: {}".format(z))

    for i in range(z):
        print("i ist: {}".format(i))
        order_list.append(drink_list[int(i - 1)])

    print("order_list Array: {}".format(order_list))
    #loesche Array um neue Bestellung aufzunehmen
    del drink_list

    ap = app.App(order_list)
    ap.orderManager()
    print("nach app.app")




run(host='192.168.178.72', port=8080, server=GeventWebSocketServer)

#run(host='192.168.178.72', reloader=True, port=8080, debug=True)
