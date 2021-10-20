#need a pwm signal to ramp motor from max speed to still in 2 sec

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin = 26
GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(pin, 50) # PWM object at 50 Hz (20 ms period)
pwm.start(0)

