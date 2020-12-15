import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from twico import *
import re

consumer_key = 'consumer key'
consumer_secret = 'consumer secret'
access_token = 'access token'
access_token_secret = 'access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

class MyStream(tweepy.StreamListener):

    def on_status(self, status):
        try:
            text1 = 'Maintenance: All Worlds Maintenance'
            search = re.search(text1, status.text)
            if search:
                txt = client.messages.create(
                    to = my_num,
                    from_ = twilio_num,
                    body = f'At {status.created_at}, @{status.user.screen_name} said: {status.text}'
                )
                print(txt.sid)
        except ssl.SSLError:
            pass

stweam = Stream(auth, MyStream())
stweam.filter(follow=['1019238758'])
