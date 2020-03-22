import tweepy
from live_stream import AuthHandler
from live_stream.config import consumer_api_token, consumer_api_secret, access_token, access_secret
import time
class Streamer(tweepy.StreamListener):
	
    def on_status(self, status):
        print(status.text)
    
    def on_error(self, status_code):
        print("Woops, Something went wrong:: Status code="+str(status_code))

    def on_data(self, data):
        print("Data recieved:{}".format(data))
        time.sleep(1)

def main():
    #Create stream instance
    # TODO: Move Stream class to different file
    streamer = Streamer()
    auth = AuthHandler(consumer_api_token, consumer_api_secret, access_token, access_secret)
    stream = tweepy.Stream(auth.api(), listener=streamer)
    while True:
        try:
            stream.filter(track=['corona', 'COVID-19'])
        except Exception as e:
            print(e)
    
if __name__ == '__main__':
    main()
