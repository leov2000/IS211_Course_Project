from flask import Flask
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('blog.db', check_same_thread=False)

@app.route('/')
def root():
    pass

@app.route('/login')
def home():
    pass 

@app.route('/login', methods=['POST'])
def admin_login():
    pass 

@app.route("/logout")
def logout():
    pass 

if __name__ == '__main__':
    app.run(debug=True)