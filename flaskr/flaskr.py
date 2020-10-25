import os, sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

config = {}
config['DATABASE'] = os.path.join(app.root_path, 'flaskr.py')
config['SECRET_KEY'] = 'development key'
config['USERNAME'] = 'admin'
config['PASSWORD'] = 'default'

app.config.update(config)
app.config.from_envvar('FLASKR_SETTINGS',silent=True)

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

