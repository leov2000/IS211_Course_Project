import sqlite3
from seed.seed_data import seed_user_data, seed_blog_posts_data

def create_tables():
    conn = sqlite3.connect('blog.db')
    sql_file = open('schema.sql')
    sql_tables = sql_file.read()

    conn.executescript(sql_tables)
    conn.commit()
    conn.close()

    sql_file.close()

def insert_data():
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    insert_users = seed_user_data()
    insert_blogs = seed_blog_posts_data()
    print(insert_blogs)

    cursor.executescript(insert_users)
    cursor.executescript(insert_blogs)
    conn.commit()
    conn.close()



if __name__ == '__main__':
    create_tables()
    insert_data()