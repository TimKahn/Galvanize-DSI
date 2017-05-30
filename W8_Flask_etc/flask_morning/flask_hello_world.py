# from http://flask.pocoo.org/docs/0.10/quickstart/

from flask import Flask
app = Flask(__name__)  # instantiating a Flask object
# use __name__ for simple applications, see documentation for other

@app.route('/')  #this decorator is associated with what happens at '/' at the URL below
def hello_world(): # name is arbritrary
    return 'Hello World!'  # returning something to browser

if __name__ == '__main__':
    #app.run() # run the app, using defaults
    app.run(host='127.0.0.1',port=5000)
