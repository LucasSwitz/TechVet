from joysticks.buttons.AxisButton import AxisButton


class LogitechF710AxisButton(AxisButton):
    def __init__(self, id_number):
        AxisButton.__init__(self, id_number)

    def get_magnitude(self):
        return (self.get_value() - 128) / 128.0
