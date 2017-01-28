from command.Command import Command
from techvet.TechVet import TechVet

class DriveToCheckpointCommand(Command):
    def __init__(self, checkpoint):
        Command.__init__(self)
        self._checkpoint = checkpoint
        self._drive_train = TechVet.drivetrain
        self._checkpoint_tracker = TechVet.drivetrain.get_instance().get_check_point_senor()
        self._finished = False

    def init(self):
        pass

    def execute(self):

        if self._checkpoint_tracker.get_current_checkpoint_count() != self._checkpoint:
            self._drive_train.drive_on_line()
        else:
            self._finished = True

    def finished(self):
        return self._finished

    def end(self):
        self._checkpoint_tracker.pause()
        self._drive_train.set(0, 0)

    def _interrupted(self):
        pass
