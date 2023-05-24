# WindCapstone main code
# Alden Dent

import time, board, digitalio, analogio, adafruit_mpl3115a2, busio, os

i2c = busio.I2C(board.GP17, board.GP16) # Barometric altimeter setup
b = adafruit_mpl3115a2.MPL3115A2(i2c)
b.sealevel_pressure = 103040

windIn = analogio.AnalogIn(board.GP28) # Wind sensor setup
tempIn = analogio.AnalogIn(board.GP27)

buttonPin = digitalio.DigitalInOut(board.GP0) # Mode button setup
buttonPin.direction = digitalio.Direction.INPUT
buttonPin.pull = digitalio.Pull.UP

rPin = digitalio.DigitalInOut(board.GP6) #LED setup
rPin.direction = digitalio.Direction.OUTPUT
gPin = digitalio.DigitalInOut(board.GP7)
gPin.direction = digitalio.Direction.OUTPUT
bPin = digitalio.DigitalInOut(board.GP8)
bPin.direction = digitalio.Direction.OUTPUT

red, green, blue, cyan = (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, 1) # variables for different colors to input to setColor function

def setColor(c): # Sets the color of the LED
    rPin.value = c[0]
    gPin.value = c[1]
    bPin.value = c[2]

def buttonPressed(): # Simplifying confusing negatives for semantic ease
    return not buttonPin.value

def getVoltage(inVal): # Converts analog input to voltage
    return (inVal * 3.3) / 65536

def voltsToArduinoIn(volts): # Converts voltage input to arduino analog reading
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
        startTime = time.time()
        while not buttonPressed(): # Records data until button is pressed
            windVolts = getVoltage(windIn.value)
            windMPH = ((voltsToArduinoIn(windVolts) - 264) / 85.6814)**3
            tempVolts = getVoltage(tempIn.value)
            tempC = (tempVolts-.4) / .0195
            dataList.append(f"{b.altitude},{windMPH},{b.temperature},{tempC},{windVolts},{time.time()-startTime}\n") # Recording data to list
        while buttonPressed(): # Wait for button release
            pass
        time.sleep(.5)
        setColor(cyan)
        with open(filePath, "w") as file: # Writes data to a file
            file.write("altitude,windMPH,barometerTemp,windTemp,windVolts,timeFromStart\n")
            for dataLine in dataList:
                file.write(dataLine)
        flightNum = flightNum + 1
except: # Shows if there has been an error
    setColor(red)
    while True:
        pass
