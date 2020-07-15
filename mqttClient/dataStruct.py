public class DataStruct:
  
  lidar = 0
  humidity = 0
  steering_angle = 0
  temperature = 0
  speed = 0
  altimeter = 0
  acc = [0, 0, 0]
  mag = [0, 0, 0]
  gyro = [0, 0, 0]
  
  def __init__(self, lidar, humidity, steering_angle, temperature, speed, altimeter, acc, mag, gyro):
    self.lidar = lidar
    self.humidity = humidity
    self.steering_angle = steering_angle
    self.temperature = temperature
    self.speed = speed
    self.altimeter = altimeter
    self.acc = acc
    self.mag = mag
    self.gyro = gyro
    
   
  
  
  
