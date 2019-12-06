-- Check and see if the posts table already exists, if it does, drop it
DROP TABLE IF EXISTS ;

-- Check and see if the users table already exists, if it does, drop it
DROP TABLE IF EXISTS users;

-- Create posts table
CREATE TABLE posts (
    posts_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    users_id INT NOT NULL,
    title TEXT,
    category TEXT,
    ishidden BOOLEAN,
    published DATE,
    content TEXT
);

-- Create albums users
CREATE TABLE users (
    users_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_name TEXT,
    users_password TEXT
);
