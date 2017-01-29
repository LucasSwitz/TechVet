import smbus
from motorcontrollers.RPiMotorController import RPiMotorController


class I2CMotorController(RPiMotorController):
    def __init__(self, pins ,addr, id):
        RPiMotorController.__init__(self, pins)
        self._addr = addr
        self._bus = smbus.SMBus(1)
        self._id = id

    # between -1 and 1 and is normalized to 0 and 255
    def set(self, speed):
        bytes_out = bytearray(2)

        if speed < 0:
            self.toggle_backwards()
        else:
            self.toggle_forward()

        bytes_out[2] = abs(speed) * 255
        self._bus.write_i2c_block_data(bytes_out)

    def toggle_forward(self):
        self.set_pin(self.get_pins()[0], True)
        self.set_pin(self.get_pins()[1], False)

    def toggle_backwards(self):
        self.set_pin(self.get_pins()[1], True)
        self.set_pin(self.get_pins()[0], False)
