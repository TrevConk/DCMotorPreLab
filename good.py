import RPi.GPIO as GPIO
import time

inputPin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(inputPin, GPIO.OUT)
pwmMotor = GPIO.PWM(inputPin, 100)
pwmMotor.start(0)

try:
  while(True):
    pwmMotor.ChangeDutyCycle(100)
    time.sleep(2)
    pwmMotor.ChangeDutyCycle(0)
    time.sleep(2)
except Exception as e:
  print('There was an error',e)
  GPIO.cleanup()





