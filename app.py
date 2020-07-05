#!/usr/bin/python
#-*- coding:utf-8 -*-#
import ultraschallsensor
import getData
import pump

def dataImport():
    import server

    startHoehe = ultraschallsensor.distanz() #starthoehe für Glasgrösse
    fuellHoehe = startHoehe * 0.9
    alcnumber = server.request.forms.get('drinks')
    id_mischv = server.request.forms.get('mischverhaeltnis')
    drinknumber = server.request.forms.get('AlkoholAuswahl_1')
    fillA = fuellHoehe * (mischV / 100)
    fillB = fuellHoehe

def enter(alc, misch):
#    dataImport()
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
