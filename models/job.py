from sqlalchemy.orm import relationship

from app import db
from models.base import BaseModel
from models.network import Network


class Job(BaseModel):
    scheduled_on = db.Column(db.DateTime)
    site = db.Column(db.String)
    network_id = db.Column(db.String, db.ForeignKey('network.id'))
    network = relationship(Network, foreign_key=network_id)
    scheduled_on = db.Column(db.DateTime)
    status = db.Column(db.String(89))
