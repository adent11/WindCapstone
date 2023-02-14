import board, digitalio, time

rPin = digitalio.DigitalInOut(board.GP6)
rPin.direction = digitalio.Direction.OUTPUT
gPin = digitalio.DigitalInOut(board.GP7)
gPin.direction = digitalio.Direction.OUTPUT
bPin = digitalio.DigitalInOut(board.GP8)
bPin.direction = digitalio.Direction.OUTPUT

red, green, blue = (1, 0, 0), (0, 1, 0), (0, 0, 1)

def setColor(c):
    rPin.value = c[0]
    gPin.value = c[1]
    bPin.value = c[2]

while True:
    print("boop")
    setColor(red)
    time.sleep(.1)
    setColor(green)
    time.sleep(.1)
    setColor(blue)
    time.sleep(.1)