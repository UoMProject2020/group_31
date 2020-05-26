import requests
import sentiment as s
years = [2017,2018,2019,2020]
cities = ["Adelaide","Brisbane","Melbourne","Perth","Sydney"]


def aurinPartyData2019(city) :
    urllabor= "http://admin:admin@172.26.134.65:5984/votersdata/_design/"+city+"/_view/"+city+"_labor_party_view"
    urlliberal = "http://admin:admin@172.26.134.65:5984/votersdata/_design/"+city+"/_view/"+city+"_liberal_party_view"
    labor_party_result = requests.get(urllabor).json()
    liberal_party_result = requests.get(urlliberal).json()
    labor_party_result = labor_party_result["rows"][0]["value"]
    liberal_party_result = liberal_party_result["rows"][0]["value"]
    return [liberal_party_result, labor_party_result]

def aurinPartyData2016(city) :
    urllabor= "http://admin:admin@172.26.134.65:5984/votersdata2016/_design/"+city+"/_view/"+city+"_labor_party_view"
    urlliberal = "http://admin:admin@172.26.134.65:5984/votersdata2016/_design/"+city+"/_view/"+city+"_liberal_party_view"
    labor_party_result = requests.get(urllabor).json()
    liberal_party_result = requests.get(urlliberal).json()
    labor_party_result = labor_party_result["rows"][0]["value"]
    liberal_party_result = liberal_party_result["rows"][0]["value"]
    return [liberal_party_result, labor_party_result]


def coalitionparty(city,year):
    result=[]
    for year in years:
        url = "http://admin:admin@172.26.134.65:5984/twitter/_design/twitter/_view/coalition_"+city.lower()+"_"+str(year)
        twitter = requests.get(url).json()
        docs = twitter["rows"]
        positive = 0
        negative = 0
        neutral = 0
        for doc in docs:
            sentiment = s.get_tweet_sentiment(doc['key'])
            if(sentiment == "positive"):
                positive = positive+1
            elif(sentiment == "negative"):
                negative = negative + 1
            else:
                neutral = neutral + 1
        result.append([positive, negative, neutral])
    return result

def laborparty(city,years):
    result = []
    for year in years:
        url = "http://admin:admin@172.26.134.65:5984/twitter/_design/twitter/_view/labor_" + city.lower() + "_" + str(year)
        twitter = requests.get(url).json()
        docs = twitter["rows"]
        positive = 0
        negative = 0
        neutral = 0
        for doc in docs:
            sentiment = s.get_tweet_sentiment(doc['key'])
            if (sentiment == "positive"):
                positive = positive + 1
            elif (sentiment == "negative"):
                negative = negative + 1
            else:
                neutral = neutral + 1
        result.append([positive, negative, neutral])
    return result

def positive_coalition(city):
    result = coalitionparty(city,years)
    final_result = []
    for data in result:
        final_result.append(data[0])
    return final_result

def negative_coalition(city):
    result = coalitionparty(city,years)
    final_result = []
    for data in result:
        final_result.append(data[1])
    return final_result

def neutral_coalition(city):
    result = coalitionparty(city,years)
    final_result = []
    for data in result:
        final_result.append(data[2])
    return final_result

def positive_labor(city):
    result = laborparty(city,years)
    final_result = []
    for data in result:
        final_result.append(data[0])
    return final_result

def negative_labor(city):
    result = laborparty(city,years)
    final_result = []
    for data in result:
        final_result.append(data[1])
    return final_result

def neutral_labor(city):
    result = laborparty(city,years)
    final_result = []
    for data in result:
        final_result.append(data[2])
    return final_result


def age_data(city) :
    url = "http://admin:admin@172.26.134.65:5984/agedata/_design/" + city + "/_view/" + city + "_Age_view"
    result = requests.get(url).json()
    docs = result["rows"]
    total_youth = 0
    total_adult = 0
    total_senior = 0
    for doc in docs:
        total_youth += doc['value'][0]
        total_adult += doc['value'][1]
        total_senior += doc['value'][2]
    return [total_youth,total_adult,total_senior]

def unique_user_cities() :
    result = requests.get("http://admin:admin@172.26.134.65:5984/twitter/_design/twitter/_view/users_per_city?group_level=1").json()
    unique_user_twitter = []
    for city in cities:
        for row in result["rows"]:
            if (row["key"][0] == city.lower()):
                unique_user_twitter.append(row["value"])
    return unique_user_twitter

def voters_data():
    voters_count = []
    for city in cities:
        url = "http://admin:admin@172.26.134.65:5984/totalvoters/_design/"+city.upper()+"/_view/"+city+"_total_voterCount_view"
        result = requests.get(url).json()
        voters_count.append(result["rows"][0]["value"])
    return voters_count


