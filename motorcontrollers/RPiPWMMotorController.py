import RPi.GPIO as io

io.setmode(io.BCM)


class RPIPWNMotorController:
    def __init__(self, pins):
        set("delayed", "0")
        set("mode", "pwm")
        set("frequency", "500")
        set("active", "1")
        self._pins = pins

    @staticmethod
    def set(property_name, value):
        try:
            f = open("/sys/class/rpi-pwm/pwm0/" + property_name, 'w')
            f.write(value)
            f.close()
        except:
            print("Error writing to: " + property_name + " value: " + value)

    def setup(self):
        io.setup(self._pins[0], io.OUT)
        io.setup(self._pins[1], io.OUT)

    def set_forward(self):
        io.output(self._pins[0], True)
        io.output(self._pins[1], False)

    def set_backwards(self):
        io.output(self._pins[0], False)
        io.output(self._pins[1], True)

    # between 0 and 9?
    def set_percent_speed(self, set_speed):
        if set_speed > 0:
            self.set_forward()
        else:
            self.set_backwards()

        speed = int(abs(set_speed)) * 100
        set("duty", str(speed))
