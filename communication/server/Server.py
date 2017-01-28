import abc
import socket
from threading import Thread

from communication.server.Client import ClientThread
from communication.server.ClientListener import ClientListener


class Server(ClientListener):
    @abc.abstractmethod
    def on_data_recieve(self, data):
        """Do something with client data"""
        return

    MAX_NUM_OF_CONNECTIONS = 5

    def __init__(self, port):
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._running = False
        self._has_client = False
        self.setup()

    def setup(self):
        print("Setting up server or port: " + str(self._port))
        self._socket.bind(('', self._port))
        self._socket.listen(Server.MAX_NUM_OF_CONNECTIONS)

    def _start(self):
        print("Waiting for clients to connect...")
        self._running = True
        while self._running:
            (client_socket, address) = self._socket.accept()

            print("Client accepted from: " + str(address))
            self._has_client = True
            self.add_client(client_socket)

    def start(self):
        run_thread = Thread(target=self._start)
        run_thread.start()

    def has_client(self):
        return self._has_client

    def add_client(self, client_socket):
        client = ClientThread(client_socket)
        client.add_recieve_listener(self)
        client.start()

    def is_running(self):
        return self._running

    def stop(self):
        self._running = False
        self._socket.shutdown(socket.SHUT_RDWR)
        self._socket.close()
