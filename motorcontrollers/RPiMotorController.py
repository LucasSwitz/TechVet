import abc

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


class RPiMotorController:
    def __init__(self, pins):
        self._pins = pins
        self._setup_pins()

    def _setup_pins(self):
        for pin in self._pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

    def get_pins(self):
        return self._pins

    def set_pin(self, pin, value):
        GPIO.output(pin, value)

    @abc.abstractmethod
    def set(self, value):
        """Set Position of actuator"""
        return
