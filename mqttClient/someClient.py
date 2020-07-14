import paho.mqtt.client as mqtt
from time import sleep

import random as rd


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

for x in range(0,10):
    temperature = rd.random()
    sleep(1)
    print(temperature)
    client.publish("/SysArch/V1/someTest", temperature)


client.loop_stop()


