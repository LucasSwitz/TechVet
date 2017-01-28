import threading


class ClientThread(threading.Thread):
    CHUNK_SIZE = 1024

    def __init__(self, sock):
        super(ClientThread, self).__init__()
        self._clientSocket = sock
        self._running = False
        self._listener = None

    def run(self):
        self._running = True
        while self._running:
            data = self._clientSocket.recv(self.CHUNK_SIZE)
            if len(data) != 0:
                self.update_listener(data)

    def kill(self):
        self._running = False

    def add_recieve_listener(self, listener):
        self._listener = listener

    def update_listener(self, data):
        if self._listener is not None:
            self._listener.on_data_recieve(data)

    # send out bytes
    def send(self, out):
        self._clientSocket.send(out)
