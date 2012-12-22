from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Boolean
import m2tool
from m2tool.db import Model

class Server(m2tool.db.Model):
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    port = Column(Integer, nullable=False)
    chroot = Column(String, nullable=False)
    bind_addr = Column(String, nullable=False)
    pid_File = Column(String, nullable=False)
    default_host = Column(String)
    access_log = Column(String, nullable=False)
    error_log = Column(String, nullable=False)
    use_ssl = Column(Boolean, nullable=False)
    uuid = Column(String, nullable=False)

    def __init__(self, name, port, chroot,  bind_addr, pid_File, default_host, access_log, error_log, use_ssl, uuid):
        self.name = name
        self.port = port
        self.chroot = chroot
        self.bind_addr = bind_addr
        self.pid_File = pid_File
        self.default_host = default_host
        self.access_log = access_log
        self.error_log = error_log
        self.use_ssl = use_ssl
        self.uuid = uuid

