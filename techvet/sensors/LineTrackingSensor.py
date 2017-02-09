from sensors.I2CModuleSensor import I2CModuleSensor


class LineTrackingSensor(I2CModuleSensor):
    def __init__(self, addr, register):
        I2CModuleSensor.__init__(self, addr, register)

    def get(self):
        byte_array = self.get_raw_value()
        value = (byte_array[3] << 24) | (byte_array[2] << 16) | (byte_array[1] << 8) | (byte_array[0])
        return value

