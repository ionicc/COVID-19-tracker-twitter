import tweepy
from live_stream import AuthHandler
class Streamer(tweepy.StreamListener):
	
    def on_status(self, status):
        print(status.text)

def main():
    # Create stream instance
    # TODO: Move Stream class to different file
    streamer = Streamer()
    stream_listener = tweepy.Stream(AuthHandler())
