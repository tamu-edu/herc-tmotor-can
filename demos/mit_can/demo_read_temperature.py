from TMotorCANControl.mit_can import TMotorManager_mit_can
import time
import matplotlib.pyplot as plt

Type = 'AK80-9'
ID = 1

def checkTemp(dev):
    while True:
        print(dev.get_temperature_celsius())
        time.sleep(10)

if __name__ == "__main__":
    with TMotorManager_mit_can(motor_type=Type, motor_ID=ID) as dev:
        checkTemp(dev)