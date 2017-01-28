from techvet.sensors.ColorSensor import ColorSensor
import threading
import time

SETPOINT_DELAY = 5
SETPOINT_THRESHOLD = 1000


class SetPointTracker:
    def __init__(self, addr, register):
        self._color_sensor = ColorSensor(addr, register)
        self._current_setpoint = 0
        self._alive = True
        self._paused = False

    def get_current_checkpoint(self):
        return self._current_setpoint

    def track(self):
        if not self._alive:
            threading.Thread(target=self._track)
        else:
            self._paused = False

    def stop(self):
        self._alive = False

    def pause(self):
        self._paused = True

    def _track(self):
        self._alive = True

        while self._alive:
            while not self._paused:
                time.sleep(.001)
                colors = self._color_sensor.get()

                if colors[0] > SETPOINT_THRESHOLD:
                    self._current_setpoint += 1
                    time.sleep(SETPOINT_DELAY)
