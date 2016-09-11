import json

from flask import request, g, jsonify

from secure_river import app
from secure_river.models import Client, Job, Network

@app.route('/clients', methods=['POST'])
def create_client():
    job = models.client.register()

@app.route('/network')
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
