from communication.MessageDispatch import MessageDispatch
from communication.server.Client import ClientThread


class BotClient(ClientThread, MessageDispatch.DispatchListener):
    def handle(self, message):
        ClientThread.send(self, str.encode(message))
