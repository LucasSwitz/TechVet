class InputChannel:
    def __init__(self, state=None):
        self._state = state

    def parseData(self, data):
        if self._state is not None:
            self._state.parse(data)

    def change_input_state(self, state):
        print "Changing input state to: " + state.__class__.__name__
        self._state = state

    def get_input_state(self):
        return self._state
