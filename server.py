#!/usr/bin/env python3
#-*- coding:utf-8 -*-#
from bottle import route, run, static_file, get, post, request, template, Bottle, abort

import ultraschallsensor
import pump
import RPi.GPIO as GPIO
import time
import app
import json
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

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def server_static(filepath="mdb.html"):
    return static_file(filepath, root='./')

@get('/websocket', apply=[websocket])
def echo(ws):
    global enter
    enter = False
    counter_i = 0
    counter_debug = 0
    while True:
        msg = ws.receive()
        if msg is not None:
            ws.send(msg)
            value_1 = int(json.loads(msg))
            print("int float: {}".format(type(value_1)))
            mischv.append(value_1)
        else:
            enter = True
            print("Enter: {}".format(enter))
            break


@post('/doform')
def process():
    while True:
        if enter == True:
            try:
                print("führe Try block aus")
                return "Dein Getraenk ist in Bearbeitung."
            finally:
                print("führe finally block aus")
                order()
        else:
            time.sleep(0.5)

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

    #geraenke auslesen und als int convertieren
    drink_1 = int(request.forms.get('drink1'))
    drink_2 = int(request.forms.get('drink2'))
    drink_3 = int(request.forms.get('drink3'))
    drink_4 = int(request.forms.get('drink4'))
    drink_5 = int(request.forms.get('drink5'))
    drink_6 = int(request.forms.get('drink6'))


    if drink_1 != 6:
        drink1 = request.forms.get('drink1')
        drink_list.append(drink1)
        value = mischv[1]
        drink_list.append(value)
        number = number + 1
        print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}, mischverhaeltnis: {}".format(drink1, number, mischv[1]))
        if drink_2 != 6:
            drink2 = request.forms.get('drink2')
            drink_list.append(drink2)
            value = mischv[2]
            drink_list.append(value)
            number = number + 1
            print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}, mischverhaeltnis: {}".format(drink2, number, mischv[2]))
            if drink_3 != 6:
                drink3 = request.forms.get('drink3')
                drink_list.append(drink3)
                value = mischv[3]
                drink_list.append(value)
                number = number + 1
                print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}, mischverhaeltnis: {}".format(drink3, number, mischv[3]))
                if drink_4 != 6:
                    drink4 = request.forms.get('drink4')
                    drink_list.append(drink4)
                    value = mischv[4]
                    drink_list.append(value)
                    number = number + 1
                    if drink_5 != 6:
                        drink5 = request.forms.get('drink5')
                        drink_list.append(drink5)
                        value = mischv[5]
                        drink_list.append(value)
                        number = number + 1
                        if drink_6 != 6:
                            drink6 = request.forms.get('drink6')
                            drink_list.append(drink6)
                            value = mischv[6]
                            drink_list.append(value)
                            number = number + 1
                        else:
                            return drink_list
                    else:
                        return drink_list
                else:
                    return drink_list
            else:
                return drink_list
        else:
            return drink_list
    else:
        return drink_list


    #im Format: Anzahl der Getraenke pro Bestellung, getraenk1, getraenk2, ...
    #schreibt bestellung in Array
    counter3 = 0
    order_list.append(number)
    z = order_list[0] * 2
    print("index 0: {}".format(z))
    
    for i in drink_list:
        order_list.append(drink_list[i])

    #loesche Array um neue Bestellung aufzunehmen
    del drink_list

    ap = app.App(order_list)
    ap.orderManager()
    print("nach app.app")




run(host='192.168.178.72', port=8080, server=GeventWebSocketServer)

#run(host='192.168.178.72', reloader=True, port=8080, debug=True)
