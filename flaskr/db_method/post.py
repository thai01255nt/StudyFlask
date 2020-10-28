from . import get
from flask import current_app, g
from flask.cli import with_appcontext
import sqlite3
import click

def init_db():
    db = get.get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')