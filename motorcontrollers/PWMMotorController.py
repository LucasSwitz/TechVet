from RPiMotorController import RPiMotorController


class PWMMotorController(RPiMotorController):
    def __init__(self, pins):
        RPiMotorController.__init__(self, pins)

    def set(self, value):
        if value == 0:
            self.off()
        elif value < 0:
            self.apply_backwards(value)
        else:
            self.apply_forward(value)

    def apply_forward(self, throttle):
        self.set_pin(self.get_pins()[0], True)
        self.set_pin(self.get_pins()[1], False)

    def apply_backwards(self, throttle):
        self.set_pin(self.get_pins()[1], True)
        self.set_pin(self.get_pins()[0], False)

    def off(self):
        self.set_pin(self.get_pins()[1], False)
        self.set_pin(self.get_pins()[0], False)
