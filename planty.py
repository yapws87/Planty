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
from DropboxWrapper import Dropboxy
import AdaSensorWrapper as AdaSensor
import time
from datetime import datetime

print('****** Start Planty *******')
ada_temp = AdaFeed('temperature') # only lower case
ada_humid = AdaFeed('humidity')

while 1:
    humid = AdaSensor.get_humidity()
    temp = AdaSensor.get_temperature()
    ada_temp.send_data(temp)
    ada_humid.send_data(humid)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f'{current_time}  Temperature : {temp:.1f}°C   Humidity : {humid:.1f}%')
    time.sleep(60 * 60) # 1 hour

    