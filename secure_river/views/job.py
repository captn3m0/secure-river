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

@app.route('/jobs/<id>/submit', methods=['POST'])
def submit_job_response(id):
    job = Job.objects(id=id)
    if not job:
        return 'False'
    job = job[0]
    content = request.values

