from werkzeug.security import generate_password_hash, check_password_hash

def query_user():
    """
    A query string that queries the student table
    Parameters: None
    Returns: A sql query string
    """
    sql_query = "SELECT * FROM users;"

    return sql_query

def query_all_blogs():
    """
    A query string that queries the quizes table
    Parameters: None
    Returns: A sql query string
    """
    sql_query = "SELECT * FROM quizes;"

    return sql_query

def query_blogs_and_user():

    sql_query = """
    SELECT
    posts_id AS 'POST_ID',
    posts.title AS 'TITLE',
    posts.category AS 'CATEGORY',
    posts.ishidden AS 'HIDDEN',
    posts.published AS 'PUBLISHED',
    posts.content AS 'CONTENT',
    users.user_name AS 'USER'
    FROM posts
    JOIN users ON users.users_id = posts.users_id
    ORDER BY strftime('%s', posts.published) DESC;
    """

    return sql_query

def query_topic(topic):

    sql_query = f"""
    SELECT
    posts_id AS 'POST_ID',
    posts.title AS 'TITLE',
    posts.category AS CATEGORY,
    posts.ishidden AS 'HIDDEN',
    posts.published AS 'PUBLISHED',
    posts.content AS 'CONTENT',
    users.user_name AS 'USER'
    FROM posts
    JOIN users ON users.users_id = posts.users_id
    WHERE posts.category = '{topic}'
    ORDER BY strftime('%s', posts.published) DESC;
    """
    
    return sql_query

def get_user_entries(user):

    sql_query = f"""
    SELECT
    posts_id AS 'POST_ID',
    posts.title AS 'TITLE',
    posts.category AS CATEGORY,
    posts.ishidden AS 'HIDDEN',
    posts.published AS 'PUBLISHED',
    posts.content AS 'CONTENT',
    users.user_name AS 'USER'
    FROM posts
    JOIN users ON users.users_id = posts.users_id
    WHERE users.user_name = '{user}'
    ORDER BY strftime('%s', posts.published) DESC;
    """

    return sql_query

def get_users(user):
    sql_query = f"""
    SELECT
    users_id as user_id, 
    user_name as user,
    users_password as password
    FROM users
    WHERE user = '{user}';
    """

    return sql_query

def del_blog_post(post_id):
    sql_statement = f"""
    DELETE FROM table
    WHERE posts = '{post_id}'';
    """

    return sql_statement

def check_user_password_hash(result, entered):
    user_tuple = result[0]
    (id, user_name, hashed_password) = user_tuple
    verify = check_password_hash(hashed_password, entered)

    return verify

def insert_new_user(user, password):
    hashed_pw = generate_password_hash(password)

    insert_user = f"""
    INSERT INTO users
    (user_name, users_password)    
    VALUES
    ('{user}','{hashed_pw}');
    """

    return insert_user

def transform_to_dict(val_list):
    key_config = ('post_id', 'title', 'category', 'isHidden', 'pub_date', 'content', 'user')

    return [
        dict(zip(key_config, val_tup)) for val_tup in val_list 
    ]

def insert_blog(insert_tup):
    (users_id, title, category, ishidden, published, content) = insert_tup

    blog_insert = f"""
    INSERT INTO posts
    (users_id, title, category, ishidden, published, content)
    VALUES
    ('{users_id}',"{title}", '{category}', '{ishidden}', '{published}', "{content}" );
    """

    return blog_insert

def convert_to_model(req_dict):
    users_id = req_dict.get('userId')
    title = req_dict.get('title')
    category = req_dict.get('category')
    ishidden =  req_dict.get('isHidden')
    published = req_dict.get('pub_date')
    content = req_dict.get('content')

    return (users_id, title, category, ishidden, published, content)