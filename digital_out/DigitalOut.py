import RPi.GPIO as GPIO


class RpiDigitalOut:
    def __init__(self, pin):
        self._pin = pin
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)

    def set_high(self):
        GPIO.output(self._pin, True)

    def set_low(self):
        GPIO.output(self._pin, False)
