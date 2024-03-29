import threading

import speech_recognition as sr
import brain_api as AIBot

r = sr.Recognizer()

processorRoundIndex = 0
processedRounds = []

try:

    class Audio(sr.AudioSource):

        def __init__(self, trueSample):


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

def google_audio(audio, callingCode):
  try:
      # for testing purposes, we're just using the default API key
      # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
      # instead of `r.recognize_google(audio)`
      text = r.recognize_google(audio)
      # print("Steve1 thinks you said " + text)

      process_processor_result(text, callingCode)
  except sr.UnknownValueError:
      print("Google Speech Recognition could not understand audio")
  except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))

def wit_audio(audio, callingCode):
  # recognize speech using Wit.ai
  WIT_AI_KEY = "YGLSBDUDFTM2DCXSBL4W6DEUOPWFLVAL" # Wit.ai keys are 32-character uppercase alphanumeric strings
  try:
      text = r.recognize_wit(audio, key=WIT_AI_KEY)
      # print("Steve3 thinks you said " + text)

      process_processor_result(text, callingCode)
  except sr.UnknownValueError:
      print("Wit.ai could not understand audio")
  except sr.RequestError as e:
      print("Could not request results from Wit.ai service; {0}".format(e))

def ibm_audio(audio, callingCode):
  # recognize speech using IBM Speech to Text
  IBM_USERNAME = "2bae15e3-a034-42a6-97df-4865291f7463" # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
  IBM_PASSWORD = "vyMDnqFu0IBE" # IBM Speech to Text passwords are mixed-case alphanumeric strings
  try:
      text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
      # print("Steve2 thinks you said " + text)
      
      process_processor_result(text, callingCode)
  except sr.UnknownValueError:
      print("IBM Speech to Text could not understand audio")
  except sr.RequestError as e:
      print("Could not request results from IBM Speech to Text service; {0}".format(e))




def process_processor_result(result, callingCode):
  print("Received text: '%s'" % result)
  if((callingCode not in processedRounds) and len(result.split()) > 2):
    if "steve" in result.lower():
          question = result[(result.lower().index("steve") + len("setve")):len(result)]

          if(len(question.split()) > 2):
            processedRounds.append(callingCode)
            print("Steve thinks you said: %s" % question)
            AIBot.query(question)


def listen_for_speech(input_stream):
  global processorRoundIndex

  while input_stream is not None:

    with Audio(input_stream) as source:
        r.adjust_for_ambient_noise(source)
        print("listening to stream")
        audio = r.listen(source)

    print("starting audio processing")

    google_processor = threading.Thread(target=google_audio, args=(audio,processorRoundIndex))
    google_processor.daemon = True
    google_processor.start()

    wit_processor = threading.Thread(target=wit_audio, args=(audio,processorRoundIndex))
    wit_processor.daemon = True
    wit_processor.start()

    ibm_processor = threading.Thread(target=ibm_audio, args=(audio,processorRoundIndex))
    ibm_processor.daemon = True
    ibm_processor.start()

    processorRoundIndex = processorRoundIndex + 1

