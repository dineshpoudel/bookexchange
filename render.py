import jinja2
import os
import cgi
import webapp2
import json
import urllib

from google.appengine.api import memcache
from google.appengine.ext import db

def getOneBook(id):
	book = Book.get(db.Key.from_path('Book', int(id)))
	return book

def findBook(q):
	books = db.GqlQuery('SELECT * FROM Book')
	books = list(books)
	foundBook = []
	for book in books:
		if q in book.bookTitle:
			foundBook.append(book)
	return foundBook

#google Search
def google(q):
	links = memcache.get('google_%s'%q)
	if links is None:
		url = ("https://www.googleapis.com/customsearch/v1?key=XXX&cx=011616688212487868943:hmezcysooqg&q=%s&alt=json&safe=high&searchType=image&num=10"%q)
		p = urllib.urlopen(url)
		response = json.loads(p.read())
		data = response['items']
		links = []
		for eachData in data:
			links.append(eachData['link'])
		memcache.add('google_%s'%q , links)	
	return links


#featured books
def getFeaturedBooks(updateCache = False):
	#featured books here
	books = memcache.get('featuredBooks')
	if updateCache or books is None or books == []:
		books = db.GqlQuery('SELECT * FROM Book ORDER BY timestamp DESC LIMIT 20')
		books = list(books)
		memcache.add('featuredBooks',books)
	return books


#to render HTML
jinja = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),autoescape=True)
def render(self,file,values={'junk':'junk'}):
	self.response.out.write(jinja.get_template(file).render(values))


#Book data type
class Book(db.Model):
	bookTitle = db.StringProperty()
	courseID = db.StringProperty()
	ISBN = db.IntegerProperty()
	edition = db.StringProperty()
	price = db.FloatProperty()
	contact = db.StringProperty() #phone or email or facebook
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
	book.price = float(self.request.get('price') or 0) 
	book.contact = self.request.get('contact')
	book.remark = self.request.get('remark')

	book.googleImage = self.request.get('googleImage')
	book.sold = False
	book.ipAddr = ((os.getenv("HTTP_CLIENT_IP") or 
				os.getenv("HTTP_X_FORWARDED_FOR") or 
				os.getenv("HTTP_X_FORWARDED_FOR") or 
				os.getenv("REMOTE_ADDR") or 
				"UNKNOWN"))
	return book
