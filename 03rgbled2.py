import time
import RPi.GPIO as GPIO

t = 0.5
pins = [12, 16, 18]

def init():
 GPIO.setmode(GPIO.BOARD)

 for index in range(0, len(pins)):
   GPIO.setup(pins[index], GPIO.OUT)

try:
  init()

  GPIO.output(pins[0], GPIO.LOW)
  GPIO.output(pins[1], GPIO.LOW)
  GPIO.output(pins[2], GPIO.HIGH)

  while 1:
    GPIO.output(pins[0], GPIO.HIGH)
    time.sleep(t)
 
    GPIO.output(pins[1], GPIO.LOW)
    time.sleep(t)

    GPIO.output(pins[2], GPIO.HIGH)
    time.sleep(t)

    GPIO.output(pins[0], GPIO.LOW)
    time.sleep(t)

    GPIO.output(pins[1], GPIO.HIGH)
    time.sleep(t)

    GPIO.output(pins[2], GPIO.LOW)
    time.sleep(t)
finally:
  #clean up all used ports 
  GPIO.cleanup()
