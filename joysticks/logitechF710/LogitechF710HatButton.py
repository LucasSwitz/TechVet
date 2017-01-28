from joysticks.buttons.Button import Button


class LogitechF710HatButton(Button):
    def get(self):
        return self.get_angle() > 0

    def get_angle(self):
        return (self.get_value() * 360) / 8
