from joysticks.Joystick import Joystick
from joysticks.buttons.Button import Button
from joysticks.logitechF710.LogitechF710AxisButton import LogitechF710AxisButton
from joysticks.logitechF710.LogitechF710HatButton import LogitechF710HatButton


class LogitechF710Joystick(Joystick):
    LOGITECH_F710_PRODUCT_ID = 0xc21f

    def __init__(self):
        Joystick.__init__(self, 0)
        self.add_button(LogitechF710AxisButton(Button.XL_ID))
        self.add_button(LogitechF710AxisButton(Button.YL_ID))
        self.add_button(LogitechF710AxisButton(Button.XR_ID))
        self.add_button(LogitechF710AxisButton(Button.YR_ID))
        self.add_button(LogitechF710HatButton(Button.HAT_BUTTON_ID))
        self.add_button(Button(Button.A_BUTTON_ID))

    def get_hat_button_angle(self):
        return self.get_button(Button.HAT_BUTTON_ID).get_angle()

    def get_left_Y(self):
        return self.get_button(Button.YL_ID).get_magnitude()

    def get_right_Y(self):
        return self.get_button(Button.YR_ID).get_magnitude()

    def get_left_X(self):
        return self.get_button(Button.XL_ID).get_magnitude()

    def get_a_button(self):
        return self.get_button(Button.A_BUTTON_ID).get_value()
