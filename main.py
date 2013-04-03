from render import *

class FindBook(webapp2.RequestHandler):
	def post(self):
		out = {'newBook':''}
		q = self.request.get('findBook')
		out['bookRequested'] = q
		out['books'] = findBook(q)
		render(self,'findBook.html',out)


class MainPage(webapp2.RequestHandler):
	def get(self):
		out = {'newBook':'','featuredBooks':getFeaturedBooks(False)}
		if self.request.get('success') == '1':
			out['message'] = "Book sucessfully Added!"
		render(self,'main.html',out)

	def post(self):
		out = {'featuredBooks':getFeaturedBooks(False)}
		newBook = getBook(self)
		error = False
		if not newBook.bookTitle:
			out['bookTitleError'] = 'Book Title cant be empty.'
			error = True
		elif not newBook.bookCondition:
			out['bookConditionError'] = 'Please give a brief description of the condtion of the book.'
			error = True
		elif not newBook.price:
			out['priceError'] = 'Please input the price you expect. Enter 0 if you want to donate.'
			error = True
		elif not ( newBook.phoneNumber or newBook.email or newBook.facebook):
			out['contactError'] = 'Please input at least one method of contacting you.'
			error = True
	
		out['newBook'] = newBook
		if error:
			render(self,'main.html',out)
		else:
			out['googleImages'] = google(newBook.bookTitle)
			render(self,'verify.html',out)	



		
class Verify(webapp2.RequestHandler):
	def post(self):
		newBook = getBook(self)
		if newBook.put():
			self.redirect('/?success=1')
		else:
			self.response.out('SNAPPED! contact admin')


		
app = webapp2.WSGIApplication([('/',MainPage),('/verify',Verify),('/findBook',FindBook)],debug=True)
