import json
from private import API_KEY,API_SECRET_KEY,ACCESS_TOKEN,ACCESS_TOKEN_SECRET
import tweepy

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)
with open('try.json', 'w', encoding='utf8') as f:
	for tweet in tweepy.Cursor(api.search,q="(#auspol OR politics) (health OR medicine)",tweet_mode="extended").items():
		if(('politics' in tweet._json['full_text'].split()) or ('#auspol' in tweet._json['full_text'].split()) and ('health' in tweet._json['full_text'].split()) or ('medicine' in tweet._json['full_text'].split())):
			json.dump(tweet._json, f)
			f.write("\n")
			print(tweet._json['full_text'])
			print("\n")
		
		