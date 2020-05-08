from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from private import API_KEY,API_SECRET_KEY,ACCESS_TOKEN,ACCESS_TOKEN_SECRET
import json

#create a streamlistener
class MListener(StreamListener):
	
	def on_data(self,data):
		parsed_data = json.loads(data)
		return True

	def on_error(self, status):
		print(status)

#start the stream
if __name__=="__main__":

	listener = MListener()
	auth = OAuthHandler(API_KEY, API_SECRET_KEY)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	stream = Stream(auth, listener)
	stream.filter(track=['auspol'])