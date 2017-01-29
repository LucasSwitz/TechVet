from functools import partial

from techvet.TechVetMap import TechVetMap

from System import System
from motorcontrollers.I2CMotorController import I2CMotorController
from techvet.sensors.LineTrackingSensor import LineTrackingSensor
from techvet.sensors.SetPointTracker import SetPointTracker
from PID.PIDController import PIDController

LINE_SENSOR_ID = 0x08
LINE_SENSOR_REGISTER = 0

CHECKPOINT_TRACKER_ID = 0x09
CHECKPOINT_SENSOR_REGISTER = 0

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
        self._left_motor_controller = I2CMotorController(left_pins, 0x08, 0)
        self._right_motor_controller = I2CMotorController(right_pins, 0x08, 1)

        self._line_tracker = LineTrackingSensor(LINE_SENSOR_ID, LINE_SENSOR_REGISTER)
        self._line_tracker.open()

        self._checkpoint_tracker = SetPointTracker(CHECKPOINT_TRACKER_ID, CHECKPOINT_SENSOR_REGISTER)
        self._checkpoint_tracker.track()

        self._pid = PIDController(P=0.0002)

    def drive_on_line(self):
        self._pid.setPoint(2500)
        correction = self._pid.update(self._line_tracker.get())

        self.set(DEFAULT_SPEED + correction, DEFAULT_SPEED - correction)

    def _enable(self):
        pass

    def set(self, left_throttle, right_throttle):
        self._left_motor_controller.set(left_throttle)
        self._right_motor_controller.set(right_throttle)

    def stop(self):
        self._left_motor_controller.set(0)
        self._right_motor_controller.set(0)
        self._line_tracker.stop()

    def get_line_tracker_sensor_value(self):
        return self._line_tracker.get()

    def get_checkpoint_tracker_value(self):
        return self._checkpoint_tracker.get_current_checkpoint()

    def get_cli_functions(self, args):
        functions = {
            "stop": partial(self.stop)
        }
        if len(args) > 1:
            functions["drive"] = partial(self.set, int(args[0]), int(args[1]))

        return functions
