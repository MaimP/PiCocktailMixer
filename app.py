import ultraschallsensor
import getData
import pump

def dataImport():
    startHoehe = ultraschallsensor.distanz() #starthoehe für Glasgrösse
    fuellHoehe = startHoehe * 0.9
    alc = getData.alcnumber #input von HTML welcher Alkohol
    misch = getData.drinknumber #input von HTML mischgetraenk
    mischV = getData.id_mischv #id_mischv = input von HTML Mischverhaeltnis
    fillA = fuellHoehe * (mischV / 100)
    fillB = fuellHoehe

def submit():
    #für mischverhaeltnis Höhe berechnen wieviel eingefüllt werden soll
    #erst Alkohol dann
    while ultraschallsensor.entfernung() <= fillA:
        pump.startPump(alc) #alc gibt an welche pumpe gestartet wird

        print("die aufgefüllte Menge an Alkohol beträgt:") #debugging
        print(ultraschallsensor.distand())
        alcM = ultraschallsensor.distanz() #debugging: Menge an aufgefülltem alc

    if fuellHoehe * (mischV / 120) <= fillA <= FUELLHOEHE * (mischV / 80):
        while ultraschallsensor.entfernung() <= fillB:
            pump.startPump(misch) #misch gibt an welche Pumpe gestartet wird

            print("in dem getränk sind nung insgesamt: ")
            print(ultraschallsensor.distanz())
            mischM = ultraschallsensor.distanz()

            verhaeltnisEcht = (mischM / alcM) * 100
            print("es sind", "% lakohol im Glas" sep=verhaeltnisEcht)

    else:
        print("Es konnte kein Mischgetränk eingefüllt werden, suche nach fehlern.")
