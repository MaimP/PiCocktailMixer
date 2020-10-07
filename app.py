#!/usr/bin/python
#-*- coding:utf-8 -*-#
import time
import math
import ultraschallsensor
import pump

class App:
    import ultraschallsensor
    import pump

    order_list = []
    drink_list = []

    #wird direkt ausgfuehrt, werte initialisieren
    #Noch ausweiten auf mehrere Getraenke pro Bestellung
    def __init__(self, orderlist):
        self.order_list = orderlist
        self.ultraschall_first = ultraschallsensor.realDistance() #Glashoehe
        self.process = True
        self.fillup_time = 0.2 #muss ermittelt werden, zeit wieviel pro sekunde aufgefüllt wird

    def orderManager(self):
        #nach auffuellen self.number+1 loeschen um nächste bestellung fortzufahren
        #Bestellung in einem Array festhalten, immer
        #debug, ob ordernumber funktioniert
#        print("deine Bestelleung ist an stelle: {}".format(self.ordernumber))
        self.startHoehe = self.ultraschall_first #starthoehe für Glasgrösse
        self.fuellHoehe = 3
        self.glasHoehe = (self.startHoehe - 3)

        y = self.order_list[0]

        #fuehre methode zum satrten aller pumpen aus
        for x in range(y):
            self.start()

        self.order_list.pop(0)
        self.process = False

    def start(self):
        #schreibe die Getraenke aus dem Array fuer neue Bestellung raus
        #nach ausfuehren aller die Bestellung aus Array loeschen,
        #neueBestellung auf True setzten
        drink = self.order_list[1]  #Getraenkenummer
        mischv = self.order_list[2] #mischverhaeltnis muss noch in Array geschrieben werden
        #loesche Eintraege in Array
        self.order_list.pop(1)
        self.order_list.pop(1)

        actually = self.ultraschall_first
        fillUp = int(actually) - (int(self.glasHoehe) * (int(mischv) / 100))

        distance_list = []
        entfernung = ultraschallsensor.realDistance()
        distance_list.append(entfernung)
        print("starte Pumpe, Starthoehe: {}".format(entfernung))
        pump.startPump(drink) #drink gibt an welche pumpe gestartet wird
        start_time = time.time()
        print("wird jetzt aufgefuellt bis: {}".format(fillUp))

        zaehler = 0
        while True:
            entfernung = ultraschallsensor.returnDistance()
            next_time = time.time()
            if (start_time - next_time) * entfernung * 0.95 < distance_list[0] < entfernung * 1.1:
                distance_list.append(entfernung)
                distance_list.pop(0)

                zaehler = zaehler + 1
                #Debug
                print("while schleife durchfuehrung nummer: {}".format(zaehler))
                print("die aktuelle Entfernung betraegt: {}".format(entfernung))
                hoehe = entfernung
                aufgefuellt = self.startHoehe - hoehe
                print("insgesamt wurden aufgefuellt::{}".format(aufgefuellt))
                auffuellen = hoehe - fillUp
                print("muss jetzt noch auffuellen: {}".format(auffuellen))
                if entfernung > fillUp:
                    time.sleep(0.2)


                elif entfernung <= fillUp:
                    pump.stopPump()
                    #Debug
                    print("Die pumpe wurde ausgeschaltet. aktuelle entfernung: {} cm".format(entfernung))
                    print("das Glas sollte jetzt aufgefuellt werden bis: {}".format(fillUp))
                    break

                else:
                    print("Fehler!")
                    pump.stopPump()
                    break
            else:
                pass
