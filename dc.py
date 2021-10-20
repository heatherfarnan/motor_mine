#need a pwm signal to ramp motor from max speed to still in 2 sec

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin = 26
GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(pin, 50) # PWM object at 50 Hz (20 ms period)
pwm.start(0)

for dc in range(10,0,-1):
  pwm.ChangeDutyCycle(dc)
  print(dc)

# try:
#   #while True:
#     while n < 2:
#       pwm.ChangeDutyCycle(dcMin)
#       print(dcMin)
#       time.sleep(0.5)
#       pwm.ChangeDutyCycle(dcMax)
#       print(dcMax)
#       time.sleep(0.5)
#       n += 1
#       print(n)
# except KeyboardInterrupt:
#   print("closing")
# GPIO.cleanup()