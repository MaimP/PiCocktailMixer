#!/usr/bin/python
import RPi.GPIO as GPIO
import time, sys

FLOW_SENSOR = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)
global count
count = 0

global process_flow
process_flow = False

def proces():
    global process_flow
    process_flow = False
    return process_flow

def measure():
    global process_flow
    process_flow = True
    global count
    def countPulse(channel):

        global count
        if start_counter == 1:
            count = count+1

    GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)
    flow_array = []
    #debug
    start_time = time.time()
    counter = 0
    while True:
        if process_flow:
            start_counter = 1
            time.sleep(1)
            start_counter = 0
            flow = ((count / 7.5) * 16.6666) # Pulse frequency (Hz) = 7.5Q, Q is flow rate in L/min.
            print("The flow is: %.3f ml/sek" % (flow))
            flow_array.append(flow)
            print("gesamt durchfluss: {}".format(sum(flow_all)))
            flow_all = sum(flow_array)
            count = 0
        else:
            break

if __name__ == '__main__':
    measure()
