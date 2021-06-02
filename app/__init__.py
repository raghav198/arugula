import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

__all__ = ['app', 'db']

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    SQLALCHEMY_DATABASE_URI='sqlite:///data.db')

db = SQLAlchemy(app)


app.config.from_pyfile('config.py', silent=True)

# make sure the app directories exist
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# Add some basic routing handlers
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')
