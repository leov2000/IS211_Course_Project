from flask import Flask, session, request, jsonify, url_for, render_template
import random
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from utilities import query_blogs_and_user, transform_to_dict, query_topic

app = Flask(__name__)
conn = sqlite3.connect('blog.db', check_same_thread=False)
bundle_js = '/static/src.e31bb0bc.js'
bundle_css = '/static/src.e31bb0bc.css'

def render_javascript_assets():
    return render_template('index.html', cache_bust=random.random(), bundle_js=bundle_js, bundle_css=bundle_css)

@app.route('/')
def index():
    return render_javascript_assets()

@app.route('/dashboard')
def get_dashboard():
    return render_javascript_assets()

@app.route('/login')
def get_login():
    return render_javascript_assets()

@app.route('/posts')
def get_posts():
    topic = request.args.get('topic')
    query = query_blogs_and_user() if topic == 'all' or topic == None else query_topic(topic)

    cursor = conn.cursor()    
    cursor.execute(query)

    result = cursor.fetchall()
    dict_values = transform_to_dict(result)

    return jsonify(dict_values)
    #show all the blog posts
    # query db for all posts 

@app.route('/posts/<id>', methods=['PUT'])
def update_post(id):
    #search for post
    # update post here
    #send back successful JSON response
    pass 

@app.route('/posts', methods=['POST'])
def insert_post():
    #insert post
    # send back successful JSON response
    pass 

@app.route('/posts/<id>', methods=['DELETE'])
def delete_post(id):
    # search for post
    # delete post 
    # send back successful JSON response
    pass

@app.route('/login', methods=['POST'])
def admin_login():
    # check if the user exists in the DB. 
    # send back an error if password/user is incorrect
    pass 

@app.route('/signup', methods=['POST'])
def user_signup():
    # signup form 
    # take values from form
    # add them to db
    # send success message JSON.
    pass 

@app.route('/logout/<id>')
def logout(id):
    # delete session here.
    pass 

if __name__ == '__main__':
    app.run(debug=True)