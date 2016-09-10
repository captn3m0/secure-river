from sqlalchemy_utils import UUIDType
import uuid

class Client(Base):
    __tablename__ = 'clients'

    # Pass `binary=False` to fallback to CHAR instead of BINARY
    id = sa.Column(UUIDType(binary=False), primary_key=True)