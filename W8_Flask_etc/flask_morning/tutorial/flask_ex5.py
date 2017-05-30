
from flask import Flask, render_template
from random import random
app = Flask(__name__)


@app.route('/')
def index():
    n = 10
    x = range(n)
    y = [round(random(),3) for i in x]
    # table.html is an existing file in the templates folder
    # isn't this nice, no html here!
    return render_template('table.html', data=zip(x, y))  # using Jinja here, the render_template call

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)