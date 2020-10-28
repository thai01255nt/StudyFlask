from flask import current_app, g
from flask.cli import with_appcontext
import sqlite3


def get_db():
    if not hasattr(g,"db"):
        g.db = sqlite3.connect(
            current_app.config['DATABASE']
        )
        g.db.row_factory = sqlite3.Row
    return g.db