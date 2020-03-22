import tweepy

class Streamer(tweepy.StreamListener):
	
    def on_status(self, status):
        print(status.text)

def main():
    streamer = Streamer()
    stream_listener = tweepy.Stream()
