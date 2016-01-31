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

class Handler(websocket.WebSocketHandler):
  def check_origin(self, origin):
    return True

  def open(self):
        global stream
        if len(clients) < 1:
          print("opening streams")
          
          stream = p.open(format=p.get_format_from_width(2),
                  input=True,
                  channels=1,
                  rate=16000,
                  output=True)


          speech_listener = threading.Thread(target=Speech.listen_for_speech, args=(stream,))
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
    global stream

    if stream is not None:
      stream.write(message)

