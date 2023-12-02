
from Adafruit_IO import Client, RequestError, Feed
import os

ada_id = os.getenv('ADAFRUIT_IO_ID')
ada_pw = os.getenv('ADAFRUIT_IO_PW')

print(f"Ada_id : {ada_id}")
print(f"Ada_pw : {ada_pw}")
aio = Client(ada_id, ada_pw)


class AdaFeed:

    def __init__(self, feed_name):
        print(f"AdaFeed __init__ : {feed_name}")
        
        try:
            self.feed = aio.feeds(feed_name)
        except RequestError:  # If feed doesn't exist, create it
            self.feed = aio.create_feed(Feed(name=feed_name))

    def send_data(self,data):
        aio.send_data(self.feed.key, data)

    def get_feed_names(self,):
        feeds = aio.feeds()
        return feeds