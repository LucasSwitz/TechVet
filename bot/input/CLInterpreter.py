from bot.Bot import Bot
from command.CommandFactory import CommandFactory
from communication.MessageDispatch import MessageDispatch


class CLInterpreter:
    @staticmethod
    def run_execute_command(args):

        if args is None or len(args) < 1:
            MessageDispatch.instance.dispatch("Invalid use of 'execute' ")
            return

        factory = CommandFactory()
        command = factory.parse_command(args)

        if command is not None:
            command.run()

    def run_system_command(self, args):

        if args is None or len(args) < 1:
            MessageDispatch.instance.dispatch("Invalid use of 'execute' ")
            return

        system = Bot.systems.get(args[0], None)

        if system is not None:
            system.cli_input(args[1:len(args)])

    def run_cli_command(self, base, args):
        switch = {
            "execute": self.run_execute_command,
            "system": self.run_system_command
        }

        func = switch.get(base, None)
        if func is not None:
            func(args)
        else:
            MessageDispatch.instance.dispatch("Invalid CLI command")
