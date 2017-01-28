import RPi.GPIO as io

io.setmode(io.BCM)


class RPIPWNMotorController:
    def __init__(self, pins, port):
        self.set("delayed", "0")
        self.set("mode", "pwm")
        self.set("frequency", "500")
        self.set("active", "1")

        file_paths = {
            1: "/sys/class/rpi-pwm/pwm0/",
            2: "/sys/class/rpi-pwm/pwm1/"
        }

        self._path = file_paths.get(port)

        self._pins = pins

    def set(self, property_name, value):
        try:
            f = open(self._path + property_name, 'w')
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
        self.set("duty", str(speed))
