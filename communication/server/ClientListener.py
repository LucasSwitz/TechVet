import abc


class ClientListener:
    @abc.abstractmethod
    def on_data_recieve(self, data):
        """Do something with recieved Client data"""
        return
