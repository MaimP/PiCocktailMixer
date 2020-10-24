#!/usr/bin/python
#-*- coding:utf-8 -*-#
class App:
    import time
    import math
    import pump as pm
    import flowSensor as fs

    #wird direkt ausgfuehrt, werte initialisieren
    #Noch ausweiten auf mehrere Getraenke pro Bestellung
    def __init__(self, orderlist):
        self.order_list = orderlist

    def orderManager(self):
        #nach auffuellen self.number+1 loeschen um nächste bestellung fortzufahren
        #Bestellung in einem Array festhalten, immer
        #debug, ob ordernumber funktioniert
        self.volume = self.order_list[2] #welches Volumen das Glas hat
        print("volume: {}".format(self.volume))
        self.volume = int(self.volume) #welches Volumen das Glas hat
        print("volume: {}".format(self.volume))
        self.menge = int(self.order_list[1]) #wieviele von diesem Cocktail
        anzahl = self.order_list[0] #wiviele Getraenke pro Glas

        counter_menge = 0
        for x in range(self.menge):
            if counter_menge == 0:
                self.process = False

            while True:
                if not self.process:
                    self.process = True
                    for x in range(anzahl):
                        self.start()
                    break
                else:
                    #thread oder sowas wartet auf False von website
                    time.sleep(5)

        self.order_list.pop(0)
        self.order_list.pop(0)
        self.order_list.pop(0)
        self.process = False

    def start_next_cup():
        '''falls fehler beim starten von befuellen des naechsten
        Bechers, starte manuell über website'''
        self.process = True

    def start(self):
        try:
            #schreibe die Getraenke aus dem Array fuer neue Bestellung raus
            #nach ausfuehren aller die Bestellung aus Array loeschen,
            #neueBestellung auf True setzten
            drink = self.order_list[3]  #Getraenkenummer
            mischv = self.order_list[4] #mischverhaeltnis muss noch in Array geschrieben werden
            #loesche genutzte Werte in Array
            self.order_list.pop(1)
            self.order_list.pop(1)

            fillUp = (self.volume / 100) * mischv #berechnet wieviel aufgefuellt werden muss in ml
            print("wird jetzt aufgefuellt bis: {} ml".format(fillUp))

            flowSensor.measure() #muss dauerhaft Menge übermitteln

            pm.startPump(drink) #drink gibt an welche pumpe gestartet wird

            zaehler = 0
            while True:
                from flow_sensor import flow_all
                flow = flow_all
                if flow < fillUp:
                    zaehler = zaehler + 1
                    #Debug
                    print("while schleife durchfuehrung nummer: {}".format(zaehler))
                    print("es wurde aufgefuellt: {} ml".format(flow))

                elif flow >= fillUp:
                    pm.stopPump()
                    fs.process()
                    print("flow ist größer oder gleich fillUp")
                    print("es wurde aufgefuellt:{} ml".format(flow))
                    break
                else:
                    pm.stopPump()
                    print("FEHLER!")
                    break

        except KeyboardInterrupt:
            print('\nkeyboard interrupt!')
            fs.process()
            GPIO.cleanup()
