from sensors.I2CModuleSensor import I2CModuleSensor


class ColorSensor(I2CModuleSensor):
    def __init__(self, addr, register):
        I2CModuleSensor.__init__(addr, register)
        self._listener = None

    def get(self):
        return self.get_raw_value()