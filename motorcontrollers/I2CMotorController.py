import smbus
from motorcontrollers.RPiMotorController import RPiMotorController
import time
import subprocess

class I2CMotorController(RPiMotorController):
    def __init__(self, pins, addr, id):
        RPiMotorController.__init__(self, pins)
        self._addr = addr
        self._bus = smbus.SMBus(1)
        self._id = id
        self._direction = False

    # between -1 and 1 and is normalized to 0 and 255
    def set(self, speed):
        bytes_out = [0, 0]

        if speed < 0:
            if self._direction:
                self.toggle_backwards()
        else:
            if not self._direction:
                self.toggle_forward()

        bytes_out[0] = self._id
        bytes_out[1] = int(abs(speed) * 255)

        try:
            self._bus.write_i2c_block_data(self._addr, 0, bytes_out)
        except IOError:
            subprocess.call(['i2cdetect','-y','1'])

    def toggle_forward(self):
        print "Toggle Forward!"
        self.set_pin(self._pins[0], True)
        self.set_pin(self._pins[1], False)

    def toggle_backwards(self):
        print "Toggle Backwards!"
        self.set_pin(self._pins[1], True)
        self.set_pin(self._pins[0], False)
