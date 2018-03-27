from flask import request, g
import base64
from secure_river.models import Client

def auth():
    token = request.headers.get('Authorization', None)
    if token == None:
        g.client = False
    else:
        # Get the token
        token = token.split(' ')[1].strip()
        token = base64.b64decode(token).strip()
        # This becomes None in special cases
        res = Client.objects(token=token)
        if res:
            g.client = str(res[0].id)
        else:
            g.client = False
