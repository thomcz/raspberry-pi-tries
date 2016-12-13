import time
import random
import RPi.GPIO as GPIO

t = 0.5
pins = [16]

def init():
 GPIO.setmode(GPIO.BOARD)
 
 GPIO.setup(16, GPIO.IN, GPIO.PUD_DOWN)
 GPIO.setup(18, GPIO.OUT)

try:
  init()
    
  while(1):
    if GPIO.input(16) == GPIO.LOW:
      GPIO.output(18, GPIO.HIGH)
      print("on")
    else:
      GPIO.output(18, GPIO.LOW)
      print("off")
    time.sleep(t)


finally:
  #clean up all used ports 
  GPIO.cleanup()

