# 192.168.0.144
# import RPi.GPIO as GPIO
# import time


# LED_PIN = 17  # Replace with your GPIO pin number
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(LED_PIN, GPIO.OUT)

# try:
#     while True:
#         GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on
#         time.sleep(1)  # Wait for 1 second
#         GPIO.output(LED_PIN, GPIO.LOW)  # Turn off
#         time.sleep(1)
# except KeyboardInterrupt:
#     GPIO.cleanup()  # Clean up GPIO on CTRL+C exit


from AdaFruitWrapper import AdaFeed 
from AdaFruitWrapper import AdaTrigger, AdaToggle 
from DropboxWrapper import Dropboxy
import AdaSensorWrapper as AdaSensor
import MotorWrapper as AdaMotor
import LEDWrapper as AdaLED
import AdaCameraWrapper as AdaCam
import time
from datetime import datetime, timedelta

print('****** Start Planty *******')



# Define functions
def water_plant():
    print("forward")
    AdaMotor.motor_forward()
    time.sleep(4)
    print("Stop1")
    AdaMotor.motor_stop()
    time.sleep(1)

def sunlight_on():
    AdaLED.FORCE_ON()

def sunlight_off():
    AdaLED.FORCE_OFF()

# init adafruit feeds
ada_temp = AdaFeed('temperature') # only lower case
ada_humid = AdaFeed('humidity')
ada_soil = AdaFeed('soil')
ada_image = AdaFeed('plantpicture')
ada_light = AdaFeed('sunlight')
adaWaterTrigger = AdaTrigger('waterpump',water_plant)
adaSunlightTrigger = AdaToggle('sunlight',sunlight_on,sunlight_off)

image_path = "/home/pi/github/Planty/image.jpg"


dropbox = Dropboxy()
# 
adaWaterTrigger.connect()
adaSunlightTrigger.connect()
captured_hour = 0

now = datetime.now()
filename = '/' + str(now) + '_test.jpg'
image_str = AdaCam.capture(image_path)
dropbox.upload_file(image_path,filename)

# initial Light setting
time_morning = datetime(now.year, now.month, now.day,  7, 0, 0)
time_evening = datetime(now.year, now.month, now.day, 22, 0, 0)
if now > time_morning and now < time_evening:
    ada_light.send_data(1)
else:
    ada_light.send_data(0)


while 1:

    # Get sensor values
    humid = AdaSensor.get_humidity()
    temp = AdaSensor.get_temperature()
    soil = AdaSensor.get_soil()

    # update data
    ada_temp.send_data(temp)
    ada_humid.send_data(humid)
    ada_soil.send_data(soil)

    # run motor when soil dry
    if soil == 0:
        water_plant()
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # Time based light system
    time_morning = datetime(now.year, now.month, now.day,  7, 0, 0)
    time_evening = datetime(now.year, now.month, now.day, 22, 0, 0)

    if now > time_morning and now < time_evening:
        if int(ada_light.read_data()) == 0:
            ada_light.send_data(1)
            print("LET THERE BE LIGHT")

        if now.hour % 2 == 0 and now.hour != captured_hour:   
            # Capture Image
            image_str = AdaCam.capture(image_path)
            ada_image.send_data(image_str)

            # send to dropbox
            filename = '/' + str(now) + '.jpg'
            dropbox.upload_file(image_path,filename)
            captured_hour = now.hour
    else:
        if int(ada_light.read_data()) == 1:
            print("Darkness surrounds you")
            ada_light.send_data(0)

    # Calculate the time to the next hour
   


        print(f'{current_time}  Temperature : {temp:.1f}°C   Humidity : {humid:.1f}%  Soil : {soil}')
    time.sleep(60) # 1 minutes
