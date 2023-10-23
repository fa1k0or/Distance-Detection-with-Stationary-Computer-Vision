import random
import time
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = "zhtczycart"
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

client = mqtt_client.Client(client_id)
client.on_connect = on_connect
client.connect(broker, port)
client.loop_start()

msg_count=0

state = True

time.sleep(2)
while True:
    msg_count += 1
    with open('distance.output','r') as fin:
        msg = fin.readline()
    if state and 'None' not in msg:
        print('======================================')
        print(msg,msg_count)
        result = client.publish(topic, msg)
        state = False
    if not state:
        break
    time.sleep(0.05)
    #print(result) #this result is kind of useless, it doesn't provide a lot of useful info