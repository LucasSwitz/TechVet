from enum import Enum


class SubscriptionBase:
    instance = None

    def __init__(self):
        self._subscriptions = dict()

    def add_subscriber(self, subscriber):
        for subscription in subscriber.get_subscriptions():
            if subscription.get_name not in self._subscriptions:
                self._add_subcription(subscription)
            self._subscriptions[subscription.name].append(subscriber)

    def update(self, value):
        if value.name not in self._subscriptions.keys():
            self._add_subcription(value)
        self.update_subscribers(value)

    def _add_subcription(self, subscription):
        self._subscriptions[subscription.name] = list()

    def update_subscribers(self, value):
        for sub in self._subscriptions.get(value.name):
            sub.on_update(value)

    @staticmethod
    def get_instance():
        if SubscriptionBase.instance is None:
            SubscriptionBase.instance = SubscriptionBase()
        return SubscriptionBase.instance


class SubscriptionValue:
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type

    def __setattr__(self, key, value):
        self.value = value
        SubscriptionBase.get_instance().update(self)


class SubscriptionType(Enum):
    BOOL = 0
    INT = 1
    FLOAT = 2
    STRING = 3
    BYTE = 5
