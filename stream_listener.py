from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from keys import consumer_key,consumer_secret,access_key,access_secret
import couchdb
import json

###
global parsed_tweet

#create a streamlistener
class MListener(StreamListener):

	def on_data(self,data):
		parsed_data = json.loads(data)
		if parsed_data['id'] not in parsed_tweet:
			json.dump(parsed_data, f)
			f.write("\n")
			db.save(parsed_data)
			parsed_tweet.append(parsed_data['id'])
		return True

	def on_error(self, status_code):
		if status_code == 420:
			print(status_code)	# returning False in on_error disconnects the stream
			return False

#start the stream
if __name__=="__main__":

	parsed_tweet = []

	file = open("stream_tweets_uni.txt", "r")
	for line in file:
		json_text = json.loads(line.strip())
		parsed_tweet.append(json_text['id'])
	print(len(parsed_tweet))
	file.close()

	fName = 'stream_tweets_uni.txt'  # We'll store the tweets in a text file.
	f = open(fName, 'a')

	couch = couchdb.Server('http://admin:admin@172.26.134.65:5984/')
	db = couch['twitter_stream_listener']  # existing

	listener = MListener()
	auth = OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_key,access_secret)
	stream = Stream(auth, listener)
	stream.filter(track=['auspol'])
