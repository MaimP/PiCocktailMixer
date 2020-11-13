import pump

global gpios
gpios = [5, 6, 13, 17, 27, 22]

try:
    for i in gpios:
            print("START Pump {}".format(i))
            pump.startPump(i)


except KeyboardInterrupt():
    print("STOP Pump")
    pump.stopPump()
