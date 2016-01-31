import serial
import time
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)

def sendServo(servoNum, degree):
  port.write('(%s,%s)' % (servoNum, degree))

def sendMessage(message):
  message = message.replace('|', '')
  port.write('(6,%s)' % (message))





