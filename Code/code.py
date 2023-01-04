import time, board, digitalio, analogio, adafruit_mpl3115a2, busio, os

i2c = busio.I2C(board.GP17, board.GP16)
b = adafruit_mpl3115a2.MPL3115A2(i2c)
b.sealevel_pressure = 103040

windIn = analogio.AnalogIn(board.GP28)
tempIn = analogio.AnalogIn(board.GP27)

buttonPin = digitalio.DigitalInOut(board.GP0)
buttonPin.direction = digitalio.Direction.INPUT
buttonPin.pull = digitalio.Pull.UP

rPin = digitalio.DigitalInOut(board.GP6)
rPin.direction = digitalio.Direction.OUTPUT
gPin = digitalio.DigitalInOut(board.GP7)
gPin.direction = digitalio.Direction.OUTPUT
bPin = digitalio.DigitalInOut(board.GP8)
bPin.direction = digitalio.Direction.OUTPUT

red, green, blue, cyan = (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, 1)

def setColor(c):
    rPin.value = c[0]
    gPin.value = c[1]
    bPin.value = c[2]

def buttonPressed():
    return not buttonPin.value

def getVoltage(inVal):
    return (inVal * 3.3) / 65536

def voltsToArduinoIn(volts):
    return volts * 1023 / 5

flightNum = 1

try:
    while True:
        filePath = f"flight{flightNum}Data.csv"
        dataList = []
        setColor(green)
        while not buttonPressed(): # Waiting for button press
            pass
        while buttonPressed(): # Then button release
            pass
        time.sleep(.5)
        setColor(blue)
        while not buttonPressed(): # Records data until button is pressed
            windVolts = getVoltage(windIn.value)
            windMPH = ((voltsToArduinoIn(windVolts) - 264) / 85.6814)**3
            tempVolts = getVoltage(tempIn.value)
            tempC = (tempVolts-.4) / .0195
            dataList.append(f"{b.altitude},{windMPH},{b.temperature},{tempC},{windVolts}\n") # Recording data to list
        while buttonPressed(): # Wait for button release
            pass
        time.sleep(.5)
        setColor(cyan)
        with open(filePath, "w") as file:
            file.write("altitude,windMPH,barometerTemp,windTemp,windVolts\n")
            for dataLine in dataList:
                file.write(dataLine)
        flightNum = flightNum + 1
except:
    setColor(red)