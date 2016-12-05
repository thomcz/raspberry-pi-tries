import time
import RPi.GPIO as GPIO

try:
  #time to wait
  t = 0.5
  #use RPi.GPIO Layout (like pin-numbers)
  GPIO.setmode(GPIO.BOARD)
  #set pin 12 (GPIO 18)
  GPIO.setup(12, GPIO.OUT)
  #set pin 16 (GPIO 23)
  GPIO.setup(16, GPIO.OUT)
  #set pin 18 (GPIO 24)
  GPIO.setup(18, GPIO.OUT)

  GPIO.output(12, GPIO.LOW)
  GPIO.output(16, GPIO.LOW)
  GPIO.output(18, GPIO.HIGH)

  while 1:
    GPIO.output(12, GPIO.HIGH)
    time.sleep(t)
 
    GPIO.output(18, GPIO.LOW)
    time.sleep(t)

    GPIO.output(16, GPIO.HIGH)
    time.sleep(t)

    GPIO.output(12, GPIO.LOW)
    time.sleep(t)

    GPIO.output(18, GPIO.HIGH)
    time.sleep(t)

    GPIO.output(16, GPIO.LOW)
    time.sleep(t)
finally:
  #clean up all used ports 
  GPIO.cleanup()
