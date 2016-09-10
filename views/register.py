import json

from app import app
from flask import request

from models import Client

from uuid import uuid4

@app.route('/register', methods=['GET'])
def register_mobile():
    token = uuid4()
    client = Client(token=token.hex)
    client.save()
    return client.token

@app.route('/get_all', methods=['GET'])
def get_all_token():
    clients = Client.objects()
    print clients
    c_tokens = map(lambda d: d.token, clients)
    return json.dumps(c_tokens)

@app.route('/authenticate', methods=['GET'])
def authenticate():
    token = request.args.get('token')
    c_token = Client.objects(token=token)
    if c_token is None:
        return "No"
    else:
        return 'Yes'

