import serial_sender as BOT
# import SocketManager
import time
from threading import Timer

LEFT_SHOULDER = 0
LEFT_WING = 4
LEFT_ELBOW = 2
RIGHT_SHOULDER = 3
RIGHT_WING = 1
RIGHT_ELBOW = 6
HEAD = 5

lastKnownHeadPosition = 20

def action_tilt_head():
    BOT.sendServo(HEAD, lastKnownHeadPosition)
    positionTo = random.randint(0,40)
    currentPosition = lastKnownHeadPosition
    for x in range(0, positionTo):
        if positionTo > currentPosition:
            currentPosition += 1
            BOT.sendServo(HEAD, currentPosition)
        elif positionTo < currentPosition:
            currentPosition -= 1
            BOT.sendServo(HEAD, currentPosition)

    lastKnownHeadPosition = currentPosition


def action_be_happy():
  BOT.sendServo(RIGHT_SHOULDER, 0)
  BOT.sendServo(LEFT_SHOULDER, 180)
  BOT.sendServo(RIGHT_WING, 0)
  BOT.sendServo(LEFT_WING, 90)
  BOT.sendServo(LEFT_ELBOW, 90)
  BOT.sendServo(LEFT_ELBOW, 90)
#   for client in SocketManager.clients:
#           client.write_message("emotion:happy")
#   pass
#
# def action_be_unhappy():
#   for client in SocketManager.clients:
#           client.write_message("emotion:unhappy")
#   pass
#
# def action_be_angry():
#   for client in SocketManager.clients:
#           client.write_message("emotion:angry")
#   pass
#
# def action_be_neutral():
#   for client in SocketManager.clients:
#           client.write_message("emotion:neutral")
#   pass
#
# def action_be_surprised():
#   for client in SocketManager.clients:
#           client.write_message("emotion:surprised")
#   pass
def action_be_confused():
  pass

def action_be_reset():
  BOT.sendServo(RIGHT_SHOULDER, 180)
  BOT.sendServo(LEFT_SHOULDER, 0)
  BOT.sendServo(RIGHT_WING, 0)

  BOT.sendServo(LEFT_WING, 90)
  BOT.sendServo(LEFT_ELBOW, 0)
  BOT.sendServo(RIGHT_ELBOW, 100)
  pass


def init():
   print("Reseting...")
   action_be_reset()

   class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(1):
            print "my thread"
            action_tilt_head()


t= Timer(3.0,init)
t.start()
