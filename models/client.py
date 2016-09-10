from sqlalchemy_utils import UUIDType

from base import BaseModel
from report import Report
import uuid
import sqlalchemy as sa


class Client(BaseModel):
    __tablename__ = 'client'

    name =
    trust_score =
    site =
    token =
    timestamp =
    scheduled_on =
    status =
    area =
