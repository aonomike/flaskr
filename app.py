import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify



# configuration
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'my_precious'
USERNAME = 'admin'
PASSWORD = 'admin'

# create and initialize the app
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    """connects to the database"""
    rv = sqlite3.connect(app.config["DATABASE"])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    """creates the database"""
    with app.app_context():
        db = get_db()
        with app.open_resource("schema.sql", mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

#open database connection
def get_db():
    if not hasattr(g, 'sqlitedb'):
        g.sqlitedb = connect_db()
    return g.sqlitedb

#close db connection 
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlitedb'):
        g.sqlitedb.close()



if __name__ == '__main__':
    init_db()
    app.run()