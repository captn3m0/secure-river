from sqlalchemy.orm import relationship

from app import db
from base import BaseModel
from client import Client
from job import Job
from network import Network


class Report(BaseModel):
    __tablename__ = 'report'

    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    network_id = db.Column(db.Integer, db.ForeinKey('network.id'))
    network_id_appr = db.Column(db.Integer, db.ForeignKey('network.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))

    # relationship
    network = relationship(Network, foreign_keys=network_id)
    network_apparent = relationship(
            Network,
            foreign_keys=network_ip_appr)

    status = db.Column(db.String)
    response = db.Column(db.String)
