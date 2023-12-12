
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

    def read_data(self):
        # Reading the most recent data from the feed
        data = self.client.receive(self.feed.key)
        return data.value

    def get_feed_names(self,):
        feeds = self.client.feeds()
        return feeds
    
class AdaTrigger:
    def __init__(self,feed_name,action):
        print(f"AdaTrigger __init__ : {feed_name}")
        self.feed_name = feed_name
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        
        self.client.username_pw_set(ada_id, ada_pw)
        self.client.connect("io.adafruit.com",1883,60)

        self.action = action
        #self.client = MQTTClient(ada_id,ada_pw)
        # self.client.on_connect = self.connected
        # self.client.on_disconnect = self.disconnected
        # self.client.on_message = self.message
        


    def connect(self):
        #self.client.connect()
        self.client.loop_start()

    def on_connect(self,client, userdata, flags, rc):
        print(f"Connected to {self.feed_name} ")
        client.subscribe(f"{ada_id}/feeds/{self.feed_name}")

    def on_message(self,client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        self.action()
        # Handle message (turn LED on or off)




class AdaToggle:
    def __init__(self,feed_name,action_on,action_off):
        print(f"AdaToggle __init__ : {feed_name}")
        self.feed_name = feed_name
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        
        self.client.username_pw_set(ada_id, ada_pw)
        self.client.connect("io.adafruit.com",1883,60)

        self.action_on = action_on
        self.action_off = action_off
        #self.client = MQTTClient(ada_id,ada_pw)
        # self.client.on_connect = self.connected
        # self.client.on_disconnect = self.disconnected
        # self.client.on_message = self.message
        


    def connect(self):
        #self.client.connect()
        self.client.loop_start()

    def on_connect(self,client, userdata, flags, rc):
        print("Connected with result code ")
        client.subscribe(f"{ada_id}/feeds/{self.feed_name}")

    def on_message(self,client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        if msg.payload == b'0':
            self.action_off()
            print(f"OFF {msg.payload}" )
        else:
            self.action_on()
            print(f"ON {msg.payload}" )
        # Handle message (turn LED on or off)


    