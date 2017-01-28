import smbus
import time
import threading
import abc

bus = smbus.SMBus(0)
BYTES_TO_READ = 4

class I2CModuleSensor:
    def __init__(self, addr, register):
        self._addr = id
        self._alive = False
        self._register = register
        self._raw_data = bytearray()

    @abc.abstractmethod
    def get(self):
        '''Returns a single value'''
        pass

    def open(self):
        threading.Thread(target=self.query_loop)

    def get_raw_value(self):
        return self._raw_data

    def query_loop(self):
        while self._alive:
            time.sleep(.001)
            self._raw_data = bus.read_i2c_block_data(self._addr, BYTES_TO_READ)
