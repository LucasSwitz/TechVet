from joysticks.JoystickMonitor import JoystickMonitor
from joysticks.logitechF710.LogitechF710Joystick import LogitechF710Joystick


class HectorOI:
    drive_stick = LogitechF710Joystick()
    JoystickMonitor.get_instance().add_joystick(drive_stick)
