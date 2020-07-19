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

global zustand

@route('/')
def server_static(filepath="index.html"):
    return static_file(filepath, root='./')

@post('/doform')
def process():
    getData()
    return "Your name is {0} and you are a(n) {1} {2}".format(alcnumber, id_mischv, drinknumber)

def enter(alc, misch):
    try:
        print(alc)
        print(misch)
        print("Die Starthoehe betraegt: {}".format(startHoehe))
        print("test round: {}".format(fillA))
        global hoehe
        global entfernung
        zaehler = 0
        #für mischverhaeltnis Höhe berechnen wieviel eingefüllt werden soll
        #erst Alkohol dann
        while True:
            entfernung = ultraschallsensor.distanz()
            zaehler = zaehler + 1
            print("while schleife durchfuehrung nummer: {}".format(zaehler))
            print("die aktuelle Entfernung betraegt: {}".format(entfernung))
            if entfernung >= fillA:
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
                    print("fillA: es muss noch aufgefuellt werden: {}".format(auffuellen))
                    time.sleep(0.1)

                else:
                    print("Die while Schleife hat keine passende if Anweisung.")

            elif entfernung <= fillA:
                #Messfehler ausschließen
                print("elif anweisung gestartet")
                counter = 0
                global c
                c = 0
                for x in range(3):
                    c = c + ultraschallsensor.distanz()
                    counter = counter + 1
                    print("Die addierte Entfernung ist aktuell: {}".format(c))
                    return c
                    time.sleep(0.05)

                average = c / 3
                print("entfernung ist kleiner als fillA. der durchschnitt ist: {}".format(average))
                if (average * 0.95) > entfernung:
                    return average

                else:
                    pump.stopPump()
                    print("Die pumpe wurde ausgeschaltet. es befinden sich: ")
                    print(entfernung)
                    zustand == False
                    break

            else:
                print("while schleife auffuellen schief gelaufen.")
                break

    # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        pump.stopPump()

#    if (fillA * 0.85) <= ultraschallsensor.entfernung() <= (fillA * 1.15):
#        while ultraschallsensor.entfernung() <= fillB:
#            pump.startPump(misch) #misch gibt an welche Pumpe gestartet wird
#
#            print("in dem getränk sind nun insgesamt: ")
#            print(ultraschallsensor.distanz())
#            mischM = ultraschallsensor.distanz()
#
#            verhaeltnisEcht = (mischM / alcM) * 100
#            print("es sind", "% lakohol im Glas" sep=verhaeltnisEcht)

#        pump.stopPump()

#    else:
#        print("Es konnte kein Mischgetränk eingefüllt werden, suche nach fehlern.")

def getData():
    global fuellHoehe
    global alcnumber
    global id_mischv
    global drinknumber
    global startHoehe
    startHoehe = ultraschallsensor.distanz() #starthoehe für Glasgrösse
    fuellHoehe = (startHoehe - 5) * 0.9
    alcnumber = request.forms.get('drinks')
    id_mischv = request.forms.get('mischverhaeltnis')
    drinknumber = request.forms.get('AlkoholAuswahl_1')
    int(drinknumber)
    global fillA
    global fillB
    global unroundA
    global unroundB
    unroundA = startHoehe - (fuellHoehe * (int(id_mischv)) / 100)
    unroundB = fuellHoehe
    fillA = round(unroundA, 2)
    fillB = round(unroundB, 2)
    enter(drinknumber, alcnumber)


run(host='192.168.178.72', reloader=True, port=8080, debug=True)
