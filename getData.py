#!/usr/bin/python
#-*- coding:utf-8 -*-#
import server
import time

def Data():
    alcnumber = server.request.forms.get('drinks')
    id_mischv = server.request.forms.get('mischverhaeltnis')
    drinknumber = server.request.forms.get('AlkoholAuswahl_1')
    return alcnumber
    return id_mischv
    return drinknumber
