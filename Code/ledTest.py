import board, digitalio

rPin = digitalio.DigitalInOut(board.GP6)
gPin = digitalio.DigitalInOut(board.GP7)
bPin = digitalio.DigitalInOut(board.GP8)

red = (0, 1, 1)
green = (1, 0, 1)
blue = (1, 1, 0)