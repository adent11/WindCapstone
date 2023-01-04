import time, board, analogio, adafruit_mpl3115a2, busio, os

i2c = busio.I2C(board.GP17, board.GP16)
b = adafruit_mpl3115a2.MPL3115A2(i2c)
b.sealevel_pressure = 103040

windIn = analogio.AnalogIn(board.GP28)
tempIn = analogio.AnalogIn(board.GP27)

def getVoltage(inVal):
    return (inVal * 3.3) / 65536

def voltsToArduinoIn(volts):
    return volts * 1023 / 5

with open("record.csv", "w") as fp:
    fp.write("altitude,windMPH,barometerTemp,windTemp,windVolts\n")
    for i in range(1000):
        windVolts = getVoltage(windIn.value)
        windMPH = ((voltsToArduinoIn(windVolts) - 264) / 85.6814)**3
        tempVolts = getVoltage(tempIn.value)
        tempC = (tempVolts-.4) / .0195
        fp.write(f"{b.altitude},{windMPH},{b.temperature},{tempC},{windVolts}\n")