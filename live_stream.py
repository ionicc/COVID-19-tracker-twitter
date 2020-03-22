import tweepy
from live_stream import AuthHandler
from live_stream.config import api_key, api_secret
class Streamer(tweepy.StreamListener):
	
    def on_status(self, status):
        print(status.text)
    
    def on_error(self, status_code):
        print("Woops, Something went wrong:: Status code="+str(status_code))

    def on_data(self, data):
        print(f"Data recieved:  {data}")

def main():
    #Create stream instance
    # TODO: Move Stream class to different file
    streamer = Streamer()
    auth = AuthHandler(api_key, api_secret)
    tweepy.Stream(auth.api(), listener=streamer)
    

