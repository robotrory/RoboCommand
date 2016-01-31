from tornado import websocket, web, ioloop
from bitarray import bitarray
import json
import threading
import wave
import struct
import random
import time

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()

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

input_stream = None
output_stream = None

try:
    import pyaudio
    class Audio(sr.AudioSource):

        def __init__(self, trueSample):

          self.format = pyaudio.paInt16
          self.SAMPLE_WIDTH = 2
          self.SAMPLE_RATE = 16000
          self.CHUNK = 1024
          self.stream = trueSample

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            type(self)
except ImportError:
    pass

class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        global input_stream, output_stream
        if len(clients) < 1:
          print("opening streams")

          output_stream = p.open(format=p.get_format_from_width(2),
                  channels=1,
                  rate=16000,
                  output=True)
          
          input_stream = p.open(format=p.get_format_from_width(2),
                  input=True,
                  channels=1,
                  rate=16000,
                  output=True)


          speech_listener = threading.Thread(target=listen_for_speech())
          speech_listener.daemon = True
          speech_listener.start()

        if self not in clients:
            clients.append(self)

    def on_close(self):
        global input_stream, output_stream
        if self in clients:
            clients.remove(self)

        if len(clients) < 1:
          print("closing streams")
          input_stream.stream()
          input_stream.close()
          input_stream = None
          output_stream.stream()
          output_stream.close()
          output_stream = None

    def on_message(self, message):
      global input_stream, output_stream

      if input_stream is not None:
        input_stream.write(message)

      if output_stream is not None:
        output_stream.write(message)

def keep_alive():
  while True:
    time.sleep(1)
    print("message")

app = web.Application([
    (r'/', SocketHandler)
])

def run_webserver():
  app.listen(3110)
  ioloop.IOLoop.instance().start()

def google_audio(audio):
  try:
      # for testing purposes, we're just using the default API key
      # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
      # instead of `r.recognize_google(audio)`
      text = r.recognize_google(audio)
      print("Steve1 thinks you said " + text)

      if "steve" in text.lower():
          question = text[(text.lower().index("steve") + len("setve")):len(text)]
          print("question: %s" % question)
  except sr.UnknownValueError:
      print("Google Speech Recognition could not understand audio")
  except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))

def wit_audio(audio):
  # recognize speech using Wit.ai
  WIT_AI_KEY = "YGLSBDUDFTM2DCXSBL4W6DEUOPWFLVAL" # Wit.ai keys are 32-character uppercase alphanumeric strings
  try:
      text = r.recognize_wit(audio, key=WIT_AI_KEY)
      print("Steve3 thinks you said " + text)

      if "steve" in text.lower():
          question = text[(text.lower().index("steve") + len("setve")):len(text)]
          print("question: %s" % question)
  except sr.UnknownValueError:
      print("Wit.ai could not understand audio")
  except sr.RequestError as e:
      print("Could not request results from Wit.ai service; {0}".format(e))

def ibm_audio(audio):
  # recognize speech using IBM Speech to Text
  IBM_USERNAME = "2bae15e3-a034-42a6-97df-4865291f7463" # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
  IBM_PASSWORD = "vyMDnqFu0IBE" # IBM Speech to Text passwords are mixed-case alphanumeric strings
  try:
      text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
      print("Steve2 thinks you said " + text)

      if "steve" in text.lower():
          question = text[(text.lower().index("steve") + len("setve")):len(text)]
          print("question: %s" % question)
  except sr.UnknownValueError:
      print("IBM Speech to Text could not understand audio")
  except sr.RequestError as e:
      print("Could not request results from IBM Speech to Text service; {0}".format(e))

def listen_for_speech():
  global input_stream
  while input_stream is not None:

    with Audio(input_stream) as source:
        print("listening to stream")
        audio = r.listen(source)

    print("starting audio processing")

    google_processor = threading.Thread(target=google_audio, args=(audio,))
    google_processor.daemon = True
    google_processor.start()

    wit_processor = threading.Thread(target=wit_audio, args=(audio,))
    wit_processor.daemon = True
    wit_processor.start()

    ibm_processor = threading.Thread(target=ibm_audio, args=(audio,))
    ibm_processor.daemon = True
    ibm_processor.start()



if __name__ == '__main__':
  webserver = threading.Thread(target=run_webserver)
  webserver.daemon = True

  webserver.start()

  # keep_alived = threading.Thread(target=keep_alive)
  # keep_alived.daemon = True
  # keep_alived.start()

  while (1):
        face = raw_input('What\'s your face? ')
        face_type = NEUTRAL_FACE

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

        # out_array = bitarray()
        # for i in range(0, len(in_array)):
        #   for j in range(0, len(in_array[i])):
        #     out_array.append(True if in_array[i][j] == 1 else False)

        for client in clients:
          client.write_message(face_type)
    