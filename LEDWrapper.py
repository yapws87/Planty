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

# stop_yellow.set()
# stop_white.set()

def yellow_LED(duty_c):
    while not stop_yellow.is_set():
        seconds = 0.5 
        GPIO.output(LED_YELLOW, GPIO.HIGH)
    GPIO.output(LED_YELLOW, GPIO.LOW)
        # time.sleep( duty_c * seconds)
        # GPIO.output(LED_YELLOW, GPIO.LOW)
        # time.sleep((1- duty_c) * seconds)
 
def white_LED(duty_c):
    while not stop_white.is_set():
        seconds = 0.5
        GPIO.output(LED_WHITE, GPIO.HIGH)
    GPIO.output(LED_WHITE, GPIO.LOW)
        # time.sleep(duty_c * seconds)
        # GPIO.output(LED_WHITE, GPIO.LOW)
        # time.sleep((1 - duty_c) * seconds)
 
# Create and start the thread
#blink_time = 0.01


# led_white_thread.start()
# led_yellow_thread.start()

led_white_thread = None
led_yellow_thread = None
def on_white_light(blink_time):
    stop_white.clear()
    led_white_thread = threading.Thread(target=white_LED, args=(blink_time,))
    led_white_thread.start()

def off_white_light():
    stop_white.set()
    if led_white_thread is not None:
        led_white_thread.join()

def on_yellow_light(blink_time):
    stop_yellow.clear()
    led_yellow_thread = threading.Thread(target=yellow_LED, args=(blink_time,))
    led_yellow_thread.start()
    

def off_yellow_light():
    stop_yellow.set()
    if led_yellow_thread is not None:
        led_yellow_thread.join()



