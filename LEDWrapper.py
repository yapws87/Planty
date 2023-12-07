import RPi.GPIO as GPIO
import time
import threading

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
# Motor GPIO Pins
#motor_enable_pin = 18  # Change to your GPIO pin
LED_YELLOW = 10
LED_WHITE  = 9   

# Set up the motor pins
#GPIO.setup(motor_enable_pin, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT)
GPIO.setup(LED_WHITE , GPIO.OUT)

# Set up PWM for motor speed control
#pwm = GPIO.PWM(motor_enable_pin, 1000)  # PWM at 1000 Hz
#pwm.start(0)  # Start PWM with 0% duty cycle (off)

# Stop flags for each thread
stop_yellow = threading.Event()
stop_white = threading.Event()

stop_yellow.set()
stop_white.set()

def yellow_LED(seconds):
    while not stop_yellow.is_set():
        GPIO.output(LED_YELLOW, GPIO.HIGH)
        time.sleep(seconds)
        GPIO.output(LED_YELLOW, GPIO.LOW)
        time.sleep(seconds)
 
def white_LED(seconds):
    while not stop_yellow.is_set():
        GPIO.output(LED_WHITE, GPIO.HIGH)
        time.sleep(seconds)
        GPIO.output(LED_WHITE, GPIO.LOW)
        time.sleep(seconds)
 
# Create and start the thread
blink_time = 0.1
led_white_thread = threading.Thread(target=white_LED, args=(blink_time,))
led_yellow_thread = threading.Thread(target=yellow_LED, args=(blink_time,))

def on_white_light():
        stop_white.clear()
        #led_white_thread = threading.Thread(target=white_LED, args=(True,))
        led_white_thread.start()

def off_white_light():
        stop_white.set()
        led_white_thread.start()

def on_yellow_light():
        stop_yellow.clear()
        led_yellow_thread.join()
        #led_yellow_thread = threading.Thread(target=yellow_LED, args=(True,))

def off_yellow_light():
        stop_yellow.set()
        led_yellow_thread.join()



