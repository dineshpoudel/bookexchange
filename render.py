import jinja2
import os
import cgi
import webapp2

from google.appengine.api import memcache
from google.appengine.ext import db

#to render HTML
def render(self,file,values={'junk':'junk'}):
	self.response.out.write(jinja.get_template(file).render(values))

jinja = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),autoescape=True)

def getFeaturedBooks(cacheUpdated = True):
	#featured books here
	books = memcache.get('featuredBooks')
	if not cacheUpdated or books is None:
		books = db.GqlQuery('SELECT * FROM Book ORDER BY timestamp DESC LIMIT 20')
		books = list(books)
		memcache.add('featuredBooks',books)
		cacheUpdated = True
	return books


#Book data type
class Book(db.Model):
	bookTitle = db.StringProperty()
	courseID = db.StringProperty()
	ISBN = db.IntegerProperty()
	edition = db.StringProperty()
	bookCondition = db.TextProperty()
	price = db.FloatProperty()
	phoneNumber = db.StringProperty() #do not use phone property
	email = db.StringProperty() #do not use email property
	facebook = db.StringProperty() #do not use linkProperty because linkProperty cannot be null
	remark = db.TextProperty()
	
	googleImage = db.StringProperty() #do not use linkProperty
	sold = db.BooleanProperty(indexed=False)
	ipAddr = db.StringProperty()
	timestamp = db.DateTimeProperty(auto_now_add=True)

def getBook(self):
	book = Book()
	book.bookTitle = self.request.get('bookTitle')
	book.courseID = self.request.get('courseID')
	book.ISBN = int(self.request.get('ISBN') or 0)
	book.edition = self.request.get('edition')
	book.bookCondition = self.request.get('bookCondition')
	book.price = float(self.request.get('price') or 0) 
	book.phoneNumber = self.request.get('phoneNumber')
	book.email = self.request.get('email')
	book.facebook = self.request.get('facebook')
	book.remark = self.request.get('remark')

	book.googleImage = ''
	book.sold = False
	book.ipAddr = ((os.getenv("HTTP_CLIENT_IP") or 
				os.getenv("HTTP_X_FORWARDED_FOR") or 
				os.getenv("HTTP_X_FORWARDED_FOR") or 
				os.getenv("REMOTE_ADDR") or 
				"UNKNOWN"))
	return book
