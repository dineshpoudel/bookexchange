import jinja2
import os
import cgi
import webapp2
import logging #just for debugging purpose

from google.appengine.ext import db

def render(self,file,values={'junk':'junk'}):
	self.response.out.write(jinja.get_template(file).render(values))

jinja = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),autoescape=True)
