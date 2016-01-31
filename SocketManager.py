import pyaudio
from tornado import websocket

import threading

import SpeechManager as Speech

import wave
import struct
import random
import time

clients = []

stream = None

p = pyaudio.PyAudio()

import speech_recognition as sr

class BufferContainer(sr.AudioSource):
    def __init__(self):
        self.event = threading.Event()
        self.event.clear()
        self.lines = []

    def write(self, text):

        self.lines.append(text)
        self.event.set()

    def writelines(self, *args):
         for item in args: self.lines.append(item)

    def open(self):
        self.lines = []

    def read(self, extra):

        self.event.wait()

        elem = None
        if (len(self.lines) > 0):
          elem = self.lines.pop()

        # print("")
        if (len(self.lines) < 1):
            self.event.clear()

        return elem

    def close (self):
        pass

buffer = BufferContainer()

class Handler(websocket.WebSocketHandler):
  def check_origin(self, origin):
    return True

  def open(self):
        global stream
        if len(clients) < 1:
          print("opening streams")
          
          stream = p.open(format=p.get_format_from_width(2),
                  # input=True,
                  channels=1,
                  rate=16000,
                  output=True)


          speech_listener = threading.Thread(target=Speech.listen_for_speech, args=(buffer,))
          speech_listener.daemon = True
          speech_listener.start()

        if self not in clients:
            clients.append(self)

  def on_close(self):
      global stream
      if self in clients:
          clients.remove(self)

      if len(clients) < 1:
        print("closing streams")
        stream.stream()
        stream.close()
        stream = None

  def on_message(self, message):
    global stream, buffer

    if buffer is not None:
      buffer.write(message)

    if stream is not None:
      stream.write(message)

