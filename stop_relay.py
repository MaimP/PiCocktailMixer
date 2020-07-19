#!/usr/bin/python
#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
global GPIOs
GPIOs = [5, 6, 13, 17, 27, 22]


def stopPump():
    for x in GPIOs:
        GPIO.setup(x, GPIO.OUT)
        GPIO.output(x, GPIO.HIGH)
        GPIO.output(x, GPIO.LOW)
        print("low")

if __name__ == '__main__':
    try:
        for x in GPIOs:
            GPIO.setup(x, GPIO.OUT)

        stopPump()
        print("Realay wurde gestoppt.")

        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        GPIO.cleanup()
