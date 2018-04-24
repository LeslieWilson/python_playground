
# assigning functions to particular addresses on my webpage.
# brings you back to origional homepage, url lets you figure out where in the website a post is
from flask import Flask, render_template, request, redirect, url_for
from models import *

app = Flask(__name__)



# When I wanna create a new route use @app.route decorator. / route is homepage
@app.route('/')
def hello_world():
    return 'Hello, Flask'

# @app.route('/hello')
# def hello():
#     return 'Hello World'



@app.route('/hello/<name>')
def hello(name):
    return 'hello, %s' % name

# debug = true, when you are in your application, if you change a file it will automatically reload your server. Also if you crash it will give you a backtrace of what goes wrong in the browser. Good for testing but need to take it out when it goes live or people can execute arbitrary code when they visit.

if __name__ == '__main__':
    app.run(debug = True)
