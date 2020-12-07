from flask import Flask,jsonify

DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

# The default URL ends in / ("my-website.com/").
@app.route('/')
def index():
    return 'Hello World!'

#   my_list = ["Hey", "check", "this", "out"]
#   return my_list[0] # Works!
#json
@app.route('/json')
def dog():
    return jsonify(name="Frankie", age=8)
#variables
@app.route('/sayhi/<username>') # When someone goes here...
def hello(username): # Do this.
    return "Hello {}".format(username)    
# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)