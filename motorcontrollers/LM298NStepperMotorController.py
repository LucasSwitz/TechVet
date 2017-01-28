import time

from motorcontrollers.RPiMotorController import RPiMotorController


# Using the LM298N driver

class LM298NSetepperMotorController(RPiMotorController):
    sequence = \
        [[1, 0, 1, 0],
         [0, 1, 1, 0],
         [0, 1, 0, 1],
         [1, 0, 0, 1]]

    def __init__(self, port, pins, steps=200):
        RPiMotorController.__init__(self, port)
        self._pins = pins
        self._current_position = 0
        self._goal_position = 0
        self.MAX_STEPS = steps

    def set(self, value):
        self.step_to_angle(value)

    def disable(self):
        for pin in self._pins:
            self.set_pint(pin, False)

    def step_to_angle(self, angle):
        self.take_steps(self.convert_angle_to_step(angle))

    def step_to_position(self, steps):
        self.take_steps(steps)

    def take_steps(self, steps):

        self._goal_position = steps

        if steps > 0:
            direction = 1
        else:
            direction = 0

        to_step = abs(steps)

        while to_step > 0:
            if direction == 0:
                if self._current_position == 0:
                    self._current_position = self.MAX_STEPS
                self._current_position -= 1
            elif direction == 1:
                self._current_position += 1
                if self._current_position == self.MAX_STEPS:
                    self._current_position = 0

            to_step -= 1
            self.__step()

    def __step(self):
        for xpin in range(0, 4):
            pin = self._pins[xpin]
            time.sleep(.001)
            if self.sequence[self._current_position % len(self.sequence)][xpin] != 0:
                self.set_pint(pin, True)
            else:
                self.set_pint(pin, False)

    def on_target(self):
        return self._goal_position == self._current_position

    def get_current_step(self):
        return self._current_position

    def get_current_angle(self):
        return self.convert_step_to_angle(self._current_position)

    @staticmethod
    def convert_angle_to_step(angle):
        return round(float(angle) * (5.0 / 9.0))

    @staticmethod
    def convert_step_to_angle(step):
        return round(float(step) * (9.0 / 5.0))
