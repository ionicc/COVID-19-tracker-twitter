import tweepy

class AuthHandler():

    def __init__(self, consumer_token, consumer_secret):
        self.consumer_secret = consumer_secret
        self.consumer_token = consumer_token
        self.auth = tweepy.OAuthHandler(self.consumer_token, self.consumer_secret)
        self.auth.set_access_token(self.consumer_token, self.consumer_token)

    def api(self):
        return tweepy.API(self.auth)
        

