from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from os.path import abspath, dirname

import sys

# Import models here to migrate
from models.network import Network
from models.job import Job
from models.client import Client
from models.report import Report

sys.path.append(abspath(dirname(__file__)))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/jobs')
def fetch_jobs():
    # returns the network entity
    network = network.get_network()
    return models.job.find_by_network(network).json()

@app.route('/jobs/<id>')
def fetch_job_details(id):
    return models.job.find_by_id(id).json()

@app.route('/network/<id>')
def fetch_network_reports(id):
    return models.network.find_by_id(id).reports().json()

@app.route('/jobs/<id>/submit')
def submit_job_response(id):
    job = models.job.find(id)

