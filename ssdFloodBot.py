

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import API
from tweepy import Cursor
from os import environ

###********** Authentication Keys **********
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#wait_on_rate_limit monitors and lets the API wait when we hit some limits.

class StreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
    def on_status(self, status):
        #Ignores the tweet so long as I am the Author, or it's a reply to a tweet
        if status.in_reply_to_status_id is not None or \
            status.user.id == self.me.id:
            return
        if not status.retweeted:
            try:
                status.retweet()
            except:
                print("Retweet Error")
                return True
        print(status.text)
        #print(dir(status))

        def on_error(self, status_code):
            if status_code == 420:
                print("Error on_data %s" % str(e))
                print("Error from limits")
                return True
            if status_code == 429:
                print("Error on_data %s" % str(e))
                print("LIMIT EXCEEDED")
                return True

stream_listener = StreamListener(api)
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
ssd_list = ["@ssdFloodBot",
"flooding south sudan","south sudan flooding",
"south sudan floods", "floods south sudan",
"floods in south sudan","south sudan in floods", "flooding in south sudan",
"south sudan flooding",
"flooding bor", "bor flooding",
"flooding akobo", "AKOBO FLOODING"]

stream.filter(track= ssd_list)
