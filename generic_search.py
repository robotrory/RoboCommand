import urllib2
import json


def ask_question(message):
    response = urllib2.urlopen('http://api.duckduckgo.com/?q=%s&format=json&pretty=1' % message)
    data = json.load(response)

    abstract_data = data['Abstract']
    first_sentence = abstract_data.split(".", )[0]
    return first_sentence
