import abc


class Command:
    def __init__(self, parallel=False):
        self._parallel = parallel
        self._valid = True
        self.switches = {
            "-p": Command.set_parallel(self, True)
        }
        self._used_system = None
        self._interruptable = True
        self._was_interrupted = False

    def is_parallel(self):
        return self._parallel

    @abc.abstractmethod
    def init(self):
        """Called once at the start of the Command"""

    @abc.abstractmethod
    def finished(self):
        """Returned true when the Command is finished"""

    @abc.abstractmethod
    def execute(self):
        """Called until command is finished"""

    @abc.abstractmethod
    def end(self):
        """Called when command ends"""

    @abc.abstractmethod
    def _interrupted(self):
        """Called when command ends"""

    def interrupt(self):
        self._was_interrupted = True
        self._interrupted()

    def set_attributes(self, args):
        for arg in args:
            self.switches.get(arg)

    def set_interruptable(self, interruptable):
        self._interruptable = interruptable

    def is_interruptable(self):
        return self._interruptable

    @staticmethod
    def from_args(args):
        """Returns object of Class from parsed string"""
        return Command()

    def set_parallel(self, parallel):
        self._parallel = parallel

    def run(self):
        if self.acquire_system():
            self.init()
            while not self.finished() and not self._was_interrupted:
                self.execute()
            self.end()

    def uses(self, system):
        self._used_system = system

    def acquire_system(self):
        if self._used_system is not None:
            return self._used_system.lock(self)
