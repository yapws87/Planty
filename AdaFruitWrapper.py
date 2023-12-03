
from Adafruit_IO import Client, RequestError, Feed
import paho.mqtt.client as mqtt

import os

ada_id = os.getenv('ADAFRUIT_IO_ID')
ada_pw = os.getenv('ADAFRUIT_IO_PW')

print(f"Ada_id : {ada_id}")
print(f"Ada_pw : {ada_pw}")



class AdaFeed:

    def __init__(self, feed_name):
        print(f"AdaFeed __init__ : {feed_name}")
        self.client = Client(ada_id, ada_pw)        
        try:
            self.feed = self.client.feeds(feed_name)
        except RequestError:  # If feed doesn't exist, create it
            self.feed = self.client.create_feed(Feed(name=feed_name))

    def send_data(self,data):
        self.client.send_data(self.feed.key, data)

    def get_feed_names(self,):
        feeds = self.client.feeds()
        return feeds
    
class AdaTrigger:
    def __init__(self,feed_name):
        self.feed_name = feed_name
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect()
        self.client.on_message = self.on_message()
        
        self.client.username_pw_set(ada_id, ada_pw)
        self.client.connect("io.adafruit.com",1883,60)
        #self.client = MQTTClient(ada_id,ada_pw)
        # self.client.on_connect = self.connected
        # self.client.on_disconnect = self.disconnected
        # self.client.on_message = self.message
        


    def connect(self):
        self.client.connect()
        #self.client.loop_start()

    def on_connect(client, userdata, flags):
        print("Connected with result code ")
        client.subscribe(f"{ada_id}/feeds/{self.feed_name}")

    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        # Handle message (turn LED on or off)


    # def connected(self,client):
    #     print('Connected to Adafruit IO! Listening for ON/OFF signals...')
    #     self.client.subscribe(self.feed_name)  # replace 'onoff' with your feed name

    # def disconnected(self,client):
    #     print('Disconnected from Adafruit IO!')
    #     #sys.exit(1)

    # def message(self,client, feed_id, payload):
    #     print('Feed {0} received new value: {1}'.format(feed_id, payload))
    #     if payload == 'ON':
    #         # Implement your logic here when ON signal is received
    #         print('ON signal received')
    #     elif payload == 'OFF':
    #         # Implement your logic here when OFF signal is received
    #         print('OFF signal received')

    