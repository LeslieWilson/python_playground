
# brings you back to origional homepage, url lets you figure out where in the website a post is
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS, cross_origin
from models import *


app = Flask(__name__)
CORS(app)


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

#this route takes a get request from my home.js and sends up a json representation of everything in the database
@app.route('/api/Home', methods = ['GET'])
@cross_origin()
def result():
    entries=Entry.select().order_by(Entry.date.desc())
    array = []
    for entry in entries:
        array.append({"name": entry.name, "email": entry.email, "country": entry.country, "state": entry.state, "city": entry.city, "zip": entry.zip})
    return jsonify(array)

    # print (posts)

@app.route('/api/Form1', methods = ['POST'])
@cross_origin():
# takes information it receives and enters it into database
def databaseEntry():




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
