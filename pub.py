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

time.sleep(2)
while True:
    with open('distance.output','r') as fin:
        msg = fin.readline()
    if 'None' not in msg:
        print('======================================')
        print(msg)
        print()
        result = client.publish(topic, msg)
        time.sleep(10)
    time.sleep(0.1)
    #print(result) #this result is kind of useless, it doesn't provide a lot of useful info