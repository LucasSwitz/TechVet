from bot.input.CLInterpreter import CLInterpreter
from bot.input.InputState import InputState


class CLIInputState(InputState):
    def parse(self, data):
        cli = CLInterpreter()
        data = self.normalize_string(data)
        (base_command, args) = self.get_cli_command(data)
        cli.run_cli_command(base_command, args)

    def get_cli_command(self, user_input):
        base_command = ""
        for c in str(user_input):
            if c == " ":
                return base_command, self.get_cli_args(user_input[len(base_command) + 1:len(user_input)])
            base_command += c
        return base_command, None

    @staticmethod
    def get_cli_args(args_input):
        args = []
        current_arg = ""
        for c in args_input:
            if c == ' ':
                args.append(current_arg)
                current_arg = ""
            else:
                current_arg += c

        args.append(current_arg)
        return args

    @staticmethod
    def normalize_string(string):
        while '  ' in string:
            string = str.replace(string, '  ', ' ')
        if string[len(string) - 1] == ' ':
            string = string[0:len(string) - 1]
        if string[0] == ' ':
            string = string[1:len(string)]
        return string

    def __init__(self):
        pass
