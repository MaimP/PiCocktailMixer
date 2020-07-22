#!/usr/bin/python
#-*- coding:utf-8 -*-#
class App:
    import server
    import ultraschallsensor
    import pump

    order_list = []

    #wird direkt ausgfuehrt, werte initialisieren
    #Noch ausweiten auf mehrere Getraenke pro Bestellung
    def __init__(self,):
        #Variabel für Anzahl der getraenke pro Bestelleung
        self.number = 2 #muss noch variabel werden

        self.startHoehe = ultraschallsensor.real_distance() #starthoehe für Glasgrösse
        self.fuellHoehe = 5
        self.glasHoehe = (startHoehe - 5)
        self.alcnumber = server.request.forms.get('drinks')
        self.id_mischv = server.request.forms.get('mischverhaeltnis')
        self.drinknumber = server.request.forms.get('AlkoholAuswahl_1')
        self.drinknumber = int(drinknumber)
        global unroundA
        global unroundB
        unroundA = startHoehe - (glasHoehe * (int(id_mischv)) / 100)
        unroundB = fuellHoehe
        self.fillA = round(unroundA, 2)
        self.fillB = round(unroundB, 2)

        #provisorisches dict fuer zwei Getraenke:
        self.order_dict{
        "1": self.drinknumber
        "2": self.alcnumber
        }

        #debug, ob richtig in dict aufgenommen
        print("order dict 1: {}, order dict 2:{}".format(self.order_dict.values("1"), self.order_dict("2")))
        #schreibt dict für liste in orderManager()
#        counter4 = 0
#        for x in range(self.number):
#            counter4 = counter4 + 1
#            order_dict[counter4] = self.drinknumber
        orderManager()
        #loescht dict fuer naschte Bestellung
        del order_dict

    def orderManager(self):
        #nach auffuellen self.number+1 loeschen um nächste bestellung fortzufahren
        #Bestellung in einem Array festhalten, immer
        counter3 = 0
        self.order_list.append(self.number)
        for x in range(self.number):
            counter3 = counter3 + 1
            #gibt in Value(Getraenkenummer) aus, mit dem "Index" von Counter3
            drink = self.order_dict.values(counter3)
            #macht eine Liste mit den Getraenkenummer
            #im Format: Anzahl der Getraenke, getraenk1, getraenk2, ...
            self.order_list.append(drink)
            #gibt die Laenge des Arrays aus
            order_len = len(order_list)
            #debug, wie range zaehlt, ob bei 0 oder 1 anfaengt und ob alles funkt.
            print("der counter ist bei: {}, drink(von dict): {}, order_list an Stelle:{} ".format(counter3, drink, order_len))

        #Bestellposition: Bestellung wird in einem Array festgehalten
        self.ordernumber_raw = len(order_list)
        self.ordernumber = self.ordernumber_raw / self.number + 1
        #debug, ob ordernumber funktioniert
        print("deine Bestelleung ist an stelle: {}".format(self.ordernumber))

        #fuehre methode zum satrten aller pumpen aus
        pass
        #loesche liste fuer naechste Bestellung:


    def start(self):
        for x in self.order_list[1]:

            number_for = x
            zaehler = 0
            #für mischverhaeltnis Höhe berechnen wieviel eingefüllt werden soll
            #erst Alkohol dann
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
                if entfernung > self.fillA:
                    hoehe = entfernung
                    print("Das Glas wird bis zur Hoehe aufgefuellt: {}".format(fuellHoehe))
                    print("Das Glas wird bis zu .. mit Alkohol aufgefuellt: {}".format(fillA))
                    if zaehler == 1:
                        pump.startPump(alc) #alc gibt an welche pumpe gestartet wird
                        zustand = True

                    elif zustand:
                        #debugging
                        print("while schleife alkohol einfüllen")
                        aufgefuellt = self.startHoehe - hoehe
                        print("die aufgefüllte Menge an Alkohol beträgt:{}".format(aufgefuellt))
                        auffuellen = self.fillA - aufgefuellt
                        print("fillA: es muss noch aufgefuellt werden: {} cm Alkohol".format(auffuellen))
                        time.sleep(0.1)

                    else:
                        print("Die while Schleife hat keine passende if Anweisung.")

                elif entfernung <= self.fillA:
                    pump.stopPump()
                    print("Die pumpe wurde ausgeschaltet. Im Glas sind: {} cm".format(entfernung))
                    zustand == False
                    break

                else:
                    print("while schleife auffuellen schief gelaufen.")
                    break

    def enter(alc, misch):
        try:

            print(alc)
            print(misch)
            print("Die Starthoehe betraegt: {}".format(self.startHoehe))
            print("test round: {}".format(self.fillA))
            zaehler = 0
            zaehler2 = 0
            #für mischverhaeltnis Höhe berechnen wieviel eingefüllt werden soll
            #erst Alkohol dann
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
                if entfernung > self.fillA:
                    hoehe = entfernung
                    print("Das Glas wird bis zur Hoehe aufgefuellt: {}".format(fuellHoehe))
                    print("Das Glas wird bis zu .. mit Alkohol aufgefuellt: {}".format(fillA))
                    if zaehler == 1:
                        pump.startPump(alc) #alc gibt an welche pumpe gestartet wird
                        zustand = True

                    elif zustand:
                        #debugging
                        print("while schleife alkohol einfüllen")
                        aufgefuellt = self.startHoehe - hoehe
                        print("die aufgefüllte Menge an Alkohol beträgt:{}".format(aufgefuellt))
                        auffuellen = self.fillA - aufgefuellt
                        print("fillA: es muss noch aufgefuellt werden: {} cm Alkohol".format(auffuellen))
                        time.sleep(0.1)

                    else:
                        print("Die while Schleife hat keine passende if Anweisung.")

                elif entfernung <= self.fillA:
                    pump.stopPump()
                    print("Die pumpe wurde ausgeschaltet. Im Glas sind: {} cm".format(entfernung))
                    zustand == False
                    break

                else:
                    print("while schleife auffuellen schief gelaufen.")
                    break

            print("Das Einfuellen des Alkohols ist abgeschlossen, es wird mit dem Mischgetraenk fortgefahren.")

            while True:
                entfernung = ultraschallsensor.real_distance()

                zaehler = zaehler + 1
                print("while schleife durchfuehrung nummer: {}".format(zaehler))
                print("die aktuelle Entfernung betraegt: {}".format(entfernung))
                if entfernung > self.fillB:
                    hoehe = entfernung
                    print("Das Glas wird bis zur Hoehe aufgefuellt: {}".format(fuellHoehe))
                    print("Das Glas wird bis zu .. mit dem Mischgetraenk aufgefuellt: {}".format(fillB))
                    if zaehler2 == 0:
                        zaehler2 = zaehler2 + 1
                        pump.startPump(misch) #misch gibt an welche pumpe gestartet wird
                        zustand = True

                    elif zustand:
                        #debugging
                        print("while schleife Mischgetraenk einfüllen")
                        aufgefuellt = self.startHoehe - hoehe
                        print("die aufgefüllte Menge an Getraenk beträgt insgesamt:{} cm".format(aufgefuellt))
                        auffuellen = self.fillB - aufgefuellt
                        print("Es muss noch insgesamt aufgefuellt werden: {} cm".format(auffuellen))
                        time.sleep(0.1)

                    else:
                        print("Die while Schleife hat keine passende if Anweisung.")

                elif entfernung <= self.fillB:
                    pump.stopPump()
                    print("Die pumpe wurde ausgeschaltet. Im Glas sind: {} cm".format(entfernung))
                    zustand == False
                    break

                else:
                    print("while schleife auffuellen schief gelaufen.")
                    break

        # Beim Abbruch durch STRG+C resetten
        except KeyboardInterrupt:
            print("Messung vom User gestoppt")
            pump.stopPump()
