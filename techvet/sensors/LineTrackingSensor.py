from sensors.I2CModuleSensor import I2CModuleSensor


class LineTrackingSensor(I2CModuleSensor):
    def __init__(self, addr, register):
        I2CModuleSensor.__init__(self, addr, register)

    def get(self):
        return self.get_raw_value()[0]
