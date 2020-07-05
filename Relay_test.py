#!/usr/bin/python
#-*- coding:utf-8 -*-
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

gpioList = [17, 27, 22, 5, 6, 13]

for i in gpioList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# Sleep time variables

sleepTimeShort = 0.2
sleepTimeLong = 0.1

# MAIN LOOP =====
# ===============

try:
    while True:
        for i in gpioList:
            GPIO.output(i, GPIO.LOW)
            time.sleep(sleepTimeShort);
            print("Relay auslösen")
            GPIO.output(i, GPIO.HIGH)
            time.sleep(sleepTimeLong);


# End program cleanly with keyboard
except KeyboardInterrupt:
    print " Quit"
