#!/usr/bin/python
#-*- coding:utf-8 -*-#
from bottle import route, run, static_file, get, post, request, template, Bottle, abort

import time
import json
import app
import recipes as re
import volume_cup as vo_cup
#Verzeichnis für multislider in mdb.html
##@route('/static/:path#.+#', name='static')
#def static(path):
#    return static_file(path, root='static')

#Routing mainsite
@route('/')
def server_static(filepath="mdb.html"):
    return static_file(filepath, root='./')
@get('/mix')
def help():
    return static_file('mix.html', root='/')

@get('/mix.html')
def help():
    return static_file('mix.html', root='/')

#@route('/mix.html')
#def server_static(filepath="mix.html"):
#    return static_file(filepath, root='./mix')

@route('/recipes.html')
def server_static(filepath="recipes.html"):
    return static_file(filepath, root='./recipes')

@route('/admin')
def server_static(filepath="admin.html"):
    return static_file(filepath, root='./admin')


@get('/dorecipes')
def recipes():
    re.getRecipes()
    from recipes import recipes
    recipes_send = json.dumps(recipes)
    return recipes_send


global ready
ready = False
@get('/readyCup')
def cup():
    global ready
    ready = True
    return ready

@get('/volume')
def volume():
    vo_cup.cupArray()
    from volume_cup import volume
    volume_send = json.dumps(volume)
    return volume_send

@post('/doform')
def process():
    print("**11")
    bestellung = json.load(request.body)
    print(bestellung)
    b = bestellung.get('verhaeltnis')
    c = bestellung.get('getraenke')
    d = list(b)
    e = list(c)
    menge = bestellung.get('anzahl') #gibt die Menge an bestellten Getraenken an
    glas = bestellung.get('volume') #gibt an welches Glas genutzt wird(Volumen)
    mischv = []
    getraenke = []
    counter_m = 0
    for i in d:
        x = float(d[counter_m])
        counter_m = counter_m + 1
        mischv.append(x)
        print("debug mischv :{}".format(x))

    counter_g = 0
    for i in e:
        x = float(e[counter_g])
        counter_g = counter_g + 1
        getraenke.append(x)
        print("debug getraenke :{}".format(x))

    order(mischv, getraenke, menge, glas)

#Daten fuer Bestellung auswerten und Bestellung in App.py starten
def order(mischv, getraenke, anzahl, volume):
    mischv = mischv
    getraenke = getraenke
    menge = anzahl
    glas = volume
    #vorläufiges Array für Bestellung
    order_list = []
    #Entgültige Bestellungsarray für Ausfuehrung in App
    drink_list = []

    print("**drinklist")
    #für warteschelife, zeigt an an welcher position deine Bestellung ist
    ordernumber_raw = 0
    ordernumber = 0
    #für ordernumber, um im Array postion zu finden, wo als naechstes fortgefahren werden soll
    x = 0
    print("**12")
    if len(order_list) > 0:
        x = (order_list[0] * 2) + 3 #order_list[0] * 2, weil noch mischverhaeltnis reingeschrieben werden muss, +3 für glas, menge, Anazhl an mischgetraenken
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


    #Variabel für menge der getraenke pro Bestelleung
    number = 0
    print("**14")

    #Hier wird die Bestellung gefiltert, in vorlaeufigen Array geschrieben
    if getraenke[0] != 6:
        drink1 = int(getraenke[0])
        drink_list.append(drink1)
        value = int(mischv[0])
        drink_list.append(value)
        number = number + 1
        print("**15")
        print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}, mischverhaeltnis: {}".format(drink1, number, mischv[0]))
        if getraenke[1] != 6:
            print("**15")
            drink2 = int(getraenke[1])
            drink_list.append(drink2)
            value = int(mischv[1])
            drink_list.append(value)
            number = number + 1
            print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}, mischverhaeltnis: {}".format(drink2, number, mischv[1]))
            if getraenke[2] != 6:
                print("**15")
                drink3 = int(getraenke[2])
                drink_list.append(drink3)
                value = int(mischv[2])
                drink_list.append(value)
                number = number + 1
                print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}, mischverhaeltnis: {}".format(drink3, number, mischv[2]))
                if getraenke[3] != 6:
                    print("**15")
                    drink4 = int(getraenke[3])
                    drink_list.append(drink4)
                    value = int(mischv[3])
                    drink_list.append(value)
                    number = number + 1
                    if getraenke[4] != 6:
                        print("**15")
                        drink5 = int(getraenke[4])
                        drink_list.append(drink5)
                        value = int(mischv[4])
                        drink_list.append(value)
                        number = number + 1
                        if getraenke[5] != 6:
                            print("**15")
                            drink6 = int(getraenke[5])
                            drink_list.append(drink6)
                            value = int(mischv[5])
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


    #im Format: menge der Getraenke pro Bestellung, wiviele von diesen, welches Glas genutzt wird
    #getraenk1, Mischv. 1, getraenk2, ...
    #schreibt bestellung in Array
    order_list.append(number)
    order_list.append(menge)
    order_list.append(glas)
    z = order_list[0] * 2

    for i in range(z):
        order_list.append(drink_list[int(i)])
        print("**16")

    print("order_list Array: {}".format(order_list))
    #loesche Array um neue Bestellung aufzunehmen
    del drink_list

    print("**17")
    ap = app.App(order_list)
    ap.orderManager()

run(host='192.168.178.72', port=8080)
