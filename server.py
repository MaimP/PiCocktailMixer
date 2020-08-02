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
app = App()

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
    app.order()
    return "Dein Getraenk ist in Bearbeitung."


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
