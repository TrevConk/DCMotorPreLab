import RPi.GPIO as GPIO

inputPin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(inputPin, GPIO.OUT)
pwmMotor = GPIO.PWM(inputPin, 100)
pwmMotor.start(0)

try:
  while(True):
    for(x in range(0,5,100))
      pwmMotor.ChangeDutyCycle(x)
      sleep(.1)
except Exception as e:
  print('There was an error',e)
  GPIO.cleanup()





