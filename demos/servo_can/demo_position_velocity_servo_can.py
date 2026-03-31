from NeuroLocoMiddleware.SoftRealtimeLoop import SoftRealtimeLoop
# try:
#      from TMotorCANControl.TMotorManager import TMotorManager
# except ModuleNotFoundError:
from sys import path
path.append("/home/pi/TMotorCANControl/src/")
from TMotorCANControl.servo_can import TMotorManager_servo_can
import time
import numpy as np

ID=0


with TMotorManager_servo_can(motor_type='AK80-9', motor_ID=ID) as dev:
    loop = SoftRealtimeLoop(dt=0.01, report=True, fade=0.0)
    dev.enter_position_velocity_control()
    for t in loop:
        dev.set_output_angle_radians(np.pi/4, vel=0.5, acc=0.5)
        dev.update()
        print("\r" + str(dev),end='')

