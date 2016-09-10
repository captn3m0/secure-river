from sqlalchemy.orm import relationship

from app import db

from datetime import datetime

from sqlalchemy_utils import UUIDType

class Client(db.Model):
    __tablename__ = 'client'
    __tableargs__ = {'extend_existing': True}

    trust_score = db.Column(db.Integer)
    token = db.Column(db.String(120))
    id         = db.Column(UUIDType(binary = False), primary_key = True)
    created_at = db.Column(db.DateTime, default=datetime.now())

class Network(db.Model):
    __tablename__ = 'network'
    __tableargs__ = {'extend_existing': True}

    id         = db.Column(db.Integer, primary_key = True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    circle = db.Column(db.String(80))
    telco = db.Column(db.String(80))
    state = db.Column(db.String(120))


class Job(db.Model):
    __tablename__ = 'job'
    __tableargs__ = {'extend_existing': True}

    scheduled_on = db.Column(db.DateTime)
    site = db.Column(db.String)
    network_id = db.Column(db.String, db.ForeignKey('network.id'))
    scheduled_on = db.Column(db.DateTime)
    status = db.Column(db.String(89))

    network = db.relationship(Network)

    id         = db.Column(UUIDType(binary = False), primary_key = True)
    created_at = db.Column(db.DateTime, default=datetime.now())




class Report(db.Model):
    __tablename__ = 'report'

    id         = db.Column(UUIDType(binary = False), primary_key = True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    network_id = db.Column(db.Integer, db.ForeignKey('network.id'))
    network_id_appr = db.Column(db.Integer, db.ForeignKey('network.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))

    # relationship
    network = db.relationship(Network, foreign_keys=network_id)
    network_apparent = relationship(
            Network,
            foreign_keys=network_id_appr)

    status = db.Column(db.String)
    response = db.Column(db.String)
