#!/usr/bin/python
#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import stop_relay

GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
global GPIOs
GPIOs = [5, 6, 13, 17, 27, 22]
#5=Korn, 6=Bacardi, 13=Vodka,17=Fanta, 27=Cola, 22=Sprite

def startPump(drink):
    #mischgetraenke, pumpen zuweisung
    print("der ausgewaehlte getraenk ist:")
    print(drink)
    y = int(drink)

    x = GPIOs[y]
    RELAIS_1_GPIO = x #In 1

    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
    print("Die gestartete Pumpe ist:")
    print(RELAIS_1_GPIO)
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
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
        GPIO.setup(x, GPIO.OUT)
        GPIO.output(x, GPIO.HIGH)

    GPIO.cleanup()
#        print("GPIO ", "wurde ausgeschaltet" sep=x)

    print("alle Pumpen wurden ausgeschaltet.")

if __name__ == '__main__':
    try:
        stopPump()

        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        GPIO.cleanup()
