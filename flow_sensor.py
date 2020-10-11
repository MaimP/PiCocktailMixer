#!/usr/bin/python

import RPi.GPIO as GPIO
import time, sys

FLOW_SENSOR = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)
global count
count = 0

def measure(self):
    def countPulse(self):

        global count
        if start_counter == 1:
            count = count+1
    #      print count
            flow = count / (60 * 7.5)
    #      print(flow)

    GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)
    flow_array = []
    flow_all = 0
    while True:
        if fillup > flow_all:
            start_counter = 1
            time.sleep(1)
            start_counter = 0
            flow = (count * 2.25 / 1000)
            flow_array.append(flow)
            print "The flow is: %.3f Liter/sec" % (flow)
            count = 0
            flow_all = sum(flow_array)
        else:
            print("break flow_meter")
            break


'''GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)

while True:
    try:
        start_counter = 1
        time.sleep(1)
        start_counter = 0
        flow = (count * 60 * 2.25 / 1000)
        print "The flow is: %.3f Liter/min" % (flow)
        count = 0
        time.sleep(5)
    except KeyboardInterrupt:
        print '\ncaught keyboard interrupt!, bye'
        GPIO.cleanup()
        sys.exit()'''

if __name__ == '__main__':
    measure(50)
