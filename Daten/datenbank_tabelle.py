CREATE TABLE order (
    id int NOT NULL AUTO_INCREMENT, #muss mit bestellnummer uebereinstimmen, ausgegebn vom html Eintrag
    datum DATE,
    uhrzeit TIME,
    Alkohol ALKOHOL,    # id eintragen
    softdrink SOFTDRINK, # id eintragen
    mischverhaeltnis MISCHVERHAELTNIS,
    PRIMARY KEY(id)
);
##Orientierung zur .csv Tabelle



#!/usr/bin/env python
import request
import MySQLdb

db = MySQLdb.connect("localhost", "root", "Macbook4g", "pimixer")
curs=db.cursor()

curs.execute ("SELECT * FROM pimixer")

# möglicherweise reguest funktion einbinden
# korn = 0
# Bacardi = 1
# Vodka = 2
# fanta = 00
#Cola = 11
#Sprite = 22
for entry in curs.fetchall():
    if entry[3] == 0:
        if entry[4] == 00:
            print("#TEST alle gemessenen Werte#Gemessene Bestellt am {0} um {1} wurde {2} Korn gemischt mit {3} Fanta in dem Vehältnis {4}% Alkohol ".format(entry[1], entry[2], entry[3], entry[4], entry[5]))
        elif entry[4] == 11:
            print("#TEST alle gemessenen Werte#Gemessene Bestellt am {0} um {1} wurde {2} Korn gemischt mit {3} Cola in dem Vehältnis {4}% Alkohol ".format(entry[1], entry[2], entry[3], entry[4], entry[5]))
        elif entry[4] == 22:
            print("#TEST alle gemessenen Werte#Gemessene Bestellt am {0} um {1} wurde {2} Korn gemischt mit {3} Sprite in dem Vehältnis {4}% Alkohol ".format(entry[1], entry[2], entry[3], entry[4], entry[5]))
        else:
            print("Es konnte kein Mischgetränk zugeordnet werden")
    elif entry[3] == 1:
        if entry[4] == 00:
            print("#TEST alle gemessenen Werte#Gemessene Bestellt am {0} um {1} wurde {2} Bacardi gemischt mit {3} Fanta in dem Vehältnis {4}% Alkohol ".format(entry[1], entry[2], entry[3], entry[4], entry[5]))
        elif entry[4] == 11:
            print("#TEST alle gemessenen Werte#Gemessene Bestellt am {0} um {1} wurde {2} Bacardi gemischt mit {3} Cola in dem Vehältnis {4}% Alkohol ".format(entry[1], entry[2], entry[3], entry[4], entry[5]))
        elif entry[4] == 22:
            print("#TEST alle gemessenen Werte#Gemessene Bestellt am {0} um {1} wurde {2} Bacardi gemischt mit {3} Sprite in dem Vehältnis {4}% Alkohol ".format(entry[1], entry[2], entry[3], entry[4], entry[5]))
    elif entry [3] == 2:
        if entry[4] == 00:
            print("#TEST alle gemessenen Werte#Gemessene Bestellt am {0} um {1} wurde {2} Vodka gemischt mit {3} Fanta in dem Vehältnis {4}% Alkohol ".format(entry[1], entry[2], entry[3], entry[4], entry[5]))
        elif entry[4] == 11:
            print("#TEST alle gemessenen Werte#Gemessene Bestellt am {0} um {1} wurde {2} Bacardi gemischt mit {3} Cola in dem Vehältnis {4}% Alkohol ".format(entry[1], entry[2], entry[3], entry[4], entry[5]))
        elif entry[4] == 22:
            print("#TEST alle gemessenen Werte#Gemessene Bestellt am {0} um {1} wurde {2} Bacardi gemischt mit {3} Sprite in dem Vehältnis {4}% Alkohol ".format(entry[1], entry[2], entry[3], entry[4], entry[5]))
    else:
        print("Es konnte kein Alkohol zugewiesen werden")
