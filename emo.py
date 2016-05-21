import serial_sender as BOT
# import SocketManager
import time

LEFT_SHOULDER = 0
LEFT_WING = 4
LEFT_ELBOW = 2
RIGHT_SHOULDER = 6
RIGHT_WING = 1
RIGHT_ELBOW = 3
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
  BOT.sendServo(RIGHT_SHOULDER, 0)
  BOT.sendServo(LEFT_SHOULDER, 180)
  BOT.sendServo(RIGHT_WING, 0)
  BOT.sendServo(LEFT_WING, 90)
  BOT.sendServo(LEFT_ELBOW, 90)
  BOT.sendServo(LEFT_ELBOW, 90)
  pass


action_be_reset()
