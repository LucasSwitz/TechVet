from Subscriber import Subscriber
from communication.server.Server import Server


class SubscritpionServer(Server, Subscriber):
    def __init__(self, port):
        Server.__init__(self, port)

    def on_update(self, value):
        pass

    def get_subscriptions(self):
        pass

    def on_data_recieve(self, data):
        pass

    def _build_value_update_packet(self, value):
        bytes = []
