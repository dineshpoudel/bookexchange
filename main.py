from render import *

class Book(db.Model):
	bookTitle = db.StringProperty()
	courseID = db.StringProperty()
	ISBN = db.IntegerProperty()
	edition = db.StringProperty()
	bookCondition = db.TextProperty()
	price = db.FloatProperty()
	phoneNumber = db.PhoneNumberProperty()
	email = db.StringProperty() #do not use email property
	facebook = db.StringProperty() #do not use linkProperty because linkProperty cannot be null
	remark = db.TextProperty()
	
	googleImage = db.StringProperty() #do not use linkProperty
	sold = db.BooleanProperty(indexed=False)
	ipAddr = db.StringProperty()
	timestamp = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
	def get(self):
		out = {'mainpageTitle':'Book Exchange','submit':'Add Book','reset':'Reset','resetAction':'reset()'}
		render(self,'front.html',out)
	
	def post(self):
		if self.request.get('submit') == 'Verify Data':
			#store data to database
			newBook = Book()			

			newBook.bookTitle = self.request.get('bookTitle')
			newBook.courseID = self.request.get('courseID')
			newBook.ISBN = int(self.request.get('ISBN'))
			newBook.edition = self.request.get('edition')
			newBook.bookCondition = self.request.get('bookCondition')
			newBook.price = float(self.request.get('price'))
			newBook.phoneNumber = db.PhoneNumber(self.request.get('phoneNumber'))
			newBook.email = self.request.get('email')
			newBook.facebook = self.request.get('facebook')
			newBook.remark = self.request.get('remark')
			
			newBook.googleImage = ''
			newBook.sold = False
			newBook.ipAddr = ((os.getenv("HTTP_CLIENT_IP") or 
						os.getenv("HTTP_X_FORWARDED_FOR") or 
						os.getenv("HTTP_X_FORWARDED_FOR") or 
						os.getenv("REMOTE_ADDR") or 
						"UNKNOWN"))

			newBook.put()
			

			self.redirect('/bookAdded')  #display front page with thankyou message
		
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

class BookAdded(webapp2.RequestHandler):
	def get(self):
		out = {'mainpageTitle':'Book Exchange','submit':'Add Book','reset':'Reset','resetAction':'reset()','message':'Book Successfully Added!'}
		render(self,'front.html',out)
			
app = webapp2.WSGIApplication([('/',MainPage),('/bookAdded',BookAdded)],debug=True)
