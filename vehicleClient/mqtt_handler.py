import paho.mqtt.client as mqtt
from time import sleep

import random as rd

from dataStruct import DataStruct
from json_handler import JSONDumper

ds = DataStruct()
jsondump = JSONDumper()

# creates a MQTT Client

client = mqtt.Client("Pi10AsAClient")

client.username_pw_set("V1","DE1")
client.connect("localhost", 8884)

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
    client.publish("/SysArch/V1/sensor", jsondump.generate_json(ds))

client.loop_stop()
