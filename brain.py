import time
import requests
from tweepy import OAuthHandler
import tweepy
json_data = ""
dataCheck = False

consumer_key = '1MUDOQv80dafJg6sMrjr3YRol'
consumer_secret = 'uizOJFjZ8nGmgvCbPLupeQiE5fhjNYFDeqXlNXif7CtJyjIM6H'
access_token = '4864903228-PVG0k3kFy8ojtLMFhUIewkpjUybpPJo1WBVDFdD'
access_secret = '3l7rIzf7bp0twTHHvJm6hKQeW2cY8Z8xBBZQHmJhWVUs0'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


# Gets tweets to @ArmHackathonBot
from tweepy import Stream
from tweepy.streaming import StreamListener, json
class MyListener(StreamListener):
    globals()
    def on_data(self, dataTwitter):
        global dataCheck
        text = json.loads(dataTwitter)['text'].replace("@ArmHackathonBot ", "")
        name = json.loads(dataTwitter)['user']['name']
        nameTwitter = json.loads(dataTwitter)['user']['screen_name']
        #get data
        main(text,name,nameTwitter)
        dataCheck = True
        return True

    def on_error(self, status):
        print(status)
        if status == 420 :
            return False
        time.sleep(0.5)
        return True

twitter_stream = Stream(auth, MyListener())

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['@ArmHackathonBot'], async=True)

# Search twitter
def searchTwitter(info):
    search_results = api.search(q='america', rrp = 8, count=10, lang='en')
    list_results = []
    for tweet in search_results:
        text = tweet.text.replace("RT", "")
        list_results.append(text)
    return list_results






# Convert sentiment api output to single + or - value
def convertSentiment(data):
    total = 0
    for i in data :
        if i['result'] == 'Positive':
            total = total + float(i['confidence'])
        elif i['result'] == 'Negative':
            total = total - float(i['confidence'])
    return total

# Input txt list, returns sentiment values as a Json List
def sendRecieveMeaningCloud(tweets):
    url = 'http://sentiment.vivekn.com/api/batch/'
    data = tweets
    r = requests.post(url, data=json.dumps(data))
    return r

# input list of tweets, output single value.
def sentimentValue(tweets):
    r = sendRecieveMeaningCloud(tweets)
    data = json.loads(r.content)
    sentiment = convertSentiment(data)
    return sentiment

def formJSON(sentimentValue,text, name, nameTwitter):
    global json_data
    data = {}
    data['sentimentValue'] = sentimentValue
    data['text'] = text
    data['name'] = name
    data['nameTwitter'] = nameTwitter
    json_data = json.dumps(data)

def main(text, name, nameTwitter):
    value = sentimentValue(searchTwitter(text))
    formJSON(value,text,name,nameTwitter)
    print(value)
    print(text)
    print(name)
    print(nameTwitter)

def newData():
    global json_data
    global dataCheck
    if dataCheck :
        dataCheck = False
        return json_data
    else:
        return False
