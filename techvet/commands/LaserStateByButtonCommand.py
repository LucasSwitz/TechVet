from command.Command import Command
from techvet.TechVetOI import HectorOI
from techvet.systems.Laser import Laser


class LaserStateByButtonCommand(Command):
    def __init__(self):
        Command.__init__(self)
        self._laser = Laser.get_instance()
        self.uses(self._laser)
        self._stick = HectorOI.drive_stick

    def init(self):
        Command.__init__(self, parallel=True)

    def execute(self):

        if self._laser.is_on():
            if not self._stick.get_a_button():
                self._laser.off()
        else:
            if self._stick.get_a_button():
                self._laser.on()

    def _interrupted(self):
        self.end()

    def end(self):
        pass

    def finished(self):
        return True
