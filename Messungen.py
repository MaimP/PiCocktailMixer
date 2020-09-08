#!/usr/bin/python
#-*- coding:utf-8 -*-
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern

class Messungen:
    
    def aufzeichnung():
        GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
