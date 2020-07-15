#!/usr/bin/python

### Python module to control several aspects of Pololu's AltIMU-10v5 ###
#
# This file contains several constants used by the various module
# classes.
#
# The Python code is developed and maintained by
# Torsten Kurbad <github@tk-webart.de>
#
########################################################################

## Global constants

# I2C device addresses - Chip select SA0 == 1 (default)
LSM6DS33_ADDR   = 0x6b      # Gyrometer / accelerometer
#LIS3MDL_ADDR    = 0x1e      # Magnetometer
LPS25H_ADDR     = 0x5d      # Barometric pressure sensor


# I2C device addresses - Chip select SA0 == 0
LSM6DS33_ADDR_SLAVE   = 0x6a      # Gyrometer / accelerometer
LIS3MDL_ADDR_SLAVE    = 0x1c      # Magnetometer
LPS25H_ADDR_SLAVE     = 0x5c      # Barometric pressure sensor

SA0_HIGH    = 1             # SA0 uses 10k ohm pullup internally - default
SA0_LOW     = 0
#SA0_DEFAULT = SA0_HIGH     # SA0 uses 10k ohm pullup internally


#LSM6DS33 constants - Accelerometer & Gryoscope
#LSM6DS33_WHO_ID    0x69
#LSM6DS33_SA0_HIGH_ADDRESS 0b1101011 # 0x6b
#LSM6DS33_SA0_LOW_ADDRESS  0b1101010 # 0x6a


#LIS3MDL constants - Magnetometer
#LIS3MDL_WHO_ID  0x3D
#LIS3MDL_SA0_HIGH_ADDRESS  0b0011110  # 0x1e
#LIS3MDL_SA0_LOW_ADDRESS   0b0011100  # 0x1c


#LPS25H constants - Barometric pressure sensor
#LPS25H_WHO_ID   0xBD
#LPS25H_SA0_HIGH_ADDRESS 0b1011101  # 0x5d
#LPS25H_SA0_LOW_ADDRESS  0b1011100  # 0x5c

