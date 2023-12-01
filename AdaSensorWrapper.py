import Adafruit_DHT


SENSOR = Adafruit_DHT.DHT11
ADA_PIN = 4

def get_climate():
    humidity, temp = Adafruit_DHT.read_retry(SENSOR,ADA_PIN)
    return humidity, temp

def get_humidity():
    humidity, temp = Adafruit_DHT.read_retry(SENSOR,ADA_PIN)
    return humidity

def get_temperature():
    humidity, temp = Adafruit_DHT.read_retry(SENSOR,ADA_PIN)
    return temp