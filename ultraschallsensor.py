#!/usr/bin/python
#-*- coding:utf-8 -*-
#Bibliotheken einbinden
import time
import smbus

#bus = smbus.SMBus(0) # Rev 1 Pi
bus = smbus.SMBus(1) # Rev 2 Pi

DEVICE = 0x20 # Device Adresse (A0-A2)
IODIRA = 0x00 # Pin Register fuer die Richtung
IODIRB = 0x01 # Pin Register fuer die Richtung
OLATB = 0x15 # Register fuer Ausgabe (GPB)
GPIOA = 0x12 # Register fuer Eingabe (GPA)
GPIOB = 0x13

bus.write_byte_data(DEVICE,IODIRB,1)
def relayEin():
    bus.write_byte_data(DEVICE,IODIRA,0) #Channel 7 Relay eingeschaltet, der Rest aus

def relayAus():
    bus.write_byte_data(DEVICE,GPIOA,FF)
def entfernungsmesserGpioAn():
    relayEin() #Pin B7 wurde auf output gesetzt,
    print("Entfernungsmesser wurde eingeschaltet") #der Rest ist Input --> Relay ausegloest

def entfernungsmesserGpioAus():
    relayAus()
    print("Entfernungsmesser wurde ausgeschaltet")

def distanz():
    # setze Trigger auf HIGH
    # distanzGpioan()
    # starte Sensor über gpio_expander, entfernungsmesserGpioaAn()

    entfernungsmesserGpioAn()
    # setze Trigger nach 0.01ms aus LOW
    while bus.read_byte_data(DEVICE,OLATB,0x1):
        StartZeit = time.time()
    time.sleep(0.00001)
    # distanzGpioaus()
    entfernungsmesserGpioAus()
    while bus.read_byte_data(DEVICE,OLATB,0x2):
        StopZeit = time.time()
    StartZeit = time.time()
    StopZeit = time.time()

    # speichere Startzeit
    # expander einbinden
    # einzelnen Pin des Entfernungsmesser einbeziehen
    #while bus.read_byte_data(DEVICE,OLATB,0x1):
    #    StartZeit = time.time()

    # speichere Ankunftszeit
    #while bus.read_byte_data(DEVICE,OLATB,0x2):
    #    StopZeit = time.time()

    # Zeit Differenz zwischen Start und Ankunft
    TimeElapsed = StopZeit - StartZeit
    # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
    # und durch 2 teilen, da hin und zurueck
    distanz = (TimeElapsed * 34300) / 2

    return distanz

if __name__ == '__main__':
    try:
        while True:
            abstand = distanz()
            print ("Gemessene Entfernung = %.1f cm" % abstand)
            time.sleep(1)

        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        bus.write_byte_data(DEVICE,GPIOA,1)
