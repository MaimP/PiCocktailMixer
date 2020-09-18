#!/usr/bin/python
#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import csv

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

def writing():
    distance_list = []
    for i in range(200):

        distance = distanz()
        distance_list.append(distance)
        print("distanz: {}".format(distance))

    with open("distance.csv", "wb") as csv_file:

        writer = csv.writer(csv_file)
        for i in range(0, len(distance_list)):
            writer.writerows(distance_list[int(i)])

if __name__ == '__main__':
    try:
        writing()

        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        GPIO.cleanup()
