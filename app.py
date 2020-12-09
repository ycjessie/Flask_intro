#g global, a global access to db for the app
from flask import Flask,jsonify,g
#=======import CORS module=============
from flask_cors import CORS
#=======import Login Manager module to session=============
from flask_login import LoginManager
#=========import dog file=============
from resources.dogs import dog # adding this line
#=========importing resource=============

from resources.user import user ############ added this line
login_manager = LoginManager() # sets up the ability to set up the session
#===============import models===============
import models
DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)
###################### loginManaer

app.secret_key = "LJAKLJLKJJLJKLSDJLKJASD" 
## Need this to encode the session
login_manager.init_app(app) 
# set up the sessions on the app

@login_manager.user_loader 
# decorator function, that will load the user object whenever we access the session, we can get the user
# by importing current_user from the flask_login
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None
###################### loginManaer
@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response
#==================Middleware CORS=======================
CORS(dog, origins=['http://localhost:3000'], supports_credentials=True) # adding this line
#register blueprint(Route) define a prefix, 
# like Express app.use('/api/v1/dogs', require('dogsControllers.js'))
app.register_blueprint(dog, url_prefix='/api/v1/dogs') # adding this line

################## CORS
CORS(user, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(user, url_prefix='/user')
################## CORS


# The default URL ends in / ("my-website.com/").
@app.route('/')
def index():
    # return 'Hello World!'

  my_list = ["Hey", "check", "this", "out"]
  return my_list[0] # Works!
#json
# @app.route('/json')
# def dog():
#     return jsonify(name="Frankie", age=8)
#variables
@app.route('/sayhi/<username>') # When someone goes here...
def hello(username): # Do this.
    return "Hello {}".format(username)    

# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)