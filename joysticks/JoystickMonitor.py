import time
from threading import Thread

from command.CommandQueue import CommandQueue
from joysticks.buttons.Button import Button


class JoystickMonitor:
    instance = None

    def __init__(self):
        self.joysticks = dict()
        self._monitoring = False

    def add_joystick(self, stick):
        self.joysticks[stick.get_id()] = stick

    def update_joystick(self, joystick_id, button_values):
        if joystick_id in self.joysticks.keys():
            stick = self.joysticks[joystick_id]
            stick.get_button(Button.XL_ID).update(button_values[0])
            stick.get_button(Button.YL_ID).update(button_values[1])
            stick.get_button(Button.XR_ID).update(button_values[2])
            stick.get_button(Button.YR_ID).update(button_values[3])
            stick.get_button(Button.HAT_BUTTON_ID).update(button_values[4])
            stick.get_button(Button.A_BUTTON_ID).update(button_values[5])

    def start_monitor(self):
        self._monitoring = True
        monitor_thread = Thread(target=self._monitor)
        monitor_thread.daemon = True
        monitor_thread.start()

    def stop_monitor(self):
        self._monitoring = False

    def _monitor(self):
        while self._monitoring:
            # sleep for a little while to allow updates
            time.sleep(.0001)
            for stick in self.joysticks:
                for button in stick.get_button():
                    if button.get():
                        CommandQueue.get_instance().add_command(button.get_command())

    @staticmethod
    def get_instance():
        if JoystickMonitor.instance is None:
            JoystickMonitor.instance = JoystickMonitor()
        return JoystickMonitor.instance
