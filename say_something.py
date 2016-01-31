import os
import SocketManager
import emotions as Emotions

messageIndex = 0

def extractAction(message):
  if message.split()[0].startswith("!"):
    return (message.split()[0].replace("!",""), message[len(message.split()[0]) : len(message)])
  else:
    return (None, message)

def say_message(message):
  global messageIndex
  print("We say '%s'" % message)

  (action, restOfPhrase) = extractAction(message)

  print("action: %s" % action)
  print("restOfPhrase: %s" % restOfPhrase)

  if action is not None:
    for client in SocketManager.clients:
        client.write_message("emotion:%s" % action)

  thisIndex = messageIndex

  filename = os.path.realpath('audio/%s.wav' % thisIndex)
  os.system("espeak -w %s \"%s\"" % (filename, restOfPhrase))
  messageIndex = messageIndex + 1
  for client in SocketManager.clients:
        client.write_message("audio:http://33ca8f47.ngrok.io/audio/%s.wav" % thisIndex)
  