__author__ = 'recovery'

from google.appengine.ext import db

class TouchInfo(db.Model):
    createDate = db.DateProperty()
    touchType = db.StringProperty()
    touchId = db.StringProperty()
    count = db.IntegerProperty()
    deviceId = db.StringProperty()
