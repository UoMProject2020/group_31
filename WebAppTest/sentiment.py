import re
from textblob import TextBlob
import couchdb
import couchdb.design

def server_config():
    username = "admin"
    password = "admin"
    # ip = "localhost"
    ip = "172.26.134.65"
    server = couchdb.Server("http://" + username + ":" + password + "@" + ip + ":5984/")
    return server

def create_views(db):
    view_key = []

    count_map = 'function(doc) { if(doc.full_text.includes("Liberal") && doc.user.location.includes("melbourne")) {' \
                'emit(doc.full_text);}} '
    view = couchdb.design.ViewDefinition('twitter', 'Liberal_melbourne_tweets', count_map)
    view.sync(db)

    for doc in db.view('twitter/Liberal_melbourne_tweets'):
        view_key.append(doc[ 'key' ])

    return view_key

def create_views_voter(dbname,city):
    server = server_config()
    db = server[dbname]
    view_name = city+"_view"
    map = 'function(doc) { if(doc.division_name.includes("'+city+'")) {emit(doc.tpp_australian_labor_party_votes,doc.tpp_liberal_national_coalition_votes);}}'
    view = couchdb.design.ViewDefinition(city, view_name, map)
    view.sync(db)
    labor_party_votes = 0
    liberal_party_votes = 0
    for doc in db.view(city+"/"+view_name) :
        labor_party_votes += doc["key"]
        liberal_party_votes += doc["value"]
    return labor_party_votes,liberal_party_votes



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
