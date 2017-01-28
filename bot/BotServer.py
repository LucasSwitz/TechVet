from binascii import hexlify

from bot.AbstractBotProgram import BotMode
from bot.BotClient import BotClient
from bot.BotPacket import BotPacket
from bot.BotProgram import BotProgram
from bot.input.CLIInputState import CLIInputState
from bot.input.InputChannel import InputChannel
from bot.input.TeleopInputState import TeleopInputState
from communication.MessageDispatch import MessageDispatch
from communication.server.Server import Server


class BotServer(Server):
    def __init__(self, port, bot):
        Server.__init__(self, port)
        MessageDispatch()
        self.inputChannel = InputChannel()

        self._bot = bot
        self._bot_program = BotProgram(bot)
        self._bot_program.change_mode(BotMode.TELEOP)

    def start(self):
        Server.start(self)
        while not self.has_client():
            pass
        self._bot_program.run()

    def add_client(self, client_socket):
        client = BotClient(client_socket)
        client.add_recieve_listener(self)
        MessageDispatch.instance.add_listener(client)
        client.start()

    def on_data_recieve(self, data):
        if data == "close":
            MessageDispatch.instance.dispatch("Server Closing....")
            self._bot().disable_all_systems()
            Server.stop(self)

        data = self.to_hex(data)
        self.parse_hector_packet(data)

    @staticmethod
    def to_hex(data):
        new_data = [0] * len(data)
        for i in range(0, len(data)):
            new_data[i] = hexlify(data[i])

        return new_data

    def parse_hector_packet(self, data):
        self._check_input_state(data[BotPacket.INPUT_MODE_BYTE])
        self._check_hector_mode(data[BotPacket.HECTOR_MODE_BYTE])

        # Currently set to only work on Joystick
        self.inputChannel.parseData(data[BotPacket.JOYSTICK_RESERVE_START:len(data)])

    def _check_input_state(self, state):
        input_mode = None
        if int(state, 16) == BotPacket.CLI_INPUT_MODE:
            input_mode = CLIInputState()
        elif int(state, 16) == BotPacket.TELEOP_INPUT_MODE:
            input_mode = TeleopInputState()

        if self.inputChannel.get_input_state().__class__ != input_mode.__class__:
            self.inputChannel.change_input_state(input_mode)

    def _check_hector_mode(self, mode):

        modes = {
            BotPacket.HECTOR_MODE_DISABLED: BotMode.DISABLED,
            BotPacket.HECTOR_MODE_AUTO: BotMode.AUTONOMOUS,
            BotPacket.HECTOR_MODE_TELEOP: BotMode.TELEOP
        }

        hector_mode = modes.get(mode)

        if self._bot_program.get_mode() != hector_mode:
            self._bot_program.change_mode(hector_mode)
