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
    posts.title AS 'TITLE',
    posts.category AS 'CATEGORY',
    posts.ishidden AS 'HIDDEN',
    posts.published AS 'PUBLISHED',
    posts.content AS 'CONTENT',
    users.user_name AS 'USER'
    FROM posts
    JOIN users ON users.users_id = posts.users_id;
    """

    return sql_query

def transform_to_dict(val_list):
    key_config = ('title', 'category', 'isHidden', 'pub_date', 'content', 'user')

    return [
        dict(zip(key_config, val_tup)) for val_tup in val_list 
    ]
