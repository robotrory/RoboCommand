import os
import SocketManager

messageIndex = 0

def say_message(message):
  global messageIndex
  print("We say '%s'" % message)
  thisIndex = messageIndex
  os.system("espeak -w audio/%s.wav \"%s\"" % (thisIndex, message))
  messageIndex = messageIndex + 1
  for client in SocketManager.clients:
        client.write_message("audio:http://33ca8f47.ngrok.io/audio/%s.wav" % thisIndex)
  