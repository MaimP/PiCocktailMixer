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
        self.ultraschall_first = ultraschallsensor.real_distance() #Glashoehe
        self.process = True
        self.fillup_time = 0.2 #muss ermittelt werden, zeit wieviel pro sekunde aufgefüllt wird

    def orderManager(self):
        #nach auffuellen self.number+1 loeschen um nächste bestellung fortzufahren
        #Bestellung in einem Array festhalten, immer
        #debug, ob ordernumber funktioniert
#        print("deine Bestelleung ist an stelle: {}".format(self.ordernumber))
        self.startHoehe = self.ultraschall_first #starthoehe für Glasgrösse
        self.fuellHoehe = 5
        self.glasHoehe = (self.startHoehe - 5)
        #Mischverhaeltnisse muessen noch auf mehrere Getraenke angepasst werden,
        #erstemal bei zwei lassen
        global unroundA
        global unroundB
#        unroundA = self.startHoehe - (self.glasHoehe * (int(self.id_mischv)) / 100)
#        unroundB = self.fuellHoehe
#        self.fillA = round(unroundA, 2)
#        self.fillB = round(unroundB, 2)

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
        self.order_list.pop(2)

        actually = self.ultraschall_first
        fillUp = int(actually) - (int(self.glasHoehe) * (int(mischv) / 100))

        last_distance = []
        zaehler = 0
        while True:
            if zaehler == 0:
                entfernung = ultraschallsensor.realDistance()
                last_distance.append(entfernung)
                pump.startPump(drink) #drink gibt an welche pumpe gestartet wird

            else:
                entfernung = ultraschallsensor.returnDistance()
                zaehler = zaehler + 1
                print("while schleife durchfuehrung nummer: {}".format(zaehler))
                print("die aktuelle Entfernung betraegt: {}".format(entfernung))
                if entfernung > fillUp:
                    hoehe = entfernung
                    print("Das Glas wird bis zur Hoehe aufgefuellt: {}".format(self.fuellHoehe))
                    print("Das Glas wird bis zu .. mit Alkohol aufgefuellt: {}".format(fillUp))
                    aufgefuellt = self.startHoehe - hoehe
                    print("die aufgefüllte Menge an Alkohol beträgt:{}".format(aufgefuellt))
                    auffuellen = fillUp - aufgefuellt
                    print("fillA: es muss noch aufgefuellt werden: {} cm Alkohol".format(auffuellen))
                    time.sleep(0.1)


                elif entfernung <= fillUp:
                    pump.stopPump()
                    print("Die pumpe wurde ausgeschaltet. Im Glas sind: {} cm".format(entfernung))
                    break

                else:
                    print("Fehler!")
                    break
