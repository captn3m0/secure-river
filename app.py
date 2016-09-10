from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import network

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

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
