from flask import Flask, render_template, send_file, request
import json
import volume_cup as vo_cup
from drinks import Drinks
import math
import RPi.GPIO as GPIO


app = Flask(__name__)


@app.route('/bulma/css/bulma.min.css')
def getBulma():
    return send_file('./static/bulma/css/bulma.min.css')


@app.route('/bulma/css/mystyles.scss')
def getmystyle():
    return send_file('./static/bulma/css/mystyles.scss')


@app.route('/bulma/sass/utilities/initial-variables.sass')
def getmyinitial():
    return send_file('./static/bulma/sass/utilities/initial-variables.sass')


@app.route('/bulma/sass/utilities/functions.sass')
def gettest():
    return send_file('./static/bulma/sass/utilities/functions.sass')


@app.route('/bulma/<file>')
def testmystyle(file):
    print("test bulma")
    return send_file('./static/'+file)


@app.route('/')
@app.route('/mdb.html')
def home():
    return render_template('/mdb.html')


@app.route('/recipes.html')
def recipes():
    return render_template('/recipes.html')


@app.route('/mix.html')
def mix():
    return render_template('/mix.html')


@app.route('/change_drinks.html')
def changeDrinks():
    return render_template('/change_drinks.html')


@app.route('/pic_vol/<fileName>')
def pictures(fileName):
    print("extra routing")
    file = './static/pic_vol/' + fileName
    return send_file(file, mimetype='image/jpeg')


@app.route('/<request>', methods=['GET'])
def runFkt(request):
    splitt = request.split('.')
    if len(splitt) > 1 and splitt[1] == 'html':
        return render_template('/admin.html')
    return eval(request+'()')


@app.route('/<request>', methods=['Post'])
def postFnkt(request):
    return eval(request+'()')


def volume():
    volume = vo_cup.cupArray()
    volume_send = json.dumps(volume)
    print("test")
    return volume_send


def doform():
    print("**11")
    raw_bestellung = request.form.to_dict()
    print(f"raw_bestellung: {raw_bestellung}")
    for i in raw_bestellung:
        bestellung = json.loads(i)
    print(bestellung)
    b = bestellung.get('verhaeltnis')
    c = bestellung.get('getraenke')
    d = list(b)
    e = list(c)
    menge = bestellung.get('anzahl')  # gibt die Menge an bestellten Getraenken an
    glas = bestellung.get('volume')  # gibt an welches Glas genutzt wird(Volumen)
    mischv = []
    getraenke = []
    counter_m = 0
    for i in d:
        x = float(d[counter_m])
        counter_m += 1
        mischv.append(x)
        print("debug mischv :{}".format(x))

    counter_g = 0
    for i in e:
        x = float(e[counter_g])
        counter_g = counter_g + 1
        getraenke.append(x)
        print("debug getraenke :{}".format(x))

    order(mischv, getraenke, menge, glas)
    return '', 204


def getOldChoice():
    from drinks import Drinks
    obj = Drinks()
    obj.__init__()
    return json.dumps(obj.newchoice)


def dorecipes():
    import recipes as re
    recipes = re.getRecipes()
    recipes_send = json.dumps(recipes)
    return recipes_send


def newDrink():
    print("new drink ewrde ausgefuehrt")
    raw_data = request.form.to_dict()
    for i in raw_data:
        selection = json.loads(i)
    print(f"selection: {selection}")
    addDrink = selection.get('addDrink')
    old_drink = selection.get('oldDrink')
    print("new drink: {}".format(addDrink))
    print("oldDrink: {}".format(old_drink))
    obj = Drinks()
    obj.newDrinks(addDrink)
    obj.newChoice(old_drink, addDrink)
    return '', 204


def newChoice():
    raw_data = request.form.to_dict()
    for i in raw_data:
        selection = json.loads(i)
    new_drink = selection.get('newDrink')
    old_drink = selection.get('oldDrink')
    print("new drink: {}".format(new_drink))
    print("old drink: {}".format(old_drink))
    obj = Drinks()
    obj.newChoice(old_drink, new_drink)
    return '', 204


def getChoiceOption():
    obj = Drinks()
    obj.readDrinks()
    unsorted_choice = obj.drinklist
    unsorted_choice.sort()
    return json.dumps(unsorted_choice)


# Daten fuer Bestellung auswerten und Bestellung in App.py starten
def order(mischv, getraenke, anzahl, volume):
    menge = anzahl
    # vorläufiges Array für Bestellung
    order_list = []
    # Entgültige Bestellungsarray für Ausfuehrung in App
    drink_list = []

    print("**drinklist")
    # für warteschelife, zeigt an an welcher position deine Bestellung ist
    ordernumber_raw = 0
    ordernumber = 0
    # für ordernumber, um im Array postion zu finden, wo als naechstes fortgefahren werden soll
    x = 0
    print("**12")
    if len(order_list) > 0:
        x = (order_list[0] * 2) + 3  # order_list[0] * 2, weil noch mischverhaeltnis reingeschrieben werden muss, +3 für glas, menge, Anazhl an mischgetraenken
        ordernumber_raw = ordernumber_raw + 1
        print("**13")
        while True:
            if x < len(order_list):
                x = x + order_list[x] + 1
                ordernumber_raw = ordernumber_raw + 1
            else:
                ordernumber = math.ceil(ordernumber_raw)
                print("Deine Bestellung ist an Position: {}".format(ordernumber))
                break
    else:
        print("**13")
        print("Dein Bestellung ist an erster Position")


    # Variabel für menge der getraenke pro Bestelleung
    number = 0
    print("**14")

    # Hier wird die Bestellung gefiltert, in vorlaeufigen Array geschrieben
    if getraenke[0] != 6:
        drink1 = int(getraenke[0])
        drink_list.append(drink1)
        value = int(mischv[0])
        drink_list.append(value)
        number = number + 1
        print("**15")
        print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}, mischverhaeltnis: {}".format(drink1, number, mischv[0]))
        if getraenke[1] != 6:
            print("**15")
            drink2 = int(getraenke[1])
            drink_list.append(drink2)
            value = int(mischv[1])
            drink_list.append(value)
            number = number + 1
            print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}, mischverhaeltnis: {}".format(drink2, number, mischv[1]))
            if getraenke[2] != 6:
                print("**15")
                drink3 = int(getraenke[2])
                drink_list.append(drink3)
                value = int(mischv[2])
                drink_list.append(value)
                number = number + 1
                print("drink_list: hinzugefügtes Getraenk: {}, number bei: {}, mischverhaeltnis: {}".format(drink3, number, mischv[2]))
                if getraenke[3] != 6:
                    print("**15")
                    drink4 = int(getraenke[3])
                    drink_list.append(drink4)
                    value = int(mischv[3])
                    drink_list.append(value)
                    number = number + 1
                    if getraenke[4] != 6:
                        print("**15")
                        drink5 = int(getraenke[4])
                        drink_list.append(drink5)
                        value = int(mischv[4])
                        drink_list.append(value)
                        number = number + 1
                        if getraenke[5] != 6:
                            print("**15")
                            drink6 = int(getraenke[5])
                            drink_list.append(drink6)
                            value = int(mischv[5])
                            drink_list.append(value)
                            number = number + 1

    # im Format: menge der Getraenke pro Bestellung, wiviele von diesen, welches Glas genutzt wird
    # getraenk1, Mischv. 1, getraenk2, ...
    # schreibt bestellung in Array
    order_list.append(number)
    order_list.append(menge)
    order_list.append(volume)
    z = order_list[0] * 2

    for i in range(z):
        order_list.append(drink_list[int(i)])
        print("**16")

    print("order_list Array: {}".format(order_list))
    # loesche Array um neue Bestellung aufzunehmen
    del drink_list

    print("**17")
    import app as appl
    ap = appl.App(order_list)
    ap.orderManager()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
