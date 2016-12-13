import time
import random
import RPi.GPIO as GPIO

t = 0.5
pins = [16, 18, 22]

def init():
 GPIO.setmode(GPIO.BOARD)

 for index in range(0, len(pins)):
   GPIO.setup(pins[index], GPIO.OUT)

def setRandomLED(index):
  GPIO.output(pins[index], GPIO.HIGH)
  time.sleep(t)
  GPIO.output(pins[index], GPIO.LOW)


try:
  init()

  while(1):
    setRandomLED(random.randint(0, 2))
    time.sleep(t)
    setRandomLED(random.randint(0, 2))
    time.sleep(t)

finally:
  #clean up all used ports 
  GPIO.cleanup()

