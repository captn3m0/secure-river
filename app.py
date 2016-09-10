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
import seeder

app.before_request(network_util.Network.middleware)

@app.route('/jobs', methods=['GET'])
def fetch_jobs():
    print(g.networks)
    return models.job.find_by_network(network).json()

@app.route('/jobs/<id>', methods=['GET'])
def fetch_job_details(id):
    return models.job.find_by_id(id).json()

@app.route('/network/<id>', methods=['GET'])
def fetch_network_reports(id):
    return models.network.find_by_id(id).reports().json()

@app.route('/jobs/<id>/submit', methods=['POST'])
def submit_job_response(id):
    job = models.job.find(id)

@app.route('/clients', methods=['POST'])
def create_client():
    job = models.client.register()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.cli.command()
def populate_networks():
    click.echo('Populating network database')
    seeder.seed()
