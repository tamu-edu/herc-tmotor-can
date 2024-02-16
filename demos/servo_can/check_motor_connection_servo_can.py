from TMotorCANControl.servo_can import TMotorManager_servo_can
print("loading from home/jedsimms/HERCLabDrive/TMotorCANControl/demos/servo_can/check_motor_connection_servo_can.py")
# CHANGE THESE TO MATCH YOUR DEVICE!
Type = 'AK80-9'
ID = 0

with TMotorManager_servo_can(motor_type=Type, motor_ID=ID) as dev:
    if dev.check_can_connection():
        print("\nmotor is successfully connected!\n")
    else:
        print("\nmotor not connected. Check dev power, network wiring, and CAN bus connection.\n")
    