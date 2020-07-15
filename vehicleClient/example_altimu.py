#!/usr/bin/python

from datetime import datetime
from time import sleep

from altimu.altimu import AltIMU

imu = AltIMU()
imu.enable()

start = datetime.now()

while True:
    print(" Sampling")
    sleep(0.02)
