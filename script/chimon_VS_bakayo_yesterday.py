#coding: UTF-8

"""
チーモンチョウチュウと馬鹿よ貴方はの昨日どっちのほうがツイート数が多かったかを競わせるスクリプト
"""

import sqlite3
conn = sqlite3.connect('../Twitter_test/bakayo_VS_chimon.db')
c = conn.cursor()

from datetime import datetime
yesterday = int(datetime.now().strftime("%d")) - 1

def count_tweet(tbl_name):
    query = '''
    SELECT count(id), month, day, year
    FROM {tbl}
    WHERE day = {yesterday}
    GROUP BY month, day, year
    '''.format(tbl=tbl_name, yesterday=yesterday)
    count_id = c.execute(query)

    for row in count_id:
        cnt = row[0]
        #print(row[0])
        
    return cnt

cnt_bakayo = count_tweet('bakayo_time')
cnt_chimon = count_tweet('chimon_time')

if cnt_bakayo == max(cnt_bakayo, cnt_chimon):
    winner = '馬鹿よ'
elif cnt_chimon == max(cnt_bakayo, cnt_chimon):
    winner = 'チーモン'
    
day = datetime.now().strftime("%m")
day += '/'
day += str(yesterday)

script = '''
昨日({day})のツイート数は、
馬鹿よ：{cnt_bakayo}
チーモン：{cnt_chimon}
で、{winner}の勝ち！
'''.format(day=day, cnt_bakayo=cnt_bakayo, cnt_chimon=cnt_chimon, winner=winner)


from requests_oauthlib import OAuth1Session
import json
import settings

twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

params = {"status": script}
req = twitter.post("https://api.twitter.com/1.1/statuses/update.json",params = params)
