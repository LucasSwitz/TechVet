from command.Command import Command
from techvet.TechVetOI import HectorOI
from techvet.systems.DriveTrain import DriveTrain


class DriveByJoystickCommand(Command):
    def __init__(self):
        Command.__init__(self, parallel=True)
        self._drive_train = DriveTrain.get_instance()
        self.uses(self._drive_train)
        self._stick = HectorOI.drive_stick

    def init(self):
        self._drive_train.dispatch_message("Driving with joysticks...")
        print "Started Drive By Joystick"

    def execute(self):

        left_throttle = self._stick.get_left_Y()
        right_throttle = self._stick.get_right_Y()

        self._drive_train.set(left_throttle, right_throttle)

    def _interrupted(self):
        self.end()

    def finished(self):
        return False

    def end(self):
        pass
