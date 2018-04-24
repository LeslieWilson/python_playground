
# assigning functions to particular addresses on my webpage.
from flask import flask
app = Flask(__name__)

# When I wanna create a new route use @app.route decorator. / route is homepage
@app.route('/')
def hello_world():
    return 'Hello, Flask'

@app.route('/hello')
def hello():
    return 'Hello World'

# debug = true, when you are in your application, if you change a file it will automatically reload your server. Also if you crash it will give you a backtrace of what goes wrong in the browser. Good for testing but need to take it out when it goes live or people can execute arbitrary code when they visit. 

if __name__ == '__main__':
    app.run(debug = True)
