class Subscriber:
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_subscriptions(self):
        """Return a list of subscription"""

    @abc.abstractmethod
    def on_update(self, value):
        """Define what to do with a value when a susbcribed value is updated"""
        return
