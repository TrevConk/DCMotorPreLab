import RPi.GPIO as GPIO

inputPin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(inputPin, GPIO.OUT)
pwmMotor = GPIO.PWM(inputPin, 100)
pwmMotor.start(0)

try:
  while(True):
    pwmMotor.ChangeDutyCycle(int(input('Enter the speed of the motor:')))
except Exception as e:
  print('There was an error',e)
  GPIO.cleanup()





