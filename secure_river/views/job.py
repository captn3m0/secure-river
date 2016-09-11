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
    values = {
        'network': g.networks[0],
        'network_appr': g.networks[1],
        'point': {'lon': content['lon'], 'lat': content['lat']},
        'http_response': content['http'],
        'https_response': content['https'],
        'dns_ip': content['dns_ip'],
        'tcp': content['tcp'],
        'job': job,
        'client': g.client,
    }
    report  = Report(values)
    report.save()
    return report.to_json()

# Submit a job
@app.route('/job', method=['POST'])
def create_job():
    data = request.values
    values = {
        'site': data['site']
    }
    job = Job(values)
    job.save()
    return job.to_json()


