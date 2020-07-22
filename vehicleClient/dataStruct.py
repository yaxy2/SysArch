

from time import sleep
from altimu.altimu import AltIMU
from altimu.lsm6ds33 import LSM6DS33
from altimu.lis3mdl  import LIS3MDL
from altimu.lps25h   import LPS25H
import time
import datetime
import RPi.GPIO as GPIO
from MFRC522.MFRC522 import *
from Read import read

class DataStructSensor:
  
  lidar = 0
  humidity = 0
  steering_angle = 0
  temperature = 0
  speed = 0
  alti = 0
  acc = [0, 0, 0]
  mag = [0, 0, 0]
  gyro = [0, 0, 0]
  ts = 0
  abs_acc = 0
  
  
  def get_data(self):
    imu = AltIMU()
    imu.enable_temperature()
    self.temperature = imu.getTemperatureCelsius()

    imu = LSM6DS33()  # Accelerometer and Gyroscope
    imu.enable()

  #  imu.setAccelerometerFullScale2G()
  #  imu.setAccelerometerFullScale4G()
    imu.setAccelerometerFullScale8G()
  #  imu.setAccelerometerFullScale16G()

    self.gyro = imu.getGyroscopeDPS()
    self.acc = imu.getAccelerometerMPS2()

    # Calculation for Speed
    self.abs_acc = (abs(self.acc[0])+abs(self.acc[1])+abs(self.acc[2])-9.81)

    magnet = LIS3MDL()  # Magnetometer
    magnet.enable()
    self.mag = magnet.getMagnetometerRaw()
    self.mag[0] = (((self.mag[0]) * 16) / 27368.0) * 100  # (4 guass scale) * (6842 LSB/guass at 4 guass scale)
    self.mag[1] = (((self.mag[1]) * 16) / 27368.0) * 100  # (4 guass scale) * (6842 LSB/guass at 4 guass scale)
    self.mag[2] = (((self.mag[2]) * 16) / 27368.0) * 100  # (4 guass scale) * (6842 LSB/guass at 4 guass scale)



    baro = LPS25H()  # Barometric and Temperature
    baro.enable()

    self.alti = baro.getAltitude()

    epoch_time = time.time()
    self.ts = str(datetime.datetime.fromtimestamp(epoch_time))

    pass
  
  
class DataStructRFID:
  tokenID = ""
  login = False
  ts = 0
  
  def get_data(self):
    
    self.tokenID = read()
  
    epoch_time = time.time()
    self.ts = str(datetime.datetime.fromtimestamp(epoch_time))  

    pass
  
  
  
