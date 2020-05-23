import couchdb
import couchdb.design

def server_config():
    username = "admin"
    password = "admin"
    ip = "localhost"
    # ip = "172.26.134.65"
    server = couchdb.Server("http://" + username + ":" + password + "@" + ip + ":5984/")
    return server

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
    print(labor_party_votes)
    return {'labor_party_votes': labor_party_votes,'liberal_party_votes' : liberal_party_votes}

