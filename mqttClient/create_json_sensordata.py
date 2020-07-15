import json
import time



# Dummy data

lidar = 23
humidity = 53
steering_angle = 32
temperature = 54
speed = 54
altimeter = 12

acc_x = 43
acc_y = 23
acc_z = 65

mag_x = 23
mag_y = 42
mag_z = 65

gyro_x = 95
gyro_y = 84
gyro_z = 83

# Dummy timestamp data

ts = time.time()*1000

# ts_lidar = 2345634534566
# ts_humidity = 533452345254
# ts_steering_angle = 3234523452345
# ts_temperature = 545463563456
# ts_speed = 54345345345
# ts_altimeter = 1234523542345

# ts_acc = 4332463635
# ts_mag = 2345634563465
# ts_gyro = 952345234523563


# Define JSON and pass values


public class JSON_dumper:
  def generateJSON(sensorData):

sensor_data =   {
                    "SensorValue1": [
                        {"name":"LIDAR", "timestamp":ts, "value":sensorData.lidar},
                        {"name":"Humidity", "timestamp":ts, "value":sensorData.humidity},
                        {"name":"SteeringAngle","timestamp":ts, "value":sensorData.steering_angle},
                        {"name":"Temperature", "timestamp":ts, "value":sensorData.temperature},
                        {"name":"Speed", "timestamp":ts, "value":sensorData.speed},
                        {"name":"Altimeter", "timestamp":ts, "value":sensorData.altimeter}
                    ],

                    "SensorValue3": [
                        {"name":"Acceleration", "timestamp":ts, "valueX":sensorData.acc.acc_x, "valueY":sensorData.acc.acc_y, "valueZ":sensorData.acc.acc_z},
                        {"name":"Magnetometer", "timestamp":ts, "valueX":sensorData.mag.mag_x, "valueY":sensorData.mag.mag_y, "valueZ":sensorData.mag.mag_z},
                        {"name":"Gyro", "timestamp":ts, "valueX":sensorData.gyro.gyro_x, "valueY":gyro_y, "valueZ":gyro_z}
                    ]
                }


# Save as JSON

with open('sensor_data.json', 'w') as json_file:
    json.dump(sensor_data, json_file)
