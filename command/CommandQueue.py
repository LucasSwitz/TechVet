from Queue import Queue
from threading import Thread


class CommandQueue:
    instance = None

    def __init__(self):
        self._q = Queue()

    def add_command(self, command):
        self._q.put(command)

    def run(self):
        while self._q.qsize() > 0:
            command = self._q.get()
            if command.is_parallel():
                self._run_parallel(command)
            else:
                command.run()

    def clear(self):
        self._q.empty()

    def _run_parallel(self, command):
        thread = Thread(target=command.run)
        thread.daemon = True
        thread.start()

    @staticmethod
    def get_instance():
        if CommandQueue.instance is None:
            CommandQueue.instance = CommandQueue()
        return CommandQueue.instance
