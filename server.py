#!/usr/bin/python
#-*- coding:utf-8 -*-#
from bottle import route, run, static_file, get, post, request, template, Bottle, abort

import time, os
import json
import app
import recipes as re
import volume_cup as vo_cup
from drinks import Drinks
#Verzeichnis für multislider in mdb.html
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

#Routing mainsite
@route('/')
def server_static(filepath="mdb.html"):
    return static_file(filepath, root='./')

@get('/mix.html')
def mix():
    return static_file("/mix.html", root='./')

@get('/recipes.html')
def mix():
    return static_file("/recipes.html", root='./')

@get('/admin.html')
def mix():
    return static_file("/admin.html", root='./')

@get('/mdb.html')
def mix():
    return static_file("/mdb.html", root='./')

@get('/change_drinks.html')
def mix():
    return static_file("/change_drinks.html", root='./')

@get('/pic_vol/pokal-glas-klarglas__0896474_PE609414_S5.JPG')
def image():
    return static_file("/pokal-glas-klarglas__0896474_PE609414_S5.JPG", root='./pic_vol')

@get('/pic_vol/pokal-glas-klarglas__0908826_PE609409_S5.JPG')
def image():
    return static_file("/pokal-glas-klarglas__0908826_PE609409_S5.JPG", root='./pic_vol')

@get('/pic_vol/vardagen-glas-klarglas__0896318_PE609373_S5.JPG')
def image():
    return static_file("/vardagen-glas-klarglas__0896318_PE609373_S5.JPG", root='./pic_vol')

@get('/pic_vol/plastikbecher-rot-360ml-50-einheiten.jpg')
def image():
    return static_file("/plastikbecher-rot-360ml-50-einheiten.jpg", root='./pic_vol')

@get('/dorecipes')
def recipes():
    re.getRecipes()
    from recipes import recipes
    recipes_send = json.dumps(recipes)
    return recipes_send


@get('/cupReady')
def cup():
    from app import start_next_cup
    app.start_next_cup()

@get('/volume')
def volume():
    vo_cup.cupArray()
    from volume_cup import volume
    volume_send = json.dumps(volume)
    return volume_send

@get('/getOldChoice')
def choice():
    obj = Drinks()
    obj.__init__()
    return json.dumps(obj.newchoice)

@get('/getChoiceOption')
def choiceOption():
    obj = Drinks()
    obj.readDrinks()
    unsorted_choice = obj.drinklist
    unsorted_choice.sort()
    return json.dumps(unsorted_choice)

@post('/newDrink')
def newDrink():
    selection = json.load(request.body)
    addDrink = selection.get('addDrink')
    old_drink = selection.get('oldDrink')
    print("new drink: {}".format(addDrink))
    print("oldDrink: {}".format(old_drink))
    obj = Drinks()
    obj.newDrinks(addDrink)
    obj.newChoice(old_drink, addDrink)

@post('/newChoice')
def newChoice():
    selection = json.load(request.body)
    new_drink = selection.get('newDrink')
    old_drink = selection.get('oldDrink')
    print("new drink: {}".format(new_drink))
    print("old drink: {}".format(old_drink))
    obj = Drinks()
    obj.newChoice(old_drink, new_drink)

@post('/doform')
def process():
    print("**11")
    bestellung = json.load(request.body)
    print(bestellung)
    b = bestellung.get('verhaeltnis')
    c = bestellung.get('getraenke')
    d = list(b)
    e = list(c)
    menge = bestellung.get('anzahl') #gbt die Menge an bestellten Getraenken an
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
    order_list.append(volume)
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
