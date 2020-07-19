

from time import sleep
from altimu.altimu import AltIMU
from altimu.lsm6ds33 import LSM6DS33
from altimu.lis3mdl  import LIS3MDL
from altimu.lps25h   import LPS25H
import time
import datetime

class DataStruct:
  
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
  
  # def __init__(self, lidar, humidity, steering_angle, temperature, speed, altimeter, acc, mag, gyro):
  #   self.lidar = lidar
  #   self.humidity = humidity
  #   self.steering_angle = steering_angle
  #   self.temperature = temperature
  #   self.speed = speed
  #   self.alti = alti
  #   self.acc = acc
  #   self.mag = mag
  #   self.gyro = gyro

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

    magnet = LIS3MDL()  # Magnetometer
    magnet.enable()
    self.mag = magnet.getMagnetometerRaw()

    baro = LPS25H()  # Barometric and Temperature
    baro.enable()

    self.alti = baro.getAltitude()

    epoch_time = time.time()
    ts = datetime.datetime.fromtimestamp(epoch_time)


    pass
    
   
  
  
  
