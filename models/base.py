from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import UUIDTyp

from app import db

class Base(db.Model):
    # Primary Id key
    id         = db.Column(UUIDType(binary = False), primary_key = True)
    created_at = db.Column(db.DateTime)


