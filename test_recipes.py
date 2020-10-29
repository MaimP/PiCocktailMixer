#!/usr/bin/python
#-*- coding:utf-8 -*-
from glob import glob
import json

def getRecipes():
    global recipes
    recipes = []
    #Debug
    global drinks
    drinks = []
    global measure
    measure = []
    global name_list
    name_list = []

    files = []

    pth ="/Users/mikauthmann/Documents/Github/PiCocktailMixer/recipes/" #rasp. : /home/pi/Pi...
    for i in glob(pth+"*.json"):
        files.append(i)
    print("**2")

    counter = 0
    counter_name = 0
    counter_ingr = 0

    for i in files:
        counter_name += 1
        # Opening JSON file
        f = open(files[counter])
        # returns JSON object as
        # a dictionary
        data = json.load(f) #type dict
        recipes.append(data)
        # Iterating through the json
        # list
        name = data.get('name')
        name_list.append(name)
        description = data.get('description')
        ingredients = data.get('ingredients') #type list
        directions = data.get('directions')

        #filtern von brauchbaren Getraenken, also Vodka, Bacardie, Gin, etc.


        print("ingredients: {}".format(ingredients))
        counter_in = 0
        for i in ingredients:
            counter_ingr += 1
            ingred = ingredients[counter_in] #type dict
    #        print("debug ingred, quantity: {}".format(ingred.get('quantity')))
    #        print("debug ingred, measure: {}".format(ingred.get('measure')))
    #        print("debug ingred, ingredient: {}".format(ingred.get('ingredient')))
    #        print("list ingredients: {}".format(ingred))
            drinks.append(ingred.get('ingredient'))
            print("ingret measure: {}".format(ingred['measure']))
            measure.append(ingred.get('measure'))
            counter_in += 1
        # Closing file
        f.close()
        counter = counter + 1


    #print("array drinks: {}".format(drinks))
    #print("array measure: {}".format(measure))

    import collections
    from collections import Counter


    counter=collections.Counter(measure)
    print(counter)
    mostcommon = counter.most_common(1)
    print("das häufigste measure ist:{}".format(mostcommon))

    drinks_list = list(drinks)
    print("type drinks: {}".format(type(drinks_list)))
    counter_drinks=collections.Counter(drinks_list)
    print(counter_drinks)
    print("sortierte variante: {}".format(sorted(counter_drinks)))
    mostcommon_drinks = counter_drinks.most_common(1)
    print("der häufigste drink ist:{}".format(mostcommon_drinks))

    print("länge des Namensarrays: {}".format(len(name_list)))

    print("counter_name: {}".format(counter_name))
    print("counter_ in : {}".format(counter_ingr))
    print("**3")


def recipes():
    getRecipes()
    global search_recipes
    search_recipes = []
    #Liste mit allen Rezepten, nach Alphabet sortiert
    search = "gin"
    for i in range(len(name_list)):
        if search in name_list[i]:
            print '"gin tonic" gefunden in item %s' % i

    print("recipes[0]: {}".format(recipes[0]))
#        else:
#            print("kein gin")
    #Rezepte nach ingredients durchsuchen
    counter_search = 0
    #geht jedes rezept durch
    for i in recipes:

        #werte des rezeptes werden var zugewiesen
        ingrets = recipes[counter_search].get('ingredients')
        name = recipes[counter_search].get('name')

        #prueft ob name des Rezeptes mit Suchbegriff uebereinstimmt
        if search in name:
            search_recipes.append(counter_search)
            print("rezept zutreffend nach Name: {}, index: {}".format(name, counter_search))

        else:
            ingret_list = []
            counter_ingrets_search = 0
            for i in ingrets:
                ingret_search = ingrets[counter_ingrets_search]
                ingret_list.append(ingret_search)
                counter_ingrets_search += 1

            if search in ingret_list:
                search_recipes.append(counter_search)
                print("Suchwort in Ingredients gefunden: {}, Index: {}".format(ingret_search, counter_search))

        counter_search += 1
        print("counter: {}".format(counter_search))



if __name__ == '__main__':
    recipes()
