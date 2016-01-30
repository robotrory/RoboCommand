from tornado import websocket, web, ioloop
from bitarray import bitarray
import json
import threading
import wave
import struct
import random

FACE_DEBUG_MODE = True

NEUTRAL_FACE = "neutral"
HAPPY_FACE = "happy"
UNHAPPY_FACE = "unhappy"
ANGRY_FACE = "angry"
SURPRISED_FACE = "surprised"
FINGER = "finger"

clients = []

import wave
import pyaudio

p = pyaudio.PyAudio()

stream = None


class SocketHandler(websocket.WebSocketHandler):
  def check_origin(self, origin):
    return True

  def open(self):
    global stream
    if len(clients) < 1:
      print("opening stream")
      stream = p.open(format=p.get_format_from_width(2),
                      channels=1,
                      rate=16000,
                      output=True)

    if self not in clients:
      clients.append(self)

  def on_close(self):
    global stream
    if self in clients:
      clients.remove(self)

    if len(clients) < 1:
      print("closing stream")
      stream.stop_stream()
      stream.close()
      stream = None

  def on_message(self, message):
    global stream

    if stream is not None:
      print("message")
      stream.write(message)


app = web.Application([
  (r'/', SocketHandler)
])


def run_webserver():
  app.listen(3110)
  ioloop.IOLoop.instance().start()


def input_to_face(face):
  if face == 'h':
    face_type = HAPPY_FACE
  elif face == 'u':
    face_type = UNHAPPY_FACE
  elif face == 'a':
    face_type = ANGRY_FACE
  elif face == 's':
    face_type = SURPRISED_FACE
  elif face == 'finger':
    face_type = FINGER
  else:
    face_type = NEUTRAL_FACE
  return face_type


def send_face_position(face_type):
  for client in clients:
    client.write_message(face_type)


def tweet_available():
  pass


if __name__ == '__main__':

  # Init
  webserver = threading.Thread(target=run_webserver)
  webserver.daemon = True
  webserver.start()

  # Send first face
  face_type = NEUTRAL_FACE
  send_face_position(send_face_position)


  # Rorys face debug mode
  if FACE_DEBUG_MODE:
    while (1):
      face = raw_input('What\'s your face? ')
      position = input_to_face(face)

  while (1):
    if tweet_available():
      print("Do something here")


    # out_array = bitarray()
    # for i in range(0, len(in_array)):
    #   for j in range(0, len(in_array[i])):
    #     out_array.append(True if in_array[i][j] == 1 else False)


