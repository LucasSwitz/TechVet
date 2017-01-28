import abc


class MessageDispatch:
    instance = None

    class DispatchListener:

        def __init__(self):
            pass

        @abc.abstractmethod
        def handle(self, message):
            """Handle an outgoing message"""
            return

    def __init__(self):
        if not MessageDispatch.instance:
            MessageDispatch.instance = MessageDispatch.__MessageDispatch()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def add_listener(self, listener):
        self.instance.add_listener(listener)

    def dispatch(self, message):
        self.instance.dispatch(message)

    class __MessageDispatch:

        def __init__(self):
            self._listeners = list()

        def add_listener(self, listener):
            self._listeners.append(listener)

        def dispatch(self, message):
            for listener in self._listeners:
                listener.handle(message)
