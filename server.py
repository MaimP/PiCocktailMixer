#!/usr/bin/python
#-*- coding:utf-8 -*-#
from bottle import route, run
from bottle import template

from bottle import get, post, request # or route

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" id="testid" method="post">
            <select id="select_2" name="AlkoholAuswahl_1">
                <option value="0" selected="">Korn</option>
                <option value="1">Bacardi</option>
                <option value="2">Vodka</option>
            </select>

            <input type="range" id="Mischverhaeltnis" name="mischverhaeltnis"
                min="0" max="100"
            <label for="Mischverhaeltnis">Mischverhaeltnis</label>

            <select id="Mischgetraenk" name="drinks">
                <option value="00" selected="">Fanta</option>
                <option value="11">Cola</option>
                <option value="22">Sprite</option>
            </select>

                <input value="Bestellen" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    alkohol = request.forms.get('drinks')
    mischverhaeltnis = request.forms.get('mischverhaeltnis')
    mischgetraenk = request.forms.get('AlkoholAuswahl_1')

        #Lakohol, pumpen zuweisung
        if alkohol == 0: #Korn
            return "<p>Alkohol: Korn</p>"

            if mischgetraenk == 00:
                return "<p>mischgetränk: Fanta</p>"
            elif mischgetraenk == 11:
                return "<p>mischgetränk: Cola</p>"

            elif mischgetraenk == 22:
                return "<p>mischgetränk: Sprite</p>"

            else:
                return "<p> keine passende auswahl gefunden"

        elif alkohol == 1: #Bacardi
            return "<p>alokohl: Bacardi</p>"

            if mischgetraenk == 00:
                return "<p>mischgetränk: Fanta</p>"
            elif mischgetraenk == 11:
                return "<p>mischgetränk: Cola</p>"

            elif mischgetraenk == 22:
                return "<p>mischgetränk: Sprite</p>"

            else:
                return "<p> keine passende auswahl gefunden"

        elif alkohol == 2: #Vodka
            return "<p>alokohl: Vodka</p>"

            if mischgetraenk == 00:
                return "<p>mischgetränk: Fanta</p>"
            elif mischgetraenk == 11:
                return "<p>mischgetränk: Cola</p>"

            elif mischgetraenk == 22:
                return "<p>mischgetränk: Sprite</p>"

            else:
                return "<p> keine passende auswahl gefunden"

        else:
            return template('{{alkohol}},{{mischgetraenk}}', alkohol=alkohol, mischgetraenk=mischgetraenk)

run(host='192.168.178.72', port=8080, debug=True)
