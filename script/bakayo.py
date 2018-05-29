"""
馬鹿よ貴方はに関するツイートを探してリツイートするスクリプト
"""

from requests_oauthlib import OAuth1Session
import json
import settings

twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
params = {}
req = twitter.get("https://api.twitter.com/1.1/search/tweets.json?q=\"馬鹿よ貴方は\"OR\"馬鹿よさん\"OR\"ごみラジオ\"OR\"平井ファラオ光\"&count=30", params = params)
tweets = json.loads(req.text)
for tweet_statuses in tweets['statuses']:
    tweet_id = tweet_statuses['id']
    params = {}
    print('***')
    print(tweet_statuses['text'])
    req = twitter.post("https://api.twitter.com/1.1/statuses/retweet/{tweet_id}.json".format(tweet_id=tweet_id),params = params)
