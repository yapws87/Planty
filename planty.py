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
import MotorWrapper as AdaMotor
import time
from datetime import datetime

print('****** Start Planty *******')
ada_temp = AdaFeed('temperature') # only lower case
ada_humid = AdaFeed('humidity')
ada_soil = AdaFeed('soil')

while 1:
    humid = AdaSensor.get_humidity()
    temp = AdaSensor.get_temperature()
    soil = AdaSensor.get_soil()
    ada_temp.send_data(temp)
    ada_humid.send_data(humid)
    ada_soil.send_data(soil)
    
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
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f'{current_time}  Temperature : {temp:.1f}°C   Humidity : {humid:.1f}%  Soil : {soil}')
    time.sleep(60 * 1) # 1 hour
