from motorcontrollers.I2CMotorController import I2CMotorController

motor = I2CMotorController({23, 17}, 0x08, 0)

while True:
    motor.set(.8)
