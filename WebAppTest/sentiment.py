import re
from textblob import TextBlob


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
