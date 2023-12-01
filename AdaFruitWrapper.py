
from Adafruit_IO import Client, RequestError, Feed
import os

ada_id = os.getenv('ADAFRUIT_IO_ID')
ada_pw = os.getenv('ADAFRUIT_IO_PW')
aio = Client(ada_id, ada_pw)


class AdaFeed:

    def __init__(self, feed_name):
        try:
            print(f"AdaFeet __init__ {feed_name}")
            self.feed = aio.feeds(feed_name)
        except RequestError as e:  # If feed doesn't exist, create it
            if e.status_code == 404: # Feed not found
                print(f"AdaFeet __init__ CREATE {feed_name}")
                self.feed = aio.create_feed(Feed(name=feed_name))
            else:
                raise
    def send_data(self,data):
        aio.send_data(self.feed.key, data)

