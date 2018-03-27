from secure_river import app
from flask_mongoengine import MongoEngine
import os

if ('MONGODB_URI' in os.environ):
    app.config["MONGODB_HOST"] = 'ds019996.mlab.com'
    app.config["MONGODB_PORT"] = 19996
    app.config["MONGODB_DATABASE"] = 'heroku_94m1k9q8'
    app.config["MONGODB_USERNAME"] = 'heroku_94m1k9q8'
    app.config["MONGODB_PASSWORD"] = os.environ['MONGODB_PWD']


db = MongoEngine(app)
# db.admin.authenticate(app.config['MONGODB_USERNAME'], app.config['MONGODB_PASSWORD'])

from datetime import datetime
from uuid import uuid4
from secure_river.data.isp import STATE_LOOKUPS, CODE_LOOKUPS
import re

def get_uuid():
    uid = uuid4()
    return uid.hex

class Base(db.Document):
    meta = {'allow_inheritance': True}
    id = db.UUIDField(primary_key=True, default=get_uuid)
    created_at = db.DateTimeField(default=datetime.now)

class Client(Base):
    trust_score = db.IntField(default=0, max_value=100)
    token = db.StringField(max_length=255)

class Network(Base):
    region = db.StringField(max_length=3)
    isp = db.StringField(max_length=200)
    mobile = db.BooleanField(default=False)
    mccmnc = db.StringField(max_length=6, null=True)

    @staticmethod
    def get_iff():
        return Network.objects(db.Q(region='INTERNAL') & db.Q(isp='IFF')).first()

    @staticmethod
    def find_by_mcc_mnc(mcc_mnc):
        return Network.objects(db.Q(mobile=True) & db.Q(mccmnc=mcc_mnc)).only('region', 'isp', 'mccmnc', 'mobile').first()

    # This is only called for non-mobile requests
    # Where we don't have any way of knowing
    # The data is assumed to be fetched using
    # http://ip-api.com/json/<ip>
    @staticmethod
    def find_or_create(data):
        regionName = data['regionName']
        region = data['region']
        isp = data['isp']
        city = data['city']
        # If we can get a better lookup, go for it

        for lookup in STATE_LOOKUPS:
            if re.search(lookup[0], city, flags=re.IGNORECASE):
                region = lookup[1]
                break

            if re.search(lookup[0], region, flags=re.IGNORECASE):
                region = lookup[1]
                break

        # Hopefully, we get a better lookup!
        for lookup in CODE_LOOKUPS:
            if re.search(lookup[0], isp, flags=re.IGNORECASE):
                isp = lookup[1]
                break

        if (region == ''):
            region = regionName[0:3]

        existing = Network.objects(db.Q(isp=isp) & db.Q(region=region)).first()

        if existing:
            return existing
        else:
            n = Network(mobile=False, isp=isp, region=region, mccmnc=None)
            n.save()
            return n


class Job(Base):
    scheduled_on = db.DateTimeField()
    site = db.URLField()
    status = db.StringField()


class Response(Base):
    headers = db.DictField()
    status = db.IntField()
    body = db.StringField()


class Report(Base):
    job = db.ReferenceField(Job)
    network = db.ReferenceField(Network)
    network_appr = db.ReferenceField(Network)
    client_id = db.ReferenceField(Client)
    status = db.StringField(max_length=80)
    point = db.GeoPointField(null=True)
    tcp = db.BooleanField()
    metadata = db.StringField()
    dns_ip = db.StringField(null=True)
    http_response = db.ReferenceField(Response)
    https_response = db.ReferenceField(Response)

