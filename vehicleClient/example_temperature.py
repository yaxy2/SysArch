#!/usr/bin/python
#
#  Demonstration of getting the temperature reading from the LPS25H
#

from datetime import datetime
from time import sleep

from altimu.altimu import AltIMU

imu = AltIMU()
imu.enable_temperature()

print(" Temperature in Celsius: \t" + str(imu.getTemperatureCelsius()))
print(" Temperature in Fahrenheit: \t" + str(imu.getTemperatureFahrenheit()))

print("Done")
