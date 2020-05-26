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
#--------------------------------

#--------------------------------
def create_views(db):
    #Melbourne
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("melbourne")) && (doc.created_at.split(" ").pop() == "2020")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_melbourne_2020', count_map,
                                         stale='update_after')
    view.sync(db)

    # sydney
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("sydney")) && (doc.created_at.split(" ").pop() == "2020")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_sydney_2020', count_map,
                                         stale='update_after')
    view.sync(db)

    # adelaide
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("adelaide")) && (doc.created_at.split(" ").pop() == "2020")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_adelaide_2020', count_map,
                                         stale='update_after')
    view.sync(db)

    # brisbane
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("brisbane")) && (doc.created_at.split(" ").pop() == "2020")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_brisbane_2020', count_map,
                                         stale='update_after')
    view.sync(db)

    # canberra
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("canberra")) && (doc.created_at.split(" ").pop() == "2020")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_canberra_2020', count_map,
                                         stale='update_after')
    view.sync(db)

    # darwin
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("darwin")) && (doc.created_at.split(" ").pop() == "2020")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_darwin_2020', count_map,
                                         stale='update_after')
    view.sync(db)

    # hobart
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("hobart")) && (doc.created_at.split(" ").pop() == "2020")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_hobart_2020', count_map,
                                         stale='update_after')
    view.sync(db)

    # perth
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("perth")) && (doc.created_at.split(" ").pop() == "2020")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_perth_2020', count_map, stale='update_after')
    view.sync(db)

    #Melbourne
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("melbourne")) && (doc.created_at.split(" ").pop() == "2019")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_melbourne_2019', count_map,
                                         stale='update_after')
    view.sync(db)

    # sydney
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("sydney")) && (doc.created_at.split(" ").pop() == "2019")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_sydney_2019', count_map,
                                         stale='update_after')
    view.sync(db)

    # adelaide
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("adelaide")) && (doc.created_at.split(" ").pop() == "2019")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_adelaide_2019', count_map,
                                         stale='update_after')
    view.sync(db)

    # brisbane
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("brisbane")) && (doc.created_at.split(" ").pop() == "2019")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_brisbane_2019', count_map,
                                         stale='update_after')
    view.sync(db)

    # canberra
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("canberra")) && (doc.created_at.split(" ").pop() == "2019")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_canberra_2019', count_map,
                                         stale='update_after')
    view.sync(db)

    # darwin
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("darwin")) && (doc.created_at.split(" ").pop() == "2019")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_darwin_2019', count_map,
                                         stale='update_after')
    view.sync(db)

    # hobart
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("hobart")) && (doc.created_at.split(" ").pop() == "2019")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_hobart_2019', count_map,
                                         stale='update_after')
    view.sync(db)

    # perth
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("perth")) && (doc.created_at.split(" ").pop() == "2019")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_perth_2019', count_map, stale='update_after')
    view.sync(db)

    #Melbourne
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("melbourne")) && (doc.created_at.split(" ").pop() == "2018")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_melbourne_2018', count_map,
                                         stale='update_after')
    view.sync(db)

    # sydney
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("sydney")) && (doc.created_at.split(" ").pop() == "2018")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_sydney_2018', count_map,
                                         stale='update_after')
    view.sync(db)

    # adelaide
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("adelaide")) && (doc.created_at.split(" ").pop() == "2018")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_adelaide_2018', count_map,
                                         stale='update_after')
    view.sync(db)

    # brisbane
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("brisbane")) && (doc.created_at.split(" ").pop() == "2018")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_brisbane_2018', count_map,
                                         stale='update_after')
    view.sync(db)

    # canberra
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("canberra")) && (doc.created_at.split(" ").pop() == "2018")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_canberra_2018', count_map,
                                         stale='update_after')
    view.sync(db)

    # darwin
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("darwin")) && (doc.created_at.split(" ").pop() == "2018")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_darwin_2018', count_map,
                                         stale='update_after')
    view.sync(db)

    # hobart
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("hobart")) && (doc.created_at.split(" ").pop() == "2018")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_hobart_2018', count_map,
                                         stale='update_after')
    view.sync(db)

    # perth
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("perth")) && (doc.created_at.split(" ").pop() == "2018")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_perth_2018', count_map, stale='update_after')
    view.sync(db)

    #Melbourne
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("melbourne")) && (doc.created_at.split(" ").pop() == "2017")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_melbourne_2017', count_map,
                                         stale='update_after')
    view.sync(db)

    # sydney
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("sydney")) && (doc.created_at.split(" ").pop() == "2017")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_sydney_2017', count_map,
                                         stale='update_after')
    view.sync(db)

    # adelaide
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("adelaide")) && (doc.created_at.split(" ").pop() == "2017")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_adelaide_2017', count_map,
                                         stale='update_after')
    view.sync(db)

    # brisbane
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("brisbane")) && (doc.created_at.split(" ").pop() == "2017")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_brisbane_2017', count_map,
                                         stale='update_after')
    view.sync(db)

    # canberra
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("canberra")) && (doc.created_at.split(" ").pop() == "2017")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_canberra_2017', count_map,
                                         stale='update_after')
    view.sync(db)

    # darwin
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("darwin")) && (doc.created_at.split(" ").pop() == "2017")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_darwin_2017', count_map,
                                         stale='update_after')
    view.sync(db)

    # hobart
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("hobart")) && (doc.created_at.split(" ").pop() == "2017")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_hobart_2017', count_map,
                                         stale='update_after')
    view.sync(db)

    # perth
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("perth")) && (doc.created_at.split(" ").pop() == "2017")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_perth_2017', count_map, stale='update_after')
    view.sync(db)

    #Melbourne
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("melbourne")) && (doc.created_at.split(" ").pop() == "2016")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_melbourne_2016', count_map,
                                         stale='update_after')
    view.sync(db)

    # sydney
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("sydney")) && (doc.created_at.split(" ").pop() == "2016")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_sydney_2016', count_map,
                                         stale='update_after')
    view.sync(db)

    # adelaide
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("adelaide")) && (doc.created_at.split(" ").pop() == "2016")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_adelaide_2016', count_map,
                                         stale='update_after')
    view.sync(db)

    # brisbane
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("brisbane")) && (doc.created_at.split(" ").pop() == "2016")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_brisbane_2016', count_map,
                                         stale='update_after')
    view.sync(db)

    # canberra
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("canberra")) && (doc.created_at.split(" ").pop() == "2016")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_canberra_2016', count_map,
                                         stale='update_after')
    view.sync(db)

    # darwin
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("darwin")) && (doc.created_at.split(" ").pop() == "2016")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_darwin_2016', count_map,
                                         stale='update_after')
    view.sync(db)

    # hobart
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("hobart")) && (doc.created_at.split(" ").pop() == "2016")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_hobart_2016', count_map,
                                         stale='update_after')
    view.sync(db)

    # perth
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("perth")) && (doc.created_at.split(" ").pop() == "2016")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter_stream_listener', 'labor_perth_2016', count_map, stale='update_after')
    view.sync(db)
#--------------------------------

#--------------------------------
if __name__=="__main__":

    couchdb_ip = os.getenv('couchdb_ip')
    couchdb_user = os.getenv('couchdb_user')
    couchdb_pass = os.getenv('couchdb_pass')
    couch = couchdb.Server('http://' + couchdb_user + ':' + couchdb_pass + '@' + couchdb_ip + ':5984/')
    db = couch['twitter_stream_listener'] # existing
    create_views(db)
#--------------------------------
