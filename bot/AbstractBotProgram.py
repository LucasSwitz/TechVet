import abc

from enum import Enum

from bot.Bot import Bot
from command.CommandQueue import CommandQueue


class BotMode(Enum):
    DISABLED = 0
    TELEOP = 1
    AUTONOMOUS = 2


class AbstractBotProgram:
    def __init__(self, bot):
        self._last_mode = None
        self.change_mode(BotMode.DISABLED)
        self._bot = bot

    def on_teleop_start(self):
        CommandQueue.get_instance().clear()
        self._bot.enable_all_systems()
        self._on_teleop_start()

    def on_auto_start(self):
        CommandQueue.get_instance().clear()
        self._bot.enable_all_systems()
        self._on_auto_start()

    def on_disabled_start(self):
        CommandQueue.get_instance().clear()
        self._bot.disable_all_systems()
        self._on_disabled_start()

    @abc.abstractmethod
    def _on_auto_start(self):
        """called once at the start of auto"""
        return

    @abc.abstractmethod
    def _on_teleop_start(self):
        """called once at the start of teleop"""
        return

    @abc.abstractmethod
    def _on_disabled_start(self):
        """called once at the start of disabled"""
        return

    @abc.abstractmethod
    def auto(self):
        """main auto loop"""
        return

    @abc.abstractmethod
    def teleop(self):
        """main teleop loop"""
        return

    @abc.abstractmethod
    def disabled(self):
        """main disabled loop"""
        return

    def run(self):
        while self._bot.is_alive():
            if self._mode == BotMode.DISABLED:
                if self._last_mode != BotMode.DISABLED:
                    self.on_disabled_start()
                self.disabled()
            elif self._mode == BotMode.TELEOP:
                if self._last_mode != BotMode.TELEOP:
                    self.on_teleop_start()
                self.teleop()
            elif self._mode == BotMode.AUTONOMOUS:
                if self._last_mode != BotMode.AUTONOMOUS:
                    self.on_auto_start()
                self.auto()
            self._last_mode = self._mode

    def change_mode(self, mode):
        self._mode = mode

    def get_mode(self):
        return self._mode

    def start_command_queue(self):
        CommandQueue.get_instance().run()

    def stop_command_queue(self):
        CommandQueue.get_instance().clear()
