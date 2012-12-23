from sqlalchemy.schema import Column
from sqlalchemy.types import Integer,String,Boolean

import m2tool


class Host(m2tool.db.Model):
    id = Column(Integer, primary_ket=True)
    server_id = Column(Integer, nullable=False)
    maintenance = Column(Boolean, default=0)
    name = Column(String(50), nullable=False)
    matching = Column(String, nullable=False)

    def __init__(self, server_id, maintenance, name, matching):
        self.server_id = server_id
        self.maintenance = maintenance
        self.name = name
        self.matching = matching
