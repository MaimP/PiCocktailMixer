#!/usr/bin/python
#-*- coding:utf-8 -*-
import os

global volume


def cupArray():
    global volume
    volume = [
    {
        'name': 'Ikea Pokal groß',
        'volume': '350',
        'image': '/pic_vol/pokal-glas-klarglas__0908826_PE609409_S5.JPG'
    },
    {
        'name': 'Ikea Pokal klein',
        'volume': '270',
        'image': '/pic_vol/pokal-glas-klarglas__0896474_PE609414_S5.JPG'
    },
    {
        'name': 'Ikea Vardagen',
        'volume': '310',
        'image': '/pic_vol/vardagen-glas-klarglas__0896318_PE609373_S5.JPG'
    },
    {
        'name': 'Red Cup',
        'volume': '470',
        'image': '/pic_vol/plastikbecher-rot-360ml-50-einheiten.jpg'
    }
    ]

    return volume
