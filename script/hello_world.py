#coding: UTF-8
from requests_oauthlib import OAuth1Session
import json
import settings

twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

from datetime import datetime

params = {"status": datetime.now().strftime("%Y/%m/%d %H:%M:%S")}
req = twitter.post("https://api.twitter.com/1.1/statuses/update.json",params = params)