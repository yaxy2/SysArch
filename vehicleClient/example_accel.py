#!/usr/bin/python
#
# Show the main interfaces of the three sensor classes
#
#

from time import sleep

from altimu.lsm6ds33 import LSM6DS33


imu = LSM6DS33()        # Accelerometer and Gyroscope
imu.enable()            # Must be enabled before use!

# Accelerometer is set to 4g max scale by default
# These interfaces allow it to be set to other ranges
imu.setAccelerometerFullScale2G()
imu.setAccelerometerFullScale4G()
imu.setAccelerometerFullScale8G()
imu.setAccelerometerFullScale16G()


# Series of samples to demonstrate reading values
max_samples = 10
for i in range(max_samples):
    print "Sample " + str(i + 1) + " / " + str(max_samples)
    print "Gyro:", imu.getGyroscopeRaw()
    print "Accelerometer:", imu.getAccelerometerRaw()
    sleep(0.2)

    print "Gyro Temperature:", imu.getLSMTemperatureCelsius()
    print ""
    sleep(0.1)

