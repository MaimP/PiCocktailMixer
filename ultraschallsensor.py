#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time

#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#GPIO Pins zuweisen
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distanz():
    # setze Trigger auf HIGH
    distanzGpioan()

    # setze Trigger nach 0.01ms aus LOW
    time.sleep(0.00001)
    distanzGpioaus()
    StartZeit = time.time()
    StopZeit = time.time()

    # speichere Startzeit
    # expander einbinden
    while bus.read_byte_data(DEVICE,OLATB):
        StartZeit = time.time()

    # speichere Ankunftszeit
    while GPIO.input(GPIO_ECHO) == 1:
        StopZeit = time.time()

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
        GPIO.cleanup()

#Endlosschleife, die auf Tastendruck wartet
while True:
    # Status von GPIOA Register auslesen
    Taster = bus.read_byte_data(DEVICE,GPIOA)

    if Taster & 0b10000000 == 0b10000000:
        print "Taster gedrueckt"
        aufleuchten()
#Endlosschleife, die auf Tastendruck wartet
while True:
    # Status von GPIOA Register auslesen
    Taster = bus.read_byte_data(DEVICE,GPIOA)

    if Taster & 0b10000000 == 0b10000000:
        print "Taster gedrueckt"
        aufleuchten()
