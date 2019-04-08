import twitter
import json

class Tweet:
    def __init__(self):
        with open('mezase65kg.json') as file:
            json_file = json.load(file)

        self.api = twitter.Api(
            consumer_key = json_file['consumer_key'],
            consumer_secret = json_file['consumer_secret'],
            access_token_key = json_file['access_token'],
            access_token_secret = json_file['access_token_secret']
        )

    def tweet(self, msg, img):
        self.api.PostUpdate(msg, img)
