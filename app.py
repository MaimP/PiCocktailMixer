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
        self.counter_array = 0
        self.counter_all = 0

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
        self.drinks_misch = []
        for x in range(self.menge):
            if counter_menge == 0:
                self.process = False
                counter_menge += 1
            while True:
                if not self.process:
                    self.process = True
                    for x in range(anzahl):
                        self.drinks_misch.append(self.order_list[3])
                        self.drinks_misch.append(self.order_list[4])
                        self.order_list.pop(3)
                        self.order_list.pop(3)
                        self.start()
                    self.counter_array = 0
                    break
                else:
                    #thread oder sowas wartet auf False von website
                    self.time.sleep(5)

        self.order_list.pop(0) #loesche
        self.order_list.pop(0)
        self.order_list.pop(0)
        self.counter_array = 0
        self.process = False

    def start_next_cup(self):
        '''falls fehler beim starten von befuellen des naechsten
        Bechers, starte manuell über website'''
        self.process = True

    def start(self):
        try:
            self.drink = self.drinks_misch[self.counter_array]
            self.counter_array += 1
            self.mischv = self.drinks_misch[self.counter_array]
            self.counter_array += 1
            fillUp = (self.volume / 100) * self.mischv #berechnet wieviel aufgefuellt werden muss in ml
            print("wird jetzt aufgefuellt bis: {} ml".format(fillUp))

            zaehler = 0

            self.GPIO.setmode(self.GPIO.BCM)
            self.GPIO.setup(self.FLOW_SENSOR, self.GPIO.IN, pull_up_down = self.GPIO.PUD_UP)

            def countPulse(channel):
                self.count += 1
                self.counter_all += 1
                print(f"flow_all: {self.flow_all}")

            self.GPIO.add_event_detect(self.FLOW_SENSOR, self.GPIO.FALLING, callback=countPulse)
            flow_array = []
            self.counter = 0
            self.pump.startPump(self.drink) #self.drink gibt an welche pumpe gestartet wird
            while True:
            #    self.start_counter = 1
            #    self.time.sleep(1)
            #    self.start_counter = 0
            #    flow = ((self.count / 7.5) * 16.6666) # Pulse frequency (Hz) = 7.5Q, Q is flow rate in L/min.
            #    print("The flow is: %.3f ml/sek" % (flow))
            #    flow_array.append(flow)
                self.flow_all = self.counter_all * 0.06
            #    print("gesamt durchfluss: {}".format(flow_all))
            #    self.count = 0
                if self.flow_all < fillUp:
                    zaehler = zaehler + 1
                    #Debug
                #    print("while schleife durchfuehrung nummer: {}".format(zaehler))
                #    print("es wurde aufgefuellt: {} ml".format(flow_all))

                elif self.flow_all >= fillUp:
                    self.pump.stopPump()
                    print("flow ist größer oder gleich fillUp")
                    print("es wurde aufgefuellt:{} ml".format(self.flow_all))
                    return False
                else:
                    self.pump.stopPump()
                    print("FEHLER!")
                    break

        except KeyboardInterrupt:
            print('\nkeyboard interrupt!')
            print(f"counter_all: {self.counter_al}")
            self.GPIO.cleanup()
            self.pump.stopPump()
