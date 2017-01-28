import abc

from joysticks.buttons.Button import Button


class AxisButton(Button):
    def __init__(self, id_number):
        Button.__init__(self, id_number)

    @abc.abstractmethod
    def get_magnitude(self):
        """Return value from -1 to 1 based on position of joyistick"""

    # By default an axis button will not act like a trigger
    def get(self):
        return False
