from bot.Bot import Bot
from techvet.commands.DriveByJoystickCommand import DriveByJoystickCommand
from techvet.systems.DriveTrain import DriveTrain



class TechVet(Bot):
    instance = None

    # DriveTrain Config
    drivetrain = DriveTrain.get_instance()
    drivetrain.set_default_command(DriveByJoystickCommand())

    Bot.systems[drivetrain.name()] = drivetrain

    @staticmethod
    def get_instance():
        if TechVet.instance is None:
            TechVet.instance = TechVet()
        return TechVet.instance

    def __init__(self):
        Bot.__init__(self)
