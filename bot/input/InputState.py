import abc


class InputState:
    def __init__(self):
        pass

    @abc.abstractmethod
    def parse(self, data):
        """Parsing incoming packets"""
        pass
