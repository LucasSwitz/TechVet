import smbus
import time
import threading
import abc
import sys

BYTES_TO_READ = 4


class I2CModuleSensor:
    def __init__(self, addr, register, bytes_to_read=4):
        self._addr = addr
        self._alive = False
        self._register = register
        self._raw_data = bytearray(bytes_to_read)
        self._bytes_to_read = bytes_to_read
        self._bus = smbus.SMBus(1)
        self._open = False

    @abc.abstractmethod
    def get(self):
        '''Returns a single value'''
        pass

    def open(self):
        self._alive = True

        if not self._open:
            thread = threading.Thread(target=self.query_loop)
            thread.daemon = True
            thread.start()
            self._open = True

    def get_raw_value(self):
        return self._raw_data

    def stop(self):
        self._alive = False
        self._open = False

    def is_open(self):
        return self._open

    def query_loop(self):
        while self._alive:
            time.sleep(.01)
            read = self._bus.read_i2c_block_data(self._addr, self._bytes_to_read)
            for i in range(0, len(read)):
                if read[i] == 255:
                    break
                self._raw_data[i] = read[i]
