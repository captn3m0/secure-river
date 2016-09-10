from app import db
from models.base import BaseModel


class Network(BaseModel):
    circle = db.Column(db.String(80))
    telco = db.Column(db.String(80))
    state = db.Column(db.String(120))
