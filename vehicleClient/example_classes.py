#!/usr/bin/python
#
# Show the main interfaces of the three sensor classes
#
#

from time import sleep

from altimu.lsm6ds33 import LSM6DS33
from altimu.lis3mdl  import LIS3MDL
from altimu.lps25h   import LPS25H

imu = LSM6DS33()        # Accelerometer and Gyroscope
imu.enable()

magnet = LIS3MDL()      # Magnetometer
magnet.enable()

baro = LPS25H()         # Barometric and Temperature
baro.enable()


while True:
    print "Gyro:", imu.getGyroscopeRaw()
    print "Accelerometer:", imu.getAccelerometerRaw()
    print "Magnet:", magnet.getMagnetometerRaw()
    print "hPa:", baro.getBarometerMillibars()
    print "Altitude (m):", baro.getAltitude()
    sleep(0.2)

    print "Gyro Temperature:", imu.getLSMTemperatureCelsius()
    print "Magnet Temperature:", magnet.getLISTemperatureCelsius()
    print "Baro Temperature:", baro.getLPSTemperatureCelsius()
    sleep(0.1)
