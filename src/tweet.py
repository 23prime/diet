import twitter
import json

class Tweet:
    def __init__(self):
        with open('mezase65kg.json') as file:
            self.json_file = json.load(file)

        self.api = twitter.Api(
            consumer_key = self.json_file['consumer_key'],
            consumer_secret = self.json_file['consumer_secret'],
            access_token_key = self.json_file['access_token'],
            access_token_secret = self.json_file['access_token_secret']
        )

    def tweet(self, msg, img):
        self.api.PostUpdate(msg, img)
