from bot.input.InputState import InputState
from joysticks.JoystickMonitor import JoystickMonitor


class TeleopInputState(InputState):
    def parse(self, data):
        for i in range(0, len(data)):
            data[i] = int(data[i], 16)
        JoystickMonitor.get_instance().update_joystick(data[0], data[1:len(data)])
