import time
import os
import thread

# For Robot:
#MAIN_SERVO_PIN = 0
#MAIN_SERVO_PIN = 1

# For james:
MAIN_SERVO_PIN = 22
MAIN_MESSAGE_PIN = 23

TIME_BETWEEN = 1
value = 1


START_COM = [1,1,1,1,1,1,1,1]
END_COM = [0,0,0,0,0,0,0,0]
RESET = [0,0]
MAX_LEN_MESSAGE = 10


def sendByte( cmd, pin ):
  for bit in cmd:
    os.system("gpio write %s %s" % (pin, bit))
    time.sleep(TIME_BETWEEN)


def sendServoCommand(servoNum, degrees):
  print("EXECUTION START:")
  sendByte(START_COM, MAIN_SERVO_PIN)
  servoNumBinary = list('{0:08b}'.format(servoNum))
  degreesBinary = list('{0:08b}'.format(degrees))
  print(servoNumBinary)
  print(degreesBinary)
  sendByte(servoNumBinary, MAIN_SERVO_PIN)
  sendByte(degreesBinary, MAIN_SERVO_PIN)
  sendByte(END_COM, MAIN_SERVO_PIN)
  print("EXECUTION END")


def sendTwitterNameCommand(message):
  finalArray = [0]*MAX_LEN_MESSAGE
  if len(message) > MAX_LEN_MESSAGE:
    print("Message too long")
  else:
    sendByte(START_COM, MAIN_MESSAGE_PIN)
    messageBin = [ bin(ord(ch))[2:].zfill(8) for ch in message ]
    for x in range(0,MAX_LEN_MESSAGE):
      if x < len(message):
        finalArray[x] = messageBin[x]
      else:
        finalArray[x] = '00000000'
      sendByte(finalArray[x], MAIN_MESSAGE_PIN)
    sendByte(END_COM, MAIN_MESSAGE_PIN)


def setup():
  os.system("gpio mode %s out" % (MAIN_MESSAGE_PIN))
  os.system("gpio mode %s out" % (MAIN_SERVO_PIN))



def outName(name):
  setup()
  thread.start_new_thread(sendTwitterNameCommand,(name, ) )

def outServo(num, degree):
  setup()
  thread.start_new_thread(sendServoCommand,(num, degree, ) )



outName("Hello")
outServo(3, 100)

shouldLoop = 1
while shouldLoop:
  pass

