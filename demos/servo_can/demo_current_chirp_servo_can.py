from NeuroLocoMiddleware.SoftRealtimeLoop import SoftRealtimeLoop
from NeuroLocoMiddleware.SysID import Chirp
# try:
#      from TMotorCANControl.TMotorManager import TMotorManager
# except ModuleNotFoundError:
from sys import path
path.append("/home/pi/HERCLabDrive/herc-tmotor-can/TMotorCANControl/src/")
from TMotorCANControl.servo_can import TMotorManager_servo_can
import time


def chirp_demo(dev, amp=0.4, dt=0.001):
    print("Starting current chirp demo. Press ctrl+C to quit.")
    chirp = Chirp(5, 0.5, 15)
    dev.enter_current_control()
    time.sleep(0.1)

    loop = SoftRealtimeLoop(dt = dt, report=True)
    for t in loop:
        dev.update()
        dev.current_qaxis = amp*chirp.next(t) - 8
        print(dev.current_qaxis)
         # a barely audible note

with TMotorManager_servo_can(motor_type='AK80-9', motor_ID=0) as dev:
    chirp_demo(dev, amp=8)
print("done with chirp_demo()")
