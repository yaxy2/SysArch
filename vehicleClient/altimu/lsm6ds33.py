#!/usr/bin/python

### Python library module for ST LSM6DS33 accelerometer and gyroscope ##
#
# This module enables the Raspberry PI embedded computer to set up the
# ST LSM6DS33 integrated accelerometer, gyroscope and temperature MEMS.
#
# The ST LSM6DS33 is an integral part of Pololu's AltIMU-10v5 and
# MinIMU-9v5 Inertial Measurement Units (IMUs).
# [https://www.pololu.com/product/2739]
# [https://www.pololu.com/product/2738]
#
# The datasheet for the ST LSM6DS33 is available at
# [https://www.pololu.com/file/download/LSM6DS33.pdf?file_id=0J1087]
#
# This Python code was initially derived from Pololu's own C++ Arduino
# library, available at [https://github.com/pololu/lsm6-arduino]
#
# The Python code is developed and maintained by
#  Torsten Kurbad <github@tk-webart.de>
#  Aaron S. Crandall <acrandal@gmail.com>
#
########################################################################

# Imports
from i2c import I2C
from constants import *
import time


# Code
class LSM6DS33(I2C):
    """ Class to set up and access LSM6DS33 accelerometer and gyroscope.
    """

    ##
    ## Class variables and constants
    ##

    # I2C addresses
    I2C_LSM6DS33_WHO_ID             = 0x69
    I2C_LSM6DS33_SA0_HIGH_ADDRESS   = 0x6b  # Default / Master
    I2C_LSM6DS33_SA0_LOW_ADDRESS    = 0x6a  # Grounded / Slave

    # Register addresses
    #  ([+] = used in the code, [-] = not used or useful, [ ] = TBD)
    LSM_FUNC_CFG_ACCESS   = 0x01  # [-] Configuration of embedded
                                  #     functions, e.g. pedometer

    LSM_FIFO_CTRL1        = 0x06  # [-] FIFO threshold setting
    LSM_FIFO_CTRL2        = 0x07  # [-] FIFO control register
    LSM_FIFO_CTRL3        = 0x08  # [-] Gyro/Acceleromter-specific FIFO settings
    LSM_FIFO_CTRL4        = 0x09  # [-] FIFO data storage control
    LSM_FIFO_CTRL5        = 0x0A  # [-] FIFO ODR/Mode selection

    LSM_ORIENT_CFG_G      = 0x0B  # [ ] Gyroscope sign/orientation

    LSM_INT1_CTRL         = 0x0D  # [-] INT1 pad control - unavailable for AltIMU
    LSM_INT2_CTRL         = 0x0E  # [-] INT2 pad control - unavailable for AltIMU
    LSM_WHO_AM_I          = 0x0F  # [-] Returns 0x69 (read only)
    LSM_CTRL1_XL          = 0x10  # [+] Acceleration sensor control
    LSM_CTRL2_G           = 0x11  # [+] Angular rate sensor (gyroscope) control
    LSM_CTRL3_C           = 0x12  # [+] Device/communication settings
    LSM_CTRL4_C           = 0x13  # [ ] Bandwith/sensor/communication settings
    LSM_CTRL5_C           = 0x14  # [ ] Rounding/self-test control
    LSM_CTRL6_C           = 0x15  # [ ] Gyroscope settings
    LSM_CTRL7_G           = 0x16  # [ ] Gyroscope settings
    LSM_CTRL8_XL          = 0x17  # [ ] Acceleration sensor settings
    LSM_CTRL9_XL          = 0x18  # [ ] Acceleration sensor axis control
    LSM_CTRL10_C          = 0x19  # [ ] Gyroscope axis control / misc. settings

    LSM_WAKE_UP_SRC       = 0x1B  # [-] Wake up interrupt source register
    LSM_TAP_SRC           = 0x1C  # [-] Tap source register
    LSM_D6D_SRC           = 0x1D  # [-] Orientation sensing for Android devices

    LSM_STATUS_REG        = 0x1E  # [ ] Status register. Shows if new data
                                  #     is available from one or more of the
                                  #     sensors

    LSM_OUT_TEMP_L        = 0x20  # [+] Temperature output, low byte
    LSM_OUT_TEMP_H        = 0x21  # [+] Temperature output, high byte
    LSM_OUTX_L_G          = 0x22  # [+] Gyroscope X output, low byte
    LSM_OUTX_H_G          = 0x23  # [+] Gyroscope X output, high byte
    LSM_OUTY_L_G          = 0x24  # [+] Gyroscope Y output, low byte
    LSM_OUTY_H_G          = 0x25  # [+] Gyroscope Y output, high byte
    LSM_OUTZ_L_G          = 0x26  # [+] Gyroscope Z output, low byte
    LSM_OUTZ_H_G          = 0x27  # [+] Gyroscope Z output, high byte
    LSM_OUTX_L_XL         = 0x28  # [+] Accelerometer X output, low byte
    LSM_OUTX_H_XL         = 0x29  # [+] Accelerometer X output, high byte
    LSM_OUTY_L_XL         = 0x2A  # [+] Accelerometer Y output, low byte
    LSM_OUTY_H_XL         = 0x2B  # [+] Accelerometer Y output, high byte
    LSM_OUTZ_L_XL         = 0x2C  # [+] Accelerometer Z output, low byte
    LSM_OUTZ_H_XL         = 0x2D  # [+] Accelerometer Z output, high byte

    LSM_FIFO_STATUS1      = 0x3A  # [-] Number of unread words in FIFO
    LSM_FIFO_STATUS2      = 0x3B  # [-] FIFO status control register
    LSM_FIFO_STATUS3      = 0x3C  # [-] FIFO status control register
    LSM_FIFO_STATUS4      = 0x3D  # [-] FIFO status control register
    LSM_FIFO_DATA_OUT_L   = 0x3E  # [-] FIFO data output, low byte
    LSM_FIFO_DATA_OUT_H   = 0x3F  # [-] FIFO data output, high byte

    LSM_TIMESTAMP0_REG    = 0x40  # [-] Time stamp first byte data output
    LSM_TIMESTAMP1_REG    = 0x41  # [-] Time stamp second byte data output
    LSM_TIMESTAMP2_REG    = 0x42  # [-] Time stamp third byte data output

    LSM_STEP_TIMESTAMP_L  = 0x49  # [-] Time stamp of last step (for pedometer)
    LSM_STEP_TIMESTAMP_H  = 0x4A  # [-] Time stamp of last step, high byte
    LSM_STEP_COUNTER_L    = 0x4B  # [-] Step counter output, low byte
    LSM_STEP_COUNTER_H    = 0x4C  # [-] Step counter output, high byte

    LSM_FUNC_SRC          = 0x53  # [-] Interrupt source register for
                              #     embedded functions

    LSM_TAP_CFG           = 0x58  # [-] Configuration of embedded functions
    LSM_TAP_THS_6D        = 0x59  # [-] Orientation and tap threshold
    LSM_INT_DUR2          = 0x5A  # [-] Tap recognition settings
    LSM_WAKE_UP_THS       = 0x5B  # [-] Wake up threshold settings
    LSM_WAKE_UP_DUR       = 0x5C  # [-] Wake up function settings
    LSM_FREE_FALL         = 0x5D  # [-] Free fall duration settings
    LSM_MD1_CFG           = 0x5E  # [-] Function routing for INT1
    LSM_MD2_CFG           = 0x5F  # [-] Function routing for INT2

    # Output registers used by the accelerometer
    lsmAccRegisters = [
        LSM_OUTX_L_XL,       # low byte of X value
        LSM_OUTX_H_XL,       # high byte of X value
        LSM_OUTY_L_XL,       # low byte of Y value
        LSM_OUTY_H_XL,       # high byte of Y value
        LSM_OUTZ_L_XL,       # low byte of Z value
        LSM_OUTZ_H_XL,       # high byte of Z value
    ]

    # Output registers used by the gyroscope
    lsmGyroRegisters = [
        LSM_OUTX_L_G,       # low byte of X value
        LSM_OUTX_H_G,       # high byte of X value
        LSM_OUTY_L_G,       # low byte of Y value
        LSM_OUTY_H_G,       # high byte of Y value
        LSM_OUTZ_L_G,       # low byte of Z value
        LSM_OUTZ_H_G,       # high byte of Z value
    ]

    # Output registers used by the temperature sensor
    lsmTempRegisters = [
        LSM_OUT_TEMP_L,     # low byte of temperature value
        LSM_OUT_TEMP_H,     # high byte of temperature value
    ]

    # Acceleration full scale acceleration range settings
    FS_XL_MASK              = 0xF3  # Mask for removing FullScale Accel bits
    FS_XL_2G                = 0x00  # 2g Max measurement range
    FS_XL_4G                = 0x08  # 4g
    FS_XL_8G                = 0x0C  # 8g
    FS_XL_16G               = 0x04  # 16g

    # Acceleration scaling factors
    #  -- found in LSM6D33 spec sheet, page 15
    ACC_SCALE_FACTOR_2g     = 0.061     # Raw value * factor == mg
    ACC_SCALE_FACTOR_4g     = 0.122
    ACC_SCALE_FACTOR_8g     = 0.244
    ACC_SCALE_FACTOR_16g    = 0.488

    G2MPS2                  = 9.80665  # Scaling factor for Gravities to M/S^2
        # Technically, this should be based on altitude
        # See the simple explanation here: 
        # https://simple.wikipedia.org/wiki/Acceleration_due_to_gravity#Altitude
        # Value used here is at Earth's sea level

    # Gyroscope full scale degrees per second settings
    GYRO_FS_MASK            = 0xF1  # Mask for removing Full-Scale Gyro bits
    GYRO_FS_125dps          = 0x02  # FS_G 001 - 125 dps
    GYRO_FS_245dps          = 0x00  # FS_G 000 - 245 dps
    GYRO_FS_500dps          = 0x04  # FS_G 010 - 500 dps
    GYRO_FS_1000dps         = 0x08  # FS_G_100 - 1000 dps
    GYRO_FS_2000dps         = 0x0c  # FS_G 110 - 2000 dps

    # Gyroscope scaling factors
    GYRO_SCALE_FACTOR_125dps    = 4.375  # Raw value * factor == mdps
    GYRO_SCALE_FACTOR_245dps    = 8.750
    GYRO_SCALE_FACTOR_500dps    = 17.500
    GYRO_SCALE_FACTOR_1000dps   = 35.000
    GYRO_SCALE_FACTOR_2000dps   = 70.000


    ##
    ## Class methods
    ##

    ## Private methods
    def __init__(self, busId = 1, sa0 = SA0_HIGH):
        """ Set up I2C connection and initialize some flags and values.
        """
        super(LSM6DS33, self).__init__(busId)

        self.I2C_ADDR = self.I2C_LSM6DS33_SA0_HIGH_ADDRESS
        if sa0 == SA0_LOW:
            self.I2C_ADDR = self.I2C_LSM6DS33_SA0_LOW_ADDRESS
        # Need to check if the self.WHO_ID is correct - raise if not

        self.accEnabled = False
        self.gyroEnabled = False
        self.lsmTempEnabled = False

        self.currAccScaleFactor = self.ACC_SCALE_FACTOR_4g        #default
        self.currGyroScaleFactor = self.GYRO_SCALE_FACTOR_1000dps #default


    def __del__(self):
        """ Clean up routines. """
        try:
            # Power down accelerometer
            self._writeRegister(self.I2C_ADDR, self.LSM_CTRL1_XL, 0x00)
            # Power down gyroscope
            self._writeRegister(self.I2C_ADDR, self.LSM_CTRL2_G, 0x00)
            super(LSM6DS33, self).__del__()
        except:
            pass


    ## Public methods
    def enable(self, accelerometer = True, gyroscope = True,
                  temperature = True):
        """ Enable and set up the given sensors in the IMU device. """
        # Disable accelerometer and gyroscope first
        self._writeRegister(self.I2C_ADDR, self.LSM_CTRL1_XL, 0x00)
        self._writeRegister(self.I2C_ADDR, self.LSM_CTRL2_G, 0x00)
        self._writeRegister(self.I2C_ADDR, self.LSM_CTRL3_C, 0x00)

        # Initialize flags
        self.accEnabled = False
        self.gyroEnabled = False
        self.lsmTempEnabled = False

        # Disable FIFO
        self._writeRegister(self.I2C_ADDR, self.LSM_FIFO_CTRL5, 0x00)

        if accelerometer:
            # Accelerometer - defaults: 1.66 kHz / +/- 4g
            self._writeRegister(self.I2C_ADDR, self.LSM_CTRL1_XL, 0x58)
            self.accEnabled = True
            self.setAccelerometerFullScale4G()

        if gyroscope:
            # Gyro - defaults: 208 Hz high performance / 1000 dps
            self._writeRegister(self.I2C_ADDR, self.LSM_CTRL2_G, 0x58)
            self.gyroEnabled = True
            self.setGyroscopeFullScale1000dps()

        if temperature:
            # Temperature sensor on LSM6DS33 is "always on"
            self.lsmTempEnabled = True
    
    # Acclerometer full scale setting interfaces
    #
    def setAccelerometerFullScale2G(self):
        self._setAccelerometerFullScale(self.FS_XL_2G)
    def setAccelerometerFullScale4G(self):
        self._setAccelerometerFullScale(self.FS_XL_4G)
    def setAccelerometerFullScale8G(self):
        self._setAccelerometerFullScale(self.FS_XL_8G)
    def setAccelerometerFullScale16G(self):
        self._setAccelerometerFullScale(self.FS_XL_16G)

    def _setAccelerometerFullScale(self, registerSetting):
        """ Set the maximum scale range for the accelerometer """
        if not self.accEnabled:      # Check if accelerometer has been enabled
            raise(Exception('Accelerometer has to be enabled first'))

        curr_reg = self._readRegister(self.I2C_ADDR, self.LSM_CTRL1_XL) 
        curr_reg = curr_reg & self.FS_XL_MASK       # Mask off FS_XL bits
        curr_reg = curr_reg | registerSetting       # Set new FS_XL bits
        self._writeRegister(self.I2C_ADDR, self.LSM_CTRL1_XL, curr_reg)

        # Retain the current scaling factor
        if( registerSetting == self.FS_XL_2G ):
            self.currAccScaleFactor = self.ACC_SCALE_FACTOR_2g
        elif( registerSetting == self.FS_XL_4G ):
            self.currAccScaleFactor = self.ACC_SCALE_FACTOR_4g
        elif( registerSetting == self.FS_XL_8G ):
            self.currAccScaleFactor = self.ACC_SCALE_FACTOR_8g
        elif( registerSetting == self.FS_XL_16G ):
            self.currAccScaleFactor = self.ACC_SCALE_FACTOR_16g
        else:
            raise(Exception('Accelerometer scale set to invalid value: ' +
                             hex(registerSetting)))
        # MUST do a sleep here to let the sensor re-scale
        # otherwise the first samples will be *way* off
        # found by guess and check - no documentation source for this
        time.sleep(0.01)


    def getAccelerometerRaw(self):
        """ Return a 3-dimensional vector (list) of raw accelerometer
            data.
        """
        # Check if accelerometer has been enabled
        if not self.accEnabled:
            raise(Exception('Accelerometer has to be enabled first'))

        # Read sensor data
        return self._getSensorRawLoHi3(self.I2C_ADDR, self.lsmAccRegisters)


    def getAccelerometerGravities(self):
        """ Return a 3-dimensional vector (list) of accelerometer values
            converted to Gravities based on current scaling factor
        """
        rawValues = self.getAccelerometerRaw()
        gValues = list(map(lambda x: x * self.currAccScaleFactor / 1000, 
                            rawValues))
        return gValues

    def getAccelerometerMPS2(self):
        """ Return a 3-dimensional vector (list) of accelerometer values
            converted to m/s^2
        """
        gValues = self.getAccelerometerGravities()
        mps2Values = list(map(lambda x: x * self.G2MPS2, gValues))
        return mps2Values

    # Gyroscope full scale setting interfaces
    #
    def setGyroscopeFullScale125dps(self):
        self._setGyroscopeFullScale(self.GYRO_FS_125dps)
    def setGyroscopeFullScale245dps(self):
        self._setGyroscopeFullScale(self.GYRO_FS_245dps)
    def setGyroscopeFullScale500dps(self):
        self._setGyroscopeFullScale(self.GYRO_FS_500dps)
    def setGyroscopeFullScale1000dps(self):
        self._setGyroscopeFullScale(self.GYRO_FS_1000dps)
    def setGyroscopeFullScale2000dps(self):
        self._setGyroscopeFullScale(self.GYRO_FS_2000dps)

    def _setGyroscopeFullScale(self, registerSetting):
        """ Set the maximum scale range for the accelerometer """
        if not self.gyroEnabled:      # Check if gyroscope has been enabled
            raise(Exception('Gyroscope has to be enabled first'))

        curr_reg = self._readRegister(self.I2C_ADDR, self.LSM_CTRL2_G) 
        curr_reg = curr_reg & self.GYRO_FS_MASK       # Mask off FS_XL bits
        curr_reg = curr_reg | registerSetting         # Set new FS_XL bits
        self._writeRegister(self.I2C_ADDR, self.LSM_CTRL2_G, curr_reg)

        # Retain the current scaling factor
        if( registerSetting == self.GYRO_FS_125dps ):
            self.currGyroScaleFactor = self.GYRO_SCALE_FACTOR_125dps
        elif( registerSetting == self.GYRO_FS_245dps ):
            self.currGyroScaleFactor = self.GYRO_SCALE_FACTOR_245dps
        elif( registerSetting == self.GYRO_FS_500dps ):
            self.currGyroScaleFactor = self.GYRO_SCALE_FACTOR_500dps
        elif( registerSetting == self.GYRO_FS_1000dps ):
            self.currGyroScaleFactor = self.GYRO_SCALE_FACTOR_1000dps
        elif( registerSetting == self.GYRO_FS_2000dps ):
            self.currGyroScaleFactor = self.GYRO_SCALE_FACTOR_2000dps
        else:
            raise(Exception('Gyroscope scale set to invalid value: ' +
                             hex(registerSetting)))
        # MUST do a sleep here to let the sensor re-scale
        # otherwise the first samples will be *way* off
        # found by guess and check - no documentation source for this
        time.sleep(0.01)

    #
    def getGyroscopeRaw(self):
        """ Return a 3-dimensional vector (list) of raw gyroscope data.
        """
        # Check if gyroscope has been enabled
        if not self.gyroEnabled:
            raise(Exception('Gyroscope has to be enabled first'))

        # Read sensor data
        return self._getSensorRawLoHi3(self.I2C_ADDR, self.lsmGyroRegisters)

    #
    def getGyroscopeMDPS(self):
        """ Return a 3-dimensional vector (list) of gyroscope values
            converted to milli-degrees per second using current scaling factor
        """
        rawValues = self.getGyroscopeRaw()
        gValues = list(map(lambda x: x * self.currGyroScaleFactor, 
                            rawValues))
        return gValues

    #
    def getGyroscopeDPS(self):
        """ Return a 3-dimensional vector (list) of gyroscope values
            converted to degrees per second using current scaling factor
        """
        rawValues = self.getGyroscopeRaw()
        gValues = list(map(lambda x: x * self.currGyroScaleFactor / 1000, 
                            rawValues))
        return gValues


    #
    def getLSMTemperatureCelsius(self, rounded = True):
	if rounded:
	    return round(25.0 + self.getLSMTemperatureRaw() / 16.0, 1)
        return 0.25 + self.getLSMTemperatureRaw() / 16.0
    
    #
    def getLSMTemperatureRaw(self):
        if not self.lsmTempEnabled:
	    raise(Exception('Temperature sensor has not be enabled first'))

        return self._getSensorRawLoHi1(LSM6DS33_ADDR, self.lsmAccRegisters)
    

    # Thermometer interface
    #
    def getTemperatureRaw(self):
        """ Return the raw temperature value. """
        # Check if device has been set up
        if not self.lsmTempEnabled:
            raise(Exception('Temperature sensor has to be enabled first'))

        # Read sensor data
        return self._getSensorRawLoHi1(self.I2C_ADDR, self.lsmTempRegisters)

    #
    def getTemperatureCelsius(self, rounded = True):
        """ Return the temperature sensor reading in C as a floating
            point number rounded to one decimal place by default.
        """
        # According to the datasheet, the raw temperature value is 0
        # @ 25 degrees Celsius and the resolution of the sensor is 16
        # steps per degree Celsius.
        # Thus, the following statement should return the temperature in
        # degrees Celsius.
        celsius = 25.0 + self.getTemperatureRaw() / 16.0
        if rounded:
            celsius = round(celsius, 1)
        return celsius


    # General all data interfaces
    #
    def getIMURaw(self):
        """ Return a 6-element list of the raw output values of both IMU
            sensors, accelerometer and gyroscope.
        """
        return self.getAccelerometerRaw() + self.getGyroscopeRaw()


    def getAllRaw(self):
        """ Return a 7-element list of the raw output of all three
            sensors, accelerometer, gyroscope, temperature.
        """
        return self.getAccelerometerRaw() \
                + self.getGyroscopeRaw() \
                + [self.getTemperatureRaw()]


