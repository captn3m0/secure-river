import json

from flask import request
from uuid import uuid4

from secure_river import app
from secure_river.models import Client


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
