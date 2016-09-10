import json
from app import app
from flask import request, g
import json
from models import Client, Job, Network

@app.route('/jobs/<id>', methods=['GET'])
def fetch_job_details(id):
    return (id).json()

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
    return json.dumps(g.client)
