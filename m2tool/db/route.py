from sqlalchemy.schema import Column
from sqlalchemy.types import Integer,String,Boolean

import m2tool


class Route(m2tool.db.Model):
    id = Column(Integer, primary_key=True)
    path = Column(String, nullable=False)
    reversed = Column(Boolean, default=0)
    host_id = Column(Integer, nullable=False)
    target_id = Column(Integer, nullable=False)
    target_type = Column(String(10), nullable=False)

    def __init__(self, path, reversed, host_id, target_id, target_type):
        self.path = path
        self.reversed = reversed
        self.host_id = host_id
        self.target_id = target_id
        self.target_type = target_type