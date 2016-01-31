#
import json
import urllib
import urllib2
import perform_actions as ACTION

def analyse(message):
  values = {
    'key' : '8ad960732d31af8741e42faf716b7d14',
    'txt' : message,
    'model' : 'general_en'
  }
  data = urllib.urlencode(values)
  req = urllib2.Request("https://api.meaningcloud.com/sentiment-2.0", data)
  response = urllib2.urlopen(req)
  data = json.load(response)

  if data['subjectivity'] == "SUBJECTIVE":
    # Opinion
    if data['score_tag'] == "P" or data['score_tag'] == "P+":
      print("Be happy")
      ACTION.action_be_happy()

    elif data['score_tag'] == "N" or data['score_tag'] == "N+":
      print("Be Sad")
      ACTION.action_be_unhappy()
    else:
      ACTION.action_be_surprised()
      print("No Comment")
  else:
    if data['score_tag'] == "P" or data['score_tag'] == "P+":
      print("I agree")
      ACTION.action_be_surprised()

    elif data['score_tag'] == "N" or data['score_tag'] == "N+":
      print("Be Angry")
      ACTION.action_be_angry()
    else:
      ACTION.action_be_surprised()


