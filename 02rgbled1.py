import time
import RPi.GPIO as GPIO

t = 0.5
pins = [12, 16]

def init():
 GPIO.setmode(GPIO.BOARD)

 for index in range(0, len(pins)):
   GPIO.setup(pins[index], GPIO.OUT)

try:
  init()

  while 1:
    #turn off
    GPIO.output(12, GPIO.HIGH)
    #turn on
    GPIO.output(16, GPIO.LOW)

    time.sleep(t)

    GPIO.output(16, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)

    time.sleep(t)
finally:
  #clean up all used ports 
  GPIO.cleanup()
