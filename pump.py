#!/usr/bin/python
#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
global GPIOs
GPIOs = [5, 6, 13, 17, 27, 22]
#5=Korn, 6=Bacardi, 13=Vodka,17=Fanta, 27=Cola, 22=Sprite

def startPump(drink):
    #mischgetraenke, pumpen zuweisung
    print(drink)
    int(drink)

    x = GPIOs[drink]
    RELAIS_1_GPIO = x #In 1

    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
    print("Pumpe :")
    prin(RELAIS_1_GPIOAIS_1)
    print("wurde gestartet.")
#    if drink == 00: #Fanta
#        RELAIS_1_GPIO = 17 #In 1
#        GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
#
#    elif drink == 11: #Cola
#        RELAIS_1_GPIO = 27 #In 2
#        GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
#
#    elif drink == 22: #Sprite
#        RELAIS_1_GPIO = 22 #In 3
#        GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
#
#    #Lakohol, pumpen zuweisung
#    elif drink == 0: #Korn
#        RELAIS_1_GPIO = 5 #In 4
#        GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
#
#    elif drink == 1: #Bacardi
#        RELAIS_1_GPIO = 6 #In 5
#        GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
#
#    elif drink == 2: #Vodka
#        RELAIS_1_GPIO = 13 #In 7
#        GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
#
#elif drink != 2 and drink != 1 and drink != 22 and drink != 11: #debug, testen warum er in erkennt
#    print("es ist ungleich allen anderen außer Korn und Fanta.")


#    else:
#        print("Dein Getränk konnte keiner Pumpe zugewiesen werden.")

def stopPump():
    for x in GPIOs:
        GPIO.setup(x, GPIO.IN)
#        print("GPIO ", "wurde ausgeschaltet" sep=x)

    print("alle Pumpen wurden ausgeschaltet.")
