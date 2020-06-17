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
OLATA = 0x14
GPIOA = 0x12 # Register fuer Eingabe (GPA)
GPIOB = 0x13
# MCP connection
#       Input(IODIRB 0x80)      Output(IODIRA 0x00)
#   GPB  pin    HEX         GPA pin     HEX
#   0   1      0/1          7   28      1
#   1   2       0           6   27      0
#   2   3       0           5   26      0
#   3   4       0           4   25      0
#   4   5       0           3   24      0
#   5   6       0           2   23      0
#   6   7       0           1   22      0
#   7   8       0           0   21      0
# Trigger sitzt auf GPA0/Pin 21
bus.write_byte_data(DEVICE,IODIRB,0x80) #input auf 0x80
bus.write_byte_data(DEVICE,IODIRA,0x00) #
bus.write_byte_data(DEVICE,OLATA,1)
#def relayEin():
#    bus.write_byte_data(DEVICE,IODIRA,0) #Channel 7 Relay eingeschaltet, der Rest aus

#def relayAus():
#    bus.write_byte_data(DEVICE,GPIOA,FF)

def entfernungsmesserGpioAn():
#    relayEin() #Pin A7 wurde auf output gesetzt,
    print("Trigger wurde gestartet")
    bus.write_byte_data(DEVICE,OLATA,0x00) #möglicherweise falsch, überprüfen
#    while bus.read_byte_data(DEVICE,IODIRB) == 0: #2
#        StartZeit = time.time()
#        print("Startzeit wurde erfasst.")
#    else:
#        print("Es konnte keine Startzeit ermittelt werden.")

def entfernungsmesserGpioAus():
    print("Trigger wurde gestoppt")
    bus.write_byte_data(DEVICE,OLATA,0xFF) #Trigger auf 1 gesetzt(11111111)
#    while bus.read_byte_data(DEVICE,IODIRB) == 1: #20
#        StopZeit = time.time()
#        print("Es wurde eine Stopzeit erfasst")
#    else:
#        print("Es konnte keine Stopzeit erfasst werden.")

def distanz():
    bus.write_byte_data(DEVICE,OLATA,1)
    # setze Trigger auf HIGH
    # distanzGpioan()
    # starte Sensor über gpio_expander, entfernungsmesserGpioaAn()
#    StartZeit = time.time()
#    StopZeit = time.time()
    entfernungsmesserGpioAn()

#    while bus.read_byte_data(DEVICE,GPIOB) & 0b00000010 == 0b00000000: #2
#        StartZeit = time.time()
#        print("Startzeit wurde erfasst.")
    #else:
    #        print("keine startzeit erfasst")
    # setze Trigger nach 0.01ms aus LOW
    time.sleep(0.00001)
    # distanzGpioaus()
    entfernungsmesserGpioAus()

    echo = bus.read_byte_data(DEVICE,GPIOB)

    while bus.read_byte_data(DEVICE,GPIOB) & 0b100000 == 0b00000000:
        StartZeit = time.time()
        print("Startzeit wurde erfasst")
        print(echo)

    if bus.read_byte_data(DEVICE,GPIOB) & 0b100000 == 0b10000000:
        StopZeit = time.time()
        print("Stopzeit wurde erfasst")
        print(echo)

    else:
        print("Es konnte keine Stopzeit erfasst werden")
        print(echo)

#                print(bus.read_byte_data(DEVICE,GPIOB))

#        else:
#            if bus.read_byte_data(DEVICE,GPIOB) & 0b00000010 == 0b00000010:
#                StopZeit = time.time()
#                print("Es wurde eine Stopzeit erfasst")
#                break
#            else:
#                print("keine Stopzeit")
#                print(bus.read_byte_data(DEVICE,GPIOB))
#            print("es wurde keine startzeit erfasst")
#    if bus.read_byte_data(DEVICE,GPIOB) & 0b01000000 == 0b00000000: #2
#        StartZeit = time.time()
#        print("Startzeit wurde erfasst.")
#    else:
#        print("keine startzeit erfasst")

#    while True:
#        if bus.read_byte_data(DEVICE,GPIOB) & 0b00000010 == 0b00000010: #20
#            StopZeit = time.time()
#            print("Es wurde eine Stopzeit erfasst")

#            break
#        bus.write_byte_data(DEVICE,IODIRB,0)
#        print("0")
#        else:
#            print("keine stopzeit erfasst")
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

    #    print("es gibt keine Zeiten")

if __name__ == '__main__':
    try:
        while True:
            abstand = distanz()
            print ("Gemessene Entfernung = %.1f cm" % abstand)
            time.sleep(1)

        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
