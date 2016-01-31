import os
import SocketManager

messageIndex = 0

def say_message(message):
  global messageIndex
  print("We say '%s'" % message)
  thisIndex = messageIndex
  dir = os.path.dirname(__file__)
  filename = os.path.join(dir, '/audio/%s.wav' % thisIndex)
  os.system("espeak -w %s \"%s\"" % (filename, message))
  messageIndex = messageIndex + 1
  for client in SocketManager.clients:
        client.write_message("audio:http://33ca8f47.ngrok.io/audio/%s.wav" % thisIndex)
  