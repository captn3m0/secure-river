import json

from flask import request, g, jsonify

from secure_river import app
from secure_river.models import Client, Job, Network

@app.route('/network/<id>', methods=['GET'])
def fetch_network_reports(id):
    network = Network.objects(id=id)
    if network:
        network = network[0]
        return network.to_json()

@app.route('/networks', methods=['GET'])
def fetch_all_network_reports():
    return Network.objects.only('isp','region','mobile', 'mccmnc').to_json()
