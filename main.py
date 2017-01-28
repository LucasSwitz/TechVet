from bot.BotServer import BotServer
from techvet.TechVet import TechVet

server = BotServer(4444, TechVet.get_instance())
server.start()
