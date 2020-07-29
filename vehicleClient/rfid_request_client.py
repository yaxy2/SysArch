import paho.mqtt.client as mqtt
from time import sleep

import random as rd
from tokenHandler import *
from dataStruct import DataStructRFID
from json_handler import JSONDumper

ds = DataStructRFID()
jsondump = JSONDumper()

# creates a MQTT Client

client = mqtt.Client("Pi10AsARFIDClient")

username = {insert_username}
psw = {insert_psw}

client.username_pw_set(username,password=psw)
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

    
    ds.get_data()
    if(not checkEmpty()):
	if(getToken()==ds.tokenID):
		ds.login=False
   		client.publish("/SysArch/V1/com2/web", jsondump.generate_json_from_rfid(ds),qos=2)
	else:
		print("car is in use")
    else:
	ds.login=True
	print(ds.login)
	client.publish("/SysArch/V1/com2/web", jsondump.generate_json_from_rfid(ds),qos=2)

    sleep(10)

	
client.loop_stop()
