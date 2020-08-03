#!/usr/bin/env python3
#-*- coding:utf-8 -*-#
from bottle import route, run
from bottle import template
from bottle import get, post, request # or route
from bottle import static_file

import ultraschallsensor
import pump
import RPi.GPIO as GPIO
import time
from app import App
global app = app.App(order_list)

global zustand
global hoehe
global entfernung
global progress

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def server_static(filepath="mdb.html"):
    return static_file(filepath, root='./')

@post('/process')
def process():
    getData()
    return "Dein Getraenk ist in Bearbeitung."

@post('/doform')
def process():
    order()
    return "Dein Getraenk ist in Bearbeitung."

def order():
    global order_list
    order_list = []
    global drink_list
    drink_list = []
    #für warteschelife, zeigt an an welcher position deine Bestellung ist
    ordernumber_raw = 0
    #für ordernumber, um im Array postion zu finden, wo als naechstes fortgefahren werden soll
    x = 0
    if len(order_list) > 0:
        x = order_list[0] + 1 #order_list[0] * 2, weil noc hmoischverhaeltnis reingeschrieben werden muss
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

    #muss auch noch in Array geschrieben werden
    id_mischv = request.forms.get('mischverhaeltnis')
    if drink_1 != 6:
        drink1 = request.forms.get('drink1')
        drink_list.append(drink1)
#           mischv1 = request.forms.get('mischv1')
        number = number + 1
        print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}".format(drink1, number))
        if drink_2 != 6:
            drink2 = request.forms.get('drink2')
            drink_list.append(drink2)
#           mischv2 = request.forms.get('mischv2')
            number = number + 1
            print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}".format(drink2, number))
            if drink_3 != 6:
                drink3 = request.forms.get('drink3')
                drink_list.append(drink3)
    #           mischv3 = request.forms.get('mischv3')
                number = number + 1
                print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}".format(drink3, number))
                if drink_4 != 6:
                    drink4 = request.forms.get('drink4')
                    drink_list.append(drink4)
        #           mischv4 = request.forms.get('mischv4')
                    number = number + 1
                    if drink_5 != 6:
                        drink5 = request.forms.get('drink5')
                        drink_list.append(drink5)
            #           mischv5 = request.forms.get('mischv5')
                        number = number + 1
                        if drink_6 != 6:
                            drink6 = request.forms.get('drink6')
                            drink_list.append(drink6)
                #           mischv6 = request.forms.get('mischv6')
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


    #schreibt bestellung in Array
    counter3 = 0
    order_list.append(number)
    z = order_list[0]
    print("index 0: {}".format(z))
    while True:
        if counter3 < z:
            drink = drink_list[counter3]
            #gibt in Value(Getraenkenummer) aus, mit dem "Index" von Counter3
    #            drink = order_dict.values(counter3)
            #macht eine Liste mit den Getraenkenummer
            #im Format: Anzahl der Getraenke, getraenk1, getraenk2, ...
            order_list.append(drink)
            #debug, wie range zaehlt, ob bei 0 oder 1 anfaengt und ob alles funkt.
            print("der counter ist bei: {}, hinzugefuegtes Getraenk in drink_lkist: {}".format(counter3, drink))
            counter3 = counter3 + 1

        else:
            break

    #loesche Array um neue Bestellung aufzunehmen
    del drink_list

#    while True:
#        #führe ordermanager aus mit Bestellungsarray
#        if process == False:
    app.orderManager()
    print("nach app.app")
#            print("Dein Getraenk wird nun aufgefuellt")
#            break
#        else:
#            time.sleep(3)
#            print("ein anderes Getraenk wird noch aufgefuellt, warte noch einen Augenblick")


def enter(alc, misch):
    try:

        print(alc)
        print(misch)
        print("Die Starthoehe betraegt: {}".format(startHoehe))
        print("test round: {}".format(fillA))
        zaehler = 0
        zaehler2 = 0
        #für mischverhaeltnis Höhe berechnen wieviel eingefüllt werden soll
        #erst Alkohol dann
        while True:
            if zaehler == 0:
                entfernung = ultraschallsensor.first_realDistance()
                return entfernung

            else:
                entfernung = ultraschallsensor.real_distance()
                return entfernung

            zaehler = zaehler + 1
#            progress = (startHoehe - entfernung) / glasHoehe * 100
#            prog = int(progress)
#            progress(prog)
            print("while schleife durchfuehrung nummer: {}".format(zaehler))
            print("die aktuelle Entfernung betraegt: {}".format(entfernung))
            if entfernung > fillA:
                hoehe = entfernung
                print("Das Glas wird bis zur Hoehe aufgefuellt: {}".format(fuellHoehe))
                print("Das Glas wird bis zu .. mit Alkohol aufgefuellt: {}".format(fillA))
                if zaehler == 1:
                    pump.startPump(alc) #alc gibt an welche pumpe gestartet wird
                    zustand = True

                elif zustand:
                    #debugging
                    print("while schleife alkohol einfüllen")
                    aufgefuellt = startHoehe - hoehe
                    print("die aufgefüllte Menge an Alkohol beträgt:{}".format(aufgefuellt))
                    auffuellen = fillA - aufgefuellt
                    print("fillA: es muss noch aufgefuellt werden: {} cm Alkohol".format(auffuellen))
                    time.sleep(0.1)

                else:
                    print("Die while Schleife hat keine passende if Anweisung.")

            elif entfernung <= fillA:
                pump.stopPump()
                print("Die pumpe wurde ausgeschaltet. Im Glas sind: {} cm".format(entfernung))
                zustand == False
                break

            else:
                print("while schleife auffuellen schief gelaufen.")
                break

        print("Das Einfuellen des Alkohols ist abgeschlossen, es wird mit dem Mischgetraenk fortgefahren.")

        while True:
            entfernung = ultraschallsensor.real_distance()

            zaehler = zaehler + 1
            print("while schleife durchfuehrung nummer: {}".format(zaehler))
            print("die aktuelle Entfernung betraegt: {}".format(entfernung))
            if entfernung > fillB:
                hoehe = entfernung
                print("Das Glas wird bis zur Hoehe aufgefuellt: {}".format(fuellHoehe))
                print("Das Glas wird bis zu .. mit dem Mischgetraenk aufgefuellt: {}".format(fillB))
                if zaehler2 == 0:
                    zaehler2 = zaehler2 + 1
                    pump.startPump(misch) #misch gibt an welche pumpe gestartet wird
                    zustand = True

                elif zustand:
                    #debugging
                    print("while schleife Mischgetraenk einfüllen")
                    aufgefuellt = startHoehe - hoehe
                    print("die aufgefüllte Menge an Getraenk beträgt insgesamt:{} cm".format(aufgefuellt))
                    auffuellen = fillB - aufgefuellt
                    print("Es muss noch insgesamt aufgefuellt werden: {} cm".format(auffuellen))
                    time.sleep(0.1)

                else:
                    print("Die while Schleife hat keine passende if Anweisung.")

            elif entfernung <= fillB:
                pump.stopPump()
                print("Die pumpe wurde ausgeschaltet. Im Glas sind: {} cm".format(entfernung))
                zustand == False
                break

            else:
                print("while schleife auffuellen schief gelaufen.")
                break

    # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        pump.stopPump()


def progress(progr):
    #progressbar in html über abstand
    y = int(progr)
    x = x + y

run(host='192.168.178.72', reloader=True, port=8080, debug=True)
