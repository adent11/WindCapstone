import board, adafruit_mpl3115a2, busio
i2c = busio.I2C(board.GP17, board.GP16)
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
sensor.sealevel_pressure = 103040

while True:
    #print('Pressure: {0:0.3f} pascals'.format(sensor.pressure))
    print('Altitude: {0:0.3f} meters'.format(sensor.altitude))
    #print('Temperature: {0:0.3f} degrees Celsius'.format(sensor.temperature))