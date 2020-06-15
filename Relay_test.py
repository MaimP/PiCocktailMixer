#!/usr/bin/python
#-*- coding:utf-8 -*-
import time
import smbus
import time

bus = smbus.SMBus(1)

DEVICE = 0x20 # Device Adresse (A0-A2)
IODIRA = 0x00 # Pin Register fuer die Richtung
IODIRB = 0x01 # Pin Register fuer die Richtung
OLATA = 0x14
OLATB = 0x15 # Register fuer Ausgabe (GPB)
GPIOA = 0x12 # Register fuer Eingabe (GPA)

# expander | Relay | hex
#-------------------------
#  0    01          0x80
#  1    02          0x40
#  2    03          0x20
#  3    04          0x10
#  4    05          0x8
#  5    06          0x4
#  6    07          0x2
#  7    08          0x1

#bus.write_byte_data(DEVICE,GPIOA,FF)
# initiate list with pin gpio pin numbers
bus.write_byte_data(DEVICE,GPIOA,1)
gpioList = [0x80, 0x40, 0x20, 0x10, 0x8, 0x4, 0x2, 0x1]

for i in gpioList:
    #GPIO.setup(i, GPIO.OUT)
    #GPIO.output(i, GPIO.HIGH)
    bus.write_byte_data(DEVICE,OLATA,i)

# Sleep time variables

sleepTimeShort = 0.2
sleepTimeLong = 0.1

# MAIN LOOP =====
# ===============

try:
    while True:
        for i in gpioList:
            #GPIO.output(i, GPIO.LOW)
            bus.write_byte_data(DEVICE,OLATA,i)
            time.sleep(sleepTimeShort);
            print("Relay auslösen")
            bus.write_byte_data(DEVICE,OLATA,0)
            time.sleep(sleepTimeLong);


# End program cleanly with keyboard
except KeyboardInterrupt:
    print " Quit"
