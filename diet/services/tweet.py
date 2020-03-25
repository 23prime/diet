import os

import twitter


class Tweet(object):
    def __init__(self):
        self.api = twitter.Api(
            consumer_key=os.environ['CONSUMER_KEY'],
            consumer_secret=os.environ['CONSUMER_KEY_SECRET'],
            access_token_key=os.environ['ACCESS_TOKEN'],
            access_token_secret=os.environ['ACCESS_TOKEN_SECRET'])

    def tweet(self, msg, img):
        self.api.PostUpdate(msg, img)
