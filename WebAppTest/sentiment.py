#--------------------------------
#Group No. 31
#Team Members
#Akshay Agarwal, 1141290,Melbourne
#Avi Patel,1143213,Melbourne
#Monit Patel,1135025,Melbourne
#Prabha Choudhary,1098776,Melbourne
#Shubham Parakh,1098807,Melbourne
#--------------------------------
import re
from textblob import TextBlob
import couchdb
import couchdb.design


def create_views(db):
    view_key = []

    count_map = 'function(doc) { if(doc.full_text.includes("Liberal") && doc.user.location.includes("melbourne")) {' \
                'emit(doc.full_text);}} '
    view = couchdb.design.ViewDefinition('twitter', 'Liberal_melbourne_tweets', count_map)
    view.sync(db)

    for doc in db.view('twitter/Liberal_melbourne_tweets'):
        view_key.append(doc[ 'key' ])

    return view_key


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\/\/\S+)", " ", tweet).split())


def get_tweet_sentiment(tweet):
    # create TextBlob object of passed tweet text
    analysis = TextBlob(clean_tweet(tweet))
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


def parse_tweets(file_tweets):
    # empty list to store parsed tweets
    tweets = []

    # parsing tweets one by one
    for tweet in file_tweets:
        # dictionary to store required params of a tweet
        parsed_tweet = {'text': tweet, 'sentiment': get_tweet_sentiment(tweet)}
        tweets.append(parsed_tweet)

    # return parsed tweets
    return tweets
