#--------------------------------
#Group No. 31
#Team Members
#Akshay Agarwal, 1141290,Melbourne
#Avi Patel,1143213,Melbourne
#Monit Patel,1135025,Melbourne
#Prabha Choudhary,1098776,Melbourne
#Shubham Parakh,1098807,Melbourne
#--------------------------------

import json,tweepy,couchdb,sys,os
#--------------------------------

#--------------------------------
def checkInput(inFile1,inFile2):
	try:
		fo = open(inFile1)
		fo.close()
	except:
		print(inFile1 + " not found..!!\n")
		return False

	try:
		fo = open(inFile2)
		fo.close()
	except:
		print(inFile2 + " not found..!!\n")
		return False
	return True
#--------------------------------

#--------------------------------
def collectTweets(keys_file,existing_tweet_file,couchdb_ip,couchdb_user,couchdb_pass):
	keys = {}
	key_file = open(keys_file)
	total_keys = 0
	key_parameter = 0

	for line in key_file:
		if not line.startswith("#"):
			if key_parameter == 0:
				keys[total_keys] = {}
			line_parts = line.strip().split(" = ")
			keys[total_keys][line_parts[0]] = line_parts[1]
			key_parameter += 1
			if key_parameter == 4:
				key_parameter = 0
				total_keys += 1

	total_keys = len(keys)
	key_to_be_used = 0
	parsed_tweet = []
	parsed_users = []

	file = open(existing_tweet_file,"r")
	for line in file:
		json_text = json.loads(line.strip())
		parsed_tweet.append(json_text['id'])
	print(len(parsed_tweet))
	file.close()

	searchQuery = "#auspol"  # this is what we're searching for
	tweetsPerQry = 100  # this is the max the API permits

	couch = couchdb.Server('http://' + couchdb_user + ':' + couchdb_pass + '@'+ couchdb_ip + ':5984/')
	db = couch['twitter']  # existing

	f= open(existing_tweet_file, 'a')

	while(True):
		auth = tweepy.OAuthHandler(keys[key_to_be_used]['consumer_key'], keys[key_to_be_used]['consumer_secret'])
		auth.set_access_token(keys[key_to_be_used]['access_key'], keys[key_to_be_used]['access_secret'])
		api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
		try:
			api.verify_credentials()
			print("Authentication OK with key number : ",key_to_be_used)
		except:
			print("Error during authentication with key number : ",key_to_be_used)

		try:
			for tweet in tweepy.Cursor(api.search, q=searchQuery, tweet_mode="extended",count=tweetsPerQry).items():
				if tweet._json['id'] not in parsed_tweet:
					parsed_tweet.append(tweet._json['id'])
					json.dump(tweet._json, f)
					f.write("\n")
					db.save(tweet._json)
					screen_name = tweet._json['user']['screen_name']

					for tweet_user in tweepy.Cursor(api.user_timeline, q=searchQuery, screen_name=screen_name,tweet_mode="extended",count=tweetsPerQry).items():
						if tweet_user._json['id'] not in parsed_tweet:
							parsed_tweet.append(tweet_user._json['id'])
							if searchQuery in str(tweet_user._json):
								db.save(tweet_user._json)
								json.dump(tweet_user._json, f)
								f.write("\n")

					for user in tweepy.Cursor(api.followers, screen_name=screen_name,tweet_mode="extended",count=tweetsPerQry).items():
						user_name = user._json['screen_name']
						if user_name not in parsed_users:
							parsed_users.append(user_name)
							for tweet_user1 in tweepy.Cursor(api.user_timeline, q=searchQuery, screen_name=user_name,
															tweet_mode="extended", count=tweetsPerQry).items():
								if tweet_user1._json['id'] not in parsed_tweet:
									parsed_tweet.append(tweet_user1._json['id'])
									if searchQuery in str(tweet_user1._json):
										db.save(tweet_user1._json)
										json.dump(tweet_user1._json, f)
										f.write("\n")
		except tweepy.TweepError as e:
			print("some error : " + str(e))

		if (key_to_be_used+1) >= total_keys:
			key_to_be_used = 0
		else:
			key_to_be_used += 1

#--------------------------------
if __name__ == '__main__':
	
	if checkInput(os.getenv('twitter_keys'),os.getenv('existing_tweets')) == False:
		sys.exit()

	collectTweets(os.getenv('twitter_keys'),os.getenv('existing_tweets'),os.getenv('couchdb_ip'),os.getenv('couchdb_user'),os.getenv('couchdb_pass'))
	sys.exit()
#--------------------------------
