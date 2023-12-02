import Adafruit_DHT
import RPi.GPIO as GPIO
import time


SENSOR = Adafruit_DHT.DHT11
ADA_TEMP_PIN = 4
ADA_SOIL_PIN = 24


def get_climate():
    humidity, temp = Adafruit_DHT.read_retry(SENSOR,ADA_TEMP_PIN)
    return humidity, temp

def get_humidity():
    humidity, temp = Adafruit_DHT.read_retry(SENSOR,ADA_TEMP_PIN)
    return humidity

def get_temperature():
    humidity, temp = Adafruit_DHT.read_retry(SENSOR,ADA_TEMP_PIN)
    return temp


def get_soil():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ADA_SOIL_PIN, GPIO.IN)

    water_flag = 0
        
    if GPIO.input(ADA_SOIL_PIN):
        water_flag = 1
        print("Water detected!")
    # else:
    #     print("No water detected.")
            
    GPIO.cleanup()
    return water_flag
