from flask import Flask
from flask import g

from os.path import abspath, dirname
import sys

from flask_mongoengine import MongoEngine

app = Flask(__name__)
db = MongoEngine(app)

sys.path.append(abspath(dirname(__file__)))

import click
import network as network_util
from middlewares.auth import auth
import seeder

app.before_request(network_util.Network.middleware)
app.before_request(auth)

# import all the routes
from views import register, routes

@app.cli.command()
def populate_networks():
    click.echo('Populating network database')
    seeder.seed()

@app.cli.command()
def populate_jobs():
    click.echo('Populating jobs')
    seeder.seed_jobs()
