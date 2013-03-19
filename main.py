from render import *

#out - template_values
out = {'mainpageTitle':'Book Exchange','submit':'Add Book','reset':'Reset','resetAction':'reset()','newBook':''}

class MainPage(webapp2.RequestHandler):
	def get(self):
		global out
		render(self,'front.html',out)
	
	def post(self):
		if self.request.get('submit') == 'Verify Data':
			#store data to database
			newBook = getBook(self)
			newBook.put()
			self.redirect('/bookAdded')  #display front page with thankyou message
		
		else: #validating
			global out
			newBook = getBook(self)
			out['bookTitleError'] = ''
			out['bookConditionError'] = ''
			out['priceError'] = ''
			out['contactError'] = ''
			out['message'] = ''
			if not newBook.bookTitle:
				out['bookTitleError'] = 'Book Title cant be empty.'
			elif not newBook.bookCondition:
				out['bookConditionError'] = 'Please give a brief description of the condtion of the book.'
			elif not newBook.price:
				out['priceError'] = 'Please input the price you expect. Enter 0 if you want to donate.'
			elif not ( newBook.phoneNumber or newBook.email or newBook.facebook):
				out['contactError'] = 'Please input at least one method of contacting you.'
			else:
				out['submit'] = 'Verify Data'
				out['reset'] = 'Edit Again'
				out['resetAction'] = 'back()'
			out['newBook'] = newBook
			render(self,'front.html',out)



class BookAdded(webapp2.RequestHandler):
	def get(self):
		global out
		out['message'] = 'Book successfully added!!!'
		out['newBook'] = ''
		out['submit'] = 'Add Book'
		out['reset'] = 'Reset'
		out['resetAction'] = 'reset()'
		self.redirect('/')

			
app = webapp2.WSGIApplication([('/',MainPage),('/bookAdded',BookAdded)],debug=True)
