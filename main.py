from render import *

class FindBook(webapp2.RequestHandler):
	def post(self):
		out = {}
		q = self.request.get('findBook')
		out['bookRequested'] = q
		out['books'] = findBook(q)
		render(self,'findBook.html',out)


class MainPage(webapp2.RequestHandler):
	def get(self):
		out = {'newBook':'','featuredBooks':getFeaturedBooks(False)}
		render(self,'main.html',out)

class Verify(webapp2.RequestHandler):	
	def post(self):
		if self.request.get('submit') == 'Verify Data':
			#store data to database
			newBook = getBook(self)
			if newBook.put():
				out['message'] = 'Book successfully added!!!'
				out['newBook'] = ''
				out['submit'] = 'Add Book'
				out['reset'] = 'Reset'
				out['resetAction'] = 'reset()'
				out['googleImages'] = ''
				out['featuredBooks'] = getFeaturedBooks(True)
				self.redirect('/')
			else:
				self.response.out('SNAPPED! contact admin')
		
		else: #validating
			out = {'newBook':'','featuredBooks':getFeaturedBooks(False)}
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
				out['googleImages'] = google(newBook.bookTitle)
			out['newBook'] = newBook
			render(self,'main.html',out)


			
app = webapp2.WSGIApplication([('/',MainPage),('/verify',Verify),('/findBook',FindBook)],debug=True)
