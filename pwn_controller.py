import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

def update(angle):
  p = GPIO.PWM(12, 100)
  p.start(5)
  duty = float(angle) / 10.0 + 2.5
  p.ChangeDutyCycle(duty)










