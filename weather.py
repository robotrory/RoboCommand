import json
import urllib
import urllib2

import forecastio
from geopy.geocoders import Nominatim
import perform_actions as ACTION
import say_something as TALK

api_key = "4166f22705eb95cf7000565037143c13"
geolocator = Nominatim()


def find_weather(message):
  values = {
    'key' : '8ad960732d31af8741e42faf716b7d14',
    'txt' : message,
    'model' : 'general_en'
  }
  data = urllib.urlencode(values)
  req = urllib2.Request("https://api.meaningcloud.com/sentiment-2.0", data)
  response = urllib2.urlopen(req)
  data = json.load(response)
  for x in data['sentimented_entity_list']:
    if 'Location' in x['type']:
      return weather_summary(x['form'])

def weather_summary(location):
  location = geolocator.geocode(location)
  lat = location.latitude
  lng = location.longitude
  forecast = forecastio.load_forecast(api_key, lat, lng, units="uk")
  by_day = forecast.daily()
  if by_day.icon == "rain" or by_day.icon == "wind"  or by_day.icon == "sleet" or by_day.icon == "fog":
    ACTION.action_be_unhappy()
  else:
    ACTION.action_be_happy()
  TALK.say_message(by_day.summary)
  # return by_day.summary
