import os
from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'))

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # make sure the app directories exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Add some basic routing handlers
    app.route('/')(lambda: render_template('index.html'))
    app.route('/index.html')(lambda: render_template('inde.html'))