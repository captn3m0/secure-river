from flask import request, g
import base64
from models import Client

def auth():
    token = request.headers.get('Authorization', None)
    if token == None:
        g.client = False
    else:
        # Get the token
        token = token.split(' ')[1].strip()
        token = base64.b64decode(token).strip()
        # This becomes None in special cases
        res = Client.objects(token='1c78ab7363024c2d96ccb02e9f33a4c5')
        if res:
            g.client = res[0].to_json()
        else:
            g.client = False
