import time
from tornado import web, ioloop
import threading
# import serial_sender as BOT

# obtain audio from the microphone
# r = sr.Recognizer()

import emotions as EMOTIONS
import SocketManager
import twitter_interface as Twit
import say_something as Speech

import brain as Twitter


FACE_DEBUG_MODE = True

def run_webserver():
  app.listen(3110)
  ioloop.IOLoop.instance().start()

def send_face_position(face_type):
  for client in SocketManager.clients:
    client.write_message(face_type)

def keep_alive():
  while True:
    time.sleep(1)
    print("")

if __name__ == '__main__':

  # Init
  app = web.Application([
    (r'/audio/(.*)', web.StaticFileHandler, {'path': 'audio'}),
    (r'/', SocketManager.Handler)
  ])

  webserver = threading.Thread(target=run_webserver)
  webserver.daemon = True
  webserver.start()

  twitterServer = threading.Thread(target=Twitter.begin_streaming)
  twitterServer.daemon = True
  twitterServer.start()

  alive = threading.Thread(target=keep_alive())
  alive.daemon = True
  alive.start()

  # Send first face
  face_type = EMOTIONS.ANGRY_FACE
  send_face_position(face_type)


  # Rorys face debug mode
  if FACE_DEBUG_MODE:
    while (1):
      user_input = raw_input('What\'s your face? ')
      position = EMOTIONS.input_to_face(user_input)

      for client in SocketManager.clients:
        client.write_message(position)


  while (1):
    if Twit.tweet_available():
      print("Do something here")
