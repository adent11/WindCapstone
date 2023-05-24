# WindCapstone boot code
# Alden Dent

import board, digitalio, storage, time

led = digitalio.DigitalInOut(board.LED) # LED setup
led.direction = digitalio.Direction.OUTPUT
led.value = False

buttonPin = digitalio.DigitalInOut(board.GP0) # Button Setup
buttonPin.direction = digitalio.Direction.INPUT
buttonPin.pull = digitalio.Pull.UP

# If button is pressed, CircuitPython can write to CIRCUITPY filesystem.
if not buttonPin.value:
    led.value = True # Turns on LED ot show that Pico is in write mode
    time.sleep(3)
    storage.remount("/", readonly=False)

while not buttonPin.value: # Waits for button release to continue
    pass
