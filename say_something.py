import os
import SocketManager
import emotions as Emotions
import perform_actions as ACTION
import sentiment_analysis as RESPONSE_INFO

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
    if action.lower() == "twitter":
      import brain as Brain
      Brain.searchTwitterForValue(restOfPhrase)
      return
    elif action == "neutral":
      ACTION.action_be_neutral()
    elif action == "happy":
      ACTION.action_be_happy()
    elif action == "unhappy":
      ACTION.action_be_unhappy()
    elif action == "angry":
      ACTION.action_be_angry()
    elif action == "surprised":
      ACTION.action_be_surprised()
  else:
    RESPONSE_INFO.analyse(message)

  thisIndex = messageIndex

  filename = os.path.realpath('audio/%s.wav' % thisIndex)
  os.system("espeak -g 10 -w %s \"%s\"" % (filename, restOfPhrase))
  messageIndex = messageIndex + 1
  for client in SocketManager.clients:
        client.write_message("audio:http://bb4d0cce.ngrok.io/audio/%s.wav" % thisIndex)
  
