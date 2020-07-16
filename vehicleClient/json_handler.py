import json
import time
from dataStruct import DataStruct



# Dummy data

# lidar = 23
# humidity = 53
# steering_angle = 32
# temperature = 54
# speed = 54
# altimeter = 12
#
# acc_x = 43
# acc_y = 23
# acc_z = 65
#
# mag_x = 23
# mag_y = 42
# mag_z = 65
#
# gyro_x = 95
# gyro_y = 84
# gyro_z = 83

# Dummy timestamp data

ts = time.time()

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


class JSONDumper:
  def generate_json(self, sensordata):

    sensor_data = {
                    "SensorValue1": [
                        {"name":"LIDAR", "timestamp":ts, "value":sensordata.lidar},
                        {"name":"Humidity", "timestamp":ts, "value":sensordata.humidity},
                        {"name":"SteeringAngle","timestamp":ts, "value":sensordata.steering_angle},
                        {"name":"Temperature", "timestamp":ts, "value":sensordata.temperature},
                        {"name":"Speed", "timestamp":ts, "value":sensordata.speed},
                        {"name":"Altimeter", "timestamp":ts, "value":sensordata.alti}
                    ],

                    "SensorValue3": [
                        {"name":"Acceleration", "timestamp":ts, "valueX":sensordata.acc[0], "valueY":sensordata.acc[1], "valueZ":sensordata.acc[2]},
                        {"name":"Magnetometer", "timestamp":ts, "valueX":sensordata.mag[0], "valueY":sensordata.mag[1], "valueZ":sensordata.mag[2]},
                        {"name":"Gyro", "timestamp":ts, "valueX":sensordata.gyro[0], "valueY":sensordata.gyro[1], "valueZ":sensordata.gyro[2]}
                    ]
                  }
    # Return as JSON
    return json.dumps(sensor_data)