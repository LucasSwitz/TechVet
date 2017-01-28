from command.Command import Command
from techvet.TechVetOI import HectorOI
from techvet.systems.Turret import Turret


class StepTurretByDPad(Command):
    def init(self):
        pass

    def execute(self):
        hat_angle = self._stick.get_hat_button_angle()
        if hat_angle == 135:
            Turret.get_instance().step_pan(True)
        elif hat_angle == 315:
            Turret.get_instance().step_pan(False)
        elif hat_angle == 225:
            Turret.get_instance().step_tilt(True)
        elif hat_angle == 45:
            Turret.get_instance().step_tilt(False)

    def finished(self):
        return False

    def end(self):
        pass

    def _interrupted(self):
        self.end()

    def __init__(self):
        Command.__init__(self, parallel=True)
        self.uses(Turret.get_instance())
        self._stick = HectorOI.drive_stick
