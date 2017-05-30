
from flask import Flask
app = Flask(__name__)

# first routing block
@app.route('/') # if no methods specified, default is 'GET'
def index():
    display_str = 'Hello!'
    # code below makes a button to go to the '/rainbow' block
    go_to_rainbow_html = '''
        <form action="/rainbow" >
            <input type="submit" value = "Go to rainbow"/>
        </form>
    '''
    # html that gets returned
    return display_str + go_to_rainbow_html


# second routing block
@app.route('/rainbow') # if no methods specified, default is 'GET'
def rainbow():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    color_divs = []
    for i in range(20):
        color = colors[i % len(colors)]
        # making html string that makes colors
        div = '''<div style="background-color: {0};
                             color: white;
                             text-align: center;">
                     {1}
                 </div>'''.format(color, '*' * 100)
        color_divs.append(div)
    
    # make html that gives us a button to go back to the home page
    go_to_home_html = '''
        <form action="/" >
            <input type="submit" value = "Go home"/>
        </form>
    '''
    # combine them for final html
    return '''
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Rainbow</title>
                </head>
                <body>{0}</body>
            </html>
            '''.format('\n'.join(color_divs)) + go_to_home_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)