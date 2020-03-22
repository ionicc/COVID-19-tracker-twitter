import tweepy

class AuthHandler():

    def __init__(self, consumer_token, consumer_secret, access_token, access_secret):
        self.consumer_secret = consumer_secret
        self.consumer_token = consumer_token
        self.access_token = access_token
        self.access_secret = access_secret
        self.auth = tweepy.OAuthHandler(self.consumer_token, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_secret)

    def api(self):
        print(self.auth)
        return self.auth
        

