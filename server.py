#!/usr/bin/python
#-*- coding:utf-8 -*-#
from bottle import route, run, static_file, get, post, request, template, Bottle, abort
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket

import time
import json
import app

#Verzeichnis für multislider in mdb.html
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

#Routing mainsite
@route('/')
def server_static(filepath="mdb.html"):
    return static_file(filepath, root='./')

#reequest, rest API
@post('/doform')
def process():
    print("**11")
    bestellung = json.loads(request.body)
    print(bestellung)
    print("Der Typ des empfangener request: {}".format(type(bestellung)))
    print("test dictionary. getraenke: {}".format(bestellung.get('getraenke')))
    order(bestellung)

#Daten fuer Bestellung auswerten und Bestellung in App.py starten
def order(bestellung):
    #raw Dict
    order_1 = bestellung
    #vorläufiges Array für Bestellung
    order_list = []
    #Entgültige Bestellungsarray für Ausfuehrung in App
    drink_list = []
    #Array für Mischv
    mischv = []

    print("**drinklist")
    #für warteschelife, zeigt an an welcher position deine Bestellung ist
    ordernumber_raw = 0
    ordernumber = 0
    #für ordernumber, um im Array postion zu finden, wo als naechstes fortgefahren werden soll
    x = 0
    print("**12")
    if len(order_list) > 0:
        x = (order_list[0] * 2) + 1 #order_list[0] * 2, weil noc hmoischverhaeltnis reingeschrieben werden muss
        ordernumber_raw = ordernumber_raw + 1
        print("**13")
        while True:
            if x < len(order_list):
                x = x + order_list[x] + 1
                ordernumber_raw = ordernumber_raw + 1
            else:
                ordernumber = math.ceil(ordernumber_raw)
                print("Deine Bestellung ist an Position: {}".format(ordernumber))
                break
    else:
        print("**13")
        print("Dein Bestellung ist an erster Position")


    #Variabel für Anzahl der getraenke pro Bestelleung
    number = 0
    print("**14")

    #Hier wird die Bestellung gefiltert, in vorlaeufigen Array geschrieben
    if bestellung.getraenke[0] != 6:
        drink1 = int(bestellung.getraenke[0])
        drink_list.append(drink1)
        value = int(bestellung.verhaeltnis[0])
        drink_list.append(value)
        number = number + 1
        print("**15")
        print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}, mischverhaeltnis: {}".format(drink1, number, mischv[1]))
        if bestellung.getraenke[1] != 6:
            print("**15")
            drink2 = int(bestellung.getraenke[1])
            drink_list.append(drink2)
            value = int(bestellung.verhaeltnis[1])
            drink_list.append(value)
            number = number + 1
            print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}, mischverhaeltnis: {}".format(drink2, number, mischv[2]))
            if bestellung.getraenke[2] != 6:
                print("**15")
                drink3 = int(bestellung.getraenke[2])
                drink_list.append(drink3)
                value = int(bestellung.verhaeltnis[2])
                drink_list.append(value)
                number = number + 1
                print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}, mischverhaeltnis: {}".format(drink3, number, mischv[3]))
                if bestellung.getraenke[3] != 6:
                    print("**15")
                    drink4 = int(bestellung.getraenke[3])
                    drink_list.append(drink4)
                    value = int(bestellung.verhaeltnis[3])
                    drink_list.append(value)
                    number = number + 1
                    if bestellung.getraenke[4] != 6:
                        print("**15")
                        drink5 = int(bestellung.getraenke[4])
                        drink_list.append(drink5)
                        value = int(bestellung.verhaeltnis[4])
                        drink_list.append(value)
                        number = number + 1
                        if bestellung.getraenke[5] != 6:
                            print("**15")
                            drink6 = int(bestellung.getraenke[5])
                            drink_list.append(drink6)
                            value = int(bestellung.verhaeltnis[5])
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
        print("**16")

    print("order_list Array: {}".format(order_list))
    #loesche Array um neue Bestellung aufzunehmen
    del drink_list

    print("**17")
    ap = app.App(order_list)
    ap.orderManager()

run(host='192.168.178.72', port=8080, server=GeventWebSocketServer)
