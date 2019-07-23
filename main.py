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

# Flash games section
class Home1Handler(webapp2.RequestHandler):
    def get(self):
        home1_template = the_jinja_env.get_template('Flash-games/flashHome.html')
        self.response.write(home1_template.render())
class HappyWheelsHandler(webapp2.RequestHandler):
    def get(self):
        happyWheels_template = the_jinja_env.get_template('Flash-games/happyWheels.html')
        self.response.write(happyWheels_template.render())
class RaftWarsHandler(webapp2.RequestHandler):
    def get(self):
        raftWars_template = the_jinja_env.get_template('Flash-games/raftWars.html')
        self.response.write(raftWars_template.render())
class RaftWars2Handler(webapp2.RequestHandler):
    def get(self):
        raftWars2_template = the_jinja_env.get_template('Flash-games/raftWars2.html')
        self.response.write(raftWars2_template.render())

class Run1Handler(webapp2.RequestHandler):
    def get(self):
        run1_template = the_jinja_env.get_template('Flash-games/run1.html')
        self.response.write(run1_template.render())

class Run2Handler(webapp2.RequestHandler):
    def get(self):
        run2_template = the_jinja_env.get_template('Flash-games/run2.html')
        self.response.write(run2_template.render())

class Run3Handler(webapp2.RequestHandler):
    def get(self):
        run3_template = the_jinja_env.get_template('Flash-games/run3.html')
        self.response.write(run3_template.render())

class worldsHardestGameHandler(webapp2.RequestHandler):
    def get(self):
        whg_template = the_jinja_env.get_template('Flash-games/worldsHardestGame.html')
        self.response.write(whg_template.render())

class worldsHardestGame2Handler(webapp2.RequestHandler):
    def get(self):
        whg2_template = the_jinja_env.get_template('Flash-games/worldsHardestGame2.html')
        self.response.write(whg2_template.render())

class worldsHardestGame3Handler(webapp2.RequestHandler):
    def get(self):
        whg3_template = the_jinja_env.get_template('Flash-games/worldsHardestGame3.html')

# Flash games ends here

# Nintendo starts here
# Nintendo ends here

# Sony starts here
# Sony ends here

# the routes / app configuration section
app = webapp2.WSGIApplication([
  ('/', HomeHandler),
  ('/about', AboutHandler),
  ('/results', ResultsHandler),
  ('/flashGamesHomepage', Home1Handler),
  ('/happyWheels', HappyWheelsHandler),
  ('/raftWars', RaftWarsHandler),
  ('/raftWars2', RaftWars2Handler),
  ('/run1', Run1Handler),
  ('/run2', Run2Handler),
  ('/run3', Run3Handler),
  ('/whg', worldsHardestGameHandler),
  ('/whg2', worldsHardestGame2Handler),
  ('/whg3', worldsHardestGame3Handler),
  ], debug=True)







# to spin your server, navigate to your parent folder and run in your terminal:
# dev_appserver.py app.yaml
# then go to http://localhost:8080 in your browser
# to stop your server, in your terminal press  control+C
