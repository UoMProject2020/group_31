import json
import tweepy

keys = {}
key_file = open("keys")
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
# print (total_keys)
key_to_be_used = 0
tweetCount = 0
parsed_tweet = []
parsed_users = []

# searchQuery = "#auspol"  # this is what we're searching for
searchQuery = "#accidents OR #roadaccident OR #carcrash OR #roadrage OR #speedkills OR #roadinjury OR #roadsafty OR #rashdriving"  # this is what we're searching for
searchQueryList = ["#accidents" , "#roadaccident" , "#fatality" , "#carcrash" , "#roadrage" , "#speedkills" , "#roadinjury" , "#roadsafty" , "#rashdriving"]
mainSearchQuery = "#accidents"
tweetsPerQry = 100  # this is the max the API permits
fName = 'tweets.txt' # We'll store the tweets in a text file.

f= open(fName, 'w', encoding='utf8')

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
			json.dump(tweet._json, f)
			f.write("\n")
			print(tweet._json['geo'],tweet._json['coordinates'],tweet._json['place'])
			print("Found_tweet_in_first_loop")
			screen_name = tweet._json['user']['screen_name']
			parsed_tweet.append(tweet._json['id'])

			for tweet_user in tweepy.Cursor(api.user_timeline, screen_name=screen_name,tweet_mode="extended",count=tweetsPerQry).items():
				# print("in second loop")
				if tweet_user._json['id'] not in parsed_tweet:
					parsed_tweet.append(tweet_user._json['id'])
					if any(x in str(tweet_user._json) for x in searchQueryList):
						print("Found_tweet_in_second_loop")
						json.dump(tweet_user._json, f)
						f.write("\n")

			for user in tweepy.Cursor(api.followers, screen_name=screen_name,tweet_mode="extended",count=tweetsPerQry).items():
				# print(user)
				user_name = user._json['screen_name']
				if user_name not in parsed_users:
					parsed_users.append(user_name)
					# print(user_name)
					for tweet_user1 in tweepy.Cursor(api.user_timeline, screen_name=user_name,
													tweet_mode="extended", count=tweetsPerQry).items():
						if tweet_user1._json['id'] not in parsed_tweet:
							parsed_tweet.append(tweet_user1._json['id'])
							if any(x in str(tweet_user1._json) for x in searchQueryList):
								print("Found_tweet_in_third_loop")
								json.dump(tweet_user1._json, f)
								f.write("\n")
	except tweepy.TweepError as e:
		# Just exit if any error
		print("some error : " + str(e))

	if (key_to_be_used+1) >= total_keys:
		key_to_be_used = 0
	else:
		key_to_be_used += 1
