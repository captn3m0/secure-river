from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import UUIDType

from datetime import datetime

from app import db

class BaseModel(db.Model):
    # Primary Id key
    id         = db.Column(UUIDType(binary = False), primary_key = True)
    created_at = db.Column(db.DateTime, default=datetime.now())
