import random
import time
from paho.mqtt import client as mqtt_client

fin = open('temp//distance.output', 'r')

broker = 'broker.emqx.io'
port = 1883
topic = "/falk0or/distancedetection"
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

time.sleep(2)
while True:
    print('======================================')
    msg_count += 1
    
    msg = fin.readline()
    print(msg,msg_count)
    result = client.publish(topic, msg)
    time.sleep(0.05)
    #print(result) #this result is kind of useless, it doesn't provide a lot of useful info