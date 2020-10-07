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

@post('/dorecipes')
def recipes():
    recipe_get = request.body
    recipes_send = {
        "name": "Aam Panna",
        "description": "Aam panna is an Indian drink renowned for its heat-resistant properties. It is made from raw mangoes, is yellow to very light green in color, and is consumed as a tasty and healthy beverage to fight against the intense Indian summer heat. In most instances, mint leaves are added which enhances the green color.",
        "github": "connectnitish",
        "ingredients": [
            {
                "quantity": "1",
                "measure": "",
                "ingredient": "Sugar"
            },
            {
                "quantity": "2",
                "measure": "",
                "ingredient": "Unripe Green Mango"
            },
            {
                "quantity": "3",
                "measure": "",
                "ingredient": "Cardamom"
            },
            {
                "quantity": "4",
                "measure": "",
                "ingredient": "Fresh Mint"
            },
            {
                "quantity": "5",
                "measure": "",
                "ingredient": "Black Salt"
            }
        ],
        "directions": [
            "Choose the raw mangoes which are tart.",
            "You can keep the skin on before boiling the mangoes. It gives a very distinct flavour to the Panna.",
            "Peeling the skin before boiling makes the process very easy.",
            "If the Panna is not very tangy, you can add some lemon juice to it.",
            "Boil Mango with mild heat in 1 cup of water.",
            "You can also roast mango before boiling if needed for crispy taste.",
            "The subtly smoky flavour in this drink will take it to the next level.",
            "Strain into the prepared glass.",
            "Garnish with a parsley sprig, 2 speared green olives and a lime wedge and a celery stalk (optional)."
        ],
        "image": "aam-panna.jpg",
        "keywords": [
            "fruit",
            "juice",
            "mocktail",
            "non-alcoholic",
            "vegan",
            "mango"
        ]
    }
    return json.parse(recipes)


@get('/list_recipes')
def list_recipes():
    name = request.body



#reequest, rest API
@post('/doform')
def process():
    print("**11")
    bestellung = json.load(request.body)
    print(bestellung)
    b = bestellung.get('verhaeltnis')
    c = bestellung.get('getraenke')
    d = list(b)
    e = list(c)
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

    order(mischv, getraenke)

def recipesGet():
    from glob import glob
    import json

    global recipes
    recipes = []

    files = []

    pth ="/Users/mikauthmann/Documents/Github/PiCocktailMixer/recipes/" #rasp. : /home/pi/Pi...
    for i in glob(pth+"*.json"):
        files.append(i)
    print("**2")

    counter = 0

    for i in files:
        # Opening JSON file
        f = open(files[counter])
        # returns JSON object as
        # a dictionary
        data = json.load(f)
        # Iterating through the json
        # list
        for i in data['ingredients']:
            print(i)
            recipes.append(i)
        # Closing file
        f.close()
        counter = counter + 1

    print("**3")

#Daten fuer Bestellung auswerten und Bestellung in App.py starten
def order(mischv, getraenke):
    #raw Dict
    getraenke = getraenke
    #vorläufiges Array für Bestellung
    order_list = []
    #Entgültige Bestellungsarray für Ausfuehrung in App
    drink_list = []
    #Array für Mischv
    mischv = mischv

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


    #im Format: Anzahl der Getraenke pro Bestellung, getraenk1, Mischv. 1, getraenk2, ...
    #schreibt bestellung in Array
    order_list.append(number)
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

run(host='192.168.178.72', port=8080, server=GeventWebSocketServer)
