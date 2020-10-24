#!/usr/bin/python
#-*- coding:utf-8 -*-#
class App:
    import time
    import math
    import pump
    import RPi.GPIO as GPIO

    #wird direkt ausgfuehrt, werte initialisieren
    #Noch ausweiten auf mehrere Getraenke pro Bestellung
    def __init__(self, orderlist):
        self.order_list = orderlist
        self.FLOW_SENSOR = 20
        self.count = 0
        self.GPIO.setmode(self.GPIO.BCM)

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
                    self.time.sleep(5)

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

            zaehler = 0

            self.GPIO.setup(self.FLOW_SENSOR, self.GPIO.IN, pull_up_down = self.GPIO.PUD_UP)

            def countPulse(channel):
                if start_counter == 1:
                    self.count = self.count + 1

            self.GPIO.add_event_detect(self.FLOW_SENSOR, self.GPIO.FALLING, callback=countPulse)
            flow_array = []
            self.counter = 0
            self.pump.startPump(drink) #drink gibt an welche pumpe gestartet wird
            while True:
                start_counter = 1
                self.time.sleep(1)
                start_counter = 0
                flow = ((self.count / 7.5) * 16.6666) # Pulse frequency (Hz) = 7.5Q, Q is flow rate in L/min.
                print("The flow is: %.3f ml/sek" % (flow))
                flow_array.append(flow)
                flow_all = sum(flow_array)
                print("gesamt durchfluss: {}".format(flow_all))
                self.count = 0
                if flow_all < fillUp:
                    zaehler = zaehler + 1
                    #Debug
                    print("while schleife durchfuehrung nummer: {}".format(zaehler))
                    print("es wurde aufgefuellt: {} ml".format(flow_all))

                elif flow_all >= fillUp:
                    self.pump.stopPump()
                    print("flow ist größer oder gleich fillUp")
                    print("es wurde aufgefuellt:{} ml".format(flow_all))
                    break
                else:
                    self.pump.stopPump()
                    print("FEHLER!")
                    break

        except KeyboardInterrupt:
            print('\nkeyboard interrupt!')
            self.GPIO.cleanup()
