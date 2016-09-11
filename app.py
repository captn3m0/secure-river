from flask import Flask
from flask import g

from os.path import abspath, dirname
import sys
import os

sys.path.append(abspath(dirname(__file__)))

import click
from secure_river import seeder
from secure_river import app

@app.cli.command()
def populate_networks():
    click.echo('Populating network database')
    seeder.seed()

@app.cli.command()
def populate_jobs():
    click.echo('Populating jobs')
    seeder.seed_jobs()

@app.cli.command()
def populate_clients():
    click.echo('Populating clients')
    seeder.seed_clients()
