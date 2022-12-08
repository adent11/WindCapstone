import time, board, analogio

windIn = analogio.AnalogIn(board.GP28)
tempIn = analogio.AnalogIn(board.GP27)

def getVoltage(inVal):
    return (inVal * 3.3) / 65536

def voltsToArduinoIn(volts):
    return volts * 1023 / 5

while True:
    windInVal = windIn.value
    windVolts = getVoltage(windInVal)
    windMPH = ((voltsToArduinoIn(windVolts) - 264) / 85.6814)**3
    #float windMPH =  pow(((float(windADunits) - 264.0) / 85.6814), 3.36814);
    tempInVal = tempIn.value
    tempVolts = getVoltage(tempInVal)
    tempC = (tempVolts-.4) / .0195
    print(f"windInVal: {windInVal}  windVolts: {windVolts}  windMPH: {windMPH}")
    print(f"tempInVal: {tempInVal}  tempVolts: {tempVolts}  tempC: {tempC}")
    time.sleep(0.5)