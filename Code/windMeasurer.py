import time, board, analogio, adafruit_mpl3115a2, busio

i2c = busio.I2C(board.GP17, board.GP16)
barometer = adafruit_mpl3115a2.MPL3115A2(i2c)
barometer.sealevel_pressure = 103040

windIn = analogio.AnalogIn(board.GP28)
tempIn = analogio.AnalogIn(board.GP27)

def getVoltage(inVal):
    return (inVal * 3.3) / 65536

def voltsToArduinoIn(volts):
    return volts * 1023 / 5

while True:
    b = barometer
    windVolts = getVoltage(windIn.value)
    windMPH = ((voltsToArduinoIn(windVolts) - 264) / 85.6814)**3
    tempVolts = getVoltage(tempIn.value)
    tempC = (tempVolts-.4) / .0195
    print(f"Pressure: {b.pressure}  Altitude: {b.altitude}  Temperature: {b.temperature}")
    print(f"windVolts: {windVolts}  windMPH: {windMPH}")
    print(f"tempVolts: {tempVolts}  tempC: {tempC}\n")