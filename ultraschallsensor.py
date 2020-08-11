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
    future = now + 1
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

def entfernung():
    while True:
        abstand = distanz()
        return abstand
        time.sleep(0.1)

def first_realDistance():
    import collections
    from collections import Counter
    distance_list = []
    counterc = 0
    for x in range(200):
        d = distanz()
        distance_list.append(d)
        counterc = counterc + 1
#        print("test real_distance liste erstellen: {}".format(counterc))
        time.sleep(0.021) #maximal 50 Messungen pro sekunde

    counter=collections.Counter(distance_list)
    print(counter)
    mostcommon = counter.most_common(1)
    print("die häufigste entfernung ist:{}".format(mostcommon))
    new_distancelist = [item for items, c in Counter(distance_list).most_common() for item in [items] * c]
    distance = new_distancelist[0]
    return distance

#Fehlmessungensvermeidung
def real_distance():
    import collections
    from collections import Counter
    distance_list = []
    counterc = 0
    for x in range(100):
        d = distanz()
        distance_list.append(d)
        counterc = counterc + 1
#        print("test real_distance liste erstellen: {}".format(counterc))
        time.sleep(0.02) #maximal 50 Messungen pro sekunde

    counter=collections.Counter(distance_list)
    print(counter)
    mostcommon = counter.most_common(1)
    print("die häufigste entfernung ist:{}".format(mostcommon))
    new_distancelist = [item for items, c in Counter(distance_list).most_common() for item in [items] * c]
    distance = new_distancelist[0]
    return distance
    # [(1, 4), (2, 4), (3, 2)]
def return_distance():
    while True:
        x = distanz()
        if x > 1 and x < 20:
            break
            return x
        else:
            pass


if __name__ == '__main__':
    try:
        while True:
            abstand = return_distance()
            print ("Gemessene Entfernung = %.1f cm" % abstand)
            time.sleep(1)

        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        GPIO.cleanup()
