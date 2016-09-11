import json

from flask import request, g, jsonify

from secure_river import app
from secure_river.models import Client, Job, Network

@app.route('/jobs/<id>', methods=['GET'])
def fetch_job_details(id):
    return Job.objects(id=id)[0]

@app.route('/jobs', methods=['GET'])
def fetch_all_job_details():
    return Job.objects().to_json()

@app.route('/network/<id>', methods=['GET'])
def fetch_network_reports(id):
    network = Network.objects(id=id)
    if network:
        network = network[0]
        return network.to_json()

@app.route('/networks', methods=['GET'])
def fetch_all_network_reports():
    return Network.objects.only('isp','region','mobile', 'mccmnc').to_json()

@app.route('/jobs/<id>/submit', methods=['POST'])
def submit_job_response(id):
    job = Job.objects(id=id)
    if job:
        job = job[0]
        return job.to_json()

@app.route('/clients', methods=['POST'])
def create_client():
    job = models.client.register()

@app.route('/')
def hello_world():
    n = g.networks[0]
    n1 = g.networks[1]
    res = {
        'network': {
            'region': n.region,
            'isp': n.isp,
            'mobile': n.mobile,
            'mccmnc': n.mccmnc
        },
        'network_apparent': {
            'region': n1.region,
            'isp': n1.isp,
            'mobile': n1.mobile,
            'mccmnc': n1.mccmnc
        }
    }

    return jsonify(**res)
