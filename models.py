from sqlalchemy.orm import relationship

from app import db

from datetime import datetime
from uuid import uuid4

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
    circle = db.StringField(max_length=80)
    telco = db.StringField(max_length=80)
    state = db.StringField(max_length=120)
    mobile = db.BooleanField(default=False)


class Job(Base):
    scheduled_on = db.DateTimeField()
    site = db.URLField()
    network = db.ReferenceField(Network)
    status = db.StringField()


class Response(Base):
    headers = db.StringField()
    status = db.IntField()
    body = db.StringField()


class Report(Base):
    job = db.ReferenceField(Job)
    network = db.ReferenceField(Network)
    network_appr = db.ReferenceField(Network)
    client_id = db.ReferenceField(Client)
    status = db.StringField(max_length=80)
    response = db.StringField(max_length=90)
    tcp = db.BooleanField()
    metadata = db.StringField()
    dns_ip = db.StringField(null=True)
    http_response = db.ReferenceField(Response)
