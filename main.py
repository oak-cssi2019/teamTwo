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

#page shows the console options to look at
class ConsoleHandler(webapp2.RequestHandler):
    def get(self):
        console = the_jinja_env.get_template('templates/console.html')
        self.response.write(console.render())

#page full of the playstation 4 console
class PlaystationFourHandler(webapp2.RequestHandler):
    def get(self):
        playstation4 = the_jinja_env.get_template('templates/console_ps4.html')
        self.response.write(playstation4.render())

#page full of the xbox one console
class XboxOneHandler(webapp2.RequestHandler):
    def get(self):
        xboxone = the_jinja_env.get_template('templates/console_xbox1.html')
        self.response.write(xboxone.render())

#page full of the option to go to either the ps4, xbox one, or nintendo game page.
class GamesHandler(webapp2.RequestHandler):
    def get(self):
        game = the_jinja_env.get_template('templates/games.html')
        self.response.write(game.render())

#page full of playstation 4 games
class PlaystationFourGamesHandler(webapp2.RequestHandler):
    def get(self):
        playstation = the_jinja_env.get_template('templates/sony.html')
        self.response.write(playstation.render())

        # ('/watch_dogs_legion', WatchDogsLegionHandler), #ps4 game
class WatchDogsLegionHandler(webapp2.RequestHandler):
    def get(self):
        watchdogs3 = the_jinja_env.get_template('templates/sony_watchdogs3.html')
        self.response.write(watchdogs3.render())

        # ('/marvel_avengers', MarvelAvengersHandler), #ps4 game
class MarvelAvengersHandler(webapp2.RequestHandler):
    def get(self):
        avengers = the_jinja_env.get_template('templates/sony_avengers.html')
        self.response.write(avengers.render())

        # ('/cyberpunk2077', CyberpunkHandler), #ps4 game
class CyberpunkHandler(webapp2.RequestHandler):
    def get(self):
        cyberpunk = the_jinja_env.get_template('templates/sony_cyberpunk2077.html')
        self.response.write(cyberpunk.render())

        # ('/the_last_of_us_2', LastofUsPartTwoHandler), #ps4 game
class LastofUsPartTwoHandler(webapp2.RequestHandler):
    def get(self):
        lastofus2 = the_jinja_env.get_template('templates/sony_lastofus2.html')
        self.response.write(lastofus2.render())

        # ('/medievil', MediEvilHandler), #ps4 game
class MediEvilHandler(webapp2.RequestHandler):
    def get(self):
        medievil = the_jinja_env.get_template('templates/sony_medievil.html')
        self.response.write(medievil.render())

        # ('/predator', PredatorHandler), #ps4 game
class PredatorHandler(webapp2.RequestHandler):
    def get(self):
        predator = the_jinja_env.get_template('templates/sony_predator.html')
        self.response.write(predator.render())

#page full of xbox one games
class XboxOneGamesHandler(webapp2.RequestHandler):
    def get(self):
        xbox = the_jinja_env.get_template('templates/xbox.html')
        self.response.write(xbox.render())

        # ('/spongebob_squarepants', SpongebobHandler), #xbox one game
class SpongebobHandler(webapp2.RequestHandler):
    def get(self):
        spongebob = the_jinja_env.get_template('templates/xbox_spongebob.html')
        self.response.write(spongebob.render())

        # ('/doom_eternal', DoomEternalHandler), #xbox one game
class DoomEternalHandler(webapp2.RequestHandler):
    def get(self):
        doom = the_jinja_env.get_template('templates/xbox_doom.html')
        self.response.write(doom.render())

        # ('/borderlands3', BorderlandsHandler), #xbox one game
class BorderlandsHandler(webapp2.RequestHandler):
    def get(self):
        borderlands3 = the_jinja_env.get_template('templates/xbox_borderlands3.html')
        self.response.write(borderlands3.render())

        # ('/star_wars_jedi', StarWarsJediHandler), #xbox one game
class StarWarsJediHandler(webapp2.RequestHandler):
    def get(self):
        jedi = the_jinja_env.get_template('templates/xbox_starwars.html')
        self.response.write(jedi.render())

        # ('/beyond_good_and_evil_2', BeyondGandEHandler), #xbox one game
class BeyondGandEHandler(webapp2.RequestHandler):
    def get(self):
        goodandevil = the_jinja_env.get_template('templates/xbox_beyondgande2.html')
        self.response.write(goodandevil.render())

        # ('/gears5', GearsFiveHandler) #xbox one game
class GearsFiveHandler(webapp2.RequestHandler):
    def get(self):
        gears = the_jinja_env.get_template('templates/xbox_gears5.html')
        self.response.write(gears.render())

class FlashHomeHandler(webapp2.RequestHandler):
    def get(self):
        home1_template = the_jinja_env.get_template('templates/Flash-games/flashHome.html')
        self.response.write(home1_template.render())

class HappyWheelsHandler(webapp2.RequestHandler):
    def get(self):
        happyWheels_template = the_jinja_env.get_template('templates/Flash-games/happyWheels.html')
        self.response.write(happyWheels_template.render())

class RaftWarsHandler(webapp2.RequestHandler):
    def get(self):
        raftWars_template = the_jinja_env.get_template('templates/Flash-games/raftWars.html')
        self.response.write(raftWars_template.render())

class RaftWars2Handler(webapp2.RequestHandler):
    def get(self):
        raftWars2_template = the_jinja_env.get_template('templates/Flash-games/raftWars2.html')
        self.response.write(raftWars2_template.render())

class Run1Handler(webapp2.RequestHandler):
    def get(self):
        run1_template = the_jinja_env.get_template('templates/Flash-games/run1.html')
        self.response.write(run1_template.render())

class Run2Handler(webapp2.RequestHandler):
    def get(self):
        run2_template = the_jinja_env.get_template('templates/Flash-games/run2.html')
        self.response.write(run2_template.render())

class Run3Handler(webapp2.RequestHandler):
    def get(self):
        run3_template = the_jinja_env.get_template('templates/Flash-games/run3.html')
        self.response.write(run3_template.render())

class worldsHardestGameHandler(webapp2.RequestHandler):
    def get(self):
        whg_template = the_jinja_env.get_template('templates/Flash-games/worldsHardestGame.html')
        self.response.write(whg_template.render())

class worldsHardestGame2Handler(webapp2.RequestHandler):
    def get(self):
        whg2_template = the_jinja_env.get_template('templates/Flash-games/worldsHardestGame2.html')
        self.response.write(whg2_template.render())

class worldsHardestGame3Handler(webapp2.RequestHandler):
    def get(self):
        whg3_template = the_jinja_env.get_template('templates/Flash-games/worldsHardestGame3.html')

# the routes / app configuration section
app = webapp2.WSGIApplication([
  ('/', HomeHandler),
  ('/about', AboutHandler),
  ('/results', ResultsHandler),
  ('/consoles', ConsoleHandler),
  ('/PS4', PlaystationFourHandler), #page full of the playstation 4 console
  ('/xbox_one', XboxOneHandler), #page full of the xbox one console
  ('/video_games', GamesHandler), #page full of the option to go to either the ps4, xbox one, or nintendo game page.
  ('/PS4_games', PlaystationFourGamesHandler), #page full of playstation 4 games
  ('/watch_dogs_legion', WatchDogsLegionHandler), #ps4 game
  ('/marvel_avengers', MarvelAvengersHandler), #ps4 game
  ('/cyberpunk2077', CyberpunkHandler), #ps4 game
  ('/the_last_of_us_2', LastofUsPartTwoHandler), #ps4 game
  ('/medievil', MediEvilHandler), #ps4 game
  ('/predator', PredatorHandler), #ps4 game
  ('/xbox_one_games', XboxOneGamesHandler), #page full of xbox one games
  ('/spongebob_squarepants', SpongebobHandler), #xbox one game
  ('/doom_eternal', DoomEternalHandler), #xbox one game
  ('/borderlands3', BorderlandsHandler), #xbox one game
  ('/star_wars_jedi', StarWarsJediHandler), #xbox one game
  ('/beyond_good_and_evil_2', BeyondGandEHandler), #xbox one game
  ('/gears5', GearsFiveHandler), #xbox one game
  ('/flashGamesHomepage', FlashHomeHandler),
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
