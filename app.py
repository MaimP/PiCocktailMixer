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

    def __init__(self, orderlist):
        self.order_list = orderlist
        self.ultraschall_real = ultraschallsensor.real_distance()
        counter5 = 0
        t = len(self.order_list)
        for x in range(t):
            x = self.order_list[counter5]
            print("class App: order list: {}".format(x))
        self.process = True

    #wird direkt ausgfuehrt, werte initialisieren
    #Noch ausweiten auf mehrere Getraenke pro Bestellung
    def order(self):
        self.name = name
        #für warteschelife, zeigt an an welcher position deine Bestellung ist
        ordernumber_raw = 0
        #für ordernumber, um im Array postion zu finden, wo als naechstes fortgefahren werden soll
        x = 0
        if len(order_list) > 0:
            x = order_list[0] + 1 #order_list[0] * 2, weil noc hmoischverhaeltnis reingeschrieben werden muss
            ordernumber_raw = ordernumber_raw + 1
            while True:
                if x < len(order_list):
                    x = x + order_list[x] + 1
                    ordernumber_raw = ordernumber_raw + 1
                else:
                    self.ordernumber = math.ceil(ordernumber_raw)
                    print("Deine Bestellung ist an Position: {}".format(self.ordernumber))
                    break
        else:
            print("Dein Bestellung ist an erster Position")


        #Variabel für Anzahl der getraenke pro Bestelleung
        self.number = 0

        #muss auch noch in Array geschrieben werden
        self.id_mischv = server.request.forms.get('mischverhaeltnis')
        if server.request.forms.get('drink1') != 6:
            self.drink1 = server.request.forms.get('drink1')
            drink_list.append(self.drink1)
#           mischv1 = server.request.forms.get('mischv1')
            self.number = self.number + 1
            if server.request.forms.get('drink2') != 6:
                self.drink2 = server.request.forms.get('drink2')
                drink_list.append(self.drink2)
    #           mischv2 = server.request.forms.get('mischv2')
                self.number = self.number + 1
                if server.request.forms.get('drink3') != 6:
                    self.drink3 = server.request.forms.get('drink3')
                    drink_list.append(self.drink3)
        #           mischv3 = server.request.forms.get('mischv3')
                    self.number = self.number + 1
                    if server.request.forms.get('drink4') != 6:
                        self.drink4 = server.request.forms.get('drink4')
                        drink_list.append(self.drink4)
            #           mischv4 = server.request.forms.get('mischv4')
                        self.number = self.number + 1
                        if server.request.forms.get('drink5') != 6:
                            self.drink5 = server.request.forms.get('drink5')
                            drink_list.append(self.drink5)
                #           mischv5 = server.request.forms.get('mischv5')
                            self.number = self.number + 1
                            if server.request.forms.get('drink6') != 6:
                                self.drink6 = server.request.forms.get('drink6')
                                drink_list.append(self.drink6)
                    #           mischv6 = server.request.forms.get('mischv6')
                                self.number = self.number + 1
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass


        #schreibt bestellung in Array
        counter3 = 0
        self.order_list.append(self.number)
        for x in range(self.number):
            counter3 = counter3 + 1
            drink = self.drink_list[counter3]
            #gibt in Value(Getraenkenummer) aus, mit dem "Index" von Counter3
#            drink = self.order_dict.values(counter3)
            #macht eine Liste mit den Getraenkenummer
            #im Format: Anzahl der Getraenke, getraenk1, getraenk2, ...
            self.order_list.append(drink)
            #debug, wie range zaehlt, ob bei 0 oder 1 anfaengt und ob alles funkt.
            print("der counter ist bei: {}, hinzugefuegtes Getraenk in drink_lkist: {}".format(counter3, drink))
        #loesche Array um neue Bestellung aufzunehmen
        del self.drink_list

        while True:
            #führe ordermanager aus mit Bestellungsarray
            if process == False:
                orderManager(self)
                print("Dein Getraenk wird nun aufgefuellt")
                break
            else:
                time.sleep(3)
                print("ein anderes Getraenk wird noch aufgefuellt, warte noch einen Augenblick")

    def orderManager(self):
        #nach auffuellen self.number+1 loeschen um nächste bestellung fortzufahren
        #Bestellung in einem Array festhalten, immer
        #debug, ob ordernumber funktioniert
#        print("deine Bestelleung ist an stelle: {}".format(self.ordernumber))
        self.startHoehe = self.ultraschall_real #starthoehe für Glasgrösse
        self.fuellHoehe = 5
        self.glasHoehe = (startHoehe - 5)
        #Mischverhaeltnisse muessen noch auf mehrere Getraenke angepasst werden,
        #erstemal bei zwei lassen
        global unroundA
        global unroundB
        unroundA = startHoehe - (glasHoehe * (int(id_mischv)) / 100)
        unroundB = fuellHoehe
        self.fillA = round(unroundA, 2)
        self.fillB = round(unroundB, 2)

        y = self.order_list[0]
        #fuehre methode zum satrten aller pumpen aus
        for x in range(y):
            start(self)

        self.order_list.pop(0)
        self.process = False

    def start(self):
        #schreibe die Getraenke aus dem Array fuer neue Bestellung raus
        #nach ausfuehren aller die Bestellung aus Array loeschen,
        #neueBestellung auf True setzten
        drink = self.order_list[1]  #Getraenkenummer
        mischv = self.id_mischv #mischverhaeltnis muss noch in Array geschrieben werden
#        mischv = self.order_list[2] #Mischverhaeltnis
        #loesche Eintraege in Array
        self.order_list.pop(1)
#        self.order_list.pop(2)

        actually = ultraschallsensor.real_distance()
        fillUp = actually - (glasHoehe * (mischv / 100))

        zaehler = 0
        while True:
            if zaehler == 0:
                entfernung = ultraschallsensor.first_realDistance()
                return entfernung

            else:
                entfernung = ultraschallsensor.real_distance()
                return entfernung

            zaehler = zaehler + 1
#            progress = (startHoehe - entfernung) / glasHoehe * 100
#            prog = int(progress)
#            progress(prog)
            print("while schleife durchfuehrung nummer: {}".format(zaehler))
            print("die aktuelle Entfernung betraegt: {}".format(entfernung))
            if entfernung > fillUp:
                hoehe = entfernung
                print("Das Glas wird bis zur Hoehe aufgefuellt: {}".format(fuellHoehe))
                print("Das Glas wird bis zu .. mit Alkohol aufgefuellt: {}".format(fillUp))
                if zaehler == 1:
                    pump.startPump(drink) #alc gibt an welche pumpe gestartet wird
                    zustand = True
                elif zustand:
                    aufgefuellt = self.startHoehe - hoehe
                    print("die aufgefüllte Menge an Alkohol beträgt:{}".format(aufgefuellt))
                    auffuellen = self.fillUp - aufgefuellt
                    print("fillA: es muss noch aufgefuellt werden: {} cm Alkohol".format(auffuellen))
                    time.sleep(0.1)

                else:
                    print("Die while Schleife hat keine passende if Anweisung.")

            elif entfernung <= self.fillUp:
                pump.stopPump()
                print("Die pumpe wurde ausgeschaltet. Im Glas sind: {} cm".format(entfernung))
                zustand == False
                break

    def getMischV():
        pass
