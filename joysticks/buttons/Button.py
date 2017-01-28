import abc


class Button:
    XL_ID = 0x30
    YL_ID = 0x31
    ZL_ID = 0x32

    XR_ID = 0x33
    YR_ID = 0x34
    ZR_ID = 0x35

    HAT_BUTTON_ID = 0x39
    A_BUTTON_ID = 11

    def __init__(self, id_number):
        self._id = id_number
        self._value = 0

    def get_id(self):
        return self._id

    def get_value(self):
        return self._value

    def update(self, value):
        self._value = value

    @abc.abstractmethod
    def get(self):
        """Return true when command should be launched"""
