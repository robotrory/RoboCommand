import os


def say_message(message):
  os.system("espeak -w speech.wav \"%s\"" % (message))