from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Boolean
import m2tool

class Directory(m2tool.db.Model):
    __tablename__ = 'directory'

    id = Column(Integer, primary_key=True)
    base = Column(String, nullable=False)
    index_file = Column(String, nullable=False)
    default_ctype = Column(String, nullable=False)
    cache_ttl = Column(Boolean, default=0)

    def __init__(self, base, index_file, default_ctype, cache_ttl):
        self.base = base
        self.index_file = index_file
        self.default_ctype = default_ctype
        self.cache_ttl = cache_ttl



