from bot.BotServer import BotServer
from techvet.TechVet import Hector

server = BotServer(4444, Hector.get_instance())
server.start()
