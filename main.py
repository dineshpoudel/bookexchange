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
	remark = db.TextProperty()
	
	googleImage = db.LinkProperty()
	sold = db.BooleanProperty(default=False)
	ipAddr = db.StringProperty()
	timestamp = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
	def get(self):
		out = {'mainpageTitle':'Book Exchange','submit':'Add Book','reset':'Reset','resetAction':'reset()'}
		render(self,'front.html',out)
	
	def post(self):
		if self.request.get('submit') == 'Verify Data':
			#store data to database
			self.response.out.write('storing to database')
		
		else: #validating
			out = {'mainpageTitle':'Book Exchange','submit':'Add Book','reset':'Reset','resetAction':'reset()'}
			#validating
			if not self.request.get('bookTitle'):
				out['bookTitleError'] = 'Book Title cant be empty.'
			elif not self.request.get('bookCondition'):
				out['bookConditionError'] = 'Please give a brief description of the condtion of the book.'
			elif not self.request.get('price'):
				out['priceError'] = 'Please input the price you expect. Enter 0 if you want to donate.'
			elif not ( self.request.get('phoneNumber') or self.request.get('email') or self.request.get('facebook')):
				out['contactError'] = 'Please input at least one method of contacting you.'
			else:
				out['submit'] = 'Verify Data'
				out['reset'] = 'Edit Again'
				out['resetAction'] = 'back()'

				#display all data to verify
		
			#displayingprevious values like
			out['bookTitle'] = self.request.get('bookTitle')
			out['courseID'] = self.request.get('courseID')
			out['ISBN'] = self.request.get('ISBN')
			out['edition'] = self.request.get('edition')
			out['bookCondition'] = self.request.get('bookCondition')
			out['price'] = self.request.get('price')
			out['phoneNumber'] = self.request.get('phoneNumber')
			out['email'] = self.request.get('email')
			out['facebook'] = self.request.get('facebook')
			out['remark'] = self.request.get('remark')
			render(self,'front.html',out)
			
app = webapp2.WSGIApplication([('/',MainPage)],debug=True)
