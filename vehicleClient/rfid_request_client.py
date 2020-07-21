import paho.mqtt.client as mqtt
from time import sleep

import random as rd

from dataStruct import DataStructRFID
from json_handler import JSONDumper

ds = DataStructRFID()
jsondump = JSONDumper()

# creates a MQTT Client

client = mqtt.Client("Pi10AsARFIDClient")

client.username_pw_set("V1","DE1")
client.connect("localhost",8884)

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

    sleep(10)
    ds.get_data()
    if(!checkempty()):
	if(getToken()==ds.tokenID):
		ds.login=false
    		client.publish("/SysArch/V1/com2/web", jsondump.generate_json_from_rfid(ds))
	else:
		print("car is in use")
    else:
	ds.login=true
	client.publish("/SysArch/V1/com2/web", jsondump.generate_json_from_rfid(ds))
	
client.loop_stop()
