import board, digitalio, storage, time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = False

buttonPin = digitalio.DigitalInOut(board.GP0)
buttonPin.direction = digitalio.Direction.INPUT
buttonPin.pull = digitalio.Pull.UP

# If write pin is connected to ground on start-up, CircuitPython can write to CIRCUITPY filesystem.
if not buttonPin.value:
    led.value = True
    time.sleep(3)
    storage.remount("/", readonly=False)

while not buttonPin.value:
    pass