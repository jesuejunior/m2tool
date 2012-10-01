from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
import m2tool
from m2tool.db import Model

class Server(m2tool.db.Model):
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    port = Column(String)
    uuid = Column(String)
    chroot = Column(String)
    accesslog = Column(String)
    errorlog = Column(String)
    pidfile = Column(String)
    bindaddr = Column(String)
    usessl = Column(String)
    defaulthost = Column(String)

    def __init__(self, name, port, uuid, chroot, accesslog, errorlog, pidfile, bindaddr, usessl, defaulthost):
        self.name = name
        self.port = port
        self.uuid = uuid
        self.chroot = chroot
        self.accesslog = accesslog
        self.errorlog = errorlog
        self.pidfile = pidfile
        self.bindaddr = bindaddr
        self.usessl = usessl
        self.defaulthost = defaulthost

