from google.appengine.ext import ndb

class Review(ndb.Model):
    game_name =  ndb.StringProperty(required=True)
    review =  ndb.StringProperty(required=True)
    rating =  ndb.StringProperty(required=True)
