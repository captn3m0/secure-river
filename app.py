from flask import Flask
from flask import g

from os.path import abspath, dirname
import sys
import os

sys.path.append(abspath(dirname(__file__)))

from flask_mongoengine import MongoEngine
from mongoengine import connect

if ('MONGODB_URI' in os.environ):
    connect(os.environ['MONGODB_URI'])

db = MongoEngine(app)

import click
import seeder

@app.cli.command()
def populate_networks():
    click.echo('Populating network database')
    seeder.seed()

@app.cli.command()
def populate_jobs():
    click.echo('Populating jobs')
    seeder.seed_jobs()
