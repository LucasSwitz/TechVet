from sensors.I2CModuleSensor import I2CModuleSensor


class RFIDSensor(I2CModuleSensor):

    def __init__(self, addr, register):
        I2CModuleSensor.__init__(self, addr, register)

    def get(self):
        pass

