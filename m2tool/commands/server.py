#coding: utf-8
from uuid import uuid4
from m2tool.db import Session
from m2tool.db.models import Server

def server_command(option, name=None, port=None, chroot=None, bindaddr=None, pidfile=None,
                   defaulthost=None, accesslog=None, errorlog=None, ssl=False, uuid=None, id=None):
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
        pidfile = "/run/mongrel2.pid"

    if not accesslog:
        accesslog = '/logs/access.log'

    if not errorlog:
        errorlog = '/logs/error.log'

    if ssl is True:
        usessl = True
    else:
        usessl = ssl

    session = Session()
    port_verify = session.query(Server).filter_by(port=port).count()
    uuid_verify = session.query(Server).filter_by(uuid=uuid).count()

    if port_verify :
        print 'Porta [{0}] já está em uso, por favor tente outra'.format(port)
    elif uuid_verify:
        print 'UUID [{0}] already exists, please check.'.format(uuid)

    else:
        if option == 'add':
            if not port or not name:
                print "Please verify parameters --port or --name"
            else:
                server = Server(name=name, port=port, chroot=chroot,  bind_addr=bindaddr, pid_File=pidfile,
                    default_host=defaulthost, access_log=accesslog, error_log=errorlog, use_ssl=usessl, uuid=uuid )

                session.add(server)
                session.commit()
                print 'Congratulations! Server [{0}] adding with success.'.format(name)

        elif option == 'remove':
            server = session.query(Server).get(id)
            if server:
                session.query(Server).filter_by(id=id).delete()
                session.commit()
                print 'Server [{0}] was removed with success.'.format(server.name)
            else:
                print 'Server not found.'
        elif option == 'update':
            print 'up'
        elif option == 'list':
            server = session.query(Server).order_by(Server.id).all()
            print  '| ' + 'id' + '  |  ' + 'Name' + '  |  ' + 'Port' + ' | '
            for servers in server:
                print servers.id , servers.name, servers.port
        else:
            print 'Any option selected.'