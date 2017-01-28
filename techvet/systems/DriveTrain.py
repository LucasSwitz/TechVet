from functools import partial

from techvet.TechVetMap import TechVetMap

from System import System
from techvet.TechVetOI import HectorOI
from motorcontrollers.RPiPWMMotorController import RPIPWNMotorController
from techvet.sensors.LineTrackingSensor import LineTrackingSensor
from PID.PIDController import PIDController

LINE_SENSOR_ID = 0
LINE_SENSOR_REGISTER = 0

DEFAULT_SPEED = .7


class DriveTrain(System):
    instance = None

    @staticmethod
    def get_instance():
        if DriveTrain.instance is None:
            DriveTrain.instance = DriveTrain([TechVetMap.DRIVETRAIN_LEFT_FWD, TechVetMap.DRIVETRAIN_LEFT_BKWD]
                                             , [TechVetMap.DRIVETRAIN_RIGHT_FWD, TechVetMap.DRIVETRAIN_RIGHT_BKWD])
        return DriveTrain.instance

    def __init__(self, left_pins, right_pins):
        System.__init__(self, "DriveTrain")
        self._left_motor_controller = RPIPWNMotorController(left_pins, TechVetMap.DRIVETRAIN_LEFT_PWM)
        self._right_motor_controller = RPIPWNMotorController(right_pins, TechVetMap.DRIVETRAIN_RIGHT_PWM)
        self._stick = HectorOI.drive_stick
        self._line_tracker = LineTrackingSensor(LINE_SENSOR_ID, LINE_SENSOR_REGISTER)
        self._pid = PIDController(P=0.0002)

    def drive_on_line(self):
        self._pid.setPoint(2500)
        correction = self._pid.update(self._line_tracker.get())

        self.set(DEFAULT_SPEED + correction, DEFAULT_SPEED - correction)

    def _enable(self):
        pass

    def set(self, left_throttle, right_throttle):
        if abs(right_throttle) < .5:
            right_throttle = 0
        if abs(left_throttle) < .5:
            left_throttle = 0

        self._left_motor_controller.set_percent_speed(left_throttle)
        self._right_motor_controller.set_percent_speed(right_throttle)

    def stop(self):
        self._left_motor_controller.set_percent_speed(0)
        self._right_motor_controller.set_percent_speed(0)

    def get_cli_functions(self, args):
        functions = {
            "stop": partial(self.stop)
        }
        if len(args) > 1:
            functions["drive"] = partial(self.set, int(args[0]), int(args[1]))

        return functions
