from sqlalchemy.schema import Column
from sqlalchemy.types import Integer
import m2tool

class Server(m2tool.db.Model):
    __tablename__ = 'servers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    port = Column(String)
    uuid = Column(String)
    accesslog = Column(String)
    errorlog = Column(String)
    chroot = Column(String)
    pidfile = Column(String)
    bindaddr = Column(String)
    usessl = Column(String)
    defaulthost = Column(String)
