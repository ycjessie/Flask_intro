#g global, a global access to db for the app
from flask import Flask,jsonify,g
#=======import CORS module=============
from flask_cors import CORS
#=========import dog file=============
from resources.dogs import dog # adding this line
#===============import models===============
import models
DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)
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
#==================Middleware=======================
CORS(dog, origins=['http://localhost:3000'], supports_credentials=True) # adding this line
#register blueprint(Route) define a prefix, 
# like Express app.use('/api/v1/dogs', require('dogsControllers.js'))
app.register_blueprint(dog, url_prefix='/api/v1/dogs') # adding this line

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