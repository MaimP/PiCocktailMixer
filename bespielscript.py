import smbus
import time
 
#bus = smbus.SMBus(0) # Rev 1 Pi
bus = smbus.SMBus(1) # Rev 2 Pi
 
DEVICE = 0x20 # Device Adresse (A0-A2)
IODIRA = 0x00 # Pin Register fuer die Richtung
IODIRB = 0x01 # Pin Register fuer die Richtung
OLATB = 0x15 # Register fuer Ausgabe (GPB)
GPIOA = 0x12 # Register fuer Eingabe (GPA)
 
# Definiere GPA Pin 7 als Input (10000000 = 0x80)
# Binaer: 0 bedeutet Output, 1 bedeutet Input
bus.write_byte_data(DEVICE,IODIRA,0x80)
 
# Definiere alle GPB Pins als Output (00000000 = 0x00)
bus.write_byte_data(DEVICE,IODIRB,0x00)
 
# Setze alle 7 Output bits auf 0
bus.write_byte_data(DEVICE,OLATB,0)
 
#Funktion, die alle LEDs aufleuchten laesst.
def aufleuchten():
    for MyData in range(1,8):
        # Zaehle von 1 bis 8, was binaer
        # von 001 bis 111 ist.
        bus.write_byte_data(DEVICE,OLATB,MyData)
        print "Zahl:", MyData, "Binaer:", '{0:08b}'.format(MyData)
        time.sleep(1)
        # Setze wieder alle Pins auf 0
        bus.write_byte_data(DEVICE,OLATB,0)
 
#Endlosschleife, die auf Tastendruck wartet
while True:
    # Status von GPIOA Register auslesen
    Taster = bus.read_byte_data(DEVICE,GPIOA)
 
    if Taster & 0b10000000 == 0b10000000:
        print "Taster gedrueckt"
        aufleuchten()
