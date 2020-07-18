#!/usr/bin/env python3
#-*- coding:utf-8 -*-#
from bottle import route, run
from bottle import template
import ultraschallsensor
import pump
import RPi.GPIO as GPIO

from bottle import get, post, request # or route
from bottle import static_file

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
        print("Die Starthoehe betraegt:")
        print(startHoehe)
        global hoehe
        #für mischverhaeltnis Höhe berechnen wieviel eingefüllt werden soll
        #erst Alkohol dann
        while True:
            if ultraschallsensor.distanz() >= fillA:
                x = ultraschallsensor.distanz()
                hoehe = x
                print("Das Glas wird bis zur Hoehe aufgefuellt:")
                print(fuellHoehe)
                print("Das Glas wird bis zu .. mit Alkohol aufgefuellt:")
                print(fillA)
                pump.startPump(alc) #alc gibt an welche pumpe gestartet wird

                #debugging
                print("while schleife alkohol einfüllen")
                print("die aufgefüllte Menge an Alkohol beträgt:")
                aufgefuellt = hoehe - fuellHoehe
                print(aufgefuellt)
                print("fillA: es muss noch aufgefuellt werden: ")
                auffuellen = fillA - aufgefuellt
                print(auffuellen)


            elif ultraschallsensor.distanz() <= fillA:
                pump.stopPump()
                print("Die pumpe wurde ausgeschaltet. es befinden sich: ")
                print(ultraschallsensor.distanz())
                break

            else:
                print("while schleife auffuellen schief gelaufen.")
                break

    # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        pump.stopPump()
        GPIO.cleanup()

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
    startHoehe = ultraschallsensor.distanz() #starthoehe für Glasgrösse
    fuellHoehe = (startHoehe - 5) * 0.9
    alcnumber = request.forms.get('drinks')
    id_mischv = request.forms.get('mischverhaeltnis')
    drinknumber = request.forms.get('AlkoholAuswahl_1')
    int(drinknumber)
    global fillA
    global fillB
    fillA = fuellHoehe - (fuellHoehe * (int(id_mischv)) / 100)
    fillB = fuellHoehe
    round(fillA, 2)
    round(fillB, 2)
    enter(drinknumber, alcnumber)


run(host='192.168.178.72', reloader=True, port=8080, debug=True)
