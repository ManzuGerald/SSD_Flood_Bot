

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import API
from tweepy import Cursor
from os import environ
import keys

###********** Authentication Keys **********
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
    def on_status(self, status):
        if status.in_reply_to_status_id is not None or \
            status.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not status.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                status.favorite()
            except Exception as e:
                print("Error on_data %s" % str(e))
                return True
        if not status.retweeted:
            try:
                status.retweet()
            except:
                print("Error on_data %s" % str(e))
                return True
        print(status.text)
        print(dir(status))

    def on_error(self, status_code):
        if status_code == 420 or status_code == 429:
            return False

stream_listener = StreamListener(api)
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
ssd_list = ["@ssdFloodBot",
"flooding south sudan","south sudan flooding",
"south sudan floods", "floods south sudan",
"floods in south sudan","south sudan in floods", "flooding in south sudan",
"south sudan flooding",
"flooding bor", "bor flooding"
"flooding akobo", "AKOBO FLOODING"]

stream.filter(track= ssd_list)
