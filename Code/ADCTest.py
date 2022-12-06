# Test code used to figure out raspberry pi pico ADC analog input

import time
import board
import analogio

knob = analogio.AnalogIn(board.GP28)

def get_voltage(raw):
    return (raw * 3.3) / 65536

while True:
    raw = knob.value
    volts = get_voltage(raw)
    print("raw = {:5d} volts = {:5.2f}".format(raw, volts))
    time.sleep(0.5)