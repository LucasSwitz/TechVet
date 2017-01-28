from communication.MessageDispatch import MessageDispatch


class CommandFactory:
    @staticmethod
    def get_command(command_name, args):
        switch = {

        }
        (command, args) = switch.get(command_name)

        if command is None:
            MessageDispatch.instance.dispatch("Invalid command: " + command_name)
        else:
            command.set_attributes(args)

        return command

    def parse_command(self, args):
        command_name = args[0]
        command_args = args[1:]
        return self.get_command(command_name, command_args)
