#!/usr/bin/python
#-*- coding:utf-8 -*-#
class App:
    import time
    import math
    import pump
    import flow_sensor

    #wird direkt ausgfuehrt, werte initialisieren
    #Noch ausweiten auf mehrere Getraenke pro Bestellung
    def __init__(self, orderlist):
        self.order_list = orderlist

    def messure(self):
        '''Die Funktion misst das Volumen des Glases um dann zu berechnen wieviel
        hineingefuellt werden soll, von dem Getraenk. (Vll noch vorgegebene Glaseser
        zur Auswahl stellen) Flüssigkeit wird gemessen durch flowmeter.py'''
        pass

    def orderManager(self):
        #nach auffuellen self.number+1 loeschen um nächste bestellung fortzufahren
        #Bestellung in einem Array festhalten, immer
        #debug, ob ordernumber funktioniert
        self.volume = self.order_list[2]
        self.menge = self.order_list[1]

        anzahl = self.order_list[0]

        for x < self.menge:
            if not self.process:
                self.process = True
                for x in range(anzahl):
                    self.start()
            else:
                #thread oder sowas wartet auf False von website

        self.order_list.pop(0)
        self.order_list.pop(0)
        self.order_list.pop(0)
        self.process = False

    def start_next_cup():
        '''falls fehler beim starten von befuellen des naechsten
        Bechers, starte manuell über website'''
        process = True

    def start(self):
        #schreibe die Getraenke aus dem Array fuer neue Bestellung raus
        #nach ausfuehren aller die Bestellung aus Array loeschen,
        #neueBestellung auf True setzten
        drink = self.order_list[3]  #Getraenkenummer
        mischv = self.order_list[4] #mischverhaeltnis muss noch in Array geschrieben werden
        #loesche genutzte Werte in Array
        self.order_list.pop(1)
        self.order_list.pop(1)

        fillUp = (self.volume / 100) * mischv #berechnet wieviel aufgefuellt werden muss in ml

        pump.startPump(drink) #drink gibt an welche pumpe gestartet wird
        print("wird jetzt aufgefuellt bis: {} ml".format(fillUp))

        flow_sensor.measure() #muss dauerhaft Menge übermitteln

        zaehler = 0
        while True:
            from flow_sensor import flow_all
            flow = flow_all
            if flow < fillUp:
                zaehler = zaehler + 1
                #Debug
                print("while schleife durchfuehrung nummer: {}".format(zaehler))
                print("es wurde aufgefuellt: {} ml".format(flow))

            else if flow >= fillUp:
                pump.stopPump()
                flow_sensor.process()
                print("flow ist größer oder gleich fillUp")
                print("es wurde aufgefuellt:{} ml".format(flow))

            else:
                print("FEHLER!")
