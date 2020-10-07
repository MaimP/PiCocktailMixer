#!/usr/bin/python
#-*- coding:utf-8 -*-
from glob import glob
import json

global recipes

def getRecipes():
    global recipes
    recipes = []

    files = []

    pth ="/home/pi/PiMixer/PiCocktailMixer/recipes/"
    for i in glob(pth+"*.json"):
        files.append(i)
    print("**2")

    counter = 0
    for i in files:
        # Opening JSON file
        f = open(files[counter])
        # returns JSON object as
        # a dictionary
        data = json.load(f) #type dict
        recipes.append(data)
        counter += 1

        # Closing file
        f.close()

    print("**3")
    return recipes
