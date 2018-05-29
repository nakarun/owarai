#coding: UTF-8
from requests_oauthlib import OAuth1Session
import json
import settings

twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

from datetime import datetime

params = {"status": "《定期》お気に入りのツイートをリツイートしていくボットです。リツイートされたくないなと思われましたら、ブロックお願いいたします。"}
req = twitter.post("https://api.twitter.com/1.1/statuses/update.json",params = params)