from render import *
import webapp2

from google.appengine.ext import db


class Book(db.Model):
	bookTitle = db.StringProperty()
	courseID = db.StringProperty()
	ISBN = db.IntegerProperty()
	edition = db.StringProperty()
	bookCondition = db.TextProperty()
	price = db.FloatProperty()
	phoneNumber = db.PhoneNumberProperty()
	email = db.EmailProperty()
	facebook = db.LinkProperty()
	
	googleImage = db.LinkProperty()
	sold = db.BooleanProperty(default=False)
	ipAddr = db.StringProperty()
	timestamp = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):

  def get(self):
    render(self,'front.html',{'mainpageTitle':'Book Exchange','output':''})

			
app = webapp2.WSGIApplication([('/',MainPage)],debug=True)
