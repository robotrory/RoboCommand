import serial_sender as BOT

LEFT_SHOULDER = 1
LEFT_WING = 3
LEFT_ELBOW = 5
RIGHT_SHOULDER = 0
RIGHT_WING = 2
RIGHT_ELBOW = 4


def action_be_happy():
  BOT.sendServo(RIGHT_SHOULDER, 0)
  BOT.sendServo(LEFT_SHOULDER, 180)
  BOT.sendServo(RIGHT_WING, 0)
  BOT.sendServo(LEFT_WING, 90)
  BOT.sendServo(LEFT_ELBOW, 90)
  BOT.sendServo(LEFT_ELBOW, 90)
  pass

def action_be_unhappy():
  pass

def action_be_angry():
  pass

def action_be_neutral():
  pass

def action_be_surprised():
  pass


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