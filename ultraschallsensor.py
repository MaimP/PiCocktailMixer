#!/usr/bin/python
#-*- coding:utf-8 -*-
#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time

#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#GPIO Pins zuweisen
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distanz():
    #GPIO Modus (BOARD / BCM)
    GPIO.setmode(GPIO.BCM)

    #GPIO Pins zuweisen
    GPIO_TRIGGER = 18
    GPIO_ECHO = 23

    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)

    now = time.time()
    future = now + 0.1
    # setze Trigger auf HIGH
    GPIO.output(GPIO_TRIGGER, True)
    # debug
    #print("setze trigger auf high")

    # setze Trigger nach 0.01ms aus LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    # debug
    #print("setze trigger auf low")

    StartZeit = time.time()
    StopZeit = time.time()

    # speichere Startzeit
    while GPIO.input(GPIO_ECHO) == 0 and time.time() < future:
        StartZeit = time.time()
    #    print("echo == 0")

    # speichere Ankunftszeit
    while GPIO.input(GPIO_ECHO) == 1:
        StopZeit = time.time()
    #    print("echo == 1")

    # Zeit Differenz zwischen Start und Ankunft
    TimeElapsed = StopZeit - StartZeit
    # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
    # und durch 2 teilen, da hin und zurueck
    strecke = (TimeElapsed * 34300) / 2
    distanz = round(strecke, 1)

    return distanz

#Fehlmessungensvermeidung
def realDistance():
    import collections
    from collections import Counter
    distance_list = []
    #prüft ob Messung nicht wegen Zeitueberschreitunbg abgebrochen worden ist distanz()
    counterc = 0
    while True:
        if counterc <= 50:
            d = returnDistance()
            if d > 1:
                distance_list.append(d)
                counterc = counterc + 1
            else:
                pass

            time.sleep(0.02) #maximal 50 Messungen pro sekunde
        else:
            break

    counter=collections.Counter(distance_list)
    print(counter)
    mostcommon = counter.most_common(1)
    print("die häufigste entfernung ist:{}".format(mostcommon))
    new_distancelist = [item for items, c in Counter(distance_list).most_common() for item in [items] * c]
    distance = new_distancelist[0]
    return distance


def returnDistance():
    while True:
        x = distanz()
        if x > 1:
            print("x ist größer als null, break {}".format(x))
            return x
            break
        else:
            print("x ist kleiner als null {}".format(x))
            pass


if __name__ == '__main__':
    try:
        while True:
            abstand = realDistance()
            print ("Gemessene Entfernung = %.1f cm" % abstand)
            time.sleep(1)

        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        GPIO.cleanup()
