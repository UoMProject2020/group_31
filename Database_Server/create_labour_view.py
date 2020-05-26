import couchdb
import couchdb.design

def create_views(db):
    #Melbourne
    count_map = 'function(doc) { if((doc.full_text.toLowerCase().includes("labor") || doc.full_text.toLowerCase().includes("alp")) && (doc.user.location.toLowerCase().includes("melbourne")) && (doc.created_at.split(" ").pop() == "2020")) {emit(doc.full_text);}}'
    view = couchdb.design.ViewDefinition('twitter', 'labor_melbourne_2020', count_map, stale='update_after')
    view.sync(db)

couch = couchdb.Server('http://admin:admin@172.26.134.65:5984/')
db = couch['twitter'] # existing
create_views(db)
