import os

import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
Jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class Handler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, templates, **params):
        t = Jinja_env.get_template(templates)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):

    def get(self):
        items = self.request.get_all("food")
        self.render("shopping_list.html", items=items)


class FizzBuzzHandler(Handler):

    def get(self):
        n = self.request.get('n', 0)
        n = n and int(n)
        self.render('fizzbuzz.html', n=n)

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/fizzbuzz', FizzBuzzHandler),
                               ('/fizzbuzz', FizzBuzzHandler),
                               ('/unit2/rot13', Rot13),
                               ],
                              debug=True)
