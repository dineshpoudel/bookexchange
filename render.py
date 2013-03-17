import jinja2
import os

def render(self,file,values={'mainpageTitle':'Book Exchange'}):
	self.response.out.write(jinja.get_template(file).render(values))

jinja = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),autoescape=True)
