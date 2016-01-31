import os


def say_message(message):
  os.system("espeak -w hello.wav \"%s\"" % (message))