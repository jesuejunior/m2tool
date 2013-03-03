from uuid import uuid4
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Boolean
from m2tool.conf import *
from m2tool.db import Model


class Server(Model):
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    port = Column(Integer, nullable=False)
    chroot = Column(String, nullable=False, default=DEFAULT_CHROOT)
    bind_addr = Column(String, nullable=False, default=DEFAULT_BIND_ADDR)
    pid_File = Column(String, nullable=False, default=DEFAULT_PIDFILE)
    default_host = Column(String)
    access_log = Column(String, nullable=False, default=DEFAULT_ACCESS_LOG_FILE)
    error_log = Column(String, nullable=False, default=DEFAULT_ERROR_LOG_FILE)
    use_ssl = Column(Boolean, nullable=False, default=DEFAULT_SSL)
    uuid = Column(String, nullable=False, default=uuid4)
