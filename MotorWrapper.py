import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
# Motor GPIO Pins
#motor_enable_pin = 18  # Change to your GPIO pin
motor_input1 = 17
motor_input2 = 27    

# Set up the motor pins
#GPIO.setup(motor_enable_pin, GPIO.OUT)
GPIO.setup(motor_input1, GPIO.OUT)
GPIO.setup(motor_input2, GPIO.OUT)

# Set up PWM for motor speed control
#pwm = GPIO.PWM(motor_enable_pin, 1000)  # PWM at 1000 Hz
#pwm.start(0)  # Start PWM with 0% duty cycle (off)

def motor_forward(speed=100):
    GPIO.output(motor_input1, GPIO.HIGH)
    GPIO.output(motor_input2, GPIO.LOW)
 #   pwm.ChangeDutyCycle(speed)  # Change speed

def motor_backward(speed=100):
    GPIO.output(motor_input1, GPIO.LOW)
    GPIO.output(motor_input2, GPIO.HIGH)
  #  pwm.ChangeDutyCycle(speed)  # Change speed

def motor_stop():
    GPIO.output(motor_input2, GPIO.LOW)
    GPIO.output(motor_input2, GPIO.LOW)
    #pwm.ChangeDutyCycle(0)

def motor_clear():
    GPIO.cleanup()
