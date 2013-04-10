from render import *

class ShowBook(webapp2.RequestHandler):
	def get(self,id):
		out = {'newBook':getOneBook(id)}
		render(self,'showBook.html',out)

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
		render(self,'main.html',out)

	def post(self):
		out = {'featuredBooks':getFeaturedBooks(False)}
		newBook = getBook(self)
		error = False
		if not newBook.bookTitle:
			out['bookTitleError'] = 'Book Title cant be empty.'
			error = True
		elif not newBook.price and newBook.price != 0:
			out['priceError'] = 'If you dont enter price, we will assume that you want to donate.'
			error = True
		elif not ( newBook.contact):
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
			if memcache.get('allbooks'):
				memcache.replace('allbooks',[])
			render(self,'success.html',{'dispMsg':'Book Successfully Added!'})
		else:
			render(self,'success.html',{'dispMsg':'SNAPPED! CONTACT ADMINISTRATOR!'})


		
app = webapp2.WSGIApplication([('/',MainPage),('/verify',Verify),('/findBook',FindBook),('/book/([0-9]+)',ShowBook)],debug=False)
