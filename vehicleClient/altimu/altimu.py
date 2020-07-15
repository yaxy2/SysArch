#!/usr/bin/python

### Python module to control several aspects of Pololu's AltIMU-10v5 ###
#
# This module enables the Raspberry PI embedded computer to set up and
#  use various aspects of Pololu's AltIMU-10v5 Inertial Measurement Unit (IMU)
# [https://www.pololu.com/product/2739]
#
# This Python code was initially derived from Pololu's own C++ Arduino
#  libraries, available at [https://github.com/pololu]
#
# The Python code was first developed and maintained by:
#  Torsten Kurbad <github@tk-webart.de>
#
# Code now continued by:
#  Aaron Crandall <acrandal@gmail.com>
#
########################################################################

# Imports

from constants import *         # Includes addresses on I2C bus
from lsm6ds33 import LSM6DS33   # Accel & Gyro (+ temp)
from lis3mdl import LIS3MDL     # Magnetometer (+ temp)
from lps25h import LPS25H       # Barometric Pressure & Temperature


#
# Facade class composing all three devices
#
class AltIMU():
    """ Facade class to compose Pololu's AltIMU-10v5. """

    # Private methods
    def __init__(self, busId = 1, sa0 = SA0_HIGH):
        """ Compose other classes
            busId refers to the I2C bus to use (default 1)
            sa0 refers to the I2C Master/Slave address pin status
                SA0_HIGH (default) == pullup to vcc => Master addresses
                SA0_LOW == grounded => Slave addresses
        """
        self.imu = LSM6DS33( busId = busId, sa0 = sa0 )
        self.magnet = LIS3MDL( busId, sa0 = sa0 )
        self.baro = LPS25H( busId, sa0 = sa0 )
    

    def __del__(self):
        """ Cleanup routine. """
        pass

    """ Interfaces to enable different sensors """
    def enable_accelerometer(self):
        """ Enable the Accelerometer """
        self.enable( accelerometer = True, gyroscope = False,
                     magnetometer = False,
                     barometer = False, temperature = False )

    def enable_gyroscope(self):
        """ Enable the Gyroscope """
        self.enable( accelerometer = False, gyroscope = True,
                     magnetometer = False, 
                     barometer = False, temperature = False )

    def enable_magnetometer(self):
        """ Enable the Magnetometer """
        self.enable( accelerometer = False, gyroscope = False,
                     magnetometer = True,
                     barometer = False, temperature = False )

    def enable_barometer(self):
        """ Enable the Barometer """
        self.enable( accelerometer = False, gyroscope = False,
                     magnetometer = False,
                     barometer = True, temperature = False )

    def enable_temperature(self):
        """ Enable the Thermometer """
        self.enable( accelerometer = False, gyroscope = False,
                     barometer = False,
                     magnetometer = False, temperature = True )

    def enable(self, accelerometer = True, gyroscope = True, 
               magnetometer = True, barometer = True, temperature = True):
        """ Enable the given devices. """
        # Enable LSM6DS33 if accelerometer and/or gyroscope are requested
        if accelerometer or gyroscope:
            self.imu.enable(accelerometer = accelerometer,
                                gyroscope = gyroscope,
                                temperature = temperature)

        # Enable LIS3MDL if magnetometer is requested
        if magnetometer:
            self.magnet.enable(magnetometer = magnetometer,
                                    temperature = temperature)

        # Enable LPS25H if barometric pressure or temperature sensors
        # are requested
        if barometer or temperature:
            self.baro.enable()

    """ Facade accelerometer interface """
    # Acclerometer full scale setting interfaces
    def setAccelerometerFullScale2G(self):
        self.imu.setAccelerometerFullScale2G()
    def setAccelerometerFullScale4G(self):
        self.imu.setAccelerometerFullScale4G()
    def setAccelerometerFullScale8G(self):
        self.imu.setAccelerometerFullScale8G()
    def setAccelerometerFullScale16G(self):
        self.imu.setAccelerometerFullScale16G()

    def getAccelerometerRaw(self):
        return self.imu.getAccelerometerRaw()
    def getAccelerometerGravities(self):
        return self.imu.getAccelerometerGravities()

    def getAccelerometerMPS2(self):
        return self.imu.getAccelerometerMPS2()
    def getAcceleration(self):
        return self.imu.getAccelerometerMPS2()

    """ Facade gyroscope interface """
    # gyroscope full scale setting interfaces
    def setGyroscopeFullScale125dps(self):
        self.imu.setGyroscopeFullScale125dps()
    def setGyroscopeFullScale245dps(self):
        self.imu.setGyroscopeFullScale245dps()
    def setGyroscopeFullScale500dps(self):
        self.imu.setGyroscopeFullScale500dps()
    def setGyroscopeFullScale1000dps(self):
        self.imu.setGyroscopeFullScale1000dps()
    def setGyroscopeFullScale2000dps(self):
        self.imu.setGyroscopeFullScale2000dps()

    def getGryoscopeMDPS(self):
        return self.imu.getGyroscopeMDPS()
    def getGryoscopeDPS(self):
        return self.imu.getGyroscopeDPS()


    """ Facade magnetometer interface """
    def getMagnetometerRaw(self):
        return self.magnet.getMagnetometerRaw()


    """ Facade barometric pressure interface """
    def getBarometerMillibars(self, rounded=True):
        return self.baro.getBarometerMillibars(rounded)

    def getAltitude(self, altimeterMbar = 1013.25, rounded = True):
        return self.baro.getAltitude(altimeterMbar, rounded)


    """ Facade temperature interface """
    def getTemperatureCelsius(self, rounded=True):
        return self.baro.getTemperatureCelsius(rounded)

    def getTemperatureFahrenheit(self, rounded=True):
        return self.baro.getTemperatureFahrenheit(rounded)


#
# Polymorphic inheritance to hide pin setting details
#
class AltIMU_Slave(AltIMU, object):
    def __init__(self, busId = 1):
        super(AltIMU_Slave, self).__init__(busId, sa0=SA0_LOW)

class AltIMU_Master(AltIMU, object):
    def __init__(self, busId = 1):
        super(AltIMU_Master, self).__init__(busId, sa0=SA0_HIGH)
