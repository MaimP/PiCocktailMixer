#!/usr/bin/env python3
#-*- coding:utf-8 -*-#
from bottle import route, run
from bottle import template
import ultraschallsensor

from bottle import get, post, request # or route
from bottle import static_file

@route('/')
def server_static(filepath="index.html"):
    return static_file(filepath, root='./')

@post('/doform')
def process():
    getDtata()
    return "Your name is {0} and you are a(n) {1} {2}".format(alcnumber, id_mischv, drinknumber)

def enter(alc, misch):
    #für mischverhaeltnis Höhe berechnen wieviel eingefüllt werden soll
    #erst Alkohol dann
    while ultraschallsensor.entfernung() <= fillA:
        pump.startPump(alc) #alc gibt an welche pumpe gestartet wird

        print("die aufgefüllte Menge an Alkohol beträgt:") #debugging
        print(ultraschallsensor.distand())
        alcM = ultraschallsensor.distanz() #debugging: Menge an aufgefülltem alc

    pump.stopPump()

    if (fillA * 0.85) <= ultraschallsensor.entfernung() <= (fillA * 1.15):
        while ultraschallsensor.entfernung() <= fillB:
            pump.startPump(misch) #misch gibt an welche Pumpe gestartet wird

            print("in dem getränk sind nun insgesamt: ")
            print(ultraschallsensor.distanz())
            mischM = ultraschallsensor.distanz()

            verhaeltnisEcht = (mischM / alcM) * 100
#            print("es sind", "% lakohol im Glas" sep=verhaeltnisEcht)

        pump.stopPump()

    else:
        print("Es konnte kein Mischgetränk eingefüllt werden, suche nach fehlern.")

    def dataImport():
        startHoehe = ultraschallsensor.distanz() #starthoehe für Glasgrösse
        fuellHoehe = startHoehe * 0.9
        alcnumber = request.forms.get('drinks')
        id_mischv = request.forms.get('mischverhaeltnis')
        drinknumber = request.forms.get('AlkoholAuswahl_1')
        fillA = fuellHoehe * (mischV / 100)
        fillB = fuellHoehe
        enter(drinknumber, alcnumber)


run(host='192.168.178.72', reloader=True, port=8080, debug=True)
