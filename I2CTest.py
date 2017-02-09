from techvet.sensors.LineTrackingSensor import LineTrackingSensor

sensor = LineTrackingSensor(0x08, 1)
sensor.open()

while True:
    data = sensor.get()
    print data
