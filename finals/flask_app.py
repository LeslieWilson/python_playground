
# brings you back to origional homepage, url lets you figure out where in the website a post is
from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import *


app = Flask(__name__)

@app.before_request
def before_request():
    # create db if needed and connect
    initialize_db()

@app.teardown_request
def teardown_request(exception):
    # close the db connection
    db.close()

# @app.route('/')
# def home():
#     # render the home page with the saved information
#      return render_template('home.html', posts=Post.select().order_by(Post.date.desc()))

# @app.route('/new_post/')
# def new_post():
#     return render_template('new_post.html')
# @app.route('/create/', methods=['POST'])
# def create_post():
# # create new post
#     Post.create(
#         title=request.form['title'],
#         text = request.form['text']
    # )
    # return the user to the home page
    # return redirect(url_for('home'))

@app.route('/api/Home', methods = ['GET'])
def result():
    posts=Post.select().order_by(Post.date.desc())
    print (posts)
    return jsonify(posts)


# @app.route('/result', methods = ['GET', 'POST'])
# def result():
#     if request.method == 'GET':
#         data = request.args.get('place', None)
#         Post.create(
#             title= request.args.get('place', None),
#             text= request.args.get('place', None)
#         )
#     return "some text {}".format(data)

if __name__ == '__main__':
    app.run(debug=True)
