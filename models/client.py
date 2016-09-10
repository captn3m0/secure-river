import uuid

from sqlalchemy_utils import UUIDType

from app import db
from models.base import BaseModel
from models.report import Report


class Client(BaseModel):
    __tablename__ = 'client'

    name = db.Column(db.String(50))
    trust_score = db.Column(db.Integer)
    site = db.Column(db.Text)
    token = db.Column(db.String(120))
    scheduled_on = db.Column(db.DateTime)
    status = db.Column(db.String(30))
    area = db.Column(db.String(255))
