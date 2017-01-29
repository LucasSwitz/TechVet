from sensors.I2CModuleSensor import I2CModuleSensor

sensor = I2CModuleSensor(0x08, 1)
sensor.open()

while True:
    data = sensor.get_raw_value()
    if len(data) > 0:
        print sensor.get_raw_value()