import json
import urllib
import urllib2
import sentiment_analysis as RESPONSE_INFO
import say_something as TALK
import perform_actions as ACTION

CONFUSE_RESPONSE = "I'm not sure what you mean"

def qanda(message):
  message_response = get_response(message)
  if message_response == CONFUSE_RESPONSE:
    ACTION.action_be_confused()
  else:
    RESPONSE_INFO.analyse(message_response)
  TALK.say_message(message_response)

def get_response(message):
  # header = {
  #   'Content-Type' : ,
  #   'Authorization' : 'Bearer 7fe7f921ed594df7941e9efea29a7e0c',
  #   'ocp-apim-subscription-key' : 'de9c57d0-dc85-42ee-9960-e0518dfd6c6d'
  # }
  #https://api.api.ai/v1/query?v=20150910&query=%s&lang=en&timezone=Europe/London
  quoted_query = urllib.quote(message)
  req = urllib2.Request("https://api.api.ai/v1/query?v=20150910&query=%s&lang=en&timezone=Europe/London" % ( quoted_query))
  req.add_header('Content-Type', 'application/json; charset=utf-8')
  req.add_header('Authorization', 'Bearer 7fe7f921ed594df7941e9efea29a7e0c')
  req.add_header('ocp-apim-subscription-key', 'de9c57d0-dc85-42ee-9960-e0518dfd6c6d')
  response = urllib2.urlopen(req)
  data = json.load(response)
  if data['result']['metadata']['speech'] != '':
    return data['result']['metadata']['speech']
  else:
    return CONFUSE_RESPONSE

print(get_response("asdasde"))