from uuid import uuid4
from m2tool.db import Session
from m2tool.db.models import Server

def server_command(name, port, chroot=None, bindaddr=None, pidfile=None,
                   defaulthost=None, accesslog=None, errorlog=None, ssl=False,uuid=None ):
    '''
    --uuid=UUID --accesslog=FILE --errorlog=FILE
    --chroot=PATH --pidfile=FILE --name=NAME
    --bindaddr=IP --port=PORT --ssl
    --defaulthost=HOSTNAME
    '''
    if not uuid:
        uuid = str(uuid4())

    if not chroot:
        chroot = '/var/mongrel2'

    if not bindaddr:
    #Accept connection from any host
        bindaddr = '0.0.0.0'

    if not pidfile:
        pidfile = "pid"

    if not accesslog:
        accesslog = '/logs/access.log'

    if not errorlog:
        errorlog = '/logs/error.log'

    if ssl is True:
        usessl = True
    else:
        usessl = ssl


    session = Session()
    server = Server(name=name, port=port, chroot=chroot,  bind_addr=bindaddr, pid_File=pidfile,
        default_host=defaulthost, access_log=accesslog, error_log=errorlog, use_ssl=usessl, uuid=uuid )

    session.add(server)
    session.commit()
