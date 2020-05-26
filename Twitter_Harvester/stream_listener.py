#--------------------------------
#Group No. 31
#Team Members
#Akshay Agarwal, 1141290,Melbourne
#Avi Patel,1143213,Melbourne
#Monit Patel,1135025,Melbourne
#Prabha Choudhary,1098776,Melbourne
#Shubham Parakh,1098807,Melbourne
#--------------------------------

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import couchdb
import json
import os
#--------------------------------

#--------------------------------
global parsed_tweet
#--------------------------------

#--------------------------------
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
#--------------------------------

#--------------------------------
#start the stream
if __name__=="__main__":

	parsed_tweet = []
	existing_tweet_file = os.getenv('existing_tweets')
	consumer_key = os.getenv('consumer_key')
	consumer_secret = os.getenv('consumer_secret')
	access_key = os.getenv('access_key')
	access_secret = os.getenv('access_secret')
	couchdb_ip = os.getenv('couchdb_ip')
	couchdb_user = os.getenv('couchdb_user')
	couchdb_pass = os.getenv('couchdb_pass')

	file = open(existing_tweet_file, "r")
	for line in file:
		json_text = json.loads(line.strip())
		parsed_tweet.append(json_text['id'])
	print(len(parsed_tweet))
	file.close()

	f = open(existing_tweet_file, 'a')

	couch = couchdb.Server('http://' + couchdb_user + ':' + couchdb_pass + '@' + couchdb_ip + ':5984/')
	db = couch['twitter_stream_listener']  # existing

	listener = MListener()
	auth = OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_key,access_secret)
	stream = Stream(auth, listener)
	stream.filter(track=['auspol'])
#--------------------------------
