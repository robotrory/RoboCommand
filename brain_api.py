import json
import urllib
import urllib2
import say_something as TALK
import perform_actions as ACTION
import os.path, sys

from codecs import open

try:
    import apiai
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    import apiai

CONFUSE_RESPONSE = "not sure what you mean"

CLIENT_ACCESS_TOKEN = '13096bfb50a44c9aa488935a68e83951'
SUBSCRIPTION_KEY = '514967bc-08d6-474c-8a3d-1ed4b7e774f1 '
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN, SUBSCRIPTION_KEY)



def query(message):
  print("querying message: '%s'" % message)
  message_response = get_response(message)
  if len(message_response) > 0:
    TALK.say_message(message_response)
  else:
    ACTION.action_be_confused()
    TALK.say_message(CONFUSE_RESPONSE)

def get_response(message):
  
  request = ai.text_request()

  request.lang = 'en' # optional, default value equal 'en'

  request.query = message

  response = request.getresponse()


  return json.loads(response.read())['result']['fulfillment']['speech']
      

  # if __name__ == '__main__':
  #     main("what is your name")
  # # header = {
  # #   'Content-Type' : ,
  # #   'Authorization' : 'Bearer 7fe7f921ed594df7941e9efea29a7e0c',
  # #   'ocp-apim-subscription-key' : 'de9c57d0-dc85-42ee-9960-e0518dfd6c6d'
  # # }
  # #https://api.api.ai/v1/query?v=20150910&query=%s&lang=en&timezone=Europe/London
  # quoted_query = urllib.quote(message)
  # url = "https://api.api.ai/v1/query?v=20150910&query=%s&lang=en&timezone=Europe/London" % ( quoted_query)
  # print(url)
  # req = urllib2.Request(url)
  # req.add_header('Content-Type', 'application/json; charset=utf-8')
  # req.add_header('Authorization', 'Bearer 7fe7f921ed594df7941e9efea29a7e0c')
  # req.add_header('ocp-apim-subscription-key', 'de9c57d0-dc85-42ee-9960-e0518dfd6c6d')
  # response = urllib2.urlopen(req)
  # data = json.load(response)
  # print(data)
  # if data['result']['metadata']['speech'] != '':
  #   return data['result']['metadata']['speech']
  # else:
  #   return CONFUSE_RESPONSE

# print(get_response("asdasde"))