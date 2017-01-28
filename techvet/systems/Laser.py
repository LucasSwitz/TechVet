from digital_out.DigitalOut import RpiDigitalOut
from techvet.TechVetMap import HectorMap
from techvet.systems.System import System


class Laser(System):
    instance = None

    def __init__(self):
        System.__init__(self, "Laser")
        self._digital_out = RpiDigitalOut(HectorMap.LASER_DIGITAL_OUT)
        self._on = False

    def stop(self):
        pass

    def get_cli_functions(self, args):
        pass

    def _enable(self):
        pass

    def on(self):
        self.dispatch_message("Laser On!")
        self._digital_out.set_high()
        self._on = True

    def off(self):
        self.dispatch_message("Laser Off!")
        self._digital_out.set_low()
        self._on = False

    def disable(self):
        self.off()

    def is_on(self):
        return self._on

    @staticmethod
    def get_instance():
        if Laser.instance is None:
            Laser.instance = Laser()
        return Laser.instance
