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
                entfernung = ultraschallsensor.real_distance()
                last_distance.append(entfernung)

            else:
                #filtert falsche Messwerte aus
                self.start_time = time.time() #erfasse startzeit, um entfernung zu berechnen
                loop_counter = 0 #Schleifenzaehler fuer zu viele falsche Messungen
                while True:
                    print("start: anfang entfernungsvorgang")
                    entfernung = ultraschallsensor.return_distance() #messe entfernung, wird ueberprueft ob richtig
                    new_time = time.time() #messe neue Zeit, um meogl. aufgefuellte Menge zu berechnen
                    elapsed = new_time - self.start_time #Zeitdifferenz
                    possible_distance = elapsed * self.fillup_time #berechne neue moegl. Entfernung
                    distance_length = len(last_distance) #erfasse laenge des arrays, um letzten Wert aus Array zu nehmen fuer berechnung
                    distance_before = last_distance[distance_length - 1] #speichere die alte Entfernung
                    distance_difference = distance_before - entfernung #differenz zwischen beiden Entfernungen
                    if distance_difference * 0.80 <= possible_distance >= 1.2 * distance_difference: #prueft ob gemessene entfernung im Intervall liegt, Abweichung max. 20%
                        print("entfernung liegt im Intervall")
                        last_distance.append(entfernung)
                        self.start_time = time.time() #erfasse neue Startzeit für naechste Messung
                        return entfernung #Messung war korrekt, entfernung wird benutzt
                        break
                    else:
                        loop_counter = loop_counter + 1 #zaehle wie oft Messung nicht im Toleranzbereich lag
                        if loop_counter <= 7: #wenn Messung nicht oefter als 7 mal falsch war neue Messung
                            print("start: else Schleife <= 7")
                        else:
                            pump.stopPump() #zu viele falsche Messungen
                            entfernung = ultraschallsensor.real_distance() #stoppe Pumpen um neuen Startwert zu erfassen
                            last_distance.append(entfernung)
                            self.start_time = time.time() #erfasse neue Startzeit fuer naechste Messung
                            return entfernung
                            break



            zaehler = zaehler + 1
            print("while schleife durchfuehrung nummer: {}".format(zaehler))
            print("die aktuelle Entfernung betraegt: {}".format(entfernung))
            if entfernung > fillUp:
                hoehe = entfernung
                print("Das Glas wird bis zur Hoehe aufgefuellt: {}".format(self.fuellHoehe))
                print("Das Glas wird bis zu .. mit Alkohol aufgefuellt: {}".format(fillUp))
                if zaehler == 1:
                    pump.startPump(drink) #drink gibt an welche pumpe gestartet wird
                elif zustand:
                    aufgefuellt = self.startHoehe - hoehe
                    print("die aufgefüllte Menge an Alkohol beträgt:{}".format(aufgefuellt))
                    auffuellen = fillUp - aufgefuellt
                    print("fillA: es muss noch aufgefuellt werden: {} cm Alkohol".format(auffuellen))
                    time.sleep(0.1)

                else:
                    print("Die while Schleife hat keine passende if Anweisung.")

            elif entfernung <= fillUp:
                pump.stopPump()
                print("Die pumpe wurde ausgeschaltet. Im Glas sind: {} cm".format(entfernung))
                break
