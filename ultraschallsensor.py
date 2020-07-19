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
    GPIO_ECHO = 24

    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)

    # setze Trigger auf HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # setze Trigger nach 0.01ms aus LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartZeit = time.time()
    StopZeit = time.time()

    # speichere Startzeit
    while GPIO.input(GPIO_ECHO) == 0:
        StartZeit = time.time()

    # speichere Ankunftszeit
    while GPIO.input(GPIO_ECHO) == 1:
        StopZeit = time.time()

    # Zeit Differenz zwischen Start und Ankunft
    TimeElapsed = StopZeit - StartZeit
    # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
    # und durch 2 teilen, da hin und zurueck
    strecke = (TimeElapsed * 34300) / 2
    distanz = round(strecke, 2)

    return distanz

def entfernung():
    while True:
        abstand = distanz()
        return abstand
        time.sleep(0.1)

#Fehlmessungensvermeidung
def real_distance():
    import collections
    distance_list = []
    counterc = 0
    for x in range(10):
        d = distanz()
        distance_list.append(d)
        counterc = counterc + 1
        print("test real_distance liste erstellen: {}".format(counterc))
        time.sleep(0.05)

    counter=collections.Counter(distance_list)
    print(counter)
    distance = counter.most_common(1)
    print("die häufigste entfernung ist:{}".format(distance))
    return distance
    # [(1, 4), (2, 4), (3, 2)]



if __name__ == '__main__':
    try:
        while True:
            abstand = distanz()
            print ("Gemessene Entfernung = %.1f cm" % abstand)
            time.sleep(1)

        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        GPIO.cleanup()
