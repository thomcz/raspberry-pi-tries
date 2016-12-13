import time
import random
import RPi.GPIO as GPIO

t = 0.5
pins = [16, 18, 22]

def init():
 GPIO.setmode(GPIO.BOARD)

 for index in range(0, len(pins)):
   GPIO.setup(pins[index], GPIO.OUT)

try:
  init()
    
  while(1):
    # do stuff

finally:
  #clean up all used ports 
  GPIO.cleanup()

