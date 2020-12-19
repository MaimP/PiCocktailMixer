#!/usr/bin/python
#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO

global GPIOs
GPIOs = [5, 6, 13, 17, 27, 22]
#5=Korn, 6=Bacardi, 13=Vodka,17=Fanta, 27=Cola, 22=Sprite

def startPump(drink):
    GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
    #mischgetraenke, pumpen zuweisung
    print("der ausgewaehlte getraenk ist:")
    print(drink)
    y = int(drink)

    x = GPIOs[y]
    RELAIS_1_GPIO = x #In 1

    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)  # GPIO Modus zuweisen
    print("Die gestartete Pumpe ist:")
    print(RELAIS_1_GPIO)
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
    return True

def stopPump():
    for x in GPIOs:
        GPIO.setup(x, GPIO.OUT)
        GPIO.output(x, GPIO.HIGH)

    GPIO.cleanup()
#        print("GPIO ", "wurde ausgeschaltet" sep=x)

    print("alle Pumpen wurden ausgeschaltet.")
    return False


if __name__ == '__main__':
    try:
        stopPump()

        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        GPIO.cleanup()
