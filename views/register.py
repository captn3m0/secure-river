import json
from app import app
from flask import request
from models import Client
from uuid import uuid4

@app.route('/register', methods=['GET', 'POST'])
def register_device():
    token = uuid4()
    client = Client(token=token.hex)
    client.save()
    return client.token

@app.route('/get_all', methods=['GET'])
def get_all_token():
    clients = Client.objects()
    c_tokens = map(lambda d: d.token, clients)
    return json.dumps(c_tokens)
