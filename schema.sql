-- Check and see if the posts table already exists, if it does, drop it
DROP TABLE IF EXISTS posts;

-- Check and see if the users table already exists, if it does, drop it
DROP TABLE IF EXISTS users;

-- Check and see if the results table already exists, if it does, drop it
DROP TABLE IF EXISTS results;

-- Create posts table
CREATE TABLE posts (
    posts_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    users_id INT NOT NULL,
    title TEXT,
    content TEXT,
    category TEXT,
    published, DATE
);

-- Create albums users
CREATE TABLE users (
    users_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    users_password TEXT
);
