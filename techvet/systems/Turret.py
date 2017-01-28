import threading
from functools import partial

from techvet.TechVetMap import HectorMap
from techvet.systems.System import System
from motorcontrollers.H4988StepperMotorController import H4988StepperMotorController


class Turret(System):
    instance = None

    @staticmethod
    def get_instance():
        if Turret.instance is None:
            Turret.instance = Turret()
        return Turret.instance

    def stop(self):
        self.disable()

    def _enable(self):
        pass

    def get_cli_functions(self, args):
        functions = {
            "disable": self.disable
        }

        if len(args) > 0:
            functions["set_pan"] = partial(self.set_pan, int(args[0]))
            functions["set_tilt"] = partial(self.set_tilt, int(args[0]))

        if len(args) > 1:
            functions["set_pan_tilt"] = partial(self.set_pan_tilt_parallel, int(args[0]), int(args[1]))

        return functions

    def __init__(self, ):
        System.__init__(self, "Turret")
        self._pan_controller = H4988StepperMotorController([HectorMap.PAN_DIRECTION_PIN, HectorMap.PAN_STEP_PIN])
        self._tilt_controller = H4988StepperMotorController([HectorMap.TILT_DIRECTION_PIN, HectorMap.TILT_STEP_PIN])

    def disable(self):
        System.dispatch_message(self, "Disabled.")
        self._pan_controller.disable()
        self._tilt_controller.disable()

    def set_pan(self, steps):
        System.dispatch_message(self, "Panning to " + str(steps) + " steps...")
        self._pan_controller.set(steps)

    def set_tilt(self, steps):
        System.dispatch_message(self, "Tilting to " + str(steps) + " steps...")
        self._tilt_controller.set(steps)

    def set_pan_tilt_parallel(self, pan_angle, tilt_angle):

        pan_thread = threading.Thread(target=self.set_pan, args=(pan_angle,))
        tilt_thread = threading.Thread(target=self.set_tilt, args=(tilt_angle,))

        pan_thread.start()
        tilt_thread.start()

    def step_pan(self, direction):
        if direction:
            self._pan_controller.step_forward()
        else:
            self._pan_controller.step_backward()

    def step_tilt(self, direction):
        if direction:
            self._tilt_controller.step_forward()
        else:
            self._tilt_controller.step_backward()
