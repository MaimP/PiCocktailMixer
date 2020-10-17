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
            flow = count / (60 * 7.5)

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
            flow = ((count / 7.5) * 1000 * 60) #ml/sec
            flow_array.append(flow)
            print "The flow is: %.3f ml/sec" % (flow)
            count = 0
            flow_all = sum(flow_array)
            print("Insgesamt: {}".format(flow_all))
            #debug
            stop_time = time.time()
            counter += 1
            time_intervall = (stop_time - start_time) / counter
            print("zeit pro durchlauf im durchschnitt: {}".format(time_intervall))
        else:
            break

if __name__ == '__main__':
    measure()
