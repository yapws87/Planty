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
import AdaSensorWrapper as AdaSensor
import time


ada_temp = AdaFeed('Temperature')
ada_humid = AdaFeed('Humidity')

while 1:
    
    ada_temp.send_data(AdaSensor.get_temperature())
    ada_humid.send_data(AdaSensor.get_humidity())
    time.sleep(60 * 1)

    