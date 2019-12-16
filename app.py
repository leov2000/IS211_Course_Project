from flask import Flask, session, request, jsonify, url_for, render_template
import random
import json 
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from utilities import query_blogs_and_user, transform_to_dict, query_topic, get_users, check_user_password_hash, insert_new_user, get_user_entries, insert_blog, convert_to_model, del_blog_post

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

@app.route('/signin', methods=['POST'])
def user_signin():
    parsed = json.loads(request.data)
    user = parsed.get('user').lower()
    password = parsed.get('password')

    query = get_users(user)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        is_verified = check_user_password_hash(result, password)
        dict_values = {'verified': is_verified}

        user_tuple = result[0]
        (id, user, _) = user_tuple

        return (jsonify({**dict_values, 'id': id }), 200) if is_verified else (jsonify(dict_values), 401)
    else:
        insert_user = insert_new_user(user, password)
        cursor.executescript(insert_user)

        return (jsonify({'verified': True}), 200)

@app.route('/admin')
def admin_view():
    user = request.args.get('user')

    query = get_user_entries(user)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    dict_values = transform_to_dict(result)

    return jsonify(dict_values)


@app.route('/posts', methods=['PUT'])
def update_post():
    return ""
    #search for post
    # update post here
    #send back successful JSON response

@app.route('/posts', methods=['POST'])
def insert_post():
    parsed = json.loads(request.data)
    request_object = parsed.get('requestObject')
    request_tuple = convert_to_model(request_object)
    user_name = request_object.get('user')

    blog_insert_statement = insert_blog(request_tuple)

    cursor = conn.cursor()
    cursor.executescript(blog_insert_statement)

    query = get_user_entries(user_name)
    cursor.execute(query)
    result = cursor.fetchall()

    dict_values = transform_to_dict(result)

    return jsonify(dict_values)


@app.route('/posts', methods=['DELETE'])
def delete_post():
    parsed = json.loads(request.data)
    request_object = parsed.get('requestObject')
    post_id = request_object.get('post_id')
    user_name = request_object.get('user')


    del_blog_statement = del_blog_post(post_id)

    print(del_blog_statement)
    cursor = conn.cursor()
    cursor.executescript(del_blog_statement)

    query = get_user_entries(user_name)
    cursor.execute(query)
    result = cursor.fetchall()

    dict_values = transform_to_dict(result)

    return jsonify(dict_values)

    # search for post
    # delete post 
    # send back successful JSON response


if __name__ == '__main__':
    app.run(debug=True)