#--------------------------------
#Group No. 31
#Team Members
#Akshay Agarwal, 1141290,Melbourne
#Avi Patel,1143213,Melbourne
#Monit Patel,1135025,Melbourne
#Prabha Choudhary,1098776,Melbourne
#Shubham Parakh,1098807,Melbourne
#--------------------------------
import couchdb
import couchdb.design
import os

cities = ["Melbourne","Brisbane","Perth","Sydney","Adelaide"]
states = ["VIC","QLD","WA","NSW","SA"]
years = [2020,2019,2018,2017,2016,2015]

def server_connection():
    ip = os.getenv('couchdb_ip')
    username = os.getenv('couchdb_user')
    password = os.getenv('couchdb_pass')

    server = couchdb.Server("http://" + username + ":" + password + "@" + ip + ":5984/")
    return server

server = server_connection()

def create_views_2partyvotes(dbname,cities):
    db = server[dbname]
    for city in cities:
        view_name = city+"_voters_view"
        map = 'function(doc) { if(doc.division_name.includes("'+city+'")) {emit(doc.tpp_australian_labor_party_votes,doc.tpp_liberal_national_coalition_votes);}}'
        view = couchdb.design.ViewDefinition(city, view_name, map)
        view.sync(db)


def create_views_liberalpartyvotes(dbname,cities):
    db = server[dbname]
    for city in cities:
        view_name = city+"_liberal_party_view"
        map = 'function(doc) { if(doc.division_name.includes("'+city+'")) {emit(doc.id,doc.tpp_liberal_national_coalition_votes);}}'
        reduce = 'function(keys, values) { return sum(values); }'
        view = couchdb.design.ViewDefinition(city, view_name, map,reduce_fun=reduce)
        view.sync(db)

def create_views_laborpartyvotes(dbname, cities):
    db = server[dbname]
    for city in cities:
        view_name = city + "_labor_party_view"
        map = 'function(doc) { if(doc.division_name.includes("' + city + '")) {emit(doc.id,doc.tpp_australian_labor_party_votes);}}'
        reduce = 'function(keys, values) { return sum(values); }'
        view = couchdb.design.ViewDefinition(city, view_name, map,reduce_fun=reduce)
        view.sync(db)

def create_views_totalvoterCount(dbname, cities):
    db = server[dbname]
    for city in cities:
        view_name = city + "_total_voterCount_view"
        city = city.upper()
        map = 'function(doc) { if(doc.Division.includes("' + city + '")) {emit(doc.id,doc.Enrolment);}}'
        view = couchdb.design.ViewDefinition(city, view_name, map)
        view.sync(db)

def create_views_AgeAbove15(dbname, cities):
    db = server[dbname]
    i = 0
    for state in states:
        view_name = cities[i] + "_Age_view"
        map = 'function(doc) { if(doc.State.includes("' + state + '") && doc.Region.includes("(C)")) {var youth = parseInt(doc["15 - 19"])+parseInt(doc["20 - 24"]);var adult = parseInt(doc["25 - 29"])+parseInt(doc["30 - 34"])+parseInt(doc["35 - 39"])+parseInt(doc["40 - 44"])+parseInt(doc["45 - 49"])+parseInt(doc["50 - 54"])+parseInt(doc["55 - 59"])+parseInt(doc["60 - 64"]);var senior = parseInt(doc["65 - 69"])+parseInt(doc["70 - 74"])+parseInt(doc["75 - 79"])+parseInt(doc["80 - 84"])+parseInt(doc["85 - 89"])+parseInt(doc["90 - 94"])+parseInt(doc["95 - 99"])+parseInt(doc["100 and over"]);emit(doc.Region, [youth,adult,senior]);}}'
        print(map)
        view = couchdb.design.ViewDefinition(cities[i], view_name, map)
        i=i+1
        view.sync(db)

