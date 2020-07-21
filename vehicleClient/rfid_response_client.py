import paho.mqtt.client as mqtt
from time import sleep
import json

client = mqtt.Client("Pi10AsARFIDResponse")

username = "V1"
psw = "DE1"
adress = "localhost"
port = 8884

def on_connect(client, userdata, flags, rc):
  if(rc==0):
    print("CONNACK received with code %d." % (rc))
  else:
    print("no Connection")
  
def on_message(client, userdata, msg):
  print("Got Response\n")
  m_decode = str(msg.payload.decode("utf-8","ignore"))
  print(type(m_decode))
  print(m_decode)
  m_in = json.loads(m_decode)
  print(type(m_in))
 
 #  print("%s : Login granted for %s with Username %s. Logged in with RFID Token %s" 
 #  % (m_in["user"]["email"],m_in["user"]["fullName"],m_in["user"]["userName"],m_in["tokenID"]))
    
  sleep(0.2)
  
  
client.username_pw_set(username, password=psw)
client.connect(adress, port)

client.on_connect = on_connect
client.on_message = on_message

client.subscribe("/SysArch/V1/com2/car")
client.loop_forever()
