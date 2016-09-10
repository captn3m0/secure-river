import uuid

from sqlalchemy_utils import UUIDType

from app import db
from models.base import BaseModel
from models.report import Report


class Client(BaseModel):
    __tablename__ = 'client'

    trust_score = db.Column(db.Integer)
    token = db.Column(db.String(120))
