from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Boolean
import m2tool

class Handler(m2tool.db.Model):
    __tablename__ = 'handler'

    id = Column(Integer, primary_key=True)
    send_spec = Column(String, nullable=False)
    send_ident = Column(String, nullable=False)
    recv_spec = Column(String, nullable=False)
    recv_ident = Column(String, nullable=False)
    raw_payload = Column(Integer, default=1)
    protocol = Column(String, default='json')


    def __init__(self, send_spec, send_ident, recv_spec, recv_ident, raw_payload, protocol):
        self.send_spec = send_spec
        self.send_ident = send_ident
        self.recv_spec = recv_spec
        self.recv_ident = recv_ident
        self.raw_payload = raw_payload
        self.protocol = protocol
