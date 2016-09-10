from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import g

from os.path import abspath, dirname
import sys

from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

sys.path.append(abspath(dirname(__file__)))

import models
import network as network_util

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
