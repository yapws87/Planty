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
from datetime import datetime

print('****** Start Planty *******')


ada_temp = AdaFeed('temperature') # only lower case
ada_humid = AdaFeed('humidity')
ada_soil = AdaFeed('soil')
ada_image = AdaFeed('plantpicture')

def water_plant():
    print("forward")
    AdaMotor.motor_forward()
    time.sleep(2)
    print("Stop1")
    AdaMotor.motor_stop()
    time.sleep(2)
    print("backwards")
    AdaMotor.motor_forward()
    time.sleep(2)
    print("Stop2")
    AdaMotor.motor_stop()
    time.sleep(2)


def sunlight_on():
    AdaLED.on_white_light()
    AdaLED.on_yellow_light()

def sunlight_off():
    AdaLED.off_white_light()
    AdaLED.off_yellow_light()

adaWaterTrigger = AdaTrigger('waterpump',water_plant)
adaSunlightTrigger = AdaToggle('sunlight',sunlight_on,sunlight_off)


image_path = "/home/pi/github/Planty/image.jpg"
image_str = AdaCam.capture(image_path)
ada_image.send_data(image_path)
# dropbox = Dropboxy()
# dropbox.upload_file("image.jpg","/Planty/image.jpg")


while 1:
    humid = AdaSensor.get_humidity()
    temp = AdaSensor.get_temperature()
    soil = AdaSensor.get_soil()
    ada_temp.send_data(temp)
    ada_humid.send_data(humid)
    ada_soil.send_data(soil)

    adaWaterTrigger.connect()
    adaSunlightTrigger.connect()

    # run motor when soil dry
    if soil == 0:
        water_plant()
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f'{current_time}  Temperature : {temp:.1f}°C   Humidity : {humid:.1f}%  Soil : {soil}')
    time.sleep(60 * 1) # 1 hour
