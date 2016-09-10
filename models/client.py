import uuid

from sqlalchemy_utils import UUIDType
from sqlalchemy.sql.expressions import insert

from app import db
from models.base import BaseModel


class Client(BaseModel):
    __tablename__ = 'client'

    trust_score = db.Column(db.Integer)
    token = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],

        deprecated=['md5_crypt']
    ))

   	def register(self):
   		trust_score = 1
		token = uuid.uuid4()
   		Client.insert().values((trust_score=trust_score, token=token))
   		return token

   	def findClientByToken(self, token):
   		client = Client.query.filter_by(token=token).first()
   		return client
