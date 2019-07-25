from google.appengine.ext import ndb

class Reviews(ndb.Model):
    name =  ndb.StringProperty(required=True)
    text =  ndb.StringProperty(required=True)
    rating =  ndb.IntegerProperty(required=True)
