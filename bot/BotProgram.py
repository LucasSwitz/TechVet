from AbstractBotProgram import AbstractBotProgram
from command.CommandQueue import CommandQueue
from communication.MessageDispatch import MessageDispatch


class BotProgram(AbstractBotProgram):
    def __init__(self, bot):
        AbstractBotProgram.__init__(self, bot)

    def teleop(self):
        CommandQueue.get_instance().run()

    def auto(self):
        pass

    def disabled(self):
        pass

    def _on_auto_start(self):
        pass

    def _on_disabled_start(self):
        MessageDispatch.instance.dispatch("Entered Disabled!")
        print "Entered Disabled!"

    def _on_teleop_start(self):
        MessageDispatch.instance.dispatch("Entered Teleop!")
        print "Entered Teleop"
