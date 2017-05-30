
# import Flask
from flask import Flask

# initialize the Flask app, note that all routing blocks use @app
app = Flask(__name__)  # instantiate a flask app object

# routing blocks - note there is only one in this case - @app.route('/') 

# home page - the first place your app will go
@app.route('/', methods = ['GET', 'POST'])  # GET is the default, more about GET and POST below
# the function below will be executed at the host and port followed by '/' 
# the name of the function that will be executed at '/'. Its name is arbitrary.
def index():
    return 'Hello!'

# no more routing blocks

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    # the combination of host and port are where we look for it in our browser
    # e.g. http://0.0.0.0:8080/
    # setting debug=True to see error messages - wouldn't do this on a final deployed app