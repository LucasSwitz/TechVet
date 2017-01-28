class Bot:
    instance = None

    systems = dict()

    def disable_all_systems(self):
        for system in self.systems.values():
            system.stop()

    def enable_all_systems(self):
        for system in self.systems.values():
            system.enable()

    def is_alive(self):
        return self._alive

    def kill(self):
        self._alive = False

    def __init__(self):
        self._alive = True
