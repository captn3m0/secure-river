import json

from flask import request, g, jsonify

from secure_river import app
from secure_river.models import Client, Job, Network, Response, Report
from secure_river.veritaserum import Veritaserum
from secure_river import constants
import datetime

@app.route('/jobs/<id>', methods=['GET'])
def fetch_job_details(id):
    return Job.objects(id=id)[0]

@app.route('/jobs', methods=['GET'])
def fetch_all_job_details():
    return Job.objects().to_json()

@app.route('/responses', methods=['GET'])
def fetch_all_responses():
    return jsonify(Response.objects().all())

@app.route('/reports', methods=['GET'])
def fetch_all_reports():
    return jsonify(Report.objects().all())

@app.route('/jobs/<id>/submit', methods=['POST'])
def submit_job_response(id):
    job = Job.objects(id=id)
    if not job:
        return 'False'
    job = job[0]
    # TODO: Read as JSON
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
@app.route('/jobs', methods=['POST'])
def create_job():
    data = request.values
    d = datetime.datetime.now()

    job = Job(scheduled_on=d, site=data['url'], status='PENDING')
    job.save()

    v = Veritaserum(data['url'])
    res = v.process()

    http_res = Response(**res['http'])
    https_res = Response(**res['http'])

    http_res.save()
    https_res.save()

    network = Network.get_iff()
    client = Client.objects(id=constants.VERITASERUM_CLIENT).first()

    report = Report(job=job,network=network, network_appr=network, client_id=client, status='DONE', point=None, tcp=res['tcp'], dns_ip=res['ip'], http_response=http_res, https_response=https_res)

    report.save()

    return jsonify({
        'id': job.id,
        'url': job.site,
        'status': job.status
    })
