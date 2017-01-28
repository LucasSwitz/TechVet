class Joystick:
    def __init__(self, id_number):
        self._id = id_number
        self._buttons = dict()

    def get_id(self):
        return self._id

    def add_button(self, button):
        self._buttons[button.get_id()] = button

    def get_button(self, button):
        return self._buttons[button]

    def get_buttons(self):
        return self._buttons.values()
