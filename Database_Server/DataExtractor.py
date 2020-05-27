#--------------------------------
#Group No. 31
#Team Members
#Akshay Agarwal, 1141290,Melbourne
#Avi Patel,1143213,Melbourne
#Monit Patel,1135025,Melbourne
#Prabha Choudhary,1098776,Melbourne
#Shubham Parakh,1098807,Melbourne
#--------------------------------
import requests
import sentiment as s
import os

years = [2017,2018,2019,2020]
cities = ["Adelaide","Brisbane","Melbourne","Perth","Sydney"]
couchdb_ip = os.getenv('couchdb_ip')
couchdb_user = os.getenv('couchdb_user')
couchdb_pass = os.getenv('couchdb_pass')

def aurinPartyData2019(city) :
    urllabor= "http://" + couchdb_user + ":" + couchdb_pass + "@" + couchdb_ip + ":5984/votersdata/_design/"+city+"/_view/"+city+"_labor_party_view"
    urlliberal = "http://" + couchdb_user + ":" + couchdb_pass + "@" + couchdb_ip + ":5984/votersdata/_design/"+city+"/_view/"+city+"_liberal_party_view"
    labor_party_result = requests.get(urllabor).json()
    liberal_party_result = requests.get(urlliberal).json()
    labor_party_result = labor_party_result["rows"][0]["value"]
    liberal_party_result = liberal_party_result["rows"][0]["value"]
    return [liberal_party_result, labor_party_result]

def aurin2019Australia():
    final_total=[0,0]
    for city in cities:
        temp_list=aurinPartyData2019(city)
        for i in range(2):
                final_total[i] += temp_list[i]
    return final_total

def aurinPartyData2016(city) :
    urllabor= "http://" + couchdb_user + ":" + couchdb_pass + "@" + couchdb_ip + ":5984/votersdata2016/_design/"+city+"/_view/"+city+"_labor_party_view"
    urlliberal = "http://" + couchdb_user + ":" + couchdb_pass + "@" + couchdb_ip + ":5984/votersdata2016/_design/"+city+"/_view/"+city+"_liberal_party_view"
    labor_party_result = requests.get(urllabor).json()
    liberal_party_result = requests.get(urlliberal).json()
    labor_party_result = labor_party_result["rows"][0]["value"]
    liberal_party_result = liberal_party_result["rows"][0]["value"]
    return [liberal_party_result, labor_party_result]

def aurin2016Australia():
    final_total=[0,0]
    for city in cities:
        temp_list=aurinPartyData2016(city)
        for i in range(2):
                final_total[i] += temp_list[i]
    return final_total

def coalitionparty(city,years):
    result=[]
    for year in years:
        url = "http://" + couchdb_user + ":" + couchdb_pass + "@" + couchdb_ip + ":5984/twitter/_design/twitter/_view/coalition_"+city.lower()+"_"+str(year)
        twitter = requests.get(url).json()
        docs = twitter["rows"]
        positive = 0
        negative = 0
        neutral = 0
        total = 0
        for doc in docs:
            sentiment = s.get_tweet_sentiment(doc['key'])
            if(sentiment == "positive"):
                positive = positive+1
            elif(sentiment == "negative"):
                negative = negative + 1
            else:
                neutral = neutral + 1
        total = positive+negative+neutral
        result.append([positive, negative, neutral, total])
    return result

def coalitionpartyAustralia():
    final_total=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for city in cities:
        temp_list=coalitionparty(city,years)
        for i in range(4):
            for j in range(4):
                final_total[i][j] += temp_list[i][j]
    return final_total

def laborparty(city,years):
    result = []
    for year in years:
        url = "http://" + couchdb_user + ":" + couchdb_pass + "@" + couchdb_ip + ":5984/twitter/_design/twitter/_view/labor_" + city.lower() + "_" + str(year)
        twitter = requests.get(url).json()
        docs = twitter["rows"]
        positive = 0
        negative = 0
        neutral = 0
        total = 0
        for doc in docs:
            sentiment = s.get_tweet_sentiment(doc['key'])
            if (sentiment == "positive"):
                positive = positive + 1
            elif (sentiment == "negative"):
                negative = negative + 1
            else:
                neutral = neutral + 1
        total = positive+negative+neutral
        result.append([positive, negative, neutral,total])
    return result


def laborpartyAustralia():
    final_total = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for city in cities:
        temp_list = laborparty(city, years)
        for i in range(4):
            for j in range(4):
                final_total[i][j] += temp_list[i][j]
    return final_total


def positive_coalition(city):
    if(city.lower() == "australia"):
        result = coalitionpartyAustralia()
    else:
        result = coalitionparty(city,years)
    final_result = []
    for data in result:
        if(data[3]!=0):
            final_result.append((data[0]/data[3])*100)
        else:
            final_result.append(0)
    return final_result

def negative_coalition(city):
    if (city.lower() == "australia"):
        result = coalitionpartyAustralia()
    else:
        result = coalitionparty(city,years)
    final_result = []
    for data in result:
        if (data[3] != 0):
            final_result.append((data[1] / data[3]) * 100)
        else:
            final_result.append(0)
    return final_result

def neutral_coalition(city):
    if (city.lower()=="australia"):
        result = coalitionpartyAustralia()
    else:
        result = coalitionparty(city,years)
    final_result = []
    for data in result:
        if (data[3] != 0):
            final_result.append((data[2] / data[3]) * 100)
        else:
            final_result.append(0)
    return final_result

def positive_labor(city):
    if (city.lower() == "australia"):
        result = laborpartyAustralia()
    else:
        result = laborparty(city,years)
    final_result = []
    for data in result:
        if (data[3] != 0):
            final_result.append((data[0] / data[3]) * 100)
        else:
            final_result.append(0)
    return final_result

def negative_labor(city):
    if (city.lower() == "australia"):
        result = laborpartyAustralia()
    else:
        result = laborparty(city, years)
    final_result = []
    for data in result:
        if (data[3] != 0):
            final_result.append((data[1] / data[3]) * 100)
        else:
            final_result.append(0)
    return final_result

def neutral_labor(city):
    if (city.lower() == "australia"):
        result = laborpartyAustralia()
    else:
        result = laborparty(city, years)
    final_result = []
    for data in result:
        if (data[3] != 0):
            final_result.append((data[2] / data[3]) * 100)
        else:
            final_result.append(0)
    return final_result


def age_data(city) :
    url = "http://" + couchdb_user + ":" + couchdb_pass + "@" + couchdb_ip + ":5984/agedata/_design/" + city + "/_view/" + city + "_Age_view"
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
    result = requests.get("http://" + couchdb_user + ":" + couchdb_pass + "@" + couchdb_ip + ":5984/twitter/_design/twitter/_view/users_per_city?group_level=1").json()
    unique_user_twitter = []
    print(result)
    for city in cities:
        for row in result["rows"]:
            if (row["key"][0] == city.lower()):
                unique_user_twitter.append(row["value"])
    return unique_user_twitter

def voters_data():
    voters_count = []
    for city in cities:
        url = "http://" + couchdb_user + ":" + couchdb_pass + "@" + couchdb_ip + ":5984/totalvoters/_design/"+city.upper()+"/_view/"+city+"_total_voterCount_view"
        result = requests.get(url).json()
        voters_count.append(result["rows"][0]["value"])
    return voters_count

