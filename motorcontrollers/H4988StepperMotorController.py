import time

from enum import Enum

from RPiMotorController import RPiMotorController


class H4988StepperMotorController(RPiMotorController):
    # pins[0] = directon pins pin[1] = step pin

    class Direction(Enum):
        FORWARD = 0
        BACKWARD = 1

    def __init__(self, pins):
        RPiMotorController.__init__(self, pins)
        self._current_position = 0
        self._goal_position = 0
        self.set_direction(self.Direction.FORWARD)

    def set(self, value):
        self._goal_position += value
        i = 0
        while i < value:
            self.step_forward()
            i += 1

    def disable(self):
        self._set_step_pin(False)
        self._set_step_pin(False)

    def step_forward(self):
        if self._current_direction != self.Direction.FORWARD:
            self.set_direction(self.Direction.FORWARD)

        self.step()

    def step_backward(self):
        if self._current_direction != self.Direction.BACKWARD:
            self.set_direction(self.Direction.BACKWARD)

        self.step()

    def set_direction(self, direction):
        if direction == self.Direction.FORWARD:
            self.set_direction_pin(True)
            self._current_direction = self.Direction.FORWARD
        elif direction == self.Direction.BACKWARD:
            self._current_direction = self.Direction.BACKWARD
            self.set_direction_pin(False)

    def set_direction_pin(self, state):
        if state:
            self.set_pin(self._pins[0], True)
        else:
            self.set_pin(self._pins[0], False)
        # should be 50 microseconds
        time.sleep(.000001)

    def step(self):
        self.set_pin(self._pins[1], True)
        # should be 100 microseconds
        time.sleep(.000001)
        self.set_pin(self._pins[1], False)
        # should be 100 microseconds
        time.sleep(.000001)
        self._current_position += 1

    def _set_step_pin(self, value):
        self.set_pin(self._pins[1], value)
