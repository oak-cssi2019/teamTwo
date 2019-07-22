# the import section
import webapp2
import jinja2
import os

# this initializes the jinja2 environment
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# the handler section
class HomeHandler(webapp2.RequestHandler): #homepage "/"
    def get(self):
        home_template = the_jinja_env.get_template('templates/home.html') #pulls in "home.html" template
        self.response.write(home_template.render()) #serves home.html template back to front-end

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/about.html')
        self.response.write(about_template.render())  

class ResultsHandler(webapp2.RequestHandler):
    def get(self):
        # below are the form results from the form on home.html
        results_Dict = {
          'name': self.request.get('user-first-name'), #stores form input named 'user-first-name' under key 'name' which is the same name as the placeholder on 'results.html'
          'feeling': self.request.get('user-feeling') #stores form input under 'user-feeling' under key 'feeling' which is the same name as the placeholder on 'results.html'
        }
        results_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(results_template.render(results_Dict)) #passes in results_Dict that will fill the placeholders on results.html


# the routes / app configuration section
app = webapp2.WSGIApplication([
  ('/', HomeHandler),
  ('/about', AboutHandler),
  ('/results', ResultsHandler),
  ], debug=True)







# to spin your server, navigate to your parent folder and run in your terminal:
# dev_appserver.py app.yaml
# then go to http://localhost:8080 in your browser
# to stop your server, in your terminal press  control+C
