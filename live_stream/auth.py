import tweepy

class AuthHandler():

    def __init__(self, consumer_token, consumer_secret):
        self.consumer_secret = consumer_secret
        self.consumer_token = consumer_token
    
    def connect(self):
        return tweepy.OAuthHandler(self.consumer_token, self.consumer_secret)

