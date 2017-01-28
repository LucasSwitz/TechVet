from bot.Bot import Bot
from techvet.commands.DriveByJoystickCommand import DriveByJoystickCommand
from techvet.commands.LaserStateByButtonCommand import LaserStateByButtonCommand
from techvet.commands.StepTurretByDPad import StepTurretByDPad
from techvet.systems.DriveTrain import DriveTrain
from techvet.systems.Laser import Laser
from techvet.systems.Turret import Turret


class TechVet(Bot):
    instance = None
    # Turret Config
    turret = Turret.get_instance()
    turret.set_default_command(StepTurretByDPad())

    # DriveTrain Config
    drivetrain = DriveTrain.get_instance()
    drivetrain.set_default_command(DriveByJoystickCommand())

    laser = Laser.get_instance()
    laser.set_default_command(LaserStateByButtonCommand())

    Bot.systems[turret.name()] = turret
    Bot.systems[drivetrain.name()] = drivetrain
    Bot.systems[laser.name()] = laser

    @staticmethod
    def get_instance():
        if TechVet.instance is None:
            TechVet.instance = TechVet()
        return TechVet.instance

    def __init__(self):
        Bot.__init__(self)
