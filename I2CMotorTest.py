from motorcontrollers.I2CMotorController import I2CMotorController

pins_left = [17, 23]
motor_left = I2CMotorController(pins_left, 0x09, 0)


pins_right = [27, 22]
motor_right = I2CMotorController(pins_right, 0x09, 1)

while True:
    motor_left.set(.8)
    motor_right.set(.81)
