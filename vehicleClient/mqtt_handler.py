import paho.mqtt.client as mqtt
from time import sleep

import random as rd

from dataStruct import DataStructSensor
from json_handler import JSONDumper





ds = DataStructSensor()
jsondump = JSONDumper()

# creates a MQTT Client

adress = "localhost"
port = 8884

username = {inser_username}
psw = {insert_password}

client = mqtt.Client("Pi10AsAClient")

client.username_pw_set(username,password=psw)
client.connect(adress, port)

# print("Status connected")

def on_connect(client, userdata, flags, rc):
	print("CONNACK received with code %d." % (rc))

def on_publish(client, userdata, rc):
	print("data published \n")
	pass

client.on_connect = on_connect
client.on_publish = on_publish

client.loop_start()

while True:
    sleep(1)
    ds.get_data()
    client.publish("/SysArch/V1/sensor", jsondump.generate_json_from_sensor(ds))
    f = open('data.txt','w')
    dataArray = [str(ds.speed)+"\n",str(ds.temperature)+"\n",str(ds.steering_angle)+"\n",str(ds.alti)+"\n"]
    f.writelines(dataArray)
    

client.loop_stop()
